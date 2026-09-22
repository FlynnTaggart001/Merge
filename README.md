# Merge

Action-RPG with intentional PS1 aesthetic.  
**Engine:** Unreal Engine 5.8.1 · **Primary language:** C++20 · **Complementary:** Blueprint

## Status

| Phase | Status |
|-------|--------|
| 0 — Vision / Game Bible | VALIDÉ |
| 0.5 — AI infrastructure / security | OPÉRATIONNEL pour les garde-fous et le workflow ; planner et providers IA réels en attente |
| 1 — UE5 foundation | SCAFFOLD livré ; compilation UE 5.8.1 et PIE à valider localement |
| 2+ | PROPOSÉ / à venir |

Les systèmes gameplay détaillés ci-dessous sont **spécifiés mais non déclarés comme implémentés** tant qu'ils n'ont pas été prototypés et validés dans Unreal.

## Quick links

- [GAME_BIBLE.md](GAME_BIBLE.md) — vision
- [specs/TECHNICAL_ARCHITECTURE.md](specs/TECHNICAL_ARCHITECTURE.md) — architecture cible
- [specs/GAMEPLAY_SYSTEMS_MASTER_SPEC.md](specs/GAMEPLAY_SYSTEMS_MASTER_SPEC.md) — systèmes de gameplay
- [specs/CANONICAL_SKILLS.md](specs/CANONICAL_SKILLS.md) — 46 compétences et relations canoniques
- [specs/SKILL_PROGRESSION.md](specs/SKILL_PROGRESSION.md) — progression des compétences
- [specs/CHARACTERISTIC_PROGRESSION.md](specs/CHARACTERISTIC_PROGRESSION.md) — progression cachée des caractéristiques
- [specs/PLAYER_PROGRESSION.md](specs/PLAYER_PROGRESSION.md) — architecture globale de progression
- [specs/SYSTEM_INTEGRATION_MATRIX.md](specs/SYSTEM_INTEGRATION_MATRIX.md) — cohérence entre systèmes
- [specs/PERFORMANCE_AND_SIMULATION_SPEC.md](specs/PERFORMANCE_AND_SIMULATION_SPEC.md) — performance et simulation distante
- [docs/gameplay.md](docs/gameplay.md) — synthèse gameplay
- [ROADMAP.md](ROADMAP.md) — phases
- [docs/UE5_SETUP.md](docs/UE5_SETUP.md) — setup Unreal local
- [ai/](ai/) — protocole multi-agent et runtime guards

## Principaux systèmes spécifiés

- mouvement troisième personne : roulade, bond arrière, pas de côté, franchissement, escalade contextuelle ;
- furtivité, perception, Backstab et système automatique Réflexe ;
- combat, maîtrises d'armes, blocage, parade, esquive et fenêtres défensives ;
- ciblage intelligent et lock-on ;
- groupes de PNJ et magie collective ;
- progression des 46 compétences canoniques et des 6 caractéristiques ;
- nourriture, hydratation, sommeil et altérations physiologiques ;
- maladies régionales avec diagnostic diégétique ;
- montures : achat auprès d'éleveurs ou acquisition naturelle pouvant utiliser Domptage ;
- nage, plongée, flottabilité, noyade et dégâts environnementaux ;
- écologie prédateur/proie et populations probabilistes ;
- séismes, tornades, incendies, pluies torrentielles, inondations, glissements, volcan et lave ;
- monde non régénératif et multi-mondes persistants ;
- simulation détaillée autour du joueur, avec résolution probabiliste hors zone.

`Réflexe` est un système automatique d'évitement des attaques surprises. Ce n'est ni une compétence ni une caractéristique et il ne possède aucune progression indépendante.

## Structure actuelle et architecture cible

```text
Merge.uproject
Source/Merge/     scaffold C++ actuel (Core, Character, Data)
Content/          assets Unreal à créer dans l'éditeur
Config/           configuration Unreal
ai/               orchestration IA et garde-fous
specs/            architecture cible et règles de gameplay
docs/             guides et synthèses
```

L'architecture complète décrite dans `specs/TECHNICAL_ARCHITECTURE.md` est une cible de développement ; elle ne signifie pas que tous ses modules sont déjà présents.

## Local first steps (Phase 1)

1. Installer **UE 5.8.1**.
2. Générer les project files depuis `Merge.uproject`.
3. Compiler les targets Unreal en C++20.
4. Créer les Blueprints et `L_TestArena` comme indiqué dans `Content/README.md`.
5. Assigner les assets Enhanced Input.
6. Lancer le PIE et vérifier déplacement, caméra et saut.

Voir `docs/UE5_SETUP.md` pour la checklist complète.

## Statuts documentaires

```text
PROPOSÉ → PENDING_HUMAN → APPROUVÉ → SPÉCIFIÉ → SCAFFOLD → IMPLÉMENTÉ → VALIDÉ → OPÉRATIONNEL
```

`APPROUVÉ` décrit une décision de conception. Il ne signifie ni `IMPLÉMENTÉ` ni `VALIDÉ`.
