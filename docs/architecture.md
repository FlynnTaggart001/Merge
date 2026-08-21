# Architecture — Gameplay, Ecology & Persistence

## Scope

Cette page décrit les implications architecturales des systèmes approuvés dans `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md`.

## Principes

- Les systèmes de mouvement, furtivité et combat restent découplés.
- Le Backstab consomme les informations du système de furtivité et du positionnement, mais ne doit pas fusionner les deux systèmes.
- L'écologie simule des populations abstraites ; elle ne crée pas un Actor par individu hors nécessité.
- La persistance appartient au monde et restaure les états de monde nécessaires au gameplay.
- Plusieurs mondes doivent être isolables dans le système de sauvegarde.

## Domaines

```text
Character
├── Movement
├── Stealth
└── Combat

World
├── Persistence
├── Ecology
├── Species
├── Population
├── PredatorPrey
├── Resources
├── Migration
└── Destruction
```

## Priorité d'implémentation

1. Valider le bootstrap Unreal 5.8.1 et le mouvement de base.
2. Prototyper accroupissement + roulade.
3. Prototyper détection + furtivité.
4. Prototyper Backstab.
5. Construire les données d'espèces et de populations.
6. Implémenter la simulation écologique régionale.
7. Implémenter la persistance du monde.
8. Ajouter le support de plusieurs mondes.
9. Optimiser la matérialisation des populations.

Aucun de ces points ne doit être considéré comme implémenté uniquement parce qu'il apparaît dans cette architecture.
