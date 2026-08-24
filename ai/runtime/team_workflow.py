"""End-to-end supervised team workflow for Merge.

Pipeline:
OBJECTIVE -> STATE -> PLAN -> DEPENDENCIES -> PERMISSIONS -> PROPOSAL ->
DEVIL_ADVOCATE -> REVIEW -> QA -> DECISION -> EXECUTION -> HANDOFF -> STATE.

The implementation is deliberately conservative: this module can coordinate
providers, but it does not silently grant permissions or approve human-only
decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable

from .decision_manager import DecisionManager, HumanDecision, DecisionStatus
from .handoff import Handoff, HandoffStore
from .permissions import PermissionLevel, PermissionRequest, authorize
from .project_state import ProjectStateStore
from .recommendation_engine import RecommendationEngine, RecommendationType
from .task_planner import DependencyGraph, Task, TaskStatus, validate_task_plan


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
    def __init__(
        self,
        *,
        planner: Callable[[str, object], Iterable[Task]],
        proposer,
        devil_advocate,
        reviewer=None,
        qa=None,
        state_store: ProjectStateStore | None = None,
        decision_manager: DecisionManager | None = None,
        handoff_store: HandoffStore | None = None,
    ) -> None:
        self.planner = planner
        self.proposer = proposer
        self.devil_advocate = devil_advocate
        self.reviewer = reviewer
        self.qa = qa
        self.state_store = state_store or ProjectStateStore()
        self.decision_manager = decision_manager or DecisionManager()
        self.handoff_store = handoff_store or HandoffStore()

    def run(self, objective: str, *, max_iterations: int = 10, max_handoffs: int = 20) -> WorkflowResult:
        if not objective.strip():
            return WorkflowResult(objective=objective, status="BLOCKED", blockers=["objective is empty"])

        state = self.state_store.load()
        trace = ["state:loaded"]
        tasks = list(self.planner(objective, state))
        if not tasks:
            return WorkflowResult(objective=objective, status="BLOCKED", blockers=["planner returned no tasks"], trace=trace)

        graph = validate_task_plan(tasks)
        trace.append(f"plan:validated:{len(tasks)}")
        result = WorkflowResult(objective=objective, status="IN_PROGRESS", task_ids=[t.task_id for t in tasks], trace=trace)

        for task in tasks:
            if task.iteration >= max_iterations:
                task.status = TaskStatus.BLOCKED
                result.blockers.append(f"{task.task_id}: iteration ceiling reached")
                continue
            unresolved = graph.unresolved(task)
            if unresolved:
                task.status = TaskStatus.BLOCKED
                result.blockers.append(f"{task.task_id}: unresolved dependencies {unresolved}")
                continue

            permission_ok, permission_reason = authorize(PermissionRequest(task.role, PermissionLevel.L2_CODE))
            if not permission_ok:
                task.status = TaskStatus.BLOCKED
                result.blockers.append(f"{task.task_id}: permission denied: {permission_reason}")
                continue

            task.status = TaskStatus.IN_PROGRESS
            proposal_request = self._request(task)
            review = RecommendationEngine(self.proposer, self.devil_advocate).review(
                proposal_request,
                critical=self._is_critical(task),
            )
            result.trace.append(f"{task.task_id}:proposal+devil_advocate:{review.verdict.value}")

            if review.verdict in {RecommendationType.BLOCKED, RecommendationType.PENDING_HUMAN}:
                decision_id = f"DEC-{task.task_id}"
                decision = HumanDecision(
                    decision_id=decision_id,
                    problem=f"Human authorization required for task {task.task_id}",
                    context=review.review.text,
                    options=["APPROVE", "REJECT", "REQUEST ALTERNATIVE"],
                    recommendation=review.review.text,
                    blocked_tasks=[task.task_id],
                )
                self.decision_manager.create(decision)
                state.pending_decisions.append(decision_id)
                task.status = TaskStatus.REVIEW
                result.pending_decisions.append(decision_id)
                continue

            if self.reviewer is not None:
                reviewer_response = self.reviewer.execute(self._request(task, role="REVIEWER", prompt=review.proposal.text))
                result.trace.append(f"{task.task_id}:independent_review:{reviewer_response.status}")
                if reviewer_response.status != "ok":
                    task.status = TaskStatus.REVIEW
                    result.blockers.append(f"{task.task_id}: independent review unavailable")
                    continue

            if self.qa is not None:
                qa_response = self.qa.execute(self._request(task, role="QA", prompt=review.proposal.text))
                result.trace.append(f"{task.task_id}:qa:{qa_response.status}")
                if qa_response.status != "ok":
                    task.status = TaskStatus.REVIEW
                    result.blockers.append(f"{task.task_id}: QA failed or unavailable")
                    continue

            task.status = TaskStatus.COMPLETED
            if task.task_id not in state.completed_tasks:
                state.completed_tasks.append(task.task_id)
            if task.task_id in state.active_tasks:
                state.active_tasks.remove(task.task_id)
            self.handoff_store.append(Handoff(
                task_id=task.task_id,
                status=task.status.value,
                summary=review.proposal.text,
                decisions=[],
                recommended_next_tasks=[],
            ))

        state.active_tasks = [t.task_id for t in tasks if t.status in {TaskStatus.IN_PROGRESS, TaskStatus.REVIEW}]
        state.pending_decisions = list(dict.fromkeys(state.pending_decisions))
        self.state_store.save(state)
        result.status = "BLOCKED" if result.blockers else ("PENDING_HUMAN" if result.pending_decisions else "COMPLETED")
        return result

    @staticmethod
    def _is_critical(task: Task) -> bool:
        keywords = ("architecture", "engine", "scope", "delete", "destroy", "reset", "major", "critical", "irreversible")
        text = f"{task.objective} {task.context}".lower()
        return any(keyword in text for keyword in keywords)

    @staticmethod
    def _request(task: Task, *, role: str | None = None, prompt: str | None = None):
        from .orchestrator import OrchestratorRequest
        return OrchestratorRequest(
            task_id=task.task_id,
            role=role or task.role,
            prompt=prompt or task.objective,
            estimated_input_tokens=max(1, len((prompt or task.objective).split())),
            estimated_output_tokens=500,
            metadata={"workflow": "TEAM_WORKFLOW", "task_role": task.role},
        )
