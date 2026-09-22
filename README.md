# Merge

Action-RPG with intentional PS1 aesthetic.  
**Engine:** Unreal Engine 5.8.1 · **Primary language:** C++20 · **Complementary:** Blueprint

## Status

| Phase | Status |
|-------|--------|
| 0 — Vision / Game Bible | VALIDÉ — vision et règles spécifiées |
| 0.5 — AI infrastructure / security | OPÉRATIONNEL pour les garde-fous et le workflow ; planner et providers IA réels en attente |
| 1 — UE5 foundation | SCAFFOLD livré ; compilation UE 5.8.1 et PIE à valider localement |
| 2+ | PROPOSÉ / à venir |

Les systèmes gameplay détaillés sont **spécifiés mais non déclarés comme implémentés** tant qu'ils n'ont pas été prototypés et validés dans Unreal.

## Références

- [GAME_BIBLE.md](GAME_BIBLE.md) — vision
- [specs/CANONICAL_SKILLS.md](specs/CANONICAL_SKILLS.md) — 46 compétences et relations canoniques
- [specs/SKILL_PROGRESSION.md](specs/SKILL_PROGRESSION.md) — progression des compétences
- [specs/CHARACTERISTIC_PROGRESSION.md](specs/CHARACTERISTIC_PROGRESSION.md) — réserves, poids et seuils
- [specs/PLAYER_PROGRESSION.md](specs/PLAYER_PROGRESSION.md) — architecture globale de progression
- [specs/TECHNICAL_ARCHITECTURE.md](specs/TECHNICAL_ARCHITECTURE.md) — architecture Unreal cible
- [docs/gameplay.md](docs/gameplay.md) — synthèse gameplay
- [ROADMAP.md](ROADMAP.md) — phases
- [docs/UE5_SETUP.md](docs/UE5_SETUP.md) — validation Unreal locale

## Principes canoniques

- Merge possède **46 compétences canoniques** et **6 caractéristiques** sur 0–20.
- Création : 6/20 partout, 26 points à répartir, maximum 14/20.
- Les compétences initiales sont calculées automatiquement ; aucun point de compétence n'est distribué manuellement.
- Après création : Learning by Doing par activité pertinente, pratiquée et validée.
- Les points gagnés augmentent la compétence et alimentent les caractéristiques liées via poids, réserves cachées et seuils ; aucune recomposition directe par moyenne des compétences.
- `Domptage` est une compétence canonique.
- `Réflexe` est un système automatique d'évitement des attaques surprises, basé notamment sur Agilité et Perception ; ce n'est ni une compétence ni une caractéristique et il ne progresse pas indépendamment.
- `Parade` appartient à Défense / mouvement.
- `Filature` est une compétence canonique.
- Les classes/voies sont dérivées du profil et révélées lorsque leurs conditions sont remplies.

## Structure actuelle et architecture cible

```text
Source/Merge/     scaffold C++ actuel
Content/          assets Unreal à créer dans l'éditeur
specs/            architecture cible et règles de gameplay
```

L'architecture cible ne signifie pas que tous ses modules sont déjà présents dans le scaffold.

## Validation locale

UE 5.8.1, C++20, génération des project files, Blueprints, `L_TestArena`, Enhanced Input, PIE et profiling restent à valider localement.

## Statuts

```text
PROPOSÉ → PENDING_HUMAN → APPROUVÉ → SPÉCIFIÉ → SCAFFOLD → IMPLÉMENTÉ → VALIDÉ → OPÉRATIONNEL
```

`APPROUVÉ` ne signifie ni `IMPLÉMENTÉ` ni `VALIDÉ`.
