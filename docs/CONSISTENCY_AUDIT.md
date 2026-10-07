# Second audit de cohérence — Merge

**Date :** 2026-10-05  
**Dépôt :** `FlynnTaggart001/Merge`  
**Statut :** audit documentaire combat complété ; validation Unreal locale restante

## Règles vérifiées

- 46 compétences canoniques ; `Domptage` est canonique.
- 6 caractéristiques sur 0–20.
- Création : sexe Homme/Femme ; 6/20 partout, 20 points, maximum 14/20.
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
- Les maîtrises d'armes utilisent les neuf compétences canoniques : Épée, Hache, Masse, Lance, Dague, Arme à deux mains, Arc, Arbalète et Combat à mains nues.

## Fichiers corrigés dans cet audit

- `specs/WEAPON_COMBAT_AND_MASTERY.md`
- `docs/CONSISTENCY_AUDIT.md`

Les corrections documentaires précédentes restent actives dans :

- `README.md`
- `ai/README.md`
- `Content/README.md`
- `docs/gameplay/CHARACTER_CREATION.md`
- `docs/gameplay/CHARACTER_ATTRIBUTES.md`
- `docs/gameplay/CHARACTER_STATS.md`
- `specs/SKILL_PROGRESSION.md`
- `specs/MOUNT_SYSTEM_SPEC.md`
- `specs/COMBAT_SYSTEM_SPEC.md`

## Contradiction trouvée et corrigée le 2026-10-05

`specs/WEAPON_COMBAT_AND_MASTERY.md` utilisait encore des catégories génériques de maîtrise (`OneHanded`, `TwoHanded`, `Polearm`, `RangedPhysical`) alors que la liste canonique définit neuf compétences distinctes par famille d'arme.

Correction appliquée :

- remplacement des catégories génériques par les neuf compétences canoniques ;
- interdiction explicite de créer une compétence de maîtrise générique non canonique ;
- alignement de l'architecture `WeaponMastery` avec `specs/CANONICAL_SKILLS.md` ;
- confirmation que l'utilisation d'une famille ne fait progresser que la compétence correspondante.

## Contradictions restantes

Aucune contradiction active n'a été trouvée dans les documents canoniques vérifiés lors de cet audit.

Les éléments de combat encore marqués « à définir » dans `specs/COMBAT_SYSTEM_SPEC.md` et `specs/WEAPONS_AND_EQUIPMENT_SPEC.md` sont des paramètres ou sous-systèmes non encore décidés, pas des contradictions. Ils constituent la prochaine étape de conception avant l'implémentation Unreal.

### Paramètres de combat encore à décider

- formule exacte des dégâts et coefficients de maîtrise / Force ;
- valeurs d'endurance et régénération ;
- valeurs d'armure et interaction avec tranchant / perforant / contondant ;
- formule précise du stagger ;
- fenêtres numériques de parade ;
- valeurs de charge des attaques puissantes ;
- règles précises d'interruption ;
- combos spéciaux définitifs par famille d'arme ;
- comportement exact des réactions automatiques de Réflexe ;
- formule exacte de la chance de critique utilisant Agilité, Perception et compétence d'arme ;
- valeurs de base des armes ;
- coût exact des réparations selon Forge ;
- dégradation selon la qualité.

Ces points ne doivent pas être inventés dans le code ou dans une autre spécification tant qu'ils ne sont pas validés comme règles de game design.

## Validation locale restante

La compilation UE 5.8.1, la génération des project files, la validation C++20 par le toolchain, la création des Blueprints, `L_TestArena`, Enhanced Input, le PIE et le profiling doivent encore être validés localement. Ce sont des validations techniques, pas des contradictions documentaires.
