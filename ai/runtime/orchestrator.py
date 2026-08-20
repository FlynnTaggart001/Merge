"""Provider-agnostic Merge AI orchestrator with hard runtime guardrails.

The orchestrator can plan and dry-run without any API keys. Real execution is
only possible through an explicitly registered provider and must pass rate,
circuit, token, retry/iteration, and budget gates before a call is attempted.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Protocol, Sequence
import argparse

from .budget_guard import BudgetDecision, BudgetGuard
from .circuit_breaker import CircuitBreaker
from .rate_limiter import RateLimiter
from .token_budget import TokenBudget, TokenLimitError


@dataclass
class Task:
    task_id: str
    objective: str
    role: str
    dependencies: list[str] = field(default_factory=list)
    status: str = "READY"
    context: str = ""
    estimated_cost_usd: float | None = None
    estimated_input_tokens: int = 0
    requested_output_tokens: int = 0


@dataclass
class AgentResult:
    task_id: str
    status: str
    summary: str
    files_changed: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
    provider_id: str | None = None


class AgentProvider(Protocol):
    provider_id: str
    capabilities: Sequence[str]

    def health_check(self) -> bool: ...

    def execute(self, task: Task, context: str) -> AgentResult: ...


class RepositoryContext:
    IMPORTANT_FILES = (
        "README.md", "GAME_BIBLE.md", "AI_RULES.md", "ROADMAP.md",
        "CHANGELOG.md", "specs/TECHNICAL_ARCHITECTURE.md", "ai/PROJECT_STATE.md",
        "ai/DECISIONS.md", "ai/TASK_QUEUE.md",
    )

    def __init__(self, root: Path) -> None:
        self.root = root

    def read(self, relative_path: str) -> str:
        path = self.root / relative_path
        return path.read_text(encoding="utf-8") if path.is_file() else ""

    def summary(self) -> str:
        return "".join(
            f"\n--- {name} ---\n{self.read(name)}"
            for name in self.IMPORTANT_FILES if self.read(name)
        )


class Planner:
    def plan(self, objective: str, context: str) -> list[Task]:
        objective = objective.strip()
        if not objective:
            raise ValueError("Objective cannot be empty")
        return [
            Task("TASK-AUTO-001", f"Analyse les exigences et dépendances pour : {objective}", "ARCHITECT"),
            Task("TASK-AUTO-002", f"Préparer un plan d'implémentation validable pour : {objective}", "PROGRAMMER", ["TASK-AUTO-001"]),
            Task("TASK-AUTO-003", f"Définir les validations et critères QA pour : {objective}", "QA", ["TASK-AUTO-002"]),
        ]


def _rough_tokens(text: str) -> int:
    """Conservative preflight estimate when a provider tokenizer is unavailable."""
    return max(1, (len(text) + 2) // 3)


class Orchestrator:
    """Deterministic task executor. Provider calls are always guard-gated."""

    def __init__(
        self,
        providers: Sequence[AgentProvider] = (),
        *,
        rate_limiter: RateLimiter | None = None,
        circuit_breakers: dict[str, CircuitBreaker] | None = None,
        budget_guard: BudgetGuard | None = None,
        max_input_tokens: int = 12000,
        max_output_tokens: int = 4000,
        max_total_tokens: int = 20000,
        max_iterations: int = 10,
    ) -> None:
        self.providers = {p.provider_id: p for p in providers}
        self.rate_limiter = rate_limiter or RateLimiter()
        self.circuit_breakers = circuit_breakers or {
            provider_id: CircuitBreaker() for provider_id in self.providers
        }
        self.budget_guard = budget_guard or BudgetGuard()
        self.max_iterations = max_iterations
        self.token_budget = TokenBudget(max_input_tokens, max_output_tokens, max_total_tokens)

    def _provider_for(self, role: str) -> AgentProvider | None:
        for provider in self.providers.values():
            if role in provider.capabilities and provider.health_check():
                return provider
        return None

    @staticmethod
    def _ready(task: Task, completed: set[str]) -> bool:
        return task.status == "READY" and all(dep in completed for dep in task.dependencies)

    def execute(self, tasks: Sequence[Task], context: str = "") -> list[AgentResult]:
        pending = {task.task_id: task for task in tasks}
        completed: set[str] = set()
        results: list[AgentResult] = []
        iterations = 0

        while pending:
            iterations += 1
            if iterations > self.max_iterations:
                raise RuntimeError("Maximum orchestrator iterations exceeded")
            progressed = False

            for task in list(pending.values()):
                if not self._ready(task, completed):
                    continue
                progressed = True
                provider = self._provider_for(task.role)
                if provider is None:
                    task.status = "BLOCKED_PROVIDER"
                    results.append(AgentResult(task.task_id, task.status, "No healthy provider available", blockers=[task.role]))
                    continue

                breaker = self.circuit_breakers.setdefault(provider.provider_id, CircuitBreaker())
                if not self.rate_limiter.allow() or not breaker.allow():
                    task.status = "BLOCKED_GUARD"
                    results.append(AgentResult(task.task_id, task.status, "Runtime guard denied provider call", provider_id=provider.provider_id))
                    continue

                prompt = task.context or context
                input_tokens = task.estimated_input_tokens or _rough_tokens(prompt)
                output_tokens = task.requested_output_tokens or min(4000, max(1, self.token_budget.remaining()[1]))
                try:
                    self.token_budget.authorize(input_tokens, output_tokens)
                except TokenLimitError as exc:
                    task.status = "BLOCKED_TOKENS"
                    results.append(AgentResult(task.task_id, task.status, str(exc), provider_id=provider.provider_id))
                    continue

                decision = self.budget_guard.authorize(task.estimated_cost_usd)
                if decision is BudgetDecision.DENY:
                    task.status = "BLOCKED_BUDGET"
                    results.append(AgentResult(task.task_id, task.status, "Budget guard denied provider call", provider_id=provider.provider_id))
                    continue

                try:
                    self.rate_limiter.record()
                    result = provider.execute(task, prompt)
                    breaker.record_success()
                    self.token_budget.record(input_tokens, output_tokens)
                    task.status = result.status
                    completed.add(task.task_id)
                    results.append(result)
                    self.budget_guard.record_retry() if False else None
                except Exception as exc:
                    breaker.record_failure()
                    self.budget_guard.record_retry()
                    task.status = "FAILED"
                    results.append(AgentResult(task.task_id, task.status, str(exc), provider_id=provider.provider_id))
            if not progressed:
                unresolved = ", ".join(pending)
                raise RuntimeError(f"Unresolvable task dependencies: {unresolved}")
            for result in results:
                if result.task_id in pending and result.status not in {"READY", "BLOCKED_PROVIDER", "BLOCKED_GUARD", "BLOCKED_TOKENS", "BLOCKED_BUDGET", "FAILED"}:
                    pending.pop(result.task_id, None)
            for task_id in list(pending):
                if task_id in completed:
                    pending.pop(task_id, None)
            if any(r.status.startswith("BLOCKED_") for r in results[-len(tasks):] if results):
                break
        return results


def print_plan(objective: str, tasks: list[Task]) -> None:
    print("Merge AI Orchestrator — DRY RUN")
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
    parser.add_argument("--root", default=".", help="Path to the Merge repository root")
    args = parser.parse_args()
    context = RepositoryContext(Path(args.root).resolve()).summary()
    print_plan(args.objective, Planner().plan(args.objective, context))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
