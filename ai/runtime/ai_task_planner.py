"""AI-assisted task decomposition with strict local validation.

The AI is allowed to suggest a plan; it cannot execute it. Malformed output
falls back to a single safe task rather than guessing missing dependencies.
"""

from __future__ import annotations

import json

from .role_assignment import assign_role
from .task_planner import Task
from .orchestrator import Orchestrator, OrchestratorRequest


PLANNER_PROMPT = """You are Merge's project planner.
Decompose the objective into the smallest useful sequence of independent tasks.
Respect the current project state and never invent facts that are not supplied.
Return ONLY valid JSON with this shape:
{"tasks":[{"task_id":"...","objective":"...","role":"...","dependencies":[],"expected_output":"...","acceptance_criteria":[],"validation":[]}]}.
Use roles from ARCHITECT, PROGRAMMER, GAMEPLAY_DESIGNER, WORLD_DESIGNER,
RESEARCHER, REVIEWER, DEVIL_ADVOCATE, QA, DOCUMENTATION, RELEASE.
Do not include credentials, secrets, or implementation claims you cannot verify.
"""


class AITaskPlanner:
    def __init__(self, orchestrator: Orchestrator) -> None:
        self.orchestrator = orchestrator

    def plan(self, objective: str, state) -> list[Task]:
        prompt = PLANNER_PROMPT + "\n\nPROJECT STATE:\n" + str(state.__dict__) + "\n\nOBJECTIVE:\n" + objective
        response = self.orchestrator.execute(OrchestratorRequest(
            task_id="PLAN-" + objective[:32].replace(" ", "-"),
            role="ARCHITECT",
            prompt=prompt,
            estimated_input_tokens=max(1, len(prompt.split())),
            estimated_output_tokens=1200,
            metadata={"workflow": "PLANNING"},
        ))
        if response.status != "ok":
            return [self._fallback(objective, state)]
        try:
            data = json.loads(response.text)
            tasks = [self._task_from_json(item, state) for item in data["tasks"]]
            if not tasks:
                raise ValueError("planner returned no tasks")
            return tasks
        except (KeyError, TypeError, ValueError, json.JSONDecodeError):
            return [self._fallback(objective, state)]

    @staticmethod
    def _task_from_json(item: dict, state) -> Task:
        objective = str(item["objective"]).strip()
        return Task(
            task_id=str(item["task_id"]).strip(),
            objective=objective,
            role=str(item.get("role") or assign_role(objective)).upper(),
            dependencies=list(item.get("dependencies", [])),
            context=f"Milestone: {state.milestone}",
            expected_output=str(item["expected_output"]),
            acceptance_criteria=list(item.get("acceptance_criteria", [])),
            validation=list(item.get("validation", [])),
        )

    @staticmethod
    def _fallback(objective: str, state) -> Task:
        return Task(
            task_id="FALLBACK-001",
            objective=objective,
            role=assign_role(objective),
            context=f"Milestone: {state.milestone}",
            expected_output="validated task proposal",
            acceptance_criteria=["objective understood", "review completed"],
            validation=["independent review"],
        )
