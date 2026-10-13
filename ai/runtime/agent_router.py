"""Role-to-provider routing for Merge.

Routing expresses a preference, never a bypass around Orchestrator guards.
The host runtime may substitute an available provider with equivalent
capabilities when the preferred provider is unavailable.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    role: str
    provider_id: str
    reason: str


# This table only selects a provider inside the executable runtime.
# ChatGPT Plus and Wingman are used interactively/outside this router; neither is
# a callable AgentProvider merely because the user has a subscription.
# Claude Code is the only selected repository-facing tool. Its actual runtime
# availability still depends on a compatible registered adapter.
DEFAULT_ROUTES = {
    "ARCHITECT": Route("ARCHITECT", "claude_code", "repository-aware architecture; use ChatGPT Plus interactively for design review"),
    "GAMEPLAY_DESIGNER": Route("GAMEPLAY_DESIGNER", "claude_code", "implement approved gameplay specifications; ChatGPT Plus supports design"),
    "WORLD_DESIGNER": Route("WORLD_DESIGNER", "claude_code", "repository-aware world documentation; ChatGPT Plus supports ideation"),
    "RESEARCHER": Route("RESEARCHER", "claude_code", "record sourced research in the repository; ChatGPT Plus supports interactive research"),
    "PROGRAMMER": Route("PROGRAMMER", "claude_code", "repository-aware implementation"),
    "REVIEWER": Route("REVIEWER", "claude_code", "repository/code review; ChatGPT Plus can provide an additional interactive review"),
    "DEVIL_ADVOCATE": Route("DEVIL_ADVOCATE", "claude_code", "constructive challenge and risk analysis; ChatGPT Plus can review interactively"),
    "QA": Route("QA", "claude_code", "run available repository tests; Unreal validation remains local"),
    "DOCUMENTATION": Route("DOCUMENTATION", "claude_code", "canonical documentation and cross-document consistency"),
    "RELEASE": Route("RELEASE", "claude_code", "repository-aware release preparation"),
}


def route_for(role: str) -> Route:
    normalized = role.strip().upper()
    try:
        return DEFAULT_ROUTES[normalized]
    except KeyError as exc:
        raise ValueError(f"No provider route configured for role: {normalized}") from exc


def route_table() -> dict[str, Route]:
    return dict(DEFAULT_ROUTES)
