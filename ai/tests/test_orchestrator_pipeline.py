"""Integration tests for the full Merge AI orchestrator pipeline.

All tests are offline and deterministic. No real API keys or network calls.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from ai.runtime.config import RuntimeConfig
from ai.runtime.orchestrator import Orchestrator, OrchestratorRequest
from ai.runtime.provider_base import FailingProvider, MockProvider, ProviderError
from ai.runtime.circuit_breaker import CircuitState


def _cfg(**overrides) -> RuntimeConfig:
    base = dict(
        max_input_tokens=1000,
        max_output_tokens=500,
        max_total_tokens_per_task=2000,
        max_total_tokens_per_session=5000,
        max_cost_per_call_usd=0.50,
        max_cost_per_task_usd=2.00,
        max_cost_per_session_usd=5.00,
        max_cost_per_day_usd=10.00,
        max_cost_per_month_usd=50.00,
        warning_ratio=0.70,
        max_calls_per_minute=30,
        max_calls_per_hour=500,
        request_timeout_seconds=5.0,
        max_retries=2,
        initial_backoff_seconds=0.01,
        max_backoff_seconds=0.05,
        backoff_multiplier=2.0,
        backoff_jitter=0.0,
        failure_threshold=3,
        cooldown_seconds=60.0,
        max_iterations=10,
        max_handoffs=20,
        mode="supervised",
    )
    base.update(overrides)
    return RuntimeConfig(**base)


def _req(
    task_id: str = "T1",
    input_tokens: int = 100,
    output_tokens: int = 50,
    prompt: str = "hello",
) -> OrchestratorRequest:
    return OrchestratorRequest(
        task_id=task_id,
        role="PROGRAMMER",
        prompt=prompt,
        estimated_input_tokens=input_tokens,
        estimated_output_tokens=output_tokens,
    )


def test_1_normal_request_succeeds():
    provider = MockProvider(fixed_cost=0.01, fixed_output_tokens=40)
    orch = Orchestrator(provider, config=_cfg(), sleep_fn=lambda _: None)
    resp = orch.execute(_req())
    assert resp.status == "ok"
    assert resp.provider_id == "mock"
    assert resp.attempts == 1
    assert "validation:ok" in resp.guard_trace
    assert "token_limits:ok" in resp.guard_trace
    assert "budget_guard:ALLOW" in resp.guard_trace
    assert "rate_limiter:ok" in resp.guard_trace
    assert "circuit_breaker:ok" in resp.guard_trace
    assert "cost_tracker:recorded" in resp.guard_trace
    assert len(provider.calls) == 1


def test_2_input_tokens_too_high_provider_never_called():
    provider = MockProvider()
    orch = Orchestrator(provider, config=_cfg(max_input_tokens=50), sleep_fn=lambda _: None)
    resp = orch.execute(_req(input_tokens=200))
    assert resp.status == "rejected"
    assert "token_limits" in (resp.error or "")
    assert len(provider.calls) == 0


def test_3_output_tokens_too_high_rejected():
    provider = MockProvider()
    orch = Orchestrator(provider, config=_cfg(max_output_tokens=20), sleep_fn=lambda _: None)
    resp = orch.execute(_req(output_tokens=100))
    assert resp.status == "rejected"
    assert "token_limits" in (resp.error or "")
    assert len(provider.calls) == 0


def test_4_budget_exceeded_provider_never_called():
    provider = MockProvider(fixed_cost=0.01)
    orch = Orchestrator(
        provider,
        config=_cfg(max_cost_per_call_usd=0.001),
        sleep_fn=lambda _: None,
    )
    resp = orch.execute(_req(input_tokens=500, output_tokens=200))
    assert resp.status == "rejected"
    assert "budget_guard" in (resp.error or "")
    assert len(provider.calls) == 0


def test_5_rate_limit_exceeded_provider_never_called():
    provider = MockProvider()
    orch = Orchestrator(
        provider,
        config=_cfg(max_calls_per_minute=1, max_calls_per_hour=1),
        sleep_fn=lambda _: None,
    )
    r1 = orch.execute(_req(task_id="T1"))
    assert r1.status == "ok"
    r2 = orch.execute(_req(task_id="T2"))
    assert r2.status == "rejected"
    assert "rate_limiter" in (r2.error or "")
    assert len(provider.calls) == 1


def test_6_provider_fails_then_retries_with_backoff():
    provider = MockProvider(fail_times=1, fixed_cost=0.01)
    sleeps: list[float] = []
    orch = Orchestrator(
        provider,
        config=_cfg(max_retries=2, initial_backoff_seconds=0.01),
        sleep_fn=lambda d: sleeps.append(d),
    )
    resp = orch.execute(_req())
    assert resp.status == "ok"
    assert resp.attempts == 2
    assert len(provider.calls) == 2
    assert len(sleeps) == 1


def test_7_max_retries_reached_stops():
    provider = MockProvider(fail_times=10)
    orch = Orchestrator(
        provider,
        config=_cfg(max_retries=2, failure_threshold=100),
        sleep_fn=lambda _: None,
    )
    resp = orch.execute(_req())
    assert resp.status == "rejected"
    assert "retry" in (resp.error or "") or "max retries" in (resp.error or "").lower()
    assert resp.attempts == 3
    assert len(provider.calls) == 3


def test_8_circuit_open_provider_never_called():
    provider = FailingProvider(retryable=True)
    orch = Orchestrator(
        provider,
        config=_cfg(max_retries=0, failure_threshold=1, cooldown_seconds=300),
        sleep_fn=lambda _: None,
    )
    r1 = orch.execute(_req(task_id="T1"))
    assert r1.status in ("rejected", "error")
    assert orch.circuit_breaker.state is CircuitState.OPEN
    calls_before = len(provider.calls)
    r2 = orch.execute(_req(task_id="T2"))
    assert r2.status == "rejected"
    assert "circuit_breaker" in (r2.error or "")
    assert len(provider.calls) == calls_before


def test_9_timeout_is_retryable():
    class TimeoutThenOkProvider:
        provider_id = "timeout-mock"

        def __init__(self):
            self.calls = []
            self._n = 0

        def health_check(self):
            return True

        def execute(self, request):
            from ai.runtime.provider_base import ProviderResponse
            self.calls.append(request)
            self._n += 1
            if self._n == 1:
                raise TimeoutError("simulated timeout")
            return ProviderResponse(
                provider_id=self.provider_id,
                text="ok",
                input_tokens=request.estimated_input_tokens,
                output_tokens=10,
                cost_usd=0.01,
                latency_seconds=0.01,
            )

    provider = TimeoutThenOkProvider()
    orch = Orchestrator(
        provider,
        config=_cfg(max_retries=2, initial_backoff_seconds=0.01),
        sleep_fn=lambda _: None,
    )
    resp = orch.execute(_req())
    assert resp.status == "ok"
    assert resp.attempts == 2
    assert len(provider.calls) == 2


def test_10_session_budget_blocks_further_requests():
    provider = MockProvider(fixed_cost=0.40)
    orch = Orchestrator(
        provider,
        config=_cfg(
            max_cost_per_call_usd=5.0,
            max_cost_per_session_usd=0.50,
            max_cost_per_task_usd=5.0,
            max_cost_per_day_usd=50.0,
            max_input_tokens=200_000,
            max_output_tokens=50_000,
            max_total_tokens_per_task=300_000,
            max_total_tokens_per_session=500_000,
        ),
        sleep_fn=lambda _: None,
    )
    r1 = orch.execute(_req(task_id="T1", input_tokens=10, output_tokens=10))
    assert r1.status == "ok"
    assert orch._session_cost_usd >= 0.40
    r2 = orch.execute(_req(task_id="T2", input_tokens=100_000, output_tokens=10_000))
    assert r2.status == "rejected"
    assert "budget_guard" in (r2.error or "") or "session" in (r2.error or "").lower()
    assert len(provider.calls) == 1


def test_11_full_pipeline_guard_order():
    provider = MockProvider(fixed_cost=0.01)
    orch = Orchestrator(provider, config=_cfg(), sleep_fn=lambda _: None)
    resp = orch.execute(_req())
    assert resp.status == "ok"
    expected_order = [
        "validation:ok",
        "token_limits:ok",
        "budget_guard:ALLOW",
        "rate_limiter:ok",
        "circuit_breaker:ok",
    ]
    for expected in expected_order:
        assert expected in resp.guard_trace
    indices = [resp.guard_trace.index(e) for e in expected_order]
    assert indices == sorted(indices), f"Guard order violated: {resp.guard_trace}"


def test_non_retryable_error_not_retried():
    provider = FailingProvider(retryable=False)
    orch = Orchestrator(
        provider,
        config=_cfg(max_retries=3),
        sleep_fn=lambda _: None,
    )
    resp = orch.execute(_req())
    assert resp.status == "rejected"
    assert len(provider.calls) == 1


if __name__ == "__main__":
    tests = [
        test_1_normal_request_succeeds,
        test_2_input_tokens_too_high_provider_never_called,
        test_3_output_tokens_too_high_rejected,
        test_4_budget_exceeded_provider_never_called,
        test_5_rate_limit_exceeded_provider_never_called,
        test_6_provider_fails_then_retries_with_backoff,
        test_7_max_retries_reached_stops,
        test_8_circuit_open_provider_never_called,
        test_9_timeout_is_retryable,
        test_10_session_budget_blocks_further_requests,
        test_11_full_pipeline_guard_order,
        test_non_retryable_error_not_retried,
    ]
    passed = failed = 0
    for t in tests:
        try:
            t()
            print(f"PASS  {t.__name__}")
            passed += 1
        except Exception as exc:
            print(f"FAIL  {t.__name__}: {exc}")
            failed += 1
    print(f"\n{passed}/{passed + failed} passed")
    raise SystemExit(1 if failed else 0)
