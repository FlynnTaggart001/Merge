# Merge — Mount System Specification

**Statut :** APPROUVÉ — architecture de pré-implémentation  
**Moteur :** Unreal Engine 5.8.1  
**Langage principal :** C++20

Le joueur dispose de deux voies principales :

```text
Éleveur → achat
Nature → acquisition selon les règles propres à l'espèce
```

`Domptage` est une **compétence canonique** et peut intervenir dans une acquisition naturelle lorsque l'activité et les règles de l'espèce le prévoient. L'achat auprès d'un éleveur ne nécessite pas nécessairement Domptage.

Les états propres à une monture — endurance, confiance, familiarité, mouvement et comportement — appartiennent au système de montures et ne créent pas de compétence ou caractéristique supplémentaire. Une activité de monture ne produit une progression que si elle concerne réellement une compétence canonique et respecte les règles normales de progression.

L'architecture de montures est une architecture cible ; elle n'est pas présente dans le scaffold Unreal actuel.

```text
MountSystem
├── MountDefinition
├── MountState
├── MountInteraction
├── MountAcquisition
├── MountMovement
├── MountCombat
├── MountAI
└── MountPersistence
```
