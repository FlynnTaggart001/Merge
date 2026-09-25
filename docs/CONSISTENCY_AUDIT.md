# Second audit de cohérence — Merge

**Date :** 2026-09-25  
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
- Le système de combat approuvé est centralisé dans `specs/COMBAT_SYSTEM_SPEC.md` et aligné avec la Game Bible.
- Les 46 compétences sont cohérentes avec les catégories et `Domptage` est bien canonique.
- Classes/voies dérivées du profil et révélées lorsque les conditions sont remplies.
- Architecture cible distinguée du scaffold.
- Convention `Blueprints/Characters`.
- Statuts `APPROUVÉ`, `SPÉCIFIÉ`, `SCAFFOLD`, `IMPLÉMENTÉ` et `VALIDÉ` distincts.

## Fichiers corrigés dans cet audit

- `README.md`
- `ai/README.md`
- `Content/README.md`
- `docs/gameplay/CHARACTER_CREATION.md`
- `docs/gameplay/CHARACTER_ATTRIBUTES.md`
- `docs/gameplay/CHARACTER_STATS.md`
- `specs/SKILL_PROGRESSION.md`
- `specs/MOUNT_SYSTEM_SPEC.md`
- `docs/CONSISTENCY_AUDIT.md`
- `specs/COMBAT_SYSTEM_SPEC.md`

## Documents historiques

`specs/PROGRESSION_DESIGN_BASELINE_2026-09-16.md` est conservé comme document historique et ne constitue pas une règle active. Les règles actives sont celles des quatre spécifications canoniques référencées ci-dessus.

## Contradictions corrigées après l'ajout du système de combat

- `GAME_BIBLE.md` indiquait encore **45 compétences** alors que la liste canonique en contient **46** : corrigé.
- `GAME_BIBLE.md` indiquait encore **4 compétences** en Social / communication alors que la catégorie en contient **5** avec `Domptage` : corrigé.
- `GAME_BIBLE.md` contenait encore une ancienne courbe `XP_required(level) = 100 × level^1.5`, incompatible avec l'absence de niveau global de personnage : supprimée.
- L'ancienne formulation du combat dans `GAME_BIBLE.md` présentait les dégâts tranchant/contondant/perforant/magie comme un ensemble de types génériques : remplacée par les deux catégories principales **physique/magique**, avec tranchant/perforant/contondant comme propriétés des armes.
- L'ancienne formulation de la parade a été remplacée par le système de timing approuvé, avec parade parfaite, parade réussie, parade ratée et condition d'activation.
- Les règles de lock-on, d'endurance, de stagger, de furtivité, de Réflexe et de backstab sont désormais alignées entre la Game Bible et `COMBAT_SYSTEM_SPEC.md`.

## Contradictions restantes

Aucune contradiction active n'a été trouvée dans les documents canoniques vérifiés. Les éléments de combat encore marqués « à définir » dans `COMBAT_SYSTEM_SPEC.md` sont des sous-systèmes ou paramètres non encore décidés, pas des contradictions. Les occurrences historiques éventuelles dans le document baseline restent explicitement historiques et ne doivent pas être utilisées comme règles.

## Validation locale restante

La compilation UE 5.8.1, la génération des project files, la validation C++20 par le toolchain, la création des Blueprints, `L_TestArena`, Enhanced Input, le PIE et le profiling doivent encore être validés localement. Ce sont des validations techniques, pas des contradictions documentaires.
