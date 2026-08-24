"""Persistent, atomic project-state service used by the orchestrator.

The service stores operational state separately from game design documents.
It never silently overwrites an existing state: updates are merged by key and
written atomically.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
import tempfile
from datetime import datetime, timezone


@dataclass
class ProjectState:
    milestone: str = "Phase 1 — UE5 Foundation"
    current_objectives: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
    completed_tasks: list[str] = field(default_factory=list)
    active_tasks: list[str] = field(default_factory=list)
    pending_decisions: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    known_constraints: list[str] = field(default_factory=list)
    last_handoff: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class ProjectStateStore:
    def __init__(self, path: Path | str = "ai/runtime/state/project_state.json") -> None:
        self.path = Path(path)

    def load(self) -> ProjectState:
        if not self.path.exists():
            return ProjectState()
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return ProjectState(**data)

    def save(self, state: ProjectState) -> None:
        state.updated_at = datetime.now(timezone.utc).isoformat()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps(state.__dict__, ensure_ascii=False, indent=2) + "\n"
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=self.path.parent, delete=False) as tmp:
            tmp.write(payload)
            temp_path = Path(tmp.name)
        temp_path.replace(self.path)

    def update(self, **changes) -> ProjectState:
        state = self.load()
        for key, value in changes.items():
            if not hasattr(state, key):
                raise KeyError(f"Unknown project state field: {key}")
            setattr(state, key, value)
        self.save(state)
        return state
