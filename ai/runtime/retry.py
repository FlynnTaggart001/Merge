"""Deterministic timeout/retry/backoff primitives for AI provider calls."""

from __future__ import annotations

from dataclasses import dataclass
import random
import time
from typing import Callable, TypeVar


T = TypeVar("T")


@dataclass(frozen=True)
class RetryPolicy:
    max_retries: int = 2
    timeout_seconds: float = 60.0
    base_delay_seconds: float = 1.0
    max_delay_seconds: float = 30.0
    jitter_ratio: float = 0.20

    def delay(self, retry_number: int, rng: Callable[[], float] = random.random) -> float:
        raw = min(self.max_delay_seconds, self.base_delay_seconds * (2 ** max(0, retry_number - 1)))
        jitter = raw * self.jitter_ratio * rng()
        return min(self.max_delay_seconds, raw + jitter)


def execute_with_retry(
    operation: Callable[[], T],
    policy: RetryPolicy,
    is_retryable: Callable[[Exception], bool],
    sleep: Callable[[float], None] = time.sleep,
) -> T:
    """Execute an operation with bounded exponential backoff.

    Timeout enforcement belongs to the operation itself (for example urllib's
    socket timeout). This helper only decides whether another attempt is safe.
    """
    attempts = 0
    while True:
        try:
            return operation()
        except Exception as exc:
            if attempts >= policy.max_retries or not is_retryable(exc):
                raise
            attempts += 1
            sleep(policy.delay(attempts))
