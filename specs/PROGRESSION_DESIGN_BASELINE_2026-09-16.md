# Merge — Progression Design Baseline — 2026-09-16

**Status:** HISTORICAL BASELINE — superseded by the canonical attribute-first creation rules on 2026-09-22
**Engine:** Unreal Engine 5.8.1

## 1. Skills

Merge has **45 unique canonical skills**. The complete list and skill → characteristic relationships are maintained in `specs/CANONICAL_SKILLS.md`.

### Character creation

The previous skill-point creation model is superseded.

- All 6 characteristics start at **6/20**.
- The player receives **26 characteristic points**.
- Maximum characteristic at creation: **14/20**.
- Total initial characteristic pool: **62 points**.
- No skill points are distributed manually.

Initial skills are derived from the resulting characteristic profile:
- single characteristic: `Characteristic × 4`;
- multiple characteristics: `average(Linked Characteristics) × 4`.

After creation, progression is Learning by Doing.

### Learning by doing

Skills increase through relevant gameplay actions. The action progression formula is:

`P = 0.9 × max(0, (D - S + 15) / 50) × 1 / (1 + 0.012 × S) × (0.75 + 0.025 × I)`

Where `P` is progression gained, `D` is action difficulty, `S` is current skill level and `I` is Intelligence (scale 0–20).

The action must be valid, successful and contextually relevant. Anti-farming rules prevent repetitive low-value actions from becoming a normal progression source.

### Scale

Skill level **50 is already an extremely high / superhuman level of mastery**. High skill levels must require appropriately difficult actions and must not be routine to reach through repetition.

## 2. Characteristics

Characteristics are separate from skills and increase **automatically** from linked skill progression.

They have their own hidden progression pools and thresholds. They do not simply copy skill levels.

Canonical characteristics (scale 0–20):
- Force
- Agilité
- Perception
- Intelligence
- Volonté
- Charisme

For each configured relationship:

`CharacteristicProgress += SkillProgress × Weight`

When the next characteristic threshold is reached, the characteristic increases by +1 and surplus progression is retained for the following threshold.

Weights, thresholds and characteristic limits are data-driven.

## 3. Canonical terminology

- **Parade** belongs to **Défense / mouvement**.
- **Parade is not a Combat skill.**
- **Lutte is not a Merge skill or characteristic** and must never be introduced as one.
- Canonical names must not be replaced or invented.

## 4. Classes / paths

The class system uses **fundamental classes only** as the normal class layer. There is one exceptional class: **Déité**, which is a special case and is not treated like the ordinary fundamental classes.

A class/path is determined by the player's **characteristic profile**: the distribution and levels of the six characteristics are what qualify the player for a class/path. The underlying skills matter indirectly because they are what make the characteristics progress.

If the player does not yet have enough progression in the characteristics required by a class/path, that class/path is not available yet. The player must continue playing and naturally develop the required profile.

The player should be **notified when a new path becomes available**. The **class/path name is revealed when the corresponding class/path becomes available**.

The exact final list and qualification conditions of the fundamental classes must be defined before implementation; no class names are to be invented prematurely.

## 5. Architecture intent

The progression system must remain data-driven. Skill definitions, skill → characteristic relationships, contribution weights, thresholds and class/path qualification conditions should be represented as data rather than hard-coded gameplay rules.

Skill progression is the source event for characteristic progression. Characteristic progression and class/path recognition consume progression state rather than creating a second artificial leveling system.
