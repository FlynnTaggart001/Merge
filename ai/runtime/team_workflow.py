"""End-to-end supervised team workflow for Merge."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable

from .decision_manager import DecisionManager, HumanDecision, Disagreement
from .execution_gate import ExecutionRequest, execute_if_authorized
from .handoff import Handoff, HandoffStore
from .permissions import PermissionLevel, PermissionRequest, authorize, minimum_level_for_role
from .project_state import ProjectStateStore
from .proactive_recommendations import Recommendation, RecommendationStore
from .recommendation_engine import RecommendationEngine, RecommendationType
from .role_assignment import assign_role
from .task_planner import Task, TaskStatus, validate_task_plan
from .task_store import TaskStore


@dataclass
class WorkflowResult:
    objective: str
    status: str
    task_ids: list[str] = field(default_factory=list)
    pending_decisions: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
    trace: list[str] = field(default_factory=list)


class TeamWorkflow:
    def __init__(self, *, planner: Callable[[str, object], Iterable[Task]], proposer,
                 devil_advocate, reviewer=None, qa=None,
                 proposer_for_role: Callable[[str], object] | None = None,
                 executor: Callable[[Task, str], object] | None = None,
                 followup_planner: Callable[[Task, object], Iterable[Task]] | None = None,
                 state_store: ProjectStateStore | None = None,
                 task_store: TaskStore | None = None,
                 decision_manager: DecisionManager | None = None,
                 handoff_store: HandoffStore | None = None,
                 recommendation_store: RecommendationStore | None = None) -> None:
        self.planner = planner
        self.proposer = proposer
        self.devil_advocate = devil_advocate
        self.reviewer = reviewer
        self.qa = qa
        self.proposer_for_role = proposer_for_role
        self.executor = executor
        self.followup_planner = followup_planner
        self.state_store = state_store or ProjectStateStore()
        self.task_store = task_store or TaskStore()
        self.decision_manager = decision_manager or DecisionManager()
        self.handoff_store = handoff_store or HandoffStore()
        self.recommendation_store = recommendation_store or RecommendationStore()

    def run(self, objective: str, *, max_iterations: int = 10, max_handoffs: int = 20) -> WorkflowResult:
        if not objective.strip():
            return WorkflowResult(objective=objective, status="BLOCKED", blockers=["objective is empty"])
        state = self.state_store.load()
        trace = ["state:loaded"]
        tasks = list(self.planner(objective, state))
        if not tasks:
            return WorkflowResult(objective=objective, status="BLOCKED", blockers=["planner returned no tasks"], trace=trace)
        graph = validate_task_plan(tasks)
        self.task_store.add_many(tasks)
        trace.append(f"plan:validated:{len(tasks)}")
        result = WorkflowResult(objective=objective, status="IN_PROGRESS", task_ids=[t.task_id for t in tasks], trace=trace)
        handoff_count = 0

        for task in tasks:
            if task.iteration >= max_iterations:
                task.status = TaskStatus.BLOCKED
                self.task_store.save(task)
                result.blockers.append(f"{task.task_id}: iteration ceiling reached")
                continue
            if handoff_count >= max_handoffs:
                task.status = TaskStatus.BLOCKED
                self.task_store.save(task)
                result.blockers.append("handoff ceiling reached")
                break
            unresolved = graph.unresolved(task)
            if unresolved:
                task.status = TaskStatus.BLOCKED
                self.task_store.save(task)
                result.blockers.append(f"{task.task_id}: unresolved dependencies {unresolved}")
                continue
            if not task.role:
                task.role = assign_role(task.objective)
            try:
                required_level = minimum_level_for_role(task.role)
            except ValueError as exc:
                task.status = TaskStatus.BLOCKED
                self.task_store.save(task)
                result.blockers.append(f"{task.task_id}: {exc}")
                continue
            permission_ok, permission_reason = authorize(PermissionRequest(task.role, required_level))
            if not permission_ok:
                task.status = TaskStatus.BLOCKED
                self.task_store.save(task)
                result.blockers.append(f"{task.task_id}: permission denied: {permission_reason}")
                continue

            task.status = TaskStatus.IN_PROGRESS
            self.task_store.save(task)
            proposer = self.proposer_for_role(task.role) if self.proposer_for_role else self.proposer
            review = RecommendationEngine(proposer, self.devil_advocate).review(self._request(task), critical=self._is_critical(task))
            result.trace.append(f"{task.task_id}:proposal+devil_advocate:{review.verdict.value}")
            self.recommendation_store.add(Recommendation(
                recommendation_id=f"REC-{task.task_id}", category="AI_TEAM_REVIEW",
                title=f"Review for {task.objective}", rationale=review.review.text[:2000],
                impact="HIGH" if self._is_critical(task) else "MEDIUM",
                risk="HIGH" if review.verdict in {RecommendationType.REVIEW, RecommendationType.PENDING_HUMAN} else "LOW",
                reversibility="UNKNOWN" if self._is_critical(task) else "HIGH", confidence=review.confidence,
                requires_human=review.requires_human or review.verdict is RecommendationType.PENDING_HUMAN, status=review.verdict.value,
            ))
            result.recommendations.append(f"REC-{task.task_id}")

            if review.review.status == "ok":
                self.decision_manager.add_disagreement(Disagreement(
                    disagreement_id=f"DIS-{task.task_id}", subject=task.objective,
                    opinions={"PROPOSER": review.proposal.text[:2000], "DEVIL_ADVOCATE": review.review.text[:2000]},
                    minority_opinions=[review.review.text[:1000]],
                ))
            if review.verdict in {RecommendationType.BLOCKED, RecommendationType.PENDING_HUMAN}:
                decision_id = f"DEC-{task.task_id}"
                self.decision_manager.create(HumanDecision(
                    decision_id=decision_id, problem=f"Human authorization required for task {task.task_id}",
                    context=review.review.text, options=["APPROVE", "REJECT", "REQUEST ALTERNATIVE"],
                    recommendation=review.review.text, blocked_tasks=[task.task_id],
                ))
                state.pending_decisions.append(decision_id)
                task.status = TaskStatus.REVIEW
                self.task_store.save(task)
                result.pending_decisions.append(decision_id)
                continue

            if self.reviewer is not None:
                response = self.reviewer.execute(self._request(task, role="REVIEWER", prompt=review.proposal.text))
                result.trace.append(f"{task.task_id}:independent_review:{response.status}")
                if response.status != "ok":
                    task.status = TaskStatus.REVIEW
                    self.task_store.save(task)
                    result.blockers.append(f"{task.task_id}: independent review unavailable")
                    continue
            if self.qa is not None:
                response = self.qa.execute(self._request(task, role="QA", prompt=review.proposal.text))
                result.trace.append(f"{task.task_id}:qa:{response.status}")
                if response.status != "ok":
                    task.status = TaskStatus.REVIEW
                    self.task_store.save(task)
                    result.blockers.append(f"{task.task_id}: QA failed or unavailable")
                    continue

            if self.executor is not None:
                try:
                    execute_if_authorized(ExecutionRequest(
                        task_id=task.task_id, role=task.role,
                        action=lambda t=task, p=review.proposal.text: self.executor(t, p),
                        required_level=required_level, critical=False,
                    ), self.decision_manager)
                    result.trace.append(f"{task.task_id}:execution:ok")
                except Exception as exc:
                    task.status = TaskStatus.FAILED
                    self.task_store.save(task)
                    result.blockers.append(f"{task.task_id}: execution failed: {exc}")
                    continue
            else:
                result.trace.append(f"{task.task_id}:execution:deferred")

            task.status = TaskStatus.COMPLETED
            self.task_store.save(task)
            if task.task_id not in state.completed_tasks:
                state.completed_tasks.append(task.task_id)
            followups: list[Task] = []
            if self.followup_planner is not None:
                followups = list(self.followup_planner(task, state))
                self.task_store.add_many(followups)
                result.task_ids.extend(t.task_id for t in followups)
                result.recommendations.extend(t.objective for t in followups)
                result.trace.append(f"{task.task_id}:followups:{len(followups)}")
            handoff_count += 1
            self.handoff_store.append(Handoff(
                task_id=task.task_id, status=task.status.value, summary=review.proposal.text,
                decisions=[], recommended_next_tasks=[t.task_id for t in followups],
            ))

        state.active_tasks = [t.task_id for t in tasks if t.status in {TaskStatus.IN_PROGRESS, TaskStatus.REVIEW}]
        state.pending_decisions = list(dict.fromkeys(state.pending_decisions))
        self.state_store.save(state)
        result.status = "BLOCKED" if result.blockers else ("PENDING_HUMAN" if result.pending_decisions else "COMPLETED")
        return result

    @staticmethod
    def _is_critical(task: Task) -> bool:
        text = f"{task.objective} {task.context}".lower()
        return any(k in text for k in ("architecture", "engine", "scope", "delete", "destroy", "reset", "major", "critical", "irreversible"))

    @staticmethod
    def _request(task: Task, *, role: str | None = None, prompt: str | None = None):
        from .orchestrator import OrchestratorRequest
        return OrchestratorRequest(
            task_id=task.task_id, role=role or task.role, prompt=prompt or task.objective,
            estimated_input_tokens=max(1, len((prompt or task.objective).split())), estimated_output_tokens=500,
            metadata={"workflow": "TEAM_WORKFLOW", "task_role": task.role},
        )
