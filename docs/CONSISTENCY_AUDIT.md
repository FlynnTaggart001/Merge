# Audit de cohérence documentaire — Merge

**Date de clôture :** 2026-09-22  
**Dépôt audité :** `FlynnTaggart001/Merge`  
**Statut :** CORRECTIONS DOCUMENTAIRES ET CANONIQUES APPLIQUÉES

## 1. Décisions canoniques appliquées

### 1.1 Domptage

**Décision :** `Domptage` est une **compétence canonique**.

- Le nombre de compétences canoniques passe de **45 à 46**.
- Domptage intervient dans l'acquisition naturelle des montures.
- L'achat d'une monture auprès d'un éleveur ne nécessite pas Domptage.
- Domptage est désormais présent dans `specs/CANONICAL_SKILLS.md`.
- Les références aux « 45 compétences » concernées ont été mises à jour.

### 1.2 Réflexe

**Décision :** `Réflexe` n'est **ni une compétence ni une caractéristique**.

C'est un **système défensif automatique** qui peut éviter une attaque surprise.

- Il dépend notamment de l'**Agilité** et de la **Perception**.
- Sa formule est data-driven.
- Il ne génère aucune progression indépendante.
- Il ne crée aucun nouvel élément dans les 6 caractéristiques ou les 46 compétences.

Les anciennes formulations qui présentaient Réflexe comme une compétence/caractéristique ont été corrigées.

## 2. Progression du personnage

Le modèle canonique est maintenant explicitement :

```text
Création :
Caractéristiques → Compétences

Après création :
Activité pratiquée et validée
        ↓
Points de progression de compétence
        ↓
Augmentation de la compétence
        ↓
Même progression transmise aux caractéristiques liées
        ↓
Poids + réserve cachée
        ↓
Seuil
        ↓
Caractéristique +1
```

### Règles

- Les 6 caractéristiques commencent à **6/20**.
- Le joueur reçoit **26 points** à la création.
- Maximum à la création : **14/20**.
- Les compétences initiales sont calculées à partir des caractéristiques.
- Après la création, aucune distribution manuelle de points de caractéristique.
- Une activité validée fait gagner des **points de progression de compétence**.
- Ces mêmes points alimentent la progression des caractéristiques selon les liens et poids configurés.
- La caractéristique n'est **pas** recalculée à partir de la moyenne instantanée des compétences.
- Les seuils et poids sont conservés comme système runtime canonique.
- L'Intimidation utilise Force + Charisme à la création, mais sa progression contribue uniquement au Charisme.

## 3. Échelle compétence / XP

La documentation distingue désormais :

- **Valeur de compétence :** échelle 0–100, affichée en %.
- **Points de progression / XP :** progression interne gagnée lors des activités validées.
- **Niveau 50 :** correspond à 50 % de maîtrise et représente déjà une maîtrise extrêmement élevée / surhumaine.
- Les compétences peuvent progresser jusqu'à 100 %.

La formule de création reste :

`Compétence initiale (%) = moyenne(Caractéristiques liées) × 4`

La progression après création ne réutilise pas cette formule comme recalcul inverse.

## 4. Statuts documentaires

La hiérarchie canonique est :

1. `PROPOSÉ`
2. `PENDING_HUMAN`
3. `APPROUVÉ`
4. `SPÉCIFIÉ`
5. `SCAFFOLD`
6. `IMPLÉMENTÉ`
7. `VALIDÉ`
8. `OPÉRATIONNEL`

**APPROUVÉ ≠ IMPLÉMENTÉ ≠ VALIDÉ.**

## 5. Infrastructure IA

Les documents distinguent maintenant :

- garde-fous et workflow IA : opérationnels ;
- planner : encore à réaliser ;
- providers IA réels : encore à brancher.

La CI est décrite comme une CI de runtime/garde-fous et non comme une validation Unreal complète.

## 6. Unreal Engine

Le statut Phase 1 est maintenant :

> **Scaffold livré — compilation UE 5.8.1 et validation PIE encore nécessaires localement.**

L'architecture cible est explicitement distinguée du scaffold réellement présent.

Les références à C++20 sont maintenant accompagnées d'une configuration explicite C++20 dans les targets Unreal.

## 7. Conventions de contenu

Convention retenue :

```text
Content/
├── Blueprints/
│   ├── Core/
│   ├── Characters/
│   ├── Gameplay/
│   ├── UI/
│   └── Tutorials/
└── Data/
    ├── Items/
    ├── Gameplay/
    ├── World/
    └── Loot/
```

`Character` est remplacé par `Characters` dans les références concernées.

## 8. Map de test

`Config/DefaultEngine.ini` conserve `L_TestArena` comme map de démarrage prévue.

Son absence du dépôt Git est désormais considérée comme un **asset local à créer en Phase 1**, et non comme une contradiction de configuration.

## 9. Points restant à valider localement

Les corrections documentaires sont appliquées. Les points suivants ne peuvent pas être déclarés validés depuis GitHub seul :

- compilation réelle sous Unreal Engine 5.8.1 ;
- génération des project files ;
- création/validation des Blueprints ;
- création de `L_TestArena` ;
- fonctionnement PIE ;
- validation effective du C++20 par le toolchain Unreal ;
- profiling CPU/GPU/mémoire.

Ces éléments restent des **validations techniques locales**, pas des incohérences documentaires.

## Résultat

L'audit initial a été traité selon les décisions du Game Director.

**État actuel : cohérence documentaire principale corrigée ; validation Unreal locale restante.**
