"""Persistent task store for resumable orchestration."""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path

from .task_planner import Task, TaskStatus


class TaskStore:
    def __init__(self, path: Path | str = "ai/runtime/state/tasks.json") -> None:
        self.path = Path(path)

    def _load(self) -> dict:
        if not self.path.exists():
            return {"tasks": {}}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, task: Task) -> None:
        task.validate()
        data = self._load()
        raw = asdict(task)
        raw["status"] = task.status.value
        data["tasks"][task.task_id] = raw
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def add_many(self, tasks: list[Task]) -> None:
        for task in tasks:
            self.save(task)

    def get(self, task_id: str) -> Task:
        data = self._load()
        try:
            raw = data["tasks"][task_id]
        except KeyError as exc:
            raise KeyError(f"Unknown task: {task_id}") from exc
        raw["status"] = TaskStatus(raw["status"])
        return Task(**raw)

    def pending(self) -> list[Task]:
        data = self._load()
        return [
            self._from_raw(raw)
            for raw in data["tasks"].values()
            if raw["status"] in {TaskStatus.PENDING.value, TaskStatus.READY.value, TaskStatus.REVIEW.value}
        ]

    @staticmethod
    def _from_raw(raw: dict) -> Task:
        item = dict(raw)
        item["status"] = TaskStatus(item["status"])
        return Task(**item)
