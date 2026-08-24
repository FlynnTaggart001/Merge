"""Deterministic task-planning contracts for Merge.

The planner does not invent implementation facts. It converts an objective and
known project context into validated task contracts; an AI planner may fill the
optional fields, but the contract validation remains local and fail-closed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Iterable


class TaskStatus(str, Enum):
    PENDING = "PENDING"
    READY = "READY"
    IN_PROGRESS = "IN_PROGRESS"
    REVIEW = "REVIEW"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


@dataclass
class Task:
    task_id: str
    objective: str
    status: TaskStatus = TaskStatus.PENDING
    priority: str = "MEDIUM"
    role: str = "ARCHITECT"
    assigned_agent: str = ""
    dependencies: list[str] = field(default_factory=list)
    context: str = ""
    inputs: list[str] = field(default_factory=list)
    expected_output: str = ""
    acceptance_criteria: list[str] = field(default_factory=list)
    validation: list[str] = field(default_factory=list)
    created_by: str = "orchestrator"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    iteration: int = 0
    handoffs: int = 0

    def validate(self) -> None:
        required = {
            "task_id": self.task_id,
            "objective": self.objective,
            "role": self.role,
            "expected_output": self.expected_output,
            "created_by": self.created_by,
        }
        missing = [name for name, value in required.items() if not value or not str(value).strip()]
        if missing:
            raise ValueError(f"Task missing required fields: {', '.join(missing)}")
        if self.task_id in self.dependencies:
            raise ValueError(f"Task {self.task_id} cannot depend on itself")
        if self.iteration < 0 or self.handoffs < 0:
            raise ValueError("iteration and handoffs must be >= 0")


class DependencyGraph:
    def __init__(self, tasks: Iterable[Task] = ()) -> None:
        self.tasks: dict[str, Task] = {}
        for task in tasks:
            self.add(task)

    def add(self, task: Task) -> None:
        task.validate()
        if task.task_id in self.tasks:
            raise ValueError(f"Duplicate task id: {task.task_id}")
        self.tasks[task.task_id] = task

    def unresolved(self, task: Task) -> list[str]:
        return [
            dependency
            for dependency in task.dependencies
            if dependency not in self.tasks or self.tasks[dependency].status is not TaskStatus.COMPLETED
        ]

    def ready(self) -> list[Task]:
        ready = []
        for task in self.tasks.values():
            if task.status in {TaskStatus.PENDING, TaskStatus.READY} and not self.unresolved(task):
                task.status = TaskStatus.READY
                ready.append(task)
        return ready

    def detect_cycles(self) -> list[list[str]]:
        visiting: set[str] = set()
        visited: set[str] = set()
        cycles: list[list[str]] = []

        def visit(node: str, path: list[str]) -> None:
            if node in visiting:
                index = path.index(node)
                cycles.append(path[index:] + [node])
                return
            if node in visited:
                return
            visiting.add(node)
            for dependency in self.tasks[node].dependencies:
                if dependency in self.tasks:
                    visit(dependency, path + [dependency])
            visiting.remove(node)
            visited.add(node)

        for task_id in self.tasks:
            visit(task_id, [task_id])
        return cycles


def validate_task_plan(tasks: Iterable[Task]) -> DependencyGraph:
    graph = DependencyGraph(tasks)
    cycles = graph.detect_cycles()
    if cycles:
        raise ValueError(f"Dependency cycle detected: {cycles[0]}")
    return graph
