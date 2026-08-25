"""Recommendation and Devil's Advocate orchestration for Merge."""

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
    confidence: float = 0.0
    requires_human: bool = False


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
CONFIDENCE: 0.00-1.00
IMPACT:
REVERSIBILITY:
DEPENDENCIES:
EVIDENCE:
REQUIRES_HUMAN_DECISION: YES | NO

Never modify files and never approve execution yourself.
"""


class RecommendationEngine:
    """Runs a proposal through a normal agent and a separate critical review."""

    def __init__(self, proposer: Orchestrator, devil_advocate: Orchestrator, *, human_confidence_threshold: float = 0.75) -> None:
        if not 0.0 < human_confidence_threshold <= 1.0:
            raise ValueError("human_confidence_threshold must be in (0, 1]")
        self.proposer = proposer
        self.devil_advocate = devil_advocate
        self.human_confidence_threshold = human_confidence_threshold

    def review(self, request: OrchestratorRequest, *, critical: bool = True) -> CriticalReview:
        proposal = self.proposer.execute(request)
        if proposal.status != "ok":
            return CriticalReview(request.task_id, RecommendationType.BLOCKED, proposal, proposal, DEVIL_ADVOCATE_PROMPT)

        review_request = OrchestratorRequest(
            task_id=f"{request.task_id}:devil-advocate", role="DEVIL_ADVOCATE",
            prompt=DEVIL_ADVOCATE_PROMPT + "\n\nORIGINAL PROPOSAL:\n" + proposal.text,
            estimated_input_tokens=min(self.devil_advocate.config.max_input_tokens, request.estimated_output_tokens + 1500),
            estimated_output_tokens=min(self.devil_advocate.config.max_output_tokens, 1500),
            metadata={**request.metadata, "review_of": request.task_id, "review_type": "DEVIL_ADVOCATE"},
        )
        review = self.devil_advocate.execute(review_request)
        if review.status != "ok":
            return CriticalReview(request.task_id, RecommendationType.BLOCKED, proposal, review, DEVIL_ADVOCATE_PROMPT)

        verdict = self._parse_verdict(review.text)
        confidence = self._parse_confidence(review.text)
        requires_human = self._parse_human_request(review.text)
        if critical or requires_human or confidence < self.human_confidence_threshold:
            if verdict is not RecommendationType.BLOCKED:
                verdict = RecommendationType.PENDING_HUMAN

        return CriticalReview(request.task_id, verdict, proposal, review, DEVIL_ADVOCATE_PROMPT, confidence, requires_human)

    @staticmethod
    def _parse_verdict(text: str) -> RecommendationType:
        match = re.search(r"^VERDICT:\s*(NO_CONCERN|SUGGESTION|REVIEW|PENDING_HUMAN|BLOCKED)\b", text, re.MULTILINE)
        return RecommendationType(match.group(1)) if match else RecommendationType.REVIEW

    @staticmethod
    def _parse_confidence(text: str) -> float:
        match = re.search(r"^CONFIDENCE:\s*(0(?:\.\d+)?|1(?:\.0+)?)\s*$", text, re.MULTILINE | re.IGNORECASE)
        if not match:
            return 0.0
        return float(match.group(1))

    @staticmethod
    def _parse_human_request(text: str) -> bool:
        match = re.search(r"^REQUIRES_HUMAN_DECISION:\s*(YES|NO)\s*$", text, re.MULTILINE | re.IGNORECASE)
        return bool(match and match.group(1).upper() == "YES")
