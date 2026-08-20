"""Provider interface and mock implementations for Merge AI runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol
import time


@dataclass
class ProviderRequest:
    prompt: str
    task_id: str
    role: str
    estimated_input_tokens: int
    estimated_output_tokens: int = 0
    metadata: dict = field(default_factory=dict)


@dataclass
class ProviderResponse:
    provider_id: str
    text: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    latency_seconds: float
    status: str = "ok"


class ProviderError(Exception):
    """Base provider error. Set retryable=True for transient failures."""

    def __init__(self, message: str, *, retryable: bool = False) -> None:
        super().__init__(message)
        self.retryable = retryable


class AgentProvider(Protocol):
    provider_id: str

    def health_check(self) -> bool: ...

    def execute(self, request: ProviderRequest) -> ProviderResponse: ...


class MockProvider:
    """Deterministic mock provider for offline tests. Never hits the network."""

    def __init__(
        self,
        provider_id: str = "mock",
        *,
        fail_times: int = 0,
        fail_with: Exception | None = None,
        fixed_output_tokens: int = 50,
        fixed_cost: float = 0.01,
        latency: float = 0.01,
        timeout_after: float | None = None,
    ) -> None:
        self.provider_id = provider_id
        self._fail_times = fail_times
        self._fail_with = fail_with or ProviderError("simulated failure", retryable=True)
        self._fixed_output_tokens = fixed_output_tokens
        self._fixed_cost = fixed_cost
        self._latency = latency
        self._timeout_after = timeout_after
        self.calls: list[ProviderRequest] = []
        self._call_count = 0

    def health_check(self) -> bool:
        return True

    def execute(self, request: ProviderRequest) -> ProviderResponse:
        self.calls.append(request)
        self._call_count += 1

        if self._timeout_after is not None:
            time.sleep(self._timeout_after)
            raise TimeoutError("mock provider timeout")

        if self._call_count <= self._fail_times:
            raise self._fail_with

        time.sleep(self._latency)
        return ProviderResponse(
            provider_id=self.provider_id,
            text=f"[mock:{self.provider_id}] response for task {request.task_id}",
            input_tokens=request.estimated_input_tokens,
            output_tokens=self._fixed_output_tokens,
            cost_usd=self._fixed_cost,
            latency_seconds=self._latency,
            status="ok",
        )


class FailingProvider:
    """Always fails (useful for circuit-breaker tests)."""

    def __init__(self, provider_id: str = "failing", retryable: bool = True) -> None:
        self.provider_id = provider_id
        self._retryable = retryable
        self.calls: list[ProviderRequest] = []

    def health_check(self) -> bool:
        return False

    def execute(self, request: ProviderRequest) -> ProviderResponse:
        self.calls.append(request)
        raise ProviderError("permanent provider failure", retryable=self._retryable)
