"""Retry policy with exponential backoff + jitter for Merge AI providers."""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import Callable, TypeVar

from .config import RuntimeConfig, DEFAULT_CONFIG

T = TypeVar("T")


class NonRetryableError(Exception):
    """Errors that must never be retried (auth, validation, budget, etc.)."""


class RetryExhausted(Exception):
    """Raised when max retries have been consumed."""

    def __init__(self, last_error: Exception, attempts: int) -> None:
        super().__init__(f"Retry exhausted after {attempts} attempts: {last_error}")
        self.last_error = last_error
        self.attempts = attempts


@dataclass
class RetryPolicy:
    max_retries: int
    initial_backoff: float
    max_backoff: float
    multiplier: float
    jitter: float
    timeout_seconds: float

    @classmethod
    def from_config(cls, config: RuntimeConfig | None = None) -> "RetryPolicy":
        cfg = config or DEFAULT_CONFIG
        return cls(
            max_retries=cfg.max_retries,
            initial_backoff=cfg.initial_backoff_seconds,
            max_backoff=cfg.max_backoff_seconds,
            multiplier=cfg.backoff_multiplier,
            jitter=cfg.backoff_jitter,
            timeout_seconds=cfg.request_timeout_seconds,
        )

    def compute_backoff(self, attempt: int) -> float:
        """Exponential backoff with full jitter."""
        base = min(self.initial_backoff * (self.multiplier ** attempt), self.max_backoff)
        if self.jitter <= 0:
            return base
        jitter_range = base * self.jitter
        return max(0.0, base + random.uniform(-jitter_range, jitter_range))


def is_retryable(exc: BaseException) -> bool:
    """Decide whether an exception should be retried."""
    if isinstance(exc, NonRetryableError):
        return False
    if hasattr(exc, "retryable"):
        return bool(getattr(exc, "retryable"))
    retryable_names = (
        "TimeoutError",
        "URLError",
        "ConnectionError",
        "HTTPError",
        "TemporaryFailure",
    )
    return type(exc).__name__ in retryable_names


def execute_with_retry(
    func: Callable[[], T],
    policy: RetryPolicy | None = None,
    on_retry: Callable[[int, Exception, float], None] | None = None,
    sleep_fn: Callable[[float], None] | None = None,
) -> T:
    """Execute func with retry + exponential backoff."""
    policy = policy or RetryPolicy.from_config()
    sleep = sleep_fn or time.sleep
    last_error: Exception | None = None

    for attempt in range(policy.max_retries + 1):
        try:
            return func()
        except NonRetryableError:
            raise
        except Exception as exc:
            last_error = exc
            if not is_retryable(exc) or attempt >= policy.max_retries:
                if attempt >= policy.max_retries:
                    raise RetryExhausted(exc, attempt + 1) from exc
                raise

            delay = policy.compute_backoff(attempt)
            if on_retry is not None:
                on_retry(attempt + 1, exc, delay)
            sleep(delay)

    assert last_error is not None
    raise RetryExhausted(last_error, policy.max_retries + 1)
