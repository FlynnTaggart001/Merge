"""Proactive recommendation contracts.

This layer creates suggestions from observable project signals without
executing them. It is intentionally deterministic at the storage boundary so
recommendations can be reviewed later and never disappear into a prompt.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
from pathlib import Path


@dataclass
class Recommendation:
    recommendation_id: str
    category: str
    title: str
    rationale: str
    impact: str
    risk: str
    reversibility: str
    confidence: float
    requires_human: bool
    source: str = "orchestrator"
    status: str = "SUGGESTION"
    created_at: str = ""

    def __post_init__(self) -> None:
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc).isoformat()
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")


class RecommendationStore:
    def __init__(self, path: Path | str = "ai/runtime/state/recommendations.jsonl") -> None:
        self.path = Path(path)

    def add(self, recommendation: Recommendation) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(recommendation), ensure_ascii=False) + "\n")


def scan_project_state(state) -> list[Recommendation]:
    """Generate only high-signal, non-executing recommendations from state."""
    suggestions: list[Recommendation] = []
    if getattr(state, "blockers", []):
        suggestions.append(Recommendation(
            recommendation_id="AUTO-BLOCKER-REVIEW",
            category="PROJECT_HEALTH",
            title="Review active blockers before starting unrelated work",
            rationale="The project state contains unresolved blockers.",
            impact="HIGH",
            risk="LOW",
            reversibility="FULL",
            confidence=0.98,
            requires_human=False,
        ))
    if getattr(state, "pending_decisions", []):
        suggestions.append(Recommendation(
            recommendation_id="AUTO-PENDING-DECISIONS",
            category="DECISION_HYGIENE",
            title="Resolve pending human decisions before dependent tasks",
            rationale="Pending decisions may invalidate downstream work.",
            impact="HIGH",
            risk="LOW",
            reversibility="FULL",
            confidence=0.99,
            requires_human=True,
            status="PENDING_HUMAN",
        ))
    return suggestions
