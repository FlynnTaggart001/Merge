# Audit de cohérence documentaire — Merge

**Date de l'audit :** 2026-09-22  
**Dépôt audité :** `FlynnTaggart001/Merge`  
**Périmètre :** fautes, contradictions entre documents, terminologie, statuts et incohérences entre documentation et configuration.  
**Objectif :** fournir une liste de corrections à traiter. Ce document ne modifie pas les règles de vision du jeu et ne considère pas l'écart entre vision et code comme une incohérence lorsque la documentation indique clairement qu'il s'agit d'une spécification future.

## 1. Contradictions certaines à corriger

### 1.1 `Domptage` est à la fois canonique et interdit

**Références :**

- `README.md`, section « Principaux systèmes spécifiés » : `Domptage` apparaît dans la liste de progression.
- `README.md`, section montures : les montures sont décrites comme pouvant être acquises par « domptage ».
- `docs/architecture.md` : indique qu'il n'existe pas de compétence générique `Domptage`.
- `specs/CANONICAL_SKILLS.md` : la liste canonique des 45 compétences ne contient pas `Domptage`.
- `specs/SYSTEM_INTEGRATION_MATRIX.md` : précise que le système de montures ne crée pas de compétence canonique `Domptage`.

**Problème :** le mot peut désigner soit une mécanique d'acquisition, soit une compétence de progression, mais les documents ne font pas toujours cette distinction.

**Correction à décider :** remplacer les mentions de compétence `Domptage` par une formulation uniforme, par exemple :

> Acquisition naturelle d'une monture selon les règles propres à l'espèce, sans compétence canonique `Domptage`.

### 1.2 `Réflexe` est annoncé puis explicitement interdit

**Références :**

- `README.md` : le combat mentionne « Réflexe et i-frames ».
- `docs/architecture.md` : mentionne `Réflexe` dans la progression.
- `specs/SYSTEM_INTEGRATION_MATRIX.md` : précise qu'aucun système indépendant de `Réflexe` ne doit être utilisé comme caractéristique ou compétence de progression.
- `specs/CANONICAL_SKILLS.md` : les six caractéristiques canoniques sont Force, Agilité, Perception, Intelligence, Volonté et Charisme ; `Réflexe` n'en fait pas partie.

**Problème :** `Réflexe` est présent dans des listes de systèmes alors que la matrice d'intégration interdit de l'ajouter au système canonique.

**Correction à décider :** conserver `Réflexe` uniquement comme terme descriptif d'une mécanique de combat, ou le supprimer des listes de caractéristiques/compétences. La formulation recommandée est :

> esquive, fenêtres défensives et i-frames liées à la compétence canonique `Esquive`.

### 1.3 Le statut de l'infrastructure IA n'est pas formulé de façon uniforme

**Références :**

- `README.md` : Phase 0.5 indiquée comme `Done`.
- `ai/README.md` : « infrastructure en construction ».
- `ROADMAP.md` : Phase 0.5 `P0 TERMINÉE`, mais planner et providers IA réels restent à faire.
- `ai/PROJECT_STATE.md` : infrastructure opérationnelle, intégrations réelles encore limitées.

**Problème :** les documents ne distinguent pas clairement le socle opérationnel et les fonctionnalités encore manquantes.

**Formulation recommandée :**

> Infrastructure IA de garde-fous et workflow opérationnels ; exécution réelle des tâches par planner et intégration des providers IA encore à réaliser.

### 1.4 Le statut de la Phase 1 mélange « scaffold livré » et « validation effectuée »

**Références :**

- `README.md` : « Scaffold ready — compile & assets local ».
- `ROADMAP.md` : « SCAFFOLD LIVRÉ — compilation locale requise ».
- `ai/PROJECT_STATE.md` : compilation Unreal et PIE encore à valider localement.

**Problème :** `ready` peut laisser croire que la fondation est jouable et validée, alors que la compilation UE5, les assets et le PIE restent à vérifier.

**Formulation recommandée :**

> Scaffold C++ livré ; compilation UE5, assets Blueprint et validation PIE en attente sur une machine équipée d'Unreal Engine 5.8.1.

## 2. Contradictions de terminologie et de règles

### 2.1 `Parade` est classée différemment selon les documents

**Références :**

- `README.md` : la parade est regroupée dans la liste générale du combat.
- `docs/architecture.md` : la liste Combat contient `Parry`.
- `specs/CANONICAL_SKILLS.md` et `specs/SYSTEM_INTEGRATION_MATRIX.md` : `Parade` appartient à `Défense / mouvement`, pas à Combat.

**Correction :** employer partout `Parade` comme mécanique de combat, mais classer la compétence `Parade` dans `Défense / mouvement`. Éviter de traduire alternativement `Parry` et `Parade` dans les noms de référence.

### 2.2 Mélange entre `Esquive`, `Dodge`, `i-frames` et `Réflexe`

**Références :** `README.md`, `docs/architecture.md`, `specs/SYSTEM_INTEGRATION_MATRIX.md`, `ROADMAP.md`.

**Problème :** les mêmes mécaniques sont parfois nommées en français, en anglais ou avec un attribut non canonique.

**Correction :** établir une terminologie de référence :

- compétence : `Esquive` ;
- action : esquive manuelle ou roulade ;
- défense temporelle : fenêtre défensive ;
- terme technique éventuel : `i-frames`, défini une seule fois ;
- ne pas employer `Réflexe` comme compétence ou caractéristique.

### 2.3 `Compétence`, `skill`, `niveau` et `pourcentage` ne sont pas toujours distingués

**Références :** `specs/SKILL_PROGRESSION.md` et `specs/CANONICAL_SKILLS.md`.

**Problème :** la documentation utilise à la fois « niveau 50 », « 100 % », XP et progression, sans glossaire commun. Les documents indiquent que le niveau 50 est surhumain, tandis que la liste canonique décrit les compétences sur une échelle en pourcentage jusqu'à 100 %.

**Correction :** documenter explicitement les deux échelles et leur conversion, ou choisir une seule représentation runtime. À minima préciser :

- si `S` dans la formule de `SKILL_PROGRESSION.md` est un niveau 0–100 ou une autre échelle ;
- comment le niveau 50 se rapporte au pourcentage ;
- comment l'XP est convertie en valeur de compétence affichée.

### 2.4 Deux modèles de progression des caractéristiques sont décrits

**Références :**

- `specs/CHARACTERISTIC_PROGRESSION.md` : progression par réserve cachée, poids et seuils.
- `specs/CANONICAL_SKILLS.md` : caractéristique calculée par `moyenne(compétences contributrices) / 4`.
- `specs/SYSTEM_INTEGRATION_MATRIX.md` : progression par pipeline compétence → caractéristique.

**Problème :** la réserve cachée avec seuils et la recomposition directe depuis la moyenne peuvent produire des résultats différents. Il faut déterminer si la formule de moyenne est :

- une règle de conception théorique ;
- une formule de calcul runtime ;
- ou seulement une référence de calibration.

**Correction à décider :** désigner un modèle canonique et marquer l'autre comme historique, analytique ou non implémenté.

## 3. Incohérences de structure documentaire

### 3.1 Architecture cible et scaffold actuel ne sont pas assez distingués

**Références :** `specs/TECHNICAL_ARCHITECTURE.md`, `README.md`, `ROADMAP.md`, arbre `Source/`.

**Constat :** l'architecture cible décrit `Gameplay`, `AI`, `World`, `UI`, `Save`, `Audio`, `Rendering`, etc., tandis que le scaffold actuel contient principalement `Core`, `Character` et `Data`.

**Ce n'est pas une contradiction de vision**, mais les documents doivent ajouter une mention uniforme :

> Les répertoires listés dans cette spécification décrivent l'architecture cible. Seuls les modules listés dans la roadmap Phase 1 sont actuellement présents dans le scaffold.

### 3.2 Deux conventions de répertoires Blueprint sont utilisées

**Références :**

- `Content/README.md` : `Blueprints/Core` et `Blueprints/Character`.
- `specs/TECHNICAL_ARCHITECTURE.md` : `Blueprints/Characters`, `Blueprints/Gameplay`, `Blueprints/UI`, `Blueprints/Tutorials`.

**Problème :** `Character` et `Characters` ne sont pas uniformes ; les catégories `Core` et `Tutorials` ne sont pas présentées de la même manière.

**Correction :** choisir une convention unique et l'utiliser dans `Content/README.md`, `specs/TECHNICAL_ARCHITECTURE.md` et `docs/UE5_SETUP.md`.

### 3.3 Les chemins d'assets de données ne sont pas alignés

**Références :** `specs/TECHNICAL_ARCHITECTURE.md` et `Content/README.md`.

**Problème :** l'architecture cible utilise `/Game/Data/Items`, `/Game/Data/Gameplay`, `/Game/Data/World` et `/Game/Data/Loot`, mais le guide de contenu ne donne pas ces chemins comme structure attendue.

**Correction :** soit ajouter ces chemins au guide de contenu comme structure future, soit préciser qu'ils ne seront créés qu'à partir de la Phase 2.

### 3.4 `Config/DefaultEngine.ini` référence une map non présente dans le dépôt

**Références :** `Config/DefaultEngine.ini` et `Content/README.md`.

**Problème :** `GameDefaultMap` et `EditorStartupMap` pointent vers `/Game/Maps/L_TestArena.L_TestArena`, alors qu'aucun asset `.umap` n'est présent dans l'arbre Git.

**Correction à choisir :**

- conserver la référence et marquer explicitement la map comme asset local obligatoire de Phase 1 ; ou
- retirer temporairement les références jusqu'à la création et validation de la map.

## 4. Configuration et documentation technique à aligner

### 4.1 C++20 est documenté mais pas explicitement configuré

**Références :** `specs/TECHNICAL_ARCHITECTURE.md`, `specs/SYSTEM_INTEGRATION_MATRIX.md`, `specs/PERFORMANCE_AND_SIMULATION_SPEC.md`, `Source/Merge/Merge.Build.cs`.

**Problème :** les spécifications déclarent C++20, mais `Merge.Build.cs` ne définit pas explicitement la version C++.

**Correction :** ajouter la configuration C++20 si elle est compatible avec la version UE5 retenue, puis valider par compilation Unreal.

### 4.2 Le statut de compilation n'est pas démontré par la CI

**Références :** `.github/workflows/ai-runtime.yml`, `ROADMAP.md`, `ai/PROJECT_STATE.md`.

**Constat :** la CI teste le runtime Python et l'hygiène des secrets, mais ne compile pas le module Unreal. Le dépôt reconnaît que la compilation UE5 doit être réalisée localement.

**Correction documentaire :** ne pas présenter la CI comme validation complète du projet ; la nommer précisément :

> CI des garde-fous et du runtime IA ; compilation Unreal et tests PIE hors CI, à valider localement.

### 4.3 Le fichier `.gitignore` et l'architecture documentée doivent être vérifiés ensemble

**Références :** `.gitignore` et section configuration Git de `specs/TECHNICAL_ARCHITECTURE.md`.

**Problème à vérifier :** la spécification montre un extrait de `.gitignore` UE5, mais il faut vérifier que le fichier réel contient bien les répertoires et extensions attendus (`Binaries`, `Intermediate`, `Saved`, fichiers de solution et fichiers générés). Toute différence doit être soit corrigée, soit documentée comme volontaire.

## 5. Cohérence des statuts et de l'autorité documentaire

### 5.1 `APPROUVÉ`, `TERMINÉ`, `OPÉRATIONNEL` et `IMPLÉMENTÉ` doivent être définis

**Problème général :** les documents utilisent ces termes sans définition commune.

**Correction recommandée :** ajouter un petit glossaire de statut :

- `PROPOSÉ` : idée non validée ;
- `PENDING_HUMAN` : décision attendue du Game Director ;
- `APPROUVÉ` : règle de conception validée ;
- `SPÉCIFIÉ` : règle décrite mais non codée ;
- `SCAFFOLD` : base technique créée ;
- `IMPLÉMENTÉ` : code présent ;
- `VALIDÉ` : tests appropriés réussis ;
- `OPÉRATIONNEL` : système utilisable dans son périmètre déclaré.

### 5.2 `APPROUVÉ` ne doit pas être compris comme `IMPLÉMENTÉ`

**Références :** la majorité des fichiers `specs/`, `README.md`, `ROADMAP.md`.

**Correction :** conserver les statuts `APPROUVÉ` des spécifications, mais ajouter en tête de ces documents une phrase standard :

> APPROUVÉ décrit la décision de conception ; cela ne signifie pas que le système est implémenté ou validé dans Unreal.

### 5.3 Les dates et responsables doivent être harmonisés

**Références :** `AI_RULES.md`, `specs/TECHNICAL_ARCHITECTURE.md`, `ROADMAP.md`, `ai/PROJECT_STATE.md`.

**Problème :** plusieurs dates de mise à jour et formulations de responsable existent. `specs/TECHNICAL_ARCHITECTURE.md` indique notamment `Responsable : ChatGPT`, tandis que `AI_RULES.md` définit le Game Director comme autorité finale et les rôles comme indépendants des modèles.

**Correction :** remplacer les responsables liés à un modèle par un rôle ou une équipe, par exemple `ARCHITECTURE / Game Director`, et conserver l'auteur historique dans l'historique si nécessaire.

## 6. Langue, orthographe et style

### 6.1 Mélange français/anglais non normalisé

Le dépôt mélange français et anglais dans :

- titres de fichiers ;
- titres de sections ;
- noms de systèmes ;
- statuts ;
- descriptions du README.

**Correction à décider :**

- soit documentation principalement française avec les noms techniques Unreal en anglais ;
- soit documentation principalement anglaise ;
- soit règle explicite : vision et gameplay en français, code et API en anglais.

### 6.2 Formulations à uniformiser

À rechercher et harmoniser :

- `gameplay` / `game play` ;
- `Blueprint` / `Blueprints` ;
- `provider` / `fournisseur` ;
- `skill` / `compétence` ;
- `characteristic` / `caractéristique` ;
- `world state` / `WorldState` ;
- `backstab` / `Backstab` ;
- `lock-on` / `ciblage` ;
- `i-frames` / `fenêtre d'invincibilité`.

Les noms de classes, modules, assets et variables doivent rester en anglais si c'est la convention du code ; les textes explicatifs peuvent suivre la langue choisie pour la documentation.

### 6.3 Formulations imprécises ou trop fortes

À revoir notamment :

- `Done` lorsque seule une spécification est terminée ;
- `Scaffold ready` alors que la compilation et le PIE ne sont pas validés ;
- `architecture complète` lorsqu'il s'agit d'une architecture cible ;
- `systèmes principaux` lorsqu'ils sont encore uniquement spécifiés.

## 7. Points à vérifier avant clôture de l'audit

Les points suivants nécessitent une recherche complète dans tous les fichiers avant d'être marqués comme résolus :

- occurrences de `Domptage`, `Réflexe`, `Lutte`, `Parade`, `Parry`, `Dodge` et `Esquive` ;
- mentions de `45 compétences` et `6 caractéristiques` ;
- toutes les formules de progression et leurs échelles ;
- tous les statuts `APPROUVÉ`, `DONE`, `TERMINÉ`, `OPÉRATIONNEL`, `IMPLEMENTED` ;
- toutes les références à `L_TestArena`, `BP_Merge*`, `IA_*` et `IMC_Default` ;
- les chemins `Blueprints/Character` versus `Blueprints/Characters` ;
- les références aux modules `Core`, `Gameplay`, `AI`, `World`, `UI`, `Save`, `Audio`, `Rendering` ;
- les références à l'Engine et au standard C++ ;
- les fautes d'accents, d'accords et les anglicismes non définis.

## 8. Ordre de correction recommandé

1. Corriger les contradictions `Domptage` et `Réflexe`.
2. Fixer le modèle canonique de progression des caractéristiques.
3. Définir les statuts documentaires (`APPROUVÉ`, `SPÉCIFIÉ`, `IMPLÉMENTÉ`, `VALIDÉ`).
4. Harmoniser les statuts Phase 0.5 et Phase 1.
5. Uniformiser les chemins Blueprint et Data.
6. Décider du traitement de `L_TestArena` dans la configuration.
7. Aligner la déclaration C++20 et la documentation technique.
8. Uniformiser la langue, la terminologie et le style.
9. Faire une recherche globale finale des termes interdits ou ambigus.

## Résumé

Le grand écart entre la vision et le code est **normal** et n'est pas classé comme une incohérence dans cet audit. La vision détaillée est nécessaire pour guider les futures implémentations humaines et IA.

Les corrections prioritaires concernent surtout :

- les compétences ou caractéristiques interdites mais encore mentionnées (`Domptage`, `Réflexe`) ;
- le modèle de progression des caractéristiques ;
- la différence entre conception approuvée et implémentation validée ;
- les statuts de l'infrastructure IA et du scaffold UE5 ;
- les conventions de dossiers et la terminologie ;
- les références aux assets Unreal locaux.
