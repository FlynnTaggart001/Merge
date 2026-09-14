# Skill Progression — Merge

## Overview

Merge uses a **learning-by-doing** progression system. Skills improve through use rather than through a separate character-level system.

Each skill has its own XP value and maximum level.

## Core Formula

The XP required to reach a target skill level is:

**XP_required(level) = XP_base × level^difficulty**

Current design values:

- `XP_base = 100`
- `difficulty = 1.5`

Therefore:

**XP_required(level) = 100 × level^1.5**

This value represents the XP threshold associated with the target level.

## Examples

| Target level | XP required (approx.) |
|---:|---:|
| 2 | 283 |
| 3 | 520 |
| 4 | 800 |
| 5 | 1,118 |
| 10 | 3,162 |
| 25 | 12,500 |
| 50 | 35,355 |
| 100 | 100,000 |

Values should be rounded to whole XP for gameplay/UI presentation unless a future implementation explicitly requires fractional XP.

## Progression Toward the Next Level

For a skill currently at level `L`, the progress percentage toward level `L + 1` is:

**Progress_% = (Current_XP / XP_required(L + 1)) × 100**

The gameplay implementation must clamp this value to `[0, 100]` for UI purposes.

Example:

- Current XP: `400`
- Next-level threshold: approximately `520`
- Progress: `400 / 520 × 100 ≈ 76.9%`

## Implementation Requirements

The skill system should provide deterministic calculations for:

1. XP required for a target level.
2. Skill level corresponding to accumulated XP.
3. Progress percentage toward the next level.
4. Maximum skill level enforcement.
5. XP/level values suitable for save-game serialization.

The implementation should avoid floating-point instability at gameplay boundaries. XP thresholds presented to gameplay systems should use a consistent rounding policy.

## Design Intent

The exponent `1.5` creates a gradually increasing progression cost: early skill levels are relatively quick to obtain, while high skill levels require substantially more use. This supports the RPG's learning-by-doing philosophy without making early progression unnecessarily slow.

This formula is a **current gameplay baseline**, not a permanent balance guarantee. It should remain data-driven so `XP_base`, the exponent, and the maximum level can be tuned without rewriting the skill system.
