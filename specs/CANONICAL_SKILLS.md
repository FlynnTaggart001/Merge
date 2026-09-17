# Merge — Canonical Skills

**Status:** APPROVED — canonical list
**Engine:** Unreal Engine 5.8.1

Merge has **45 unique skills**.

## Characteristics

The six canonical characteristics are:

- Force
- Agilité
- Perception
- Intelligence
- Volonté
- Charisme

### Character creation

At character creation, the player distributes characteristic points **manually**. This is the only phase where the player directly allocates characteristic points.

Current creation rules:

- Each of the 6 characteristics starts at **6**.
- The player receives **26 additional characteristic points** to distribute freely.
- A characteristic cannot exceed **14** during character creation.
- Therefore, the total starting characteristic pool is **62 points** (`6 × 6 + 26`).
- No characteristic can be reduced below its base value of 6.

### Initial skill calculation

The direction of the system is intentionally **reversed between character creation and normal gameplay**:

**At character creation:**

`Characteristics → Initial Skills`

The starting value of every skill is calculated from the characteristic values linked to that skill. The exact mathematical conversion formula is **not yet finalized** and must be defined before implementation. It must use the canonical characteristic links below and respect the game's progression scale.

**After character creation:**

`Skills → Characteristics`

The player does not manually distribute skill or characteristic points. Skills improve through **Learning by Doing**, and validated skill progression feeds the linked characteristics automatically.

The creation formula and the post-creation progression formula are two distinct systems and must not be conflated.

**Important progression rule:** A characteristic can contribute to the calculation of a skill without that skill being allowed to increase the characteristic during gameplay. Characteristic-to-skill relationships used for initial calculation do **not** automatically imply a reverse skill-to-characteristic progression relationship.

## Combat — 9

| Skill | Characteristics |
|---|---|
| Épée | Force + Agilité |
| Hache | Force + Agilité |
| Masse | Force |
| Lance | Force + Agilité |
| Dague | Agilité |
| Arme à deux mains | Force + Agilité |
| Arc | Agilité + Perception |
| Arbalète | Perception + Agilité |
| Combat à mains nues | Force + Agilité |

## Défense / mouvement — 6

| Skill | Characteristics |
|---|---|
| Esquive | Agilité + Perception |
| Parade | Agilité + Perception |
| Blocage | Force + Agilité |
| Acrobatie | Agilité |
| Escalade | Force + Agilité |
| Athlétisme | Force + Agilité |

**Parade belongs to Défense / mouvement. It is not a Combat skill.**

## Furtivité — 6

| Skill | Characteristics |
|---|---|
| Discrétion | Agilité + Perception |
| Élimination furtive | Agilité + Perception |
| Pickpocket | Agilité + Perception |
| Crochetage | Agilité + Intelligence |
| Camouflage | Perception + Intelligence |
| Filature | Perception + Agilité |

## Magie — 7

| Skill | Characteristics |
|---|---|
| Invocation | **Volonté + Intelligence** |
| Nécromancie | **Volonté + Intelligence** |
| Contrôle mental | **Volonté + Intelligence** |
| Magie élémentaire | **Volonté + Intelligence** |
| Magie physique | **Volonté + Intelligence** |
| Magie de groupe | **Volonté + Intelligence** |
| Magie de pacte | **Volonté + Intelligence** |

**Magic is primarily based on Volonté. Intelligence is secondary and represents understanding/learning rather than the core magical force.** Numeric characteristic weights remain data-driven and are not fixed in this document.

## Connaissances — 7

| Skill | Characteristics |
|---|---|
| Alchimie | Intelligence + Perception |
| Botanique | Intelligence + Perception |
| Médecine | Intelligence + Perception |
| Histoire | Intelligence |
| Géographie | Intelligence + Perception |
| Créatures | Intelligence + Perception |
| Linguistique | Intelligence + Perception |

## Artisanat — 6

| Skill | Characteristics |
|---|---|
| Forge | Force + Intelligence |
| Travail de la matière | Intelligence + Agilité |
| Couture | Agilité + Perception |
| Fabrication d'armes | Intelligence + Force |
| Fabrication d'armures | Intelligence + Force |
| Réparation | Intelligence + Perception |

## Social / communication — 4

| Skill | Characteristics |
|---|---|
| Persuasion | Charisme + Intelligence |
| Intimidation | **Charisme + Force** |
| Éloquence | Charisme + Intelligence |
| Marchandage | Charisme + Intelligence |

**Intimidation uses both Charisme and Force for its skill calculation at character creation. However, increasing Intimidation through Learning by Doing does not increase Force automatically. The Intimidation skill-to-characteristic progression must not feed Force; Force can only be increased by skills explicitly designated as contributing to Force progression.**

## Canonical terminology

- **Lutte is not a Merge skill or characteristic.**
- **Parade** is the canonical name and belongs to **Défense / mouvement**.
- No missing skill names may be invented.

## Progression relationship after character creation

Skill progression feeds characteristic progression:

`CharacteristicProgress += SkillProgress × Weight`

Each characteristic has its own hidden progression pool and threshold. When a threshold is reached, the characteristic increases by +1 and surplus progression is retained for the next threshold.

This progression is automatic. The player cannot manually assign characteristic points after character creation.

**The `Weight` used for post-creation progression is skill-to-characteristic specific. A characteristic listed for a skill's initial calculation is not automatically a valid target for post-creation progression.**

This distinction allows a skill such as Intimidation to depend on Force when calculating its initial value, while preventing Intimidation progression from increasing Force.

## Scale

Skill level **50 is already an extremely high / superhuman level of mastery**. Both initial skill calculation and progression balancing must respect this scale.

## Design rule

The system must preserve the following lifecycle:

`Character creation: Characteristics → Skills`

`Gameplay: Skills → Characteristics`

The mathematical conversion used at creation remains **TBD** and must be approved before being treated as canonical implementation data.
