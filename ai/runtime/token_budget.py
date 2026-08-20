"""Hard token ceilings for provider-agnostic AI execution.

The runtime must reject work that exceeds a configured ceiling before it can
reach a paid provider. This module deliberately uses conservative token counts
supplied by the caller; provider integrations may replace the estimator with a
real tokenizer later without changing the enforcement contract.
"""

from __future__ import annotations

from dataclasses import dataclass


class TokenLimitError(ValueError):
    """Raised when a hard token ceiling would be exceeded."""


@dataclass
class TokenBudget:
    max_input_tokens: int
    max_output_tokens: int
    max_total_tokens: int
    input_used: int = 0
    output_used: int = 0

    @property
    def total_used(self) -> int:
        return self.input_used + self.output_used

    def authorize(self, input_tokens: int, output_tokens: int) -> bool:
        if input_tokens < 0 or output_tokens < 0:
            raise TokenLimitError("Token counts cannot be negative")
        if input_tokens > self.max_input_tokens:
            raise TokenLimitError("Input token hard limit exceeded")
        if output_tokens > self.max_output_tokens:
            raise TokenLimitError("Output token hard limit exceeded")
        if input_tokens + output_tokens > self.max_total_tokens:
            raise TokenLimitError("Total token hard limit exceeded")
        if self.input_used + input_tokens > self.max_input_tokens:
            raise TokenLimitError("Cumulative input token hard limit exceeded")
        if self.output_used + output_tokens > self.max_output_tokens:
            raise TokenLimitError("Cumulative output token hard limit exceeded")
        if self.total_used + input_tokens + output_tokens > self.max_total_tokens:
            raise TokenLimitError("Cumulative total token hard limit exceeded")
        return True

    def record(self, input_tokens: int, output_tokens: int) -> None:
        self.authorize(input_tokens, output_tokens)
        self.input_used += input_tokens
        self.output_used += output_tokens

    def remaining(self) -> tuple[int, int, int]:
        return (
            self.max_input_tokens - self.input_used,
            self.max_output_tokens - self.output_used,
            self.max_total_tokens - self.total_used,
        )
