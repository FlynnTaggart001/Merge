"""Build the Merge team workflow from the runtime provider registry."""

from __future__ import annotations

from .agent_router import route_for
from .ai_task_planner import AITaskPlanner
from .orchestrator import Orchestrator
from .providers import ProviderRegistry
from .team_workflow import TeamWorkflow


def build_team(registry: ProviderRegistry, *, config=None) -> TeamWorkflow:
    """Create guarded role-specific orchestrators from registered providers."""

    cache: dict[str, Orchestrator] = {}

    def orchestrator_for(role: str) -> Orchestrator:
        normalized = role.upper()
        if normalized in cache:
            return cache[normalized]
        route = route_for(normalized)
        descriptor = registry.get(route.provider_id)
        if not descriptor.enabled or descriptor.provider is None:
            available = registry.available_for(normalized)
            if not available:
                raise RuntimeError(f"No enabled provider available for role {normalized}")
            descriptor = available[0]
        cache[normalized] = Orchestrator(descriptor.provider, config=config)
        return cache[normalized]

    planner = AITaskPlanner(orchestrator_for("ARCHITECT"))

    def execute_task(task, proposal):
        from .orchestrator import OrchestratorRequest
        response = orchestrator_for(task.role).execute(OrchestratorRequest(
            task_id=f"EXEC-{task.task_id}",
            role=task.role,
            prompt=(
                "Execute the following validated proposal for Merge. Do not invent scope. "
                "Report files changed, tests run, results, blockers and next tasks.\n\n"
                + proposal
            ),
            estimated_input_tokens=max(1, len(proposal.split())),
            estimated_output_tokens=1200,
            metadata={"workflow": "EXECUTION", "parent_task": task.task_id},
        ))
        if response.status != "ok":
            raise RuntimeError(response.error or "execution provider rejected request")
        return response.text

    return TeamWorkflow(
        planner=planner.plan,
        proposer=orchestrator_for("ARCHITECT"),
        devil_advocate=orchestrator_for("DEVIL_ADVOCATE"),
        reviewer=orchestrator_for("REVIEWER"),
        qa=orchestrator_for("QA"),
        proposer_for_role=orchestrator_for,
        executor=execute_task,
        followup_planner=lambda task, state: planner.plan(
            f"Identify the next actionable tasks after completing {task.task_id}: {task.objective}", state
        ),
    )
