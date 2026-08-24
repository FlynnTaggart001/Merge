"""Offline tests for the Merge recommendation/Devil's Advocate layer."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from ai.runtime.config import RuntimeConfig
from ai.runtime.orchestrator import Orchestrator, OrchestratorRequest
from ai.runtime.provider_base import ProviderResponse
from ai.runtime.recommendation_engine import RecommendationEngine, RecommendationType


class ScriptedProvider:
    provider_id = "scripted"

    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.calls = []

    def health_check(self):
        return True

    def execute(self, request):
        self.calls.append(request)
        text = self.outputs.pop(0)
        return ProviderResponse(
            provider_id=self.provider_id,
            text=text,
            input_tokens=request.estimated_input_tokens,
            output_tokens=50,
            cost_usd=0.01,
            latency_seconds=0.0,
        )


def _cfg():
    return RuntimeConfig(
        max_input_tokens=5000,
        max_output_tokens=2000,
        max_total_tokens_per_task=10000,
        max_total_tokens_per_session=20000,
        max_cost_per_call_usd=1.0,
        max_cost_per_task_usd=5.0,
        max_cost_per_session_usd=10.0,
        max_cost_per_day_usd=20.0,
        max_cost_per_month_usd=100.0,
        warning_ratio=0.7,
        max_calls_per_minute=30,
        max_calls_per_hour=100,
        request_timeout_seconds=5.0,
        max_retries=0,
        initial_backoff_seconds=0.01,
        max_backoff_seconds=0.05,
        backoff_multiplier=2.0,
        backoff_jitter=0.0,
        failure_threshold=5,
        cooldown_seconds=60.0,
        max_iterations=10,
        max_handoffs=20,
        mode="supervised",
    )


def _request():
    return OrchestratorRequest(
        task_id="REC-001",
        role="GAMEPLAY_DESIGNER",
        prompt="Propose an important gameplay change.",
        estimated_input_tokens=100,
        estimated_output_tokens=200,
    )


def test_critical_review_always_reaches_human():
    proposer = Orchestrator(
        ScriptedProvider(["Proposal: add adaptive reproduction."]),
        config=_cfg(),
        sleep_fn=lambda _: None,
    )
    reviewer = Orchestrator(
        ScriptedProvider([
            "VERDICT: NO_CONCERN\nOBSERVATION: none\nALTERNATIVES: one\n"
        ]),
        config=_cfg(),
        sleep_fn=lambda _: None,
    )

    result = RecommendationEngine(proposer, reviewer).review(_request(), critical=True)

    assert result.verdict is RecommendationType.PENDING_HUMAN
    assert len(reviewer.provider.calls) == 1
    assert reviewer.provider.calls[0].role == "DEVIL_ADVOCATE"


def test_non_critical_review_preserves_suggestion():
    proposer = Orchestrator(
        ScriptedProvider(["Proposal: improve loot readability."]),
        config=_cfg(),
        sleep_fn=lambda _: None,
    )
    reviewer = Orchestrator(
        ScriptedProvider(["VERDICT: SUGGESTION\nOBSERVATION: readability can improve."]),
        config=_cfg(),
        sleep_fn=lambda _: None,
    )

    result = RecommendationEngine(proposer, reviewer).review(_request(), critical=False)

    assert result.verdict is RecommendationType.SUGGESTION


def test_missing_machine_verdict_is_safe_review():
    proposer = Orchestrator(
        ScriptedProvider(["Proposal: change a major system."]),
        config=_cfg(),
        sleep_fn=lambda _: None,
    )
    reviewer = Orchestrator(
        ScriptedProvider(["This is not machine-readable."]),
        config=_cfg(),
        sleep_fn=lambda _: None,
    )

    result = RecommendationEngine(proposer, reviewer).review(_request(), critical=False)

    assert result.verdict is RecommendationType.REVIEW


if __name__ == "__main__":
    for test in (
        test_critical_review_always_reaches_human,
        test_non_critical_review_preserves_suggestion,
        test_missing_machine_verdict_is_safe_review,
    ):
        test()
        print(f"PASS {test.__name__}")
    print("3/3 passed")
