from ai.runtime.budget_guard import BudgetDecision, BudgetGuard, BudgetLimits, Usage
from ai.runtime.circuit_breaker import CircuitBreaker, CircuitState
from ai.runtime.rate_limiter import RateLimit, RateLimiter
from ai.runtime.token_budget import TokenBudget, TokenLimitError


def test_rate_limiter_blocks_after_window_limit() -> None:
    limiter = RateLimiter([RateLimit(max_calls=2, window_seconds=60.0)])
    limiter.record(0.0)
    limiter.record(1.0)
    assert limiter.allow(2.0) is False
    assert limiter.allow(61.0) is True


def test_circuit_breaker_opens_and_recovers() -> None:
    breaker = CircuitBreaker(failure_threshold=2, cooldown_seconds=10.0)
    breaker.record_failure(0.0)
    assert breaker.state is CircuitState.CLOSED
    breaker.record_failure(1.0)
    assert breaker.state is CircuitState.OPEN
    assert breaker.allow(5.0) is False
    assert breaker.allow(11.0) is True
    breaker.record_success()
    assert breaker.state is CircuitState.CLOSED


def test_circuit_breaker_reopens_after_half_open_failure() -> None:
    breaker = CircuitBreaker(failure_threshold=1, cooldown_seconds=10.0)
    breaker.record_failure(0.0)
    assert breaker.allow(10.0) is True
    breaker.record_failure(10.0)
    assert breaker.state is CircuitState.OPEN


def test_budget_guard_allows_warns_and_denies() -> None:
    guard = BudgetGuard(BudgetLimits(monthly_usd=10, daily_usd=5, task_usd=2, call_usd=1))
    assert guard.authorize(0.10) is BudgetDecision.ALLOW
    guard.record_call(Usage(cost_usd=1.40))
    assert guard.authorize(0.10) is BudgetDecision.WARN
    assert guard.authorize(1.01) is BudgetDecision.DENY
    assert guard.authorize(None) is BudgetDecision.DENY


def test_budget_guard_enforces_retries_iterations_and_handoffs() -> None:
    guard = BudgetGuard(BudgetLimits(max_retries=1, max_iterations=1, max_handoffs=1))
    guard.record_retry()
    try:
        guard.record_retry()
        assert False, "retry limit should raise"
    except RuntimeError:
        pass
    guard.reset_task()
    guard.record_iteration()
    try:
        guard.record_iteration()
        assert False, "iteration limit should raise"
    except RuntimeError:
        pass
    guard.reset_task()
    guard.record_handoff()
    try:
        guard.record_handoff()
        assert False, "handoff limit should raise"
    except RuntimeError:
        pass


def test_token_budget_hard_limit_rejects_input_and_output() -> None:
    budget = TokenBudget(max_input_tokens=10, max_output_tokens=5, max_total_tokens=12)
    assert budget.authorize(input_tokens=8, output_tokens=4) is True
    try:
        budget.authorize(input_tokens=11, output_tokens=0)
        assert False, "input token hard limit should raise"
    except TokenLimitError:
        pass
    try:
        budget.authorize(input_tokens=8, output_tokens=5)
        assert False, "total token hard limit should raise"
    except TokenLimitError:
        pass


def test_token_budget_tracks_usage() -> None:
    budget = TokenBudget(max_input_tokens=100, max_output_tokens=100, max_total_tokens=150)
    budget.record(input_tokens=40, output_tokens=20)
    assert budget.input_used == 40
    assert budget.output_used == 20
    assert budget.total_used == 60
