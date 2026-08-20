"""Provider-independent sliding-window rate limiter for AI calls."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import time


@dataclass(frozen=True)
class RateLimit:
    max_calls: int
    window_seconds: float


class RateLimiter:
    """Fail-closed limiter. Callers must ask before starting an external request."""

    def __init__(self, limits: list[RateLimit] | None = None) -> None:
        self.limits = limits or [
            RateLimit(30, 60.0),
            RateLimit(500, 3600.0),
        ]
        self._timestamps: deque[float] = deque()

    def allow(self, now: float | None = None) -> bool:
        current = time.monotonic() if now is None else now
        longest_window = max(limit.window_seconds for limit in self.limits)
        cutoff = current - longest_window
        while self._timestamps and self._timestamps[0] < cutoff:
            self._timestamps.popleft()

        for limit in self.limits:
            window_start = current - limit.window_seconds
            calls = sum(ts >= window_start for ts in self._timestamps)
            if calls >= limit.max_calls:
                return False
        return True

    def record(self, now: float | None = None) -> None:
        if not self.allow(now):
            raise RuntimeError("AI rate limit exceeded")
        self._timestamps.append(time.monotonic() if now is None else now)
