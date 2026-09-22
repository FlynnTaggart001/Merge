# Merge — Characteristic Progression

**Status:** APPROVED
**Engine:** Unreal Engine 5.8.1

## Core rules

Merge separates skills from characteristics. Skills improve through learning by doing. Characteristics improve automatically from linked skill progression. There is no global character level for distributing points.

At character creation:
- all 6 characteristics start at **6/20**;
- the player receives **26 characteristic points**;
- maximum characteristic at creation: **14/20**;
- total initial characteristic pool: **62 points**;
- the player does not manually assign skill points.

Initial skill values are derived from the final creation-time characteristic profile:
- single-characteristic skill: `Characteristic × 4`;
- multi-characteristic skill: `average(Linked Characteristics) × 4`.

After creation, no manual skill or characteristic point allocation is allowed.

## Canonical relationships

The complete 45-skill list and skill → characteristic relationships are defined in `specs/CANONICAL_SKILLS.md`.

**Parade belongs to Défense / mouvement, not Combat.**

## Automatic characteristic progression

`CharacteristicProgress += SkillProgress × Weight`

Each characteristic has its own hidden progression pool and threshold curve. When a threshold for the next characteristic level is reached, the characteristic increases by +1 and surplus progression is retained:

```text
while CharacteristicProgress >= Threshold(C + 1):
    CharacteristicProgress -= Threshold(C + 1)
    C += 1
```

Weights, thresholds and characteristic limits are data-driven.

## Progression flow

```text
Gameplay action
    ↓
Validated skill progression
    ↓
Skill XP / progression
    ↓
Weighted characteristic contribution
    ↓
Characteristic threshold
    ↓
Characteristic +1
```

Characteristic progression inherits skill progression validation and anti-farming rules.

## Terminology constraints

- **Lutte is not a Merge skill or characteristic.**
- **Parade** is the canonical skill name and belongs to **Défense / mouvement**.
- Missing canonical names must never be invented.

## Scale

Skill level **50 is already an extremely high / superhuman level of mastery**. Progression balancing must respect this scale.
