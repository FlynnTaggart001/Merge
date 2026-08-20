"""Centralized runtime configuration for Merge AI orchestrator.

All safety limits are loaded from environment variables with safe defaults.
No secrets are stored here.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


def _float(name: str, default: float) -> float:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        return default
    return float(value)


def _int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        return default
    return int(value)


@dataclass(frozen=True)
class RuntimeConfig:
    # Token limits (hard ceilings)
    max_input_tokens: int = 12_000
    max_output_tokens: int = 4_000
    max_total_tokens_per_task: int = 20_000
    max_total_tokens_per_session: int = 100_000

    # Cost limits (USD)
    max_cost_per_call_usd: float = 0.50
    max_cost_per_task_usd: float = 2.00
    max_cost_per_session_usd: float = 10.00
    max_cost_per_day_usd: float = 5.00
    max_cost_per_month_usd: float = 50.00
    warning_ratio: float = 0.70

    # Rate limits
    max_calls_per_minute: int = 30
    max_calls_per_hour: int = 500

    # Retry / timeout
    request_timeout_seconds: float = 60.0
    max_retries: int = 2
    initial_backoff_seconds: float = 0.5
    max_backoff_seconds: float = 30.0
    backoff_multiplier: float = 2.0
    backoff_jitter: float = 0.25  # ±25%

    # Circuit breaker
    failure_threshold: int = 5
    cooldown_seconds: float = 300.0

    # Iteration / handoff safety
    max_iterations: int = 10
    max_handoffs: int = 20

    # Mode
    mode: str = "supervised"  # supervised | autonomous

    @classmethod
    def from_env(cls) -> "RuntimeConfig":
        return cls(
            max_input_tokens=_int("AI_MAX_INPUT_TOKENS_PER_REQUEST", 12_000),
            max_output_tokens=_int("AI_MAX_OUTPUT_TOKENS_PER_REQUEST", 4_000),
            max_total_tokens_per_task=_int("AI_MAX_TOTAL_TOKENS_PER_TASK", 20_000),
            max_total_tokens_per_session=_int("AI_MAX_TOTAL_TOKENS_PER_SESSION", 100_000),
            max_cost_per_call_usd=_float("AI_MAX_COST_PER_CALL_USD", 0.50),
            max_cost_per_task_usd=_float("AI_MAX_COST_PER_TASK_USD", 2.00),
            max_cost_per_session_usd=_float("AI_MAX_COST_PER_SESSION_USD", 10.00),
            max_cost_per_day_usd=_float("AI_MAX_COST_PER_DAY_USD", 5.00),
            max_cost_per_month_usd=_float("AI_MAX_COST_PER_MONTH_USD", 50.00),
            warning_ratio=_float("AI_WARNING_RATIO", 0.70),
            max_calls_per_minute=_int("AI_MAX_REQUESTS_PER_MINUTE", 30),
            max_calls_per_hour=_int("AI_MAX_REQUESTS_PER_HOUR", 500),
            request_timeout_seconds=_float("AI_REQUEST_TIMEOUT_SECONDS", 60.0),
            max_retries=_int("AI_MAX_RETRIES", 2),
            initial_backoff_seconds=_float("AI_INITIAL_BACKOFF_SECONDS", 0.5),
            max_backoff_seconds=_float("AI_MAX_BACKOFF_SECONDS", 30.0),
            backoff_multiplier=_float("AI_BACKOFF_MULTIPLIER", 2.0),
            backoff_jitter=_float("AI_BACKOFF_JITTER", 0.25),
            failure_threshold=_int("AI_FAILURE_THRESHOLD", 5),
            cooldown_seconds=_float("AI_COOLDOWN_SECONDS", 300.0),
            max_iterations=_int("AI_MAX_ITERATIONS", 10),
            max_handoffs=_int("AI_MAX_HANDOFFS", 20),
            mode=os.getenv("MERGE_ORCHESTRATOR_MODE", "supervised").lower(),
        )


# Global default instance (can be overridden in tests)
DEFAULT_CONFIG = RuntimeConfig.from_env()
