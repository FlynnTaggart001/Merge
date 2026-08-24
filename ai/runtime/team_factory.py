"""Build the Merge team workflow from the runtime provider registry."""

from __future__ import annotations

from .agent_router import route_for
from .orchestrator import Orchestrator
from .providers import ProviderRegistry
from .role_assignment import assign_role
from .task_planner import Task
from .team_workflow import TeamWorkflow


def build_team(registry: ProviderRegistry, *, config=None) -> TeamWorkflow:
    """Create guarded role-specific orchestrators from registered providers."""

    def orchestrator_for(role: str) -> Orchestrator:
        route = route_for(role)
        descriptor = registry.get(route.provider_id)
        if not descriptor.enabled or descriptor.provider is None:
            available = registry.available_for(role)
            if not available:
                raise RuntimeError(f"No enabled provider available for role {role}")
            descriptor = available[0]
        return Orchestrator(descriptor.provider, config=config)

    proposer = orchestrator_for("ARCHITECT")
    devil = orchestrator_for("DEVIL_ADVOCATE")
    reviewer = orchestrator_for("REVIEWER")
    qa = orchestrator_for("QA")

    def planner(objective: str, state):
        role = assign_role(objective)
        return [Task(
            task_id="AUTO-001",
            objective=objective,
            role=role,
            context=f"Milestone: {state.milestone}",
            inputs=["PROJECT_STATE.md", "AI_RULES.md"],
            expected_output="validated proposal and implementation handoff",
            acceptance_criteria=["proposal reviewed", "dependencies resolved", "validation recorded"],
            validation=["independent review", "QA"],
        )]

    return TeamWorkflow(
        planner=planner,
        proposer=proposer,
        devil_advocate=devil,
        reviewer=reviewer,
        qa=qa,
    )
