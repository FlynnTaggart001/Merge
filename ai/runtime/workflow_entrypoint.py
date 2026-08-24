"""Public entrypoint for the Merge multi-agent workflow."""

from __future__ import annotations

from .team_workflow import TeamWorkflow, WorkflowResult


def run_team_workflow(workflow: TeamWorkflow, objective: str, *, max_iterations: int = 10, max_handoffs: int = 20) -> WorkflowResult:
    """Run a supervised workflow with hard iteration/handoff ceilings."""
    return workflow.run(
        objective,
        max_iterations=max_iterations,
        max_handoffs=max_handoffs,
    )
