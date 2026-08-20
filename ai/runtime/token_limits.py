"""Hard token limit enforcement for Merge AI requests.

Fail-closed: any request that exceeds configured token ceilings is rejected
before a provider is ever called.
"""

from __future__ import annotations

from dataclasses import dataclass

from .config import RuntimeConfig, DEFAULT_CONFIG


class TokenLimitExceeded(Exception):
    """Raised when a token ceiling would be breached."""

    def __init__(self, message: str, limit_type: str) -> None:
        super().__init__(message)
        self.limit_type = limit_type


@dataclass
class TokenUsage:
    input_tokens: int = 0
    output_tokens: int = 0

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens


class TokenGuard:
    """Enforces max input / output / total token limits."""

    def __init__(self, config: RuntimeConfig | None = None) -> None:
        self.config = config or DEFAULT_CONFIG
        self.task_tokens = 0
        self.session_tokens = 0

    def check_request(self, estimated_input: int, estimated_output: int = 0) -> None:
        """Validate estimated tokens before calling a provider. Fail closed."""
        if estimated_input < 0 or estimated_output < 0:
            raise TokenLimitExceeded("Negative token estimate is invalid", "invalid")

        if estimated_input > self.config.max_input_tokens:
            raise TokenLimitExceeded(
                f"Input tokens {estimated_input} exceed max {self.config.max_input_tokens}",
                "max_input",
            )

        if estimated_output > self.config.max_output_tokens:
            raise TokenLimitExceeded(
                f"Output tokens {estimated_output} exceed max {self.config.max_output_tokens}",
                "max_output",
            )

        projected_total = estimated_input + estimated_output

        if self.task_tokens + projected_total > self.config.max_total_tokens_per_task:
            raise TokenLimitExceeded(
                f"Task token budget exceeded: {self.task_tokens + projected_total} > "
                f"{self.config.max_total_tokens_per_task}",
                "max_task",
            )

        if self.session_tokens + projected_total > self.config.max_total_tokens_per_session:
            raise TokenLimitExceeded(
                f"Session token budget exceeded: {self.session_tokens + projected_total} > "
                f"{self.config.max_total_tokens_per_session}",
                "max_session",
            )

    def record(self, usage: TokenUsage) -> None:
        """Record actual usage after a successful (or partial) call."""
        self.task_tokens += usage.total_tokens
        self.session_tokens += usage.total_tokens

    def reset_task(self) -> None:
        self.task_tokens = 0

    def reset_session(self) -> None:
        self.task_tokens = 0
        self.session_tokens = 0
