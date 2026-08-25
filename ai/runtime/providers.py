"""Provider registry for the Merge orchestrator.

The registry contains runtime provider instances only. Credentials remain in
the host environment and are never serialized to Git.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class ProviderDescriptor:
    provider_id: str
    capabilities: list[str]
    enabled: bool = False
    provider: Any | None = None


class ProviderRegistry:
    def __init__(self) -> None:
        self._providers: dict[str, ProviderDescriptor] = {}

    def register(self, provider: ProviderDescriptor) -> None:
        self._providers[provider.provider_id] = provider

    def available_for(self, role: str) -> list[ProviderDescriptor]:
        return [
            provider
            for provider in self._providers.values()
            if provider.enabled and role in provider.capabilities and provider.provider is not None
        ]

    def get(self, provider_id: str) -> ProviderDescriptor:
        try:
            return self._providers[provider_id]
        except KeyError as exc:
            raise KeyError(f"Provider not registered: {provider_id}") from exc

    def health(self) -> dict[str, bool]:
        return {
            provider.provider_id: provider.enabled and provider.provider is not None
            for provider in self._providers.values()
        }
