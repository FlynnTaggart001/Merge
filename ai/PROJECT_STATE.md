# Merge — Project State

**Last updated:** 2026-08-20

## Current state

- Preproduction documentation: established
- Game vision: established in `GAME_BIBLE.md`
- Technical architecture: approved in `specs/TECHNICAL_ARCHITECTURE.md`
- Engine: Unreal Engine 5 — approved
- Primary language: C++ — approved
- Blueprint: complementary
- Unreal project/codebase: not yet bootstrapped
- AI orchestration infrastructure: being established
- Security/secrets policy: established
- Token/cost guardrails: established
- QA validation gate: established
- Shared orchestration protocol: established

## Current milestone

**Phase 0.5 — AI Development Infrastructure**

## Immediate objectives

1. Establish shared agent protocol.
2. Establish task/dependency tracking.
3. Establish handoffs and validation.
4. Establish safe autonomy rules.
5. Test local guardrails before external API integration.
6. Prepare Phase 1 Unreal bootstrap.

## API state

- API keys: not configured
- External AI providers: not connected
- `.env.example`: available
- Real secrets must remain outside Git.

## Safety baseline

- Request rate limits defined.
- Token limits defined.
- Task/session/day budgets defined.
- Timeout and retry limits defined.
- Concurrency limit defined.
- Circuit-breaker policy defined.

## Known blockers

No technical blocker currently recorded.

## Human decisions required

Only decisions explicitly marked `PENDING_HUMAN` in `DECISIONS.md` block automated work.

## Important constraints

- Do not change approved engine/language decisions without Game Director approval.
- Do not invent missing game design decisions.
- Do not claim tests/builds were executed unless actually executed.
- Preserve the PS1 1996–1999 visual target.
- Never commit credentials or bypass resource limits.
