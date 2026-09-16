# Merge — Canonical Skills

**Status:** APPROVED — canonical list
**Engine:** Unreal Engine 5.8.1

Merge has **45 unique skills**. All skills start at **5** at character creation. The player receives **30 specialization points**, with a maximum of **10 points invested into one skill**, so the maximum starting value of one skill is **15**.

After character creation, skill and characteristic points are not manually distributed. Skills improve through learning by doing; characteristics improve automatically from linked skill progression.

## Characteristics

The six canonical characteristics are:

- Force
- Agilité
- Perception
- Intelligence
- Volonté
- Charisme

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
| Intimidation | Charisme + Force |
| Éloquence | Charisme + Intelligence |
| Marchandage | Charisme + Intelligence |

## Canonical terminology

- **Lutte is not a Merge skill or characteristic.**
- **Parade** is the canonical name and belongs to **Défense / mouvement**.
- No missing skill names may be invented.

## Progression relationship

Skill progression feeds characteristic progression:

`CharacteristicProgress += SkillProgress × Weight`

Each characteristic has its own hidden progression pool and threshold. When a threshold is reached, the characteristic increases by +1 and surplus progression is retained for the next threshold.

## Scale

Skill level **50 is already an extremely high / superhuman level of mastery**. Progression balancing must respect this scale.
