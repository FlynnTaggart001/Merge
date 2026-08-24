"""Recommendation and Devil's Advocate orchestration for Merge.

This module deliberately keeps the human in the decision loop. It runs a
normal guarded AI call, then a second guarded call in the DEVIL_ADVOCATE role.
The reviewer must emit a machine-readable verdict. No verdict can authorize a
critical change; critical reviews always escalate to PENDING_HUMAN.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re

from .orchestrator import Orchestrator, OrchestratorRequest, OrchestratorResponse


class RecommendationType(str, Enum):
    NO_CONCERN = "NO_CONCERN"
    SUGGESTION = "SUGGESTION"
    REVIEW = "REVIEW"
    PENDING_HUMAN = "PENDING_HUMAN"
    BLOCKED = "BLOCKED"


@dataclass(frozen=True)
class CriticalReview:
    task_id: str
    verdict: RecommendationType
    proposal: OrchestratorResponse
    review: OrchestratorResponse
    prompt: str


DEVIL_ADVOCATE_PROMPT = """You are the DEVIL_ADVOCATE for Merge.

You are a constructive teammate, not an opponent of the Game Director.
Your job is to actively try to disprove or improve the proposed approach.
Do not flatter it and do not assume the human decision is optimal.

Inspect the proposal for:
- edge cases and exploits;
- gameplay and player-experience problems;
- systemic side effects and interactions;
- contradictions with the project vision/specifications;
- performance and maintenance risks;
- unnecessary technical debt or scope creep;
- long-term consequences and irreversibility;
- missing information or unjustified assumptions.

Search for at least one serious alternative when one exists. For high-impact
proposals, provide 2-3 genuinely different alternatives.

Return this machine-readable header first:
VERDICT: NO_CONCERN | SUGGESTION | REVIEW | PENDING_HUMAN | BLOCKED

Then provide:
OBSERVATION:
WHY_IT_MATTERS:
ALTERNATIVES:
RECOMMENDED_OPTION:
CONFIDENCE:
IMPACT:
REVERSIBILITY:
DEPENDENCIES:
EVIDENCE:
REQUIRES_HUMAN_DECISION:

Never modify files and never approve execution yourself.
"""


class RecommendationEngine:
    """Runs a proposal through a normal agent and a separate critical review."""

    def __init__(self, proposer: Orchestrator, devil_advocate: Orchestrator) -> None:
        self.proposer = proposer
        self.devil_advocate = devil_advocate

    def review(self, request: OrchestratorRequest, *, critical: bool = True) -> CriticalReview:
        proposal = self.proposer.execute(request)
        if proposal.status != "ok":
            return CriticalReview(
                task_id=request.task_id,
                verdict=RecommendationType.BLOCKED,
                proposal=proposal,
                review=proposal,
                prompt=DEVIL_ADVOCATE_PROMPT,
            )

        review_request = OrchestratorRequest(
            task_id=f"{request.task_id}:devil-advocate",
            role="DEVIL_ADVOCATE",
            prompt=(
                DEVIL_ADVOCATE_PROMPT
                + "\n\nORIGINAL PROPOSAL:\n"
                + proposal.text
            ),
            estimated_input_tokens=min(
                self.devil_advocate.config.max_input_tokens,
                request.estimated_output_tokens + 1500,
            ),
            estimated_output_tokens=min(
                self.devil_advocate.config.max_output_tokens,
                1500,
            ),
            metadata={
                **request.metadata,
                "review_of": request.task_id,
                "review_type": "DEVIL_ADVOCATE",
            },
        )
        review = self.devil_advocate.execute(review_request)
        verdict = self._parse_verdict(review.text) if review.status == "ok" else RecommendationType.BLOCKED

        if critical and verdict not in (RecommendationType.BLOCKED, RecommendationType.PENDING_HUMAN):
            verdict = RecommendationType.PENDING_HUMAN

        return CriticalReview(
            task_id=request.task_id,
            verdict=verdict,
            proposal=proposal,
            review=review,
            prompt=DEVIL_ADVOCATE_PROMPT,
        )

    @staticmethod
    def _parse_verdict(text: str) -> RecommendationType:
        match = re.search(r"^VERDICT:\s*(NO_CONCERN|SUGGESTION|REVIEW|PENDING_HUMAN|BLOCKED)\b", text, re.MULTILINE)
        if not match:
            return RecommendationType.REVIEW
        return RecommendationType(match.group(1))
