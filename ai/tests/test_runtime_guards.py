from ai.runtime.circuit_breaker import CircuitBreaker, CircuitState
from ai.runtime.rate_limiter import RateLimit, RateLimiter


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
