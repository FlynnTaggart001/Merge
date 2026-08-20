"""Hard safety guard for AI-provider spending and token budgets.

Provider-independent and safe to use before real API integrations exist.
The guard fails closed when estimates are missing or limits are exceeded.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class BudgetDecision(str, Enum):
    ALLOW = "ALLOW"
    WARN = "WARN"
    DENY = "DENY"


@dataclass
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens


@dataclass
class BudgetLimits:
    monthly_usd: float = 50.0
    daily_usd: float = 5.0
    task_usd: float = 2.0
    call_usd: float = 0.50
    warning_ratio: float = 0.70
    max_retries: int = 3
    max_iterations: int = 10
    max_handoffs: int = 20


@dataclass
class BudgetState:
    month_cost_usd: float = 0.0
    day_cost_usd: float = 0.0
    task_cost_usd: float = 0.0
    retries: int = 0
    iterations: int = 0
    handoffs: int = 0
    usage: Usage = field(default_factory=Usage)


class BudgetGuard:
    """Central gate. A caller must obtain ALLOW/WARN before every paid call."""

    def __init__(self, limits: BudgetLimits | None = None) -> None:
        self.limits = limits or BudgetLimits()
        self.state = BudgetState()

    def estimate_call(
        self,
        input_tokens: int | None,
        output_tokens: int | None,
        input_price_per_million: float | None,
        output_price_per_million: float | None,
    ) -> float | None:
        if None in (
            input_tokens,
            output_tokens,
            input_price_per_million,
            output_price_per_million,
        ):
            return None
        return (
            (input_tokens / 1_000_000) * input_price_per_million
            + (output_tokens / 1_000_000) * output_price_per_million
        )

    def authorize(self, estimated_cost_usd: float | None) -> BudgetDecision:
        # Fail closed: an unknown cost cannot be safely authorized in strict mode.
        if estimated_cost_usd is None or estimated_cost_usd < 0:
            return BudgetDecision.DENY

        projected = [
            self.state.month_cost_usd + estimated_cost_usd,
            self.state.day_cost_usd + estimated_cost_usd,
            self.state.task_cost_usd + estimated_cost_usd,
        ]
        limits = [
            self.limits.monthly_usd,
            self.limits.daily_usd,
            self.limits.task_usd,
        ]

        if estimated_cost_usd > self.limits.call_usd:
            return BudgetDecision.DENY
        if any(value > limit for value, limit in zip(projected, limits)):
            return BudgetDecision.DENY
        if any(value >= limit * self.limits.warning_ratio for value, limit in zip(projected, limits)):
            return BudgetDecision.WARN
        return BudgetDecision.ALLOW

    def record_call(self, usage: Usage) -> None:
        self.state.month_cost_usd += usage.cost_usd
        self.state.day_cost_usd += usage.cost_usd
        self.state.task_cost_usd += usage.cost_usd
        self.state.usage.input_tokens += usage.input_tokens
        self.state.usage.output_tokens += usage.output_tokens

    def record_retry(self) -> None:
        self.state.retries += 1
        if self.state.retries > self.limits.max_retries:
            raise RuntimeError("Maximum retries exceeded")

    def record_iteration(self) -> None:
        self.state.iterations += 1
        if self.state.iterations > self.limits.max_iterations:
            raise RuntimeError("Maximum task iterations exceeded")

    def record_handoff(self) -> None:
        self.state.handoffs += 1
        if self.state.handoffs > self.limits.max_handoffs:
            raise RuntimeError("Maximum agent handoffs exceeded")

    def reset_task(self) -> None:
        self.state.task_cost_usd = 0.0
        self.state.retries = 0
        self.state.iterations = 0
        self.state.handoffs = 0

    def reset_day(self) -> None:
        """Reset only the daily spend window; monthly spend is retained."""
        self.state.day_cost_usd = 0.0

    def reset_month(self) -> None:
        """Reset the monthly and daily spend windows."""
        self.state.month_cost_usd = 0.0
        self.state.day_cost_usd = 0.0
