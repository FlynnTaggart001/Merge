# Merge — Characteristic Progression Specification

**Status:** APPROVED — design baseline
**Engine:** Unreal Engine 5.8.1

## 1. Principle

Merge separates **skills** from **characteristics**.

- Skills improve through actual use (learning by doing).
- Characteristics are **not manually allocated after character creation**.
- A characteristic improves automatically from the progression of the skills associated with it.
- The player therefore develops a character organically through the actions they actually perform.

There is no global character level used to distribute attribute points.

## 2. Character creation

At character creation:

- all 45 skills begin at **5**;
- the player receives **30 specialization points**;
- 1 point adds +1 to one skill;
- a maximum of **10 points** may be invested into a single skill;
- therefore a skill can begin at a maximum of **15**.

After character creation, the player does **not** manually distribute skill or characteristic points.

## 3. Skill → characteristic progression

Each characteristic has a set of existing skills that contribute to it.

When a linked skill gains progression, that progression contributes to the characteristic's hidden progression pool according to the configured relationship weight.

```text
Skill progression
      ↓
Associated characteristic(s)
      ↓
Weighted characteristic progression
      ↓
Characteristic threshold reached
      ↓
Characteristic +1
      ↓
Progress continues toward the next threshold
```

A skill may contribute to more than one characteristic only where the final design establishes a genuine relationship.

### 3.1 Weighted contribution

The relationship is data-driven:

`CharacteristicProgress += SkillProgress × Weight`

The weight is a design value, not an assumption. Strongly representative skills can contribute more than partially related skills.

## 4. Characteristic progression scale

Characteristics use their **own progression scale**. They do not simply copy the level of a linked skill.

For a characteristic at level `C`, its hidden accumulated progression is compared with the threshold required for `C + 1`.

Conceptually:

```text
while CharacteristicProgress >= Threshold(C + 1):
    CharacteristicProgress -= Threshold(C + 1)
    C += 1
```

Excess progression is preserved and continues toward the next characteristic level.

## 5. Terminology constraints

**Lutte is not a Merge skill or characteristic** and must never be introduced as one.

**Parade** is the correct existing combat terminology. It must not be renamed or replaced by an invented skill name such as "Faille".

All future documentation must use the canonical names of the existing Merge skills and characteristics. Missing names must not be guessed.

## 6. Relationship with skill progression

Characteristic progression is downstream from skill progression.

The skill progression system calculates skill XP/progression. The characteristic system consumes the resulting progression events.

```text
Gameplay action
    ↓
Skill progression event
    ↓
Skill XP / skill level progression
    ↓
Characteristic contribution
    ↓
Characteristic threshold
```

This keeps characteristic growth connected to real gameplay instead of creating a second arbitrary progression source.

## 7. Anti-farming

Characteristic progression inherits the validation and anti-abuse rules of the underlying skill progression.

Meaningful, successful and contextually relevant actions should be rewarded; repetitive safe actions performed only to generate progression should not provide normal progression.

## 8. Data-driven architecture

Skill-to-characteristic relationships, weights, characteristic thresholds, minimum/maximum values and tuning parameters must be data-driven.

The C++ implementation must not hard-code the final skill/characteristic relationships into gameplay logic.

## 9. Pending design values

These values must be finalized from the canonical Merge lists before implementation:

- definitive list of 45 skills;
- definitive list of characteristics;
- skill → characteristic mapping;
- contribution weights;
- characteristic minimum/maximum;
- characteristic threshold curve;
- exact interaction with the skill maximum.

No missing skill or characteristic may be invented to complete the system.
