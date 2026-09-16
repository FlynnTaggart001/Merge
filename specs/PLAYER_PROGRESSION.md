# Merge — Player Progression Specification

**Status:** APPROVED — canonical progression architecture
**Engine:** Unreal Engine 5.8.1

## 1. Core principle

Merge uses **learning by doing**.

The player does not gain a generic level that distributes points into attributes or skills. Skills improve through meaningful, validated use. The resulting skill progression automatically feeds the linked characteristics.

After character creation, the player never manually distributes skill or characteristic points again.

## 2. Canonical character model

Merge has **45 unique skills** and **6 canonical characteristics**.

### Characteristics

- Force
- Agilité
- Perception
- Intelligence
- Volonté
- Charisme

### Skills

The complete skill list and every skill → characteristic relationship are defined exclusively in:

`specs/CANONICAL_SKILLS.md`

That document is the source of truth for names, categories and relationships.

## 3. Character creation

At character creation:

- all 45 skills start at **5**;
- the player receives **30 specialization points**;
- at most **10 points** may be invested in one skill;
- therefore the maximum starting value of a skill is **15**.

There is no manual skill/characteristic point allocation after creation.

## 4. Skill progression

A skill progresses when the player performs a relevant action successfully and the progression system validates that the action is meaningful.

The action progression baseline is defined in `specs/SKILL_PROGRESSION.md`.

The system must reject or strongly reduce progression from artificial farming, including repetitive actions performed only to generate progression.

### 4.1 Action progression

The current baseline formula is:

```text
P = 0.9 × max(0, (D - S + 15) / 50)
    × 1 / (1 + 0.012 × S)
    × (0.75 + 0.025 × I)
```

Where:

- `P` = progression gained;
- `D` = action difficulty;
- `S` = current skill level;
- `I` = Intelligence on the 0–20 characteristic scale.

This formula is for **skill progression from an action**. It must not be confused with the characteristic threshold system.

## 5. Characteristic progression

Characteristics do not receive points directly from the player.

Validated skill progression feeds the linked characteristics:

```text
CharacteristicProgress += SkillProgress × Weight
```

Each characteristic has a hidden progression pool and data-driven thresholds.

When a threshold is reached:

```text
while CharacteristicProgress >= Threshold(C + 1):
    CharacteristicProgress -= Threshold(C + 1)
    C += 1
```

Surplus progression is retained.

The characteristic system must not create a separate arbitrary source of progression that bypasses validated skill progression.

## 6. Characteristic scale

The canonical characteristic scale is **0–20**.

The exact threshold curve and numerical weights are data-driven and belong to the characteristic progression specification.

The six characteristics are not interchangeable with skills. A characteristic represents a broad underlying capability; a skill represents learned practical mastery.

## 7. Magic

Magic is represented by the seven canonical Magic skills listed in `specs/CANONICAL_SKILLS.md`.

For all seven:

**Volonté is the primary characteristic.**

**Intelligence is secondary.**

Volonté represents the mental force required to impose, sustain and control magic. Intelligence represents understanding, learning and technical comprehension of magical principles.

The canonical relationships are therefore:

```text
Invocation          → Volonté + Intelligence
Nécromancie         → Volonté + Intelligence
Contrôle mental     → Volonté + Intelligence
Magie élémentaire   → Volonté + Intelligence
Magie physique      → Volonté + Intelligence
Magie de groupe     → Volonté + Intelligence
Magie de pacte      → Volonté + Intelligence
```

No separate generic magic attribute, magic skill or hidden progression system may be introduced without updating the canonical skill specification first.

## 8. Progression validation and anti-farming

Progression events must be validated according to gameplay context.

The system should support data-driven rules for:

- required context;
- meaningful success;
- minimum intensity or difficulty;
- repetition detection;
- diminishing returns;
- frequency limits;
- prevention of actions performed solely for farming.

The objective is to reward genuine learning rather than input repetition.

## 9. Skill level scale

**Skill level 50 already represents extremely high / superhuman mastery.**

Progression balancing must preserve this meaning. Low-difficulty repetitive actions must not make level 50 routine or quickly attainable.

Higher skill levels require appropriately difficult and varied actions.

## 10. Classes and paths

Classes are derived progressively from the player's developing skill/characteristic profile rather than being freely selected as a conventional class at character creation.

When a new path becomes available:

1. the player is notified;
2. the class name is revealed;
3. its progression path can then be pursued through gameplay.

Only **fundamental classes** are planned as normal classes.

**Déité** is a special case and is not treated as an ordinary fundamental class.

Detailed fundamental-class requirements must be defined in the class specification before implementation. They must not be invented elsewhere in the repository.

## 11. Canonical terminology constraints

- **Lutte is not a Merge skill or characteristic.**
- **Parade** is a canonical skill and belongs exclusively to **Défense / mouvement**.
- The canonical skill count is **45 unique skills**.
- The canonical characteristic count is **6**.
- Do not reintroduce obsolete progression concepts such as Endurance, Défense, Réflexe or Domptage as skills/characteristics unless they are explicitly added to the canonical system.

## 12. Source-of-truth hierarchy

When two documents appear to disagree, use this hierarchy:

1. `specs/CANONICAL_SKILLS.md` — canonical skills, categories and skill → characteristic relationships.
2. `specs/SKILL_PROGRESSION.md` — skill action progression and skill-level curve.
3. `specs/CHARACTERISTIC_PROGRESSION.md` — characteristic progression, weights and thresholds.
4. Other gameplay documents — implementation/design context only; they must not redefine the canonical progression system.

Any future progression change must update the relevant source-of-truth document and then remove obsolete terminology from dependent documents.
