"""Fail-safe circuit breaker for unreliable AI providers."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import time


class CircuitState(str, Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"


@dataclass
class CircuitBreaker:
    failure_threshold: int = 5
    cooldown_seconds: float = 300.0
    state: CircuitState = CircuitState.CLOSED
    failures: int = 0
    opened_at: float | None = None

    def allow(self, now: float | None = None) -> bool:
        current = time.monotonic() if now is None else now
        if self.state is CircuitState.CLOSED:
            return True
        if self.state is CircuitState.OPEN:
            if self.opened_at is not None and current - self.opened_at >= self.cooldown_seconds:
                self.state = CircuitState.HALF_OPEN
                return True
            return False
        return True

    def record_success(self) -> None:
        self.failures = 0
        self.opened_at = None
        self.state = CircuitState.CLOSED

    def record_failure(self, now: float | None = None) -> None:
        current = time.monotonic() if now is None else now
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.state = CircuitState.OPEN
            self.opened_at = current

    def reset(self) -> None:
        self.failures = 0
        self.opened_at = None
        self.state = CircuitState.CLOSED
