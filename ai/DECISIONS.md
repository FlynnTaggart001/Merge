# AI Decision Log

## Statuses

- `PROPOSED` — suggestion not yet approved
- `SUGGESTION` — non-blocking improvement proposed by an agent
- `REVIEW` — important proposal requiring review
- `APPROVED` — explicitly accepted by the Game Director
- `PENDING_HUMAN` — requires Game Director decision
- `REJECTED` — explicitly rejected
- `SUPERSEDED` — replaced by a newer decision
- `BLOCKED` — cannot proceed without resolving a constraint

## Approved decisions

### DECISION-0001 — Unreal Engine 5
- **Status:** APPROVED
- **Decision:** Merge uses Unreal Engine 5.8.4.
- **Date:** 2026-08-19

### DECISION-0002 — Primary language
- **Status:** APPROVED
- **Decision:** C++ is the primary implementation language; Blueprint is complementary.
- **Date:** 2026-08-19

### DECISION-0003 — Merge AI toolchain
- **Status:** APPROVED
- **Decision:** The only selected AI tools for Merge development are ChatGPT Plus, Claude Code, and Wingman Premium.
- **Responsibilities:** ChatGPT Plus for interactive design/planning/review; Claude Code for repository-facing implementation and tests; Wingman Premium for Unreal Editor assistance.
- **Boundaries:** ChatGPT Plus is not OpenAI API access; Wingman is not assumed to have GitHub access; Claude Code runtime integration must not be claimed complete until a compatible adapter is tested end to end.
- **Handoff:** Changes made in Unreal must be documented and synchronized to GitHub using ai/HANDOFF_PROTOCOL.md.
- **Canonical details:** ai/TOOLCHAIN.md.
- **Date:** 2026-10-13

## Pending decisions

None recorded by the AI infrastructure at initialization.

## Runtime behavior

The runtime stores machine-readable decisions under `ai/runtime/state/decisions.json` when executed locally. It also preserves proposer/Devil's Advocate disagreements so minority opinions are not silently discarded.

## Rule

Agents must not convert `PROPOSED`, `SUGGESTION`, `REVIEW` or `PENDING_HUMAN` into `APPROVED` without explicit Game Director authorization.
