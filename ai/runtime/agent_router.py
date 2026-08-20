"""Role-to-provider routing for Merge."""

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
    "PROGRAMMER": Route("PROGRAMMER", "claude_code", "repository-aware implementation"),
    "REVIEWER": Route("REVIEWER", "grok", "independent critical review"),
    "QA": Route("QA", "grok", "adversarial validation and bug finding"),
    "DOCUMENTATION": Route("DOCUMENTATION", "openai", "cross-document consistency"),
}


def route_for(role: str) -> Route:
    try:
        return DEFAULT_ROUTES[role]
    except KeyError as exc:
        raise ValueError(f"No provider route configured for role: {role}") from exc
