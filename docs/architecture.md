# Architecture — Gameplay, Ecology & Persistence

## Scope

Cette page décrit les implications architecturales des systèmes approuvés dans `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md` et les spécifications environnementales associées.

## Principes

- Les systèmes de mouvement, furtivité et combat restent découplés.
- Le Backstab consomme les informations du système de furtivité et du positionnement, mais ne doit pas fusionner les deux systèmes.
- L'écologie simule des populations abstraites ; elle ne crée pas un Actor par individu hors nécessité.
- La persistance appartient au monde et restaure les états de monde nécessaires au gameplay.
- Plusieurs mondes doivent être isolables dans le système de sauvegarde.
- Les phénomènes naturels sont simulés à l'échelle régionale puis matérialisés localement lorsque nécessaire.

## Domaines

```text
Character
├── Movement
├── Stealth
├── Combat
└── AquaticMovement

World
├── Persistence
├── Ecology
├── Species
├── Population
├── PredatorPrey
├── Resources
├── Migration
├── Destruction
├── TimeWeather
└── NaturalEnvironment
    ├── Weather
    ├── NaturalDisasters
    ├── Propagation
    └── WorldImpact
```

## Environnement dynamique

`NaturalEnvironmentSystem` doit pouvoir gérer :

- tremblements de terre ;
- tornades ;
- feux de forêt ;
- foudre / tonnerre ;
- pluies torrentielles ;
- inondations ;
- glissements de terrain.

Ces phénomènes peuvent interagir : une foudre peut déclencher un incendie, la destruction de végétation peut fragiliser le sol et une pluie torrentielle peut déclencher un glissement de terrain.

Les conséquences durables sont envoyées au `WorldState` et peuvent affecter `Ecology`, `Factions`, `Quests`, `Resources` et la navigation du monde.

## Priorité d'implémentation

1. Valider le bootstrap Unreal 5.8.1 et le mouvement de base.
2. Prototyper accroupissement + roulade + mouvement défensif.
3. Prototyper détection + furtivité.
4. Prototyper Backstab.
5. Construire les données d'espèces et de populations.
6. Implémenter les systèmes de temps, météo et environnement dynamique.
7. Implémenter les catastrophes naturelles à l'échelle régionale.
8. Implémenter la simulation écologique régionale.
9. Implémenter la persistance du monde et les transformations environnementales.
10. Ajouter le support de plusieurs mondes.
11. Optimiser la matérialisation et la simulation hors zone active.

Aucun de ces points ne doit être considéré comme implémenté uniquement parce qu'il apparaît dans cette architecture.
