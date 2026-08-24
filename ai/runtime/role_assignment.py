"""Role assignment fallback used when an AI planner does not specify a role."""

from __future__ import annotations


KEYWORDS = {
    "PROGRAMMER": ("code", "cpp", "c++", "unreal", "implement", "bug", "fix", "compile"),
    "GAMEPLAY_DESIGNER": ("combat", "gameplay", "skill", "magic", "progression", "balance"),
    "WORLD_DESIGNER": ("world", "quest", "npc", "faction", "lore", "creature", "ecosystem"),
    "RESEARCHER": ("research", "compare", "benchmark", "investigate", "reference"),
    "ARCHITECT": ("architecture", "system", "integration", "dependency", "design"),
    "QA": ("test", "regression", "validation", "qa"),
    "DOCUMENTATION": ("documentation", "readme", "spec", "changelog", "document"),
}


def assign_role(objective: str, *, default: str = "ARCHITECT") -> str:
    text = objective.lower()
    scores = {role: sum(1 for keyword in words if keyword in text) for role, words in KEYWORDS.items()}
    best_role, best_score = max(scores.items(), key=lambda item: item[1])
    return best_role if best_score else default
