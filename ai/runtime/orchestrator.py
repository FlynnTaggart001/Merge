"""Central AI Orchestrator for Merge.

All AI requests MUST go through this orchestrator. No bypass path exists
for normal usage. Guards are executed in a fixed, fail-closed order:

    Request
      → Validation
      → Token Limits
      → Budget Guard
      → Rate Limiter
      → Circuit Breaker
      → Provider (with timeout + retry + backoff)
      → Cost Tracker
      → Response
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import argparse
import time

from .budget_guard import BudgetDecision, BudgetGuard, BudgetLimits, Usage
from .circuit_breaker import CircuitBreaker
from .config import RuntimeConfig, DEFAULT_CONFIG
from .cost_tracker import CostTracker, UsageRecord
from .provider_base import (
    AgentProvider,
    ProviderError,
    ProviderRequest,
    ProviderResponse,
)
from .rate_limiter import RateLimit, RateLimiter
from .retry import (
    NonRetryableError,
    RetryExhausted,
    RetryPolicy,
    execute_with_retry,
    is_retryable,
)
from .token_limits import TokenGuard, TokenLimitExceeded, TokenUsage


class OrchestratorError(Exception):
    """Base error for orchestrator-level rejections."""


class GuardRejected(OrchestratorError):
    """Raised when a safety guard refuses the request."""

    def __init__(self, guard: str, reason: str) -> None:
        super().__init__(f"[{guard}] {reason}")
        self.guard = guard
        self.reason = reason


@dataclass
class OrchestratorRequest:
    task_id: str
    role: str
    prompt: str
    estimated_input_tokens: int
    estimated_output_tokens: int = 500
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class OrchestratorResponse:
    task_id: str
    status: str
    text: str = ""
    provider_id: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    latency_seconds: float = 0.0
    attempts: int = 0
    guard_trace: list[str] = field(default_factory=list)
    error: str | None = None


class Orchestrator:
    """Single entry-point for every AI call in Merge."""

    def __init__(
        self,
        provider: AgentProvider,
        config: RuntimeConfig | None = None,
        cost_log_path: Path | None = None,
        *,
        sleep_fn=None,
    ) -> None:
        self.config = config or DEFAULT_CONFIG
        self.provider = provider
        self.sleep_fn = sleep_fn or time.sleep

        self.token_guard = TokenGuard(self.config)

        limits = BudgetLimits(
            monthly_usd=self.config.max_cost_per_month_usd,
            daily_usd=self.config.max_cost_per_day_usd,
            task_usd=self.config.max_cost_per_task_usd,
            call_usd=self.config.max_cost_per_call_usd,
            warning_ratio=self.config.warning_ratio,
            max_retries=self.config.max_retries,
            max_iterations=self.config.max_iterations,
            max_handoffs=self.config.max_handoffs,
        )
        self.budget_guard = BudgetGuard(limits)

        self.rate_limiter = RateLimiter(
            [
                RateLimit(self.config.max_calls_per_minute, 60.0),
                RateLimit(self.config.max_calls_per_hour, 3600.0),
            ]
        )

        self.circuit_breaker = CircuitBreaker(
            failure_threshold=self.config.failure_threshold,
            cooldown_seconds=self.config.cooldown_seconds,
        )

        log_path = cost_log_path or Path("ai/runtime/logs/usage.jsonl")
        self.cost_tracker = CostTracker(log_path)

        self.retry_policy = RetryPolicy.from_config(self.config)
        self._session_cost_usd = 0.0

    def execute(self, request: OrchestratorRequest) -> OrchestratorResponse:
        """Run the full safety pipeline. Fail-closed on any guard violation."""
        trace: list[str] = []
        attempts = 0

        try:
            self._validate(request)
            trace.append("validation:ok")

            self.token_guard.check_request(
                request.estimated_input_tokens,
                request.estimated_output_tokens,
            )
            trace.append("token_limits:ok")

            estimated_cost = self.budget_guard.estimate_call(
                request.estimated_input_tokens,
                request.estimated_output_tokens,
                input_price_per_million=1.0,
                output_price_per_million=3.0,
            )
            decision = self.budget_guard.authorize(estimated_cost)
            if decision is BudgetDecision.DENY:
                raise GuardRejected(
                    "budget_guard", f"DENIED (estimated_cost={estimated_cost})"
                )
            if decision is BudgetDecision.WARN:
                trace.append("budget_guard:WARN")
            else:
                trace.append("budget_guard:ALLOW")

            if (
                estimated_cost is not None
                and self._session_cost_usd + estimated_cost
                > self.config.max_cost_per_session_usd
            ):
                raise GuardRejected(
                    "budget_guard",
                    f"session cost ceiling exceeded "
                    f"({self._session_cost_usd + estimated_cost} > "
                    f"{self.config.max_cost_per_session_usd})",
                )

            if not self.rate_limiter.allow():
                raise GuardRejected("rate_limiter", "rate limit exceeded")
            trace.append("rate_limiter:ok")

            if not self.circuit_breaker.allow():
                raise GuardRejected(
                    "circuit_breaker",
                    f"circuit is {self.circuit_breaker.state.value}",
                )
            trace.append("circuit_breaker:ok")

            provider_request = ProviderRequest(
                prompt=request.prompt,
                task_id=request.task_id,
                role=request.role,
                estimated_input_tokens=request.estimated_input_tokens,
                estimated_output_tokens=request.estimated_output_tokens,
                metadata=request.metadata,
            )

            def _call() -> ProviderResponse:
                nonlocal attempts
                attempts += 1
                self.rate_limiter.record()
                return self.provider.execute(provider_request)

            def _on_retry(attempt: int, exc: Exception, delay: float) -> None:
                self.budget_guard.record_retry()
                if is_retryable(exc):
                    self.circuit_breaker.record_failure()

            try:
                response = execute_with_retry(
                    _call,
                    policy=self.retry_policy,
                    on_retry=_on_retry,
                    sleep_fn=self.sleep_fn,
                )
            except RetryExhausted as exc:
                self.circuit_breaker.record_failure()
                raise GuardRejected(
                    "retry", f"max retries exhausted: {exc.last_error}"
                ) from exc
            except NonRetryableError as exc:
                raise GuardRejected("provider", str(exc)) from exc
            except ProviderError as exc:
                if not getattr(exc, "retryable", False):
                    raise GuardRejected("provider", str(exc)) from exc
                self.circuit_breaker.record_failure()
                raise
            except Exception:
                self.circuit_breaker.record_failure()
                raise

            self.circuit_breaker.record_success()
            trace.append(f"provider:{response.provider_id}:ok")

            usage = Usage(
                input_tokens=response.input_tokens,
                output_tokens=response.output_tokens,
                cost_usd=response.cost_usd,
            )
            self.budget_guard.record_call(usage)
            self.token_guard.record(
                TokenUsage(
                    input_tokens=response.input_tokens,
                    output_tokens=response.output_tokens,
                )
            )
            self._session_cost_usd += response.cost_usd

            self.cost_tracker.append(
                UsageRecord(
                    timestamp=datetime.now(timezone.utc).isoformat(),
                    provider=response.provider_id,
                    model="n/a",
                    task_id=request.task_id,
                    input_tokens=response.input_tokens,
                    output_tokens=response.output_tokens,
                    cost_usd=response.cost_usd,
                    status="ok",
                )
            )
            trace.append("cost_tracker:recorded")

            return OrchestratorResponse(
                task_id=request.task_id,
                status="ok",
                text=response.text,
                provider_id=response.provider_id,
                input_tokens=response.input_tokens,
                output_tokens=response.output_tokens,
                cost_usd=response.cost_usd,
                latency_seconds=response.latency_seconds,
                attempts=attempts,
                guard_trace=trace,
            )

        except (GuardRejected, TokenLimitExceeded) as exc:
            guard = getattr(exc, "guard", "token_limits")
            reason = getattr(exc, "reason", str(exc))
            if isinstance(exc, TokenLimitExceeded):
                guard = "token_limits"
                reason = str(exc)
            trace.append(f"{guard}:REJECTED")
            return OrchestratorResponse(
                task_id=request.task_id,
                status="rejected",
                attempts=attempts,
                guard_trace=trace,
                error=f"{guard}: {reason}",
            )
        except Exception as exc:
            trace.append(f"error:{type(exc).__name__}")
            return OrchestratorResponse(
                task_id=request.task_id,
                status="error",
                attempts=attempts,
                guard_trace=trace,
                error=str(exc),
            )

    def reset_task(self) -> None:
        self.budget_guard.reset_task()
        self.token_guard.reset_task()

    def reset_session(self) -> None:
        self.budget_guard.reset_task()
        self.token_guard.reset_session()
        self._session_cost_usd = 0.0

    def _validate(self, request: OrchestratorRequest) -> None:
        if not request.task_id or not request.task_id.strip():
            raise GuardRejected("validation", "task_id is required")
        if not request.prompt or not request.prompt.strip():
            raise GuardRejected("validation", "prompt is required")
        if request.estimated_input_tokens < 0:
            raise GuardRejected(
                "validation", "estimated_input_tokens must be >= 0"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge AI orchestrator")
    parser.add_argument("objective", help="High-level objective (planning mode)")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    print("Merge AI Orchestrator — PLANNING MODE")
    print(f"Objective: {args.objective}")
    print("No provider called. Use Orchestrator.execute() for real requests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
