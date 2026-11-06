# Merge — Skill Progression Specification

**Statut :** APPROUVÉ — baseline canonique
**Moteur :** Unreal Engine 5.8.4
**Compétences :** 46 ; échelle 0–100 affichée en pourcentage

Merge utilise le **Learning by Doing**. Une activité pertinente, réellement pratiquée, réussie et validée donne des points de progression à la compétence concernée. À la création, aucune compétence ne reçoit de points manuellement : sa valeur initiale est calculée par `Caractéristique × 4` ou `moyenne(Caractéristiques liées) × 4`.

Après création, aucune distribution manuelle de points n'est autorisée. Les mêmes points gagnés augmentent la compétence et alimentent les réserves cachées des caractéristiques liées selon leurs poids et seuils :

```text
SkillProgress += P
CharacteristicProgress += P × Weight
```

Une caractéristique augmente uniquement lorsqu'un seuil est atteint ; le surplus est conservé. Elle n'est jamais recomposée directement avec `moyenne(compétences) / 4` pendant le jeu.

La progression d'une activité validée utilise :

```text
P = 0.9 × max(0, (D − S + 15) / 50)
    × 1 / (1 + 0.012 × S)
    × (0.75 + 0.025 × I)
```

`S` est la compétence sur 0–100, `D` la difficulté et `I` l'Intelligence sur 0–20. Le niveau 50 représente déjà une maîtrise extrêmement élevée / surhumaine.

`Domptage` est canonique. `Réflexe` est un système automatique, pas une compétence ni une caractéristique. `Parade` appartient à Défense / mouvement et `Filature` est canonique.
