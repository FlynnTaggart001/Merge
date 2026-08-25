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
- **Decision:** Merge uses Unreal Engine 5.8.1.
- **Date:** 2026-08-19

### DECISION-0002 — Primary language
- **Status:** APPROVED
- **Decision:** C++ is the primary implementation language; Blueprint is complementary.
- **Date:** 2026-08-19

## Pending decisions

None recorded by the AI infrastructure at initialization.

## Runtime behavior

The runtime stores machine-readable decisions under `ai/runtime/state/decisions.json` when executed locally. It also preserves proposer/Devil's Advocate disagreements so minority opinions are not silently discarded.

## Rule

Agents must not convert `PROPOSED`, `SUGGESTION`, `REVIEW` or `PENDING_HUMAN` into `APPROVED` without explicit Game Director authorization.
