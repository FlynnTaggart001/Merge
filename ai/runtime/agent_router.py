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


DEFAULT_ROUTES = {
    "ARCHITECT": Route("ARCHITECT", "openai", "architecture and project-wide reasoning"),
    "GAMEPLAY_DESIGNER": Route("GAMEPLAY_DESIGNER", "gemini", "large-context design/research"),
    "WORLD_DESIGNER": Route("WORLD_DESIGNER", "gemini", "content and world ideation"),
    "RESEARCHER": Route("RESEARCHER", "gemini", "research and comparative analysis"),
    "PROGRAMMER": Route("PROGRAMMER", "claude_code", "repository-aware implementation"),
    "REVIEWER": Route("REVIEWER", "grok", "independent critical review"),
    "DEVIL_ADVOCATE": Route("DEVIL_ADVOCATE", "grok", "adversarial constructive challenge"),
    "QA": Route("QA", "grok", "adversarial validation and bug finding"),
    "DOCUMENTATION": Route("DOCUMENTATION", "openai", "cross-document consistency"),
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
