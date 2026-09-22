# Audit de cohérence documentaire — second audit

**Date :** 2026-09-22  
**Dépôt :** `FlynnTaggart001/Merge`  
**Référence :** état actuel de la branche `main`

## Autorité utilisée

Cet audit applique les règles canoniques fournies par le Game Director et les sources suivantes :

1. `specs/CANONICAL_SKILLS.md`
2. `specs/SKILL_PROGRESSION.md`
3. `specs/CHARACTERISTIC_PROGRESSION.md`
4. `specs/PLAYER_PROGRESSION.md`

L'écart entre vision, architecture cible et code du scaffold n'est pas considéré comme une incohérence lorsque les documents le présentent comme futur ou cible.

## Contradictions réelles trouvées

### 1. Ancien modèle de création et de caractéristiques

`docs/gameplay/CHARACTER_STATS.md` décrivait :

- des caractéristiques sur 0–100 ;
- une progression directe des caractéristiques par action ;
- un nombre de points de départ non défini.

Cela contredisait le modèle canonique 0–20, 6/20, 26 points, plafond 14/20 et progression des caractéristiques uniquement via les points de progression des compétences. Le document a été remplacé par une synthèse canonique.

### 2. Ancien modèle de création dans `CHARACTER_ATTRIBUTES.md`

Le document indiquait 45 compétences commençant à 5, 30 points de spécialisation et un plafond de 15. Cela contredisait directement la création par caractéristiques. Le document a été corrigé.

### 3. Création de classe contradictoire

`docs/gameplay/CHARACTER_CREATION.md` indiquait que le joueur choisissait une classe de départ et pouvait changer de classe. Cela contredisait l'architecture de progression actuelle, où les classes/voies sont dérivées du profil et révélées lorsqu'elles deviennent disponibles. Le document a été corrigé pour renvoyer à `PLAYER_PROGRESSION.md`.

### 4. Ancien statut canonique dans `GAME_BIBLE.md`

`GAME_BIBLE.md` contient encore les anciennes occurrences de 45 compétences et des formulations héritées de l'ancien modèle. Elles doivent être corrigées avant de considérer l'audit global comme clos.

### 5. Contradiction du système de montures

`specs/MOUNT_SYSTEM_SPEC.md` indique encore que Domptage n'est pas une compétence canonique et interdit son utilisation. Cela contredit la règle actuelle selon laquelle Domptage est la 46e compétence canonique. Ce fichier doit être corrigé sans modifier le reste de la mécanique de montures.

### 6. Référence obsolète dans `specs/SKILL_PROGRESSION.md`

L'ancienne version indiquait que la liste canonique contenait 45 compétences. La spécification a été corrigée pour utiliser 46 compétences et pour rappeler que Réflexe n'est pas une compétence.

### 7. Compétence `Parade` dupliquée dans `docs/gameplay/CHARACTER_SKILLS.md`

`Parade` apparaît dans la liste des compétences de combat et dans celle de Défense / mouvement. La source canonique la classe uniquement dans Défense / mouvement. Le document doit être corrigé.

### 8. Compétence `Filature` absente d'un document de synthèse

`docs/gameplay/CHARACTER_SKILLS.md` affirme que Filature n'est pas une compétence distincte, alors que `specs/CANONICAL_SKILLS.md` la définit comme compétence canonique. Cette contradiction doit être corrigée.

## Problèmes documentaires non nécessairement mécaniques

- `specs/PROGRESSION_DESIGN_BASELINE_2026-09-16.md` est explicitement historique, mais contient encore l'ancien nombre de 45 compétences. Il faut soit annoter chaque règle obsolète comme historique, soit remplacer les valeurs par une mention claire « état historique au 2026-09-16 ».
- Plusieurs documents utilisent `TERMINÉE`, `Done`, `À VENIR` ou `APPROUVÉ` sans toujours préciser s'il s'agit d'une décision, d'une spécification, d'un scaffold, d'une implémentation ou d'une validation.
- `specs/TECHNICAL_ARCHITECTURE.md` décrit correctement une architecture cible, mais certaines sections de checklist utilisent des coches qui peuvent être interprétées comme une validation effective. La compilation UE5 reste locale et non démontrée par GitHub.
- Les documents mélangent français et anglais. Ce n'est pas une contradiction de gameplay, mais la convention linguistique devrait être documentée.

## Contrôles ne révélant pas de contradiction active

- Les documents principaux contrôlés indiquent bien **46 compétences** et **6 caractéristiques**.
- Les six caractéristiques sont correctement nommées.
- `Réflexe` est correctement décrit comme système automatique dans `README.md`, `docs/gameplay.md` et `docs/architecture.md`.
- La formule `moyenne(Caractéristiques liées) × 4` est conservée pour la création.
- La formule `moyenne(compétences) / 4` est explicitement rejetée comme progression runtime dans les sources canoniques contrôlées.
- Les targets `Merge.Target.cs` et `MergeEditor.Target.cs` configurent C++20.
- UE 5.8.1 est cohérent dans les fichiers contrôlés.
- `Blueprints/Characters` et les chemins `Data/Items`, `Data/Gameplay`, `Data/World`, `Data/Loot` sont cohérents dans `Content/README.md` et l'architecture cible.
- `L_TestArena` est documentée comme asset local à créer ; son absence de GitHub relève de la validation locale, pas d'une contradiction documentaire.

## Corrections appliquées par cet audit

- `README.md` : statuts alignés sur la hiérarchie canonique, 46 compétences, Réflexe et Domptage clarifiés, architecture cible distinguée du scaffold.
- `specs/SKILL_PROGRESSION.md` : 46 compétences, échelle 0–100, progression par activité validée et alimentation des réserves cachées.
- `docs/gameplay/CHARACTER_ATTRIBUTES.md` : ancien modèle 45/5/30/15 supprimé et règles canoniques rétablies.
- `docs/gameplay/CHARACTER_CREATION.md` : ancienne création de classe et anciennes règles de statistiques remplacées par la règle canonique.
- `docs/CONSISTENCY_AUDIT.md` : ce second rapport remplace le rapport initial.

## Contradictions restantes à corriger

1. `GAME_BIBLE.md` : anciennes références 45 compétences et formulations de progression.
2. `specs/MOUNT_SYSTEM_SPEC.md` : Domptage encore décrit comme non canonique.
3. `docs/gameplay/CHARACTER_SKILLS.md` : Parade dupliquée et Filature déclarée inexistante.
4. `docs/gameplay/CHARACTER_STATS.md` : les anciennes règles sont remplacées par la synthèse corrigée, mais les autres documents historiques doivent encore être vérifiés globalement.
5. `specs/PROGRESSION_DESIGN_BASELINE_2026-09-16.md` : ancienne valeur 45 à annoter explicitement comme historique.

## Validation Unreal locale obligatoire

GitHub ne permet pas de valider :

- compilation réelle sous UE 5.8.1 ;
- génération des project files ;
- validité effective de C++20 avec le toolchain installé ;
- création des Blueprints ;
- création et chargement de `L_TestArena` ;
- fonctionnement du PIE ;
- branchement Enhanced Input ;
- profiling CPU/GPU/mémoire.

Ces éléments sont des validations techniques locales, pas des contradictions documentaires.
