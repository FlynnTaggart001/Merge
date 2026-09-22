# Second audit de cohérence — Merge

**Date :** 2026-09-22  
**Dépôt :** `FlynnTaggart001/Merge`  
**Statut :** corrections documentaires appliquées ; validation Unreal locale restante

## Règles vérifiées

- 46 compétences canoniques ; `Domptage` est canonique.
- 6 caractéristiques sur 0–20.
- Création : 6/20 partout, 26 points, maximum 14/20.
- Aucune distribution manuelle de compétences à la création.
- Valeurs initiales calculées automatiquement à partir des caractéristiques.
- Learning by Doing par activité pertinente, pratiquée et validée.
- Les mêmes points augmentent la compétence et alimentent les réserves cachées des caractéristiques liées via poids et seuils.
- Aucune recomposition runtime par `moyenne(compétences) / 4`.
- `Réflexe` est un système automatique sans progression indépendante.
- `Parade` est dans Défense / mouvement ; `Filature` est canonique.
- Classes/voies dérivées du profil et révélées lorsque les conditions sont remplies.
- Architecture cible distinguée du scaffold.
- Convention `Blueprints/Characters`.
- Statuts `APPROUVÉ`, `SPÉCIFIÉ`, `SCAFFOLD`, `IMPLÉMENTÉ` et `VALIDÉ` distincts.

## Fichiers corrigés dans ce commit

- `README.md`
- `ai/README.md`
- `Content/README.md`
- `docs/gameplay/CHARACTER_CREATION.md`
- `docs/gameplay/CHARACTER_ATTRIBUTES.md`
- `docs/gameplay/CHARACTER_STATS.md`
- `specs/SKILL_PROGRESSION.md`
- `specs/MOUNT_SYSTEM_SPEC.md`
- `docs/CONSISTENCY_AUDIT.md`

## Documents historiques

`specs/PROGRESSION_DESIGN_BASELINE_2026-09-16.md` est conservé comme document historique et ne constitue pas une règle active. Les règles actives sont celles des quatre spécifications canoniques référencées ci-dessus.

## Contradictions restantes

Aucune contradiction active n'est déclarée dans les fichiers corrigés ci-dessus. Les occurrences historiques éventuelles dans le document baseline restent explicitement historiques et ne doivent pas être utilisées comme règles.

## Validation locale restante

La compilation UE 5.8.1, la génération des project files, la validation C++20 par le toolchain, la création des Blueprints, `L_TestArena`, Enhanced Input, le PIE et le profiling doivent encore être validés localement. Ce sont des validations techniques, pas des contradictions documentaires.
