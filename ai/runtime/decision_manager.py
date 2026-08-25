"""Human-decision, recommendation, and disagreement persistence."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
import json
from pathlib import Path


class DecisionStatus(str, Enum):
    PENDING_HUMAN = "PENDING_HUMAN"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    SUPERSEDED = "SUPERSEDED"


@dataclass
class HumanDecision:
    decision_id: str
    problem: str
    context: str
    options: list[str]
    recommendation: str
    pros_cons: dict[str, list[str]] = field(default_factory=dict)
    blocked_tasks: list[str] = field(default_factory=list)
    status: DecisionStatus = DecisionStatus.PENDING_HUMAN
    rationale: str = ""
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    decided_at: str | None = None


@dataclass
class Disagreement:
    disagreement_id: str
    subject: str
    opinions: dict[str, str]
    minority_opinions: list[str] = field(default_factory=list)
    resolution: str = ""
    resolved_by: str = ""
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class DecisionManager:
    def __init__(self, path: Path | str = "ai/runtime/state/decisions.json") -> None:
        self.path = Path(path)

    def _load(self) -> dict:
        if not self.path.exists():
            return {"decisions": [], "disagreements": []}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _save(self, data: dict) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def create(self, decision: HumanDecision) -> HumanDecision:
        data = self._load()
        data["decisions"].append(asdict(decision) | {"status": decision.status.value})
        self._save(data)
        return decision

    def resolve(self, decision_id: str, status: DecisionStatus, rationale: str) -> HumanDecision:
        data = self._load()
        for raw in data["decisions"]:
            if raw["decision_id"] == decision_id:
                raw["status"] = status.value
                raw["rationale"] = rationale
                raw["decided_at"] = datetime.now(timezone.utc).isoformat()
                self._save(data)
                data_for_model = dict(raw)
                data_for_model["status"] = DecisionStatus(data_for_model["status"])
                return HumanDecision(**data_for_model)
                return HumanDecision(**raw)
        raise KeyError(f"Unknown decision: {decision_id}")

    def add_disagreement(self, disagreement: Disagreement) -> Disagreement:
        data = self._load()
        data["disagreements"].append(asdict(disagreement))
        self._save(data)
        return disagreement

    def pending(self) -> list[dict]:
        return [d for d in self._load()["decisions"] if d["status"] == DecisionStatus.PENDING_HUMAN.value]
