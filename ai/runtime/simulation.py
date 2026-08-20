"""Offline simulation mode for testing orchestration without API calls."""

from __future__ import annotations

from dataclasses import dataclass

from budget_guard import BudgetDecision, BudgetGuard, Usage


@dataclass
class SimulatedCall:
    provider: str
    task_id: str
    input_tokens: int
    output_tokens: int
    estimated_cost_usd: float
    decision: BudgetDecision


def simulate_call(
    guard: BudgetGuard,
    provider: str,
    task_id: str,
    input_tokens: int,
    output_tokens: int,
    input_price_per_million: float,
    output_price_per_million: float,
) -> SimulatedCall:
    estimated = guard.estimate_call(
        input_tokens,
        output_tokens,
        input_price_per_million,
        output_price_per_million,
    )
    decision = guard.authorize(estimated)

    # Simulation never records provider spend: no provider is called.
    return SimulatedCall(
        provider=provider,
        task_id=task_id,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        estimated_cost_usd=estimated or 0.0,
        decision=decision,
    )
