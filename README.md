# Merge

Action-RPG with intentional PS1 aesthetic.  
**Engine:** Unreal Engine 5.8.1 · **Primary language:** C++ · **Complementary:** Blueprint

## Status

| Phase | Status |
|-------|--------|
| 0 — Vision / Game Bible | Done |
| 0.5 — AI infrastructure / security | Operational guardrails/workflow — planner & real providers pending |
| 1 — UE5 foundation | Scaffold delivered — UE 5.8.1 local compile/PIE pending |
| 2+ | Not started |

Les systèmes gameplay détaillés ci-dessous sont **spécifiés mais non déclarés comme implémentés** tant qu'ils n'ont pas été prototypés et testés dans Unreal.

## Quick links

- [GAME_BIBLE.md](GAME_BIBLE.md) — vision
- [specs/TECHNICAL_ARCHITECTURE.md](specs/TECHNICAL_ARCHITECTURE.md) — architecture technique
- [specs/GAMEPLAY_SYSTEMS_MASTER_SPEC.md](specs/GAMEPLAY_SYSTEMS_MASTER_SPEC.md) — systèmes de gameplay
- [specs/SKILL_PROGRESSION.md](specs/SKILL_PROGRESSION.md) — formule de progression des compétences
- [specs/SYSTEM_INTEGRATION_MATRIX.md](specs/SYSTEM_INTEGRATION_MATRIX.md) — cohérence entre systèmes
- [specs/PERFORMANCE_AND_SIMULATION_SPEC.md](specs/PERFORMANCE_AND_SIMULATION_SPEC.md) — performance et simulation distante
- [specs/WORLD_REGIONS_HYDROLOGY_AND_THREATS_SPEC.md](specs/WORLD_REGIONS_HYDROLOGY_AND_THREATS_SPEC.md) — direction de la carte
- [docs/gameplay.md](docs/gameplay.md) — synthèse gameplay
- [ROADMAP.md](ROADMAP.md) — phases
- [docs/UE5_SETUP.md](docs/UE5_SETUP.md) — setup Unreal local
- [ai/](ai/) — multi-agent protocol + runtime guards

## Principaux systèmes spécifiés

- mouvement troisième personne : roulade, bond arrière, pas de côté, franchissement, escalade contextuelle ;
- furtivité, perception et Backstab ;
- combat, maîtrises d'armes, blocage, parade, esquive, système Réflexe et i-frames ;
- ciblage intelligent et lock-on ;
- groupes de PNJ et magie collective ;
- progression des 46 compétences canoniques, des 6 caractéristiques, de l'Endurance, de la Médecine et de la magie par domaine ;
- nourriture, hydratation, sommeil et altérations physiologiques ;
- maladies régionales avec diagnostic diégétique ;
- montures : achat auprès d'éleveurs ou acquisition naturelle via la compétence canonique Domptage ;
- nage, plongée, flottabilité, noyade et dégâts environnementaux ;
- écologie prédateur/proie et populations probabilistes ;
- séismes, tornades, incendies, pluies torrentielles, inondations, glissements, volcan et lave ;
- monde non régénératif et multi-mondes persistants ;
- simulation détaillée uniquement autour du joueur, avec résolution probabiliste hors zone.

## Structure

```text
Merge.uproject
Source/Merge/     C++ module (Core, Character, …)
Content/          Maps, Blueprints, Input (Editor assets)
Config/           DefaultEngine, Input, GameplayTags
ai/               AI orchestration + security runtime
specs/            Architecture docs
```

## Local first steps (Phase 1)

1. Install **UE 5.8.1**
2. Generate project files from `Merge.uproject`
3. Compile
4. Create Blueprints + `L_TestArena` as described in `Content/README.md`
5. PIE → verify move / look / jump

See `docs/UE5_SETUP.md` for the full checklist.

## Statuts documentaires

- `PROPOSÉ` : idée non validée.
- `PENDING_HUMAN` : décision attendue du Game Director.
- `APPROUVÉ` : règle de conception validée.
- `SPÉCIFIÉ` : règle décrite mais non codée.
- `SCAFFOLD` : base technique créée.
- `IMPLÉMENTÉ` : code présent.
- `VALIDÉ` : tests appropriés réussis.
- `OPÉRATIONNEL` : système utilisable dans son périmètre déclaré.

**Important :** `APPROUVÉ` ne signifie pas `IMPLÉMENTÉ` ni `VALIDÉ`.
