# Merge — Skill Progression Specification

**Status:** APPROVED — gameplay baseline
**Engine:** Unreal Engine 5.8.1

## 1. Principle

Merge uses **learning by doing**. Skills improve through relevant gameplay actions rather than through a separate character-level system.

There are **45 canonical skills**, all starting at **5**. At character creation the player receives **30 specialization points**, with a maximum of **10 points per skill**, giving a maximum starting skill of **15**.

After character creation, skills are never increased by manually spending points. They increase through use.

## 2. Progression gained from an action

For a valid successful action, progression is calculated from the current skill level, action difficulty and Intelligence:

`P = 0.9 × max(0, (D - S + 15) / 50) × 1 / (1 + 0.012 × S) × (0.75 + 0.025 × I)`

Where:

- `P` = progression gained by the action;
- `D` = action difficulty;
- `S` = current skill level;
- `I` = Intelligence, on the canonical characteristic scale 0–20.

The action must first pass the skill progression validation/context rules. Repetitive actions performed only to farm progression must not receive normal progression.

## 3. Design behavior

The formula intentionally creates diminishing returns as skill increases and makes higher skill levels require appropriately difficult actions.

- Increasing `S` reduces progression from easy actions.
- Increasing `D` makes difficult actions more appropriate for advanced skills.
- Intelligence modifies progression without replacing the need to perform relevant actions.
- `max(0, ...)` prevents progression when the action is sufficiently below the required difficulty.

## 4. Skill XP / level thresholds

Skill progression is accumulated as skill XP/progression. The threshold system remains data-driven.

The current baseline threshold curve is:

`XP_required(level) = 100 × level^1.5`

This curve is a tuning baseline for the amount of accumulated progression associated with a target level; it is distinct from the **per-action progression formula** above.

## 5. High-level scale

Skill level **50 is already an extremely high / superhuman level of mastery**. The progression curve and action difficulties must preserve this meaning. Level 50 must not feel routine or easily attainable through low-difficulty repetition.

The system should therefore use increasingly demanding action difficulties and anti-farming validation at high skill levels.

## 6. Maximum and implementation

- The skill maximum is data-driven and must be enforced by the skill system.
- XP/progression values must be deterministic and suitable for save-game serialization.
- Gameplay-facing progression should use a consistent rounding policy.
- Skill → characteristic progression consumes validated skill progression events; see `specs/CHARACTERISTIC_PROGRESSION.md`.
- The canonical 45-skill list and skill → characteristic relationships are defined in `specs/CANONICAL_SKILLS.md`.

## 7. Terminology constraints

- **Lutte is not a Merge skill or characteristic.**
- **Parade** is the canonical skill name and belongs to **Défense / mouvement**.
- Do not invent missing canonical skills.
