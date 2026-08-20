"""Provider registry for the Merge orchestrator.

Providers are registered by the host runtime. No credentials or external
network calls belong in this repository module.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class ProviderDescriptor:
    provider_id: str
    capabilities: list[str]
    enabled: bool = False


class ProviderRegistry:
    def __init__(self) -> None:
        self._providers: dict[str, ProviderDescriptor] = {}

    def register(self, provider: ProviderDescriptor) -> None:
        self._providers[provider.provider_id] = provider

    def available_for(self, role: str) -> list[ProviderDescriptor]:
        return [
            provider
            for provider in self._providers.values()
            if provider.enabled and role in provider.capabilities
        ]

    def health(self) -> dict[str, bool]:
        return {provider.provider_id: provider.enabled for provider in self._providers.values()}
