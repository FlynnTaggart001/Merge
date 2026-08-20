# Merge — Project State

**Last updated:** 2026-08-20

## Current state

- Preproduction documentation: established
- Game vision: established in `GAME_BIBLE.md`
- Technical architecture: approved
- Engine: **Unreal Engine 5.5** (documented choice)
- Primary language: C++ — approved
- Blueprint: complementary
- Unreal project scaffold: **created** (`Merge.uproject`, Source/, Config/)
- Unreal local compile / PIE: **must be validated on a machine with UE5**
- AI orchestration infrastructure: operational (Phase 0.5)
- Security/secrets policy: enforced

## Current milestone

**Phase 1 — UE5 Foundation (scaffold delivered, local compile pending)**

## Immediate objectives

1. Open `Merge.uproject` with UE 5.5 and compile the `Merge` module.
2. Create foundation Blueprints + `L_TestArena` map.
3. Verify movement / camera / jump in PIE.
4. Only then start Core Game Systems (Phase 2).

## Safety baseline (AI)

- All AI calls through `Orchestrator.execute()`
- Token / budget / rate / circuit / retry enforced
- CI: `.github/workflows/ai-runtime.yml`

## Known blockers

- This environment cannot run Unreal Editor or compile UE C++.
  Local validation required (see `docs/UE5_SETUP.md`).

## Constraints

- Do not put core game rules only in Blueprint.
- Do not expand combat/inventory/quest systems until foundation PIE works.
