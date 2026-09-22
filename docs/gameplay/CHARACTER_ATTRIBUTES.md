# Caractéristiques du personnage — Merge

## Statut documentaire

Ce document est une synthèse. Les règles canoniques sont définies dans :

- `specs/CANONICAL_SKILLS.md` pour les six caractéristiques, les 46 compétences et les relations ;
- `specs/CHARACTERISTIC_PROGRESSION.md` pour les réserves cachées, poids et seuils ;
- `specs/PLAYER_PROGRESSION.md` pour l'architecture globale.

## Caractéristiques canoniques

Le personnage possède six caractéristiques sur une échelle de **0 à 20** :

- Force
- Agilité
- Perception
- Intelligence
- Volonté
- Charisme

Les caractéristiques représentent des capacités générales. Les compétences représentent des savoir-faire acquis par la pratique.

## Création

- Les six caractéristiques commencent à **6/20**.
- Le joueur reçoit **26 points** à distribuer entre elles.
- Une caractéristique ne peut pas dépasser **14/20** à la création.
- Les compétences sont calculées automatiquement à partir du profil final.
- Aucun point de compétence n'est distribué manuellement.

Pour une compétence liée à plusieurs caractéristiques :

```text
Compétence initiale (%) = moyenne(Caractéristiques liées) × 4
```

## Progression après la création

Une activité réellement pratiquée, pertinente et validée donne des points de progression à la compétence concernée. Ces mêmes points alimentent les caractéristiques liées selon leurs poids :

```text
CharacteristicProgress += SkillProgress × Weight
```

Chaque caractéristique possède une réserve cachée et des seuils data-driven. Lorsqu'un seuil est atteint, la caractéristique augmente de +1 et le surplus est conservé.

Il n'existe **aucun recalcul runtime direct** d'une caractéristique avec `moyenne(compétences) / 4`.

## Réflexe

`Réflexe` n'est ni une compétence ni une caractéristique. C'est un système automatique d'évitement des attaques surprises qui dépend notamment de l'Agilité et de la Perception. Il ne possède aucune progression indépendante.

## Échelle de compétence

Les compétences utilisent une échelle 0–100 affichée en pourcentage. Le niveau 50 représente déjà une maîtrise extrêmement élevée / surhumaine.
