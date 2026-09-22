# Merge — Project State

**Last updated:** 2026-09-22

## Current state

- Preproduction documentation: established
- Game vision: established in `GAME_BIBLE.md`
- Technical architecture: approved
- Engine: **Unreal Engine 5.8.1** (documented choice)
- Primary language: C++ — approved
- Blueprint: complementary
- Unreal project scaffold: **created** (`Merge.uproject`, Source/, Config/)
- Unreal local compile / PIE: **must be validated on a machine with UE5**
- AI orchestration infrastructure: operational (Phase 0.5)
- AI team workflow: **implemented** — planning, dependency checks, role routing, least privilege, proposal/review, Devil's Advocate, human decision gate, handoffs, state persistence and follow-up planning
- Security/secrets policy: enforced
- CI: runtime guard tests + recommendation/team workflow tests + secrets hygiene
- Progression design: **canonical attribute-first creation + Learning by Doing** (`specs/CANONICAL_SKILLS.md`, `specs/CHARACTERISTIC_PROGRESSION.md`, `specs/SKILL_PROGRESSION.md`, `specs/PLAYER_PROGRESSION.md`)
  - 45 canonical skills
  - 6 characteristics (Force, Agilité, Perception, Intelligence, Volonté, Charisme)
  - Character creation: all characteristics start at 6/20, 26 points distributed freely, maximum 14/20
  - Initial skill values are derived automatically from the final characteristic profile
  - After creation: Learning by Doing + automatic characteristic progression
  - `specs/PROGRESSION_DESIGN_BASELINE_2026-09-16.md` is retained as a historical baseline and is superseded by the canonical rules above

## Current milestone

**Phase 1 — UE5 Foundation (scaffold delivered, local compile pending)**

## Immediate objectives

1. Open `Merge.uproject` with UE 5.8.1 and compile the `Merge` module.
2. Create foundation Blueprints + `L_TestArena` map.
3. Verify movement / camera / jump in PIE.
4. Only then start Core Game Systems (Phase 2).

## AI team baseline

- All AI calls go through `Orchestrator.execute()`.
- Hard token / budget / rate / circuit / retry controls remain mandatory.
- Objectives can be decomposed into validated task contracts.
- Dependencies and cycles are checked before work starts.
- Roles are assigned and routed through the provider registry.
- Least-privilege permissions are checked before execution.
- Important proposals receive an independent Devil's Advocate review.
- Critical decisions escalate to `PENDING_HUMAN`.
- Human-only actions require explicit `APPROVED` decisions.
- Proposer/Devil's Advocate disagreement evidence is persisted.
- Handoffs and resumable project state are persisted.
- Follow-up tasks can be generated after completion.

## Known blockers

- This environment cannot run Unreal Editor or compile UE C++.
  Local validation required (see `docs/UE5_SETUP.md`).
- Real provider/API connections are host configuration and are intentionally not stored in Git.

## Constraints

- Do not put core game rules only in Blueprint.
- Do not expand combat/inventory/quest systems until foundation PIE works.
- Do not allow AI to self-approve critical/destructive changes.
