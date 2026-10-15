# Merge — Weapons and Equipment Specification

**Status:** SPÉCIFIÉ — system architecture and canonical rules  
**Engine:** Unreal Engine 5.8.1  
**Canonical combat reference:** `specs/COMBAT_SYSTEM_SPEC.md`

---

## 1. Overview

This specification defines the properties, mechanics, and data-driven architecture for weapons and equipment in Merge. It complements the combat system defined in `specs/COMBAT_SYSTEM_SPEC.md` by establishing how weapons scale damage, degrade, and interact with the character progression system.

## 2. Weapon Families

The following weapon families exist in Merge:

- Sword (Épée)
- Axe (Hache)
- Mace (Masse)
- Lance (Lance)
- Dagger (Dague)
- Two-Handed Weapon (Arme à deux mains)
- Bow (Arc)
- Crossbow (Arbalète)
- Unarmed Combat (Combat à mains nues)

Each family has unique attack properties, animations, and mastery skill. Refer to `specs/CANONICAL_SKILLS.md` for the mastery skills corresponding to each weapon family.

## 3. Damage Calculation

### 3.1 Damage Formula (Canonical)

Damage dealt by a physical weapon attack is calculated as:

```
Damage = Weapon_Base_Damage
       × (1 + Weapon_Mastery × 0.005)
       × (1 + Strength × 0.02)
       × Armor_Modifier
       × Other_Modifiers
```

Where:

- **Weapon_Base_Damage:** fixed base damage value for the weapon;
- **Weapon_Mastery:** player's mastery level in the relevant weapon family (0–100);
- **Strength:** player's Strength characteristic (0–20);
- **Armor_Modifier:** deterministic protection coefficient based on physical damage property and armor category;
- **Other_Modifiers:** contextual modifiers such as critical damage, buffs, or special effects.

Maximum weapon mastery therefore contributes **+50% damage** and each point of Strength contributes **+2% physical damage**, for a maximum Strength contribution of **+40%** at 20/20.

### 3.2 Base Damage Values (Fixed)

**Canonical principle:** Weapons of the same family and category use the same base damage value.

Example: All standard iron swords have the same base damage. A superior-quality sword does not use a different base—quality affects durability, not damage directly.

**Exact base values per weapon type:** À DÉFINIR during implementation phase.

### 3.3 Weapon Mastery Contribution

A player's skill level in the weapon family directly increases damage. This reflects genuine combat experience.

**Canonical rule:** each mastery point contributes **0.5%** to the weapon mastery damage multiplier.

Therefore:

- Mastery 0 → +0% damage
- Mastery 20 → +10% damage
- Mastery 40 → +20% damage
- Mastery 60 → +30% damage
- Mastery 80 → +40% damage
- Mastery 100 → **+50% damage**

Mastery progresses through Learning by Doing (see `specs/SKILL_PROGRESSION.md`).

### 3.4 Strength Contribution

Strength provides a fixed, deterministic bonus to physical damage.

**Canonical rule:** each point of Strength adds **2%** to the physical damage multiplier.

```
Strength_Bonus_Multiplier = 1 + (Strength × 0.02)
```

Therefore:

- Strength 0 → +0% damage
- Strength 5 → +10% damage
- Strength 10 → +20% damage
- Strength 15 → +30% damage
- Strength 20 → +40% damage

Strength ranges from 0–20. This bonus is deterministic and does not introduce damage randomization.

### 3.5 Physical Damage Properties

Weapons have three physical damage properties:

- **Slashing (Tranchant):** cutting damage, typically from swords and axes
- **Piercing (Perforant):** penetrating damage, typically from spears and arrows
- **Blunt (Contondant):** impact damage, typically from maces and other dedicated blunt weapons

These properties are characteristics of weapons, not independent primary damage categories.

Merge has only two armor categories: **Light Armor** and **Heavy Armor**. There is no Medium Armor category.

Armor protection is deterministic and uses the following damage-reduction coefficients:

| Physical property | Light Armor | Heavy Armor |
|---|---:|---:|
| **Slashing** | **35% reduction** | **60% reduction** |
| **Piercing** | **30% reduction** | **45% reduction** |
| **Blunt** | **25% reduction** | **40% reduction** |

Therefore an attack dealing 100 damage before armor deals:

- Slashing vs Light Armor → 65 damage
- Piercing vs Light Armor → 70 damage
- Blunt vs Light Armor → 75 damage
- Slashing vs Heavy Armor → 40 damage
- Piercing vs Heavy Armor → 55 damage
- Blunt vs Heavy Armor → 60 damage

The intended hierarchy is:

- Light Armor provides meaningful protection against all three properties, with piercing slightly favored against it.
- Heavy Armor is strongest against slashing, less resistant to piercing, and least resistant to blunt damage.

**Canonical weapon rule:** weapons whose primary physical property is blunt are two-handed weapons. Their strong performance against heavy armor is therefore balanced by the two-handed weapon constraint.

## 4. Durability and Breakage

### 4.1 Durability System

All weapons possess a durability value (also called "condition" or "wear"):

- **Current durability:** ranges from 0% to 100%
- **Maximum durability:** the upper limit for a specific weapon
- **Durability loss:** weapons lose durability with use, environmental effects, and damage taken

### 4.2 Breakage

When durability reaches **0%:**

- The weapon becomes **broken and unusable**
- Attacks with the broken weapon deal no damage (mechanically it cannot be equipped or used in combat)
- The weapon cannot be used in any context until repaired

### 4.3 Exceptional Weapons

Certain legendary or magical weapons may be defined to have **no durability bar**, meaning they never break. This is an exception that must be explicitly declared in the weapon's definition data.

**Canonical rule:** Only specially designated weapons are exempt from durability. Standard weapons always have a durability bar.

## 5. Repair Mechanics

### 5.1 Repair Effect

A repair action on a broken or damaged weapon restores it to **100% durability** (full condition).

Repairs are binary: a weapon is either fully repaired or not repaired at all. There is no partial repair.

### 5.2 Repair Cost

The cost to repair a weapon depends on the player's **Forge** skill (see `specs/CANONICAL_SKILLS.md`):

- **High Forge skill:** repairs cost fewer resources
- **Low Forge skill:** repairs cost more resources
- **Formula for resource cost:** À DÉFINIR

### 5.3 Scaling by Forge Mastery

As Forge skill increases (through Learning by Doing), repairs become cheaper:

```
Repair_Cost = Base_Cost × (1 - Forge_Skill_Scaling × Forge_Skill_Level)
```

Where:

- **Base_Cost:** base cost for repairing that weapon (to be defined per weapon or weapon type)
- **Forge_Skill_Scaling:** scaling factor for Forge skill (e.g., 0.01 per skill point)
- **Forge_Skill_Level:** player's Forge skill (0–100)

Exact formulas and scaling factors: À DÉFINIR

### 5.4 Repair Availability

NPCs with the Forge skill can repair weapons. Availability may depend on:

- Faction reputation (see `specs/REPUTATION_SYSTEM.md`)
- Location (whether a blacksmith is present)
- Resources available to the NPC

Details: À DÉFINIR

## 6. Quality and Degradation

### 6.1 Quality Definition

**Quality** is a property of weapons that does NOT directly increase damage output.

Quality affects **resistance to degradation:**

- **Common quality:** durability degrades faster with use
- **Rare quality:** durability degrades slowly
- **Legendary quality:** durability degrades very slowly or not at all

### 6.2 Quality Scaling

The exact relationship between quality level and degradation rate: À DÉFINIR

Example (pending confirmation):
```
Durability_Loss_Per_Hit = Base_Loss / (1 + Quality_Resistance_Scaling × Quality_Level)
```

### 6.3 Quality Acquisition

How weapons of different quality are acquired (loot, crafting, trade): À DÉFINIR

## 7. Weight and Attack Speed

### 7.1 Fixed Weapon Properties

**Canonical principle:** Weapon weight and attack speed are **fixed values**, not randomized.

- **Weight (Poids):** each weapon has a specific, unchanging weight value
- **Attack Speed (Vitesse d'attaque):** each weapon has a specific, unchanging animation/action timing

### 7.2 Mechanical Impact

These properties may have consequences (to be defined in future specifications):

- Weight may affect character mobility, stagger resistance, or endurance costs
- Attack speed determines how frequently the weapon can be used
- These are data-driven parameters, not subject to random variation

### 7.3 No Randomization

Canonical rule: **Do not introduce randomization into weight or attack speed.**

Randomness should be reserved for elements that truly benefit gameplay (e.g., random encounters, loot tables with genuine choice). Fixed properties like these are more predictable and allow for better balance and player agency.

## 8. Weapon Properties and Data Structure

### 8.1 Data-Driven Architecture

All weapon properties are stored in data tables (e.g., `DT_Weapons.uasset` in Unreal), not hardcoded in engine systems.

Properties defined per weapon:

| Property | Type | Example | Mutable |
|---|---|---|---|
| Weapon_ID | String | "sword_iron_001" | No |
| Display_Name | String | "Iron Sword" | No |
| Family | Enum | Sword | No |
| Base_Damage | Float | 15.0 | No |
| Weight | Float | 2.5 kg | No |
| Attack_Speed | Float | 1.0 sec/swing | No |
| Physical_Property | Enum | Slashing | No |
| Durability_Max | Float | 100.0% | No |
| Quality_Level | Enum | Common / Rare / Legendary | No |
| Icon | Texture | Item icon | No |
| Description | String | Flavor text | No |

Additional properties may be added as design requirements clarify.

## 9. Randomization Policy

### 9.1 What Can Be Random

Randomness should be applied to:

- **Encounter generation:** enemies, encounters, events
- **Loot tables:** which weapons drop from which enemies
- **World events:** weather, natural disasters, dynamic encounters
- **Quest variation:** similar quests with different specific details

### 9.2 What Must NOT Be Random

Randomness must NOT be applied to:

- **Weapon base damage** (must be fixed)
- **Weapon weight** (must be fixed)
- **Weapon attack speed** (must be fixed)
- **Character progression** (skill points are earned through Learning by Doing, not random)

### 9.3 Rationale

Fixed properties allow:
- Players to make informed equipment choices
- Balance and predictability in combat
- Mastery through experience rather than luck
- Clear cause-and-effect in gameplay

## 10. Critical Strikes

### 10.1 Critical Multiplier (Canonical)

Critical strikes deal **2.0× the normal damage**.

```
Critical_Damage = Normal_Damage × 2.0
```

This multiplier applies to the final damage calculation after all other modifiers have been applied.

### 10.2 Critical Chance Modifiers

Probability of landing a critical strike on a normal attack is influenced by:

- **Agility:** higher Agility increases critical chance
- **Perception:** higher Perception increases critical chance (especially relevant for detecting and exploiting weaknesses)
- **Weapon Mastery:** higher mastery with the weapon increases critical chance

The exact formula incorporating these factors and their weights: À DÉFINIR.

### 10.3 Critical Damage Contexts

Guaranteed criticals (automatic, not subject to random probability):

- **Backstab:** attacking an unaware target from behind = critical (see `specs/COMBAT_SYSTEM_SPEC.md` section 9.1)
- **Perfect Parry Counter:** successful perfect parry counter attack = critical (see `specs/COMBAT_SYSTEM_SPEC.md` section 9.1)
- **Other contextual effects:** to be defined per encounter or ability

Contextual criticals are guaranteed when conditions are met and do not use random chance for their **triggering** (though their damage may still be subject to the 2.0× multiplier).

## 11. Enchantments and Special Effects

### 11.1 Status

Enchantments, special properties, and magical effects on weapons: À DÉFINIR

This section is reserved for future development. Decisions about magical weapon effects should be made in coordination with the magic system.

## 12. Equipment Beyond Weapons

This specification focuses on weapons. Armor, accessories, and other equipment are deferred to future specifications or existing documents:

- Armor resistance: `specs/COMBAT_SYSTEM_SPEC.md` section 7
- Armor weight/mobility effects: À DÉFINIR in future armor specification

## 13. Design Principles (Summary)

1. **Fixed base values:** weapon damage, weight, and speed are not randomized
2. **Progression through mastery:** player skill and weapon mastery improve performance, not luck
3. **Quality affects durability, not damage:** rare weapons are more durable, not automatically stronger
4. **Scaling via characteristics:** Strength and Agility contribute meaningfully to damage and criticals
5. **Data-driven:** all weapon properties are configurable without engine code changes
6. **No arbitrary complexity:** randomness is reserved for scenarios where it creates meaningful gameplay choice

## 14. Elements Still To Be Defined

The rules already fixed in this document (damage scaling, armor reductions, critical multiplier, fixed weapon properties, and durability at 0% making a standard weapon unusable) must not be treated as undecided or independently redefined by another combat document.

- Base damage values for each weapon family
- Exact Forge skill scaling for repair costs
- Degradation rate per quality level
- Whether weight affects mobility or stamina costs
- Whether attack speed affects animation or cooldowns
- Critical chance formula incorporating Agility, Perception, and Mastery
- Enchantment mechanics (if implemented)
- Crafting and modification mechanics

## 15. Integration with Other Systems

This specification integrates with:

- **COMBAT_SYSTEM_SPEC.md:** weapon attacks, damage types, and critical mechanics
- **CANONICAL_SKILLS.md:** weapon mastery skills and Forge skill
- **SKILL_PROGRESSION.md:** how weapon mastery progresses
- **CHARACTERISTIC_PROGRESSION.md:** how Strength and Agility scale
- **BESTIARY.md:** creature armor and resistances (pending)
- **TECHNICAL_ARCHITECTURE.md:** data-driven implementation in Unreal

---

**Last updated:** 2026-10-15  
**Status:** SPÉCIFIÉ — Preproduction Phase 0  
**Next steps:** Define numerical values, finalize armor specification, implement in Unreal Engine 5.8.1
