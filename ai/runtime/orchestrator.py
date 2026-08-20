"""Provider-agnostic Merge AI orchestrator scaffold.

This module deliberately performs planning only until real agent providers are
configured. It is designed so providers can later implement the AgentProvider
interface without changing task/state contracts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol, Sequence
import argparse


@dataclass
class Task:
    task_id: str
    objective: str
    role: str
    dependencies: list[str] = field(default_factory=list)
    status: str = "READY"


@dataclass
class AgentResult:
    task_id: str
    status: str
    summary: str
    files_changed: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)


class AgentProvider(Protocol):
    """Common interface implemented by real external AI integrations."""

    provider_id: str
    capabilities: Sequence[str]

    def health_check(self) -> bool: ...

    def execute(self, task: Task, context: str) -> AgentResult: ...


class RepositoryContext:
    """Read only the project information needed for planning."""

    IMPORTANT_FILES = (
        "README.md",
        "GAME_BIBLE.md",
        "AI_RULES.md",
        "ROADMAP.md",
        "CHANGELOG.md",
        "specs/TECHNICAL_ARCHITECTURE.md",
        "ai/PROJECT_STATE.md",
        "ai/DECISIONS.md",
        "ai/TASK_QUEUE.md",
    )

    def __init__(self, root: Path) -> None:
        self.root = root

    def read(self, relative_path: str) -> str:
        path = self.root / relative_path
        if not path.is_file():
            return ""
        return path.read_text(encoding="utf-8")

    def summary(self) -> str:
        sections: list[str] = []
        for filename in self.IMPORTANT_FILES:
            content = self.read(filename)
            if content:
                sections.append(f"\n--- {filename} ---\n{content}")
        return "".join(sections)


class Planner:
    """Minimal deterministic planner for the first dry-run.

    A future LLM planner can replace this component while preserving the task
    contract and persistence format.
    """

    def plan(self, objective: str, context: str) -> list[Task]:
        objective = objective.strip()
        if not objective:
            raise ValueError("Objective cannot be empty")

        return [
            Task(
                task_id="TASK-AUTO-001",
                objective=f"Analyse les exigences et dépendances pour : {objective}",
                role="ARCHITECT",
            ),
            Task(
                task_id="TASK-AUTO-002",
                objective=f"Préparer un plan d'implémentation validable pour : {objective}",
                role="PROGRAMMER",
                dependencies=["TASK-AUTO-001"],
            ),
            Task(
                task_id="TASK-AUTO-003",
                objective=f"Définir les validations et critères QA pour : {objective}",
                role="QA",
                dependencies=["TASK-AUTO-002"],
            ),
        ]


def print_plan(objective: str, tasks: list[Task]) -> None:
    print(f"Merge AI Orchestrator — DRY RUN")
    print(f"Objective: {objective}\n")
    for task in tasks:
        deps = ", ".join(task.dependencies) if task.dependencies else "None"
        print(f"[{task.task_id}] {task.role} — {task.objective}")
        print(f"  Dependencies: {deps}")
        print(f"  Status: {task.status}\n")
    print("No provider was called. No game code was modified.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge AI orchestrator")
    parser.add_argument("objective", help="Single high-level objective")
    parser.add_argument(
        "--root",
        default=".",
        help="Path to the Merge repository root",
    )
    args = parser.parse_args()

    context = RepositoryContext(Path(args.root).resolve())
    project_context = context.summary()
    tasks = Planner().plan(args.objective, project_context)
    print_plan(args.objective, tasks)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
