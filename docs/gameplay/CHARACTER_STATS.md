# Système de caractéristiques — Merge

**Statut :** SYNTHÈSE ALIGNÉE SUR LES RÈGLES CANONIQUES

Les six caractéristiques sont Force, Agilité, Perception, Intelligence, Volonté et Charisme. Elles utilisent une échelle de **0 à 20**.

## Création

- chaque caractéristique commence à **6/20** ;
- le joueur reçoit **26 points** à répartir ;
- le maximum à la création est **14/20** ;
- les 46 compétences sont calculées automatiquement ;
- aucun point de compétence n'est distribué manuellement.

## Progression

Une activité pertinente, réellement pratiquée et validée donne des points de progression de compétence. Ces mêmes points augmentent la compétence et alimentent les réserves cachées des caractéristiques liées selon leurs poids.

```text
CharacteristicProgress += SkillProgress × Weight
```

Les seuils sont data-driven. Lorsqu'un seuil est atteint, la caractéristique augmente et le surplus est conservé. Une caractéristique n'est jamais recomposée directement à partir de la moyenne des compétences.

`Réflexe` est un système automatique d'évitement des attaques surprises basé notamment sur l'Agilité et la Perception. Ce n'est ni une compétence ni une caractéristique et il n'a aucune progression indépendante.
