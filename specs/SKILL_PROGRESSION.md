# Merge — Skill Progression Specification

**Status:** APPROUVÉ — baseline canonique de progression  
**Engine:** Unreal Engine 5.8.1  
**Échelle affichée des compétences:** 0–100 %

## 1. Principe

Merge utilise le **Learning by Doing**. Les compétences progressent uniquement lorsqu'une activité pertinente, réellement pratiquée, réussie et validée par les règles de contexte est effectuée.

Merge possède **46 compétences canoniques**. La liste et les relations entre compétences et caractéristiques sont définies exclusivement dans `specs/CANONICAL_SKILLS.md`.

À la création, aucune compétence ne reçoit de points distribués manuellement. Sa valeur initiale est dérivée du profil des six caractéristiques :

- compétence liée à une caractéristique : `Caractéristique × 4` ;
- compétence liée à plusieurs caractéristiques : `moyenne(Caractéristiques liées) × 4`.

Après la création, aucune distribution manuelle de points de compétence ou de caractéristique n'est autorisée.

## 2. Progression gagnée lors d'une activité

Pour une activité réussie et validée :

```text
P = 0.9 × max(0, (D − S + 15) / 50)
    × 1 / (1 + 0.012 × S)
    × (0.75 + 0.025 × I)
```

- `P` = points de progression de compétence gagnés ;
- `D` = difficulté prédéfinie de l'activité ;
- `S` = valeur actuelle de la compétence sur l'échelle 0–100 ;
- `I` = Intelligence sur l'échelle 0–20.

Les mêmes points gagnés lors de cet événement :

1. augmentent la compétence pratiquée ;
2. alimentent les réserves cachées des caractéristiques liées selon leurs poids.

```text
SkillProgress += P
CharacteristicProgress += P × Weight
```

Une caractéristique augmente uniquement lorsqu'une réserve cachée atteint son seuil. Le surplus est conservé. Une caractéristique n'est jamais recalculée directement par `moyenne(compétences) / 4` pendant le jeu.

Les actions répétitives réalisées uniquement pour farmer peuvent être rejetées ou fortement réduites par les règles de validation et d'anti-farming. Une réussite réelle d'une activité pertinente reste une source valide de progression.

## 3. Courbe et niveau de maîtrise

Les valeurs de compétence sont stockées avec leur précision interne et affichées en pourcentage. La progression interne et les seuils restent data-driven.

Le **niveau 50** représente déjà une maîtrise extrêmement élevée / surhumaine. Les difficultés et la validation doivent préserver cette échelle.

## 4. Contraintes terminologiques

- `Lutte` n'est pas une compétence ou une caractéristique canonique.
- `Domptage` est une compétence canonique.
- `Réflexe` est un système automatique d'évitement des attaques surprises, pas une compétence ni une caractéristique.
- `Parade` est la compétence canonique de `Défense / mouvement`.
