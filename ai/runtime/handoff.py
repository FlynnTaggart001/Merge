"""Structured handoff contract between Merge agents."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import json
from pathlib import Path


@dataclass
class Handoff:
    task_id: str
    status: str
    summary: str
    files_changed: list[str] = field(default_factory=list)
    tests_run: list[str] = field(default_factory=list)
    test_results: list[str] = field(default_factory=list)
    decisions: list[str] = field(default_factory=list)
    problems_found: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
    recommended_next_tasks: list[str] = field(default_factory=list)
    created_by: str = "orchestrator"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def validate(self) -> None:
        for field_name in ("task_id", "status", "summary", "created_by"):
            if not getattr(self, field_name).strip():
                raise ValueError(f"handoff field required: {field_name}")


class HandoffStore:
    def __init__(self, path: Path | str = "ai/runtime/state/handoffs.jsonl") -> None:
        self.path = Path(path)

    def append(self, handoff: Handoff) -> None:
        handoff.validate()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(handoff), ensure_ascii=False) + "\n")
