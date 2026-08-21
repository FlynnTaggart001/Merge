# Architecture — Gameplay, Ecology, Survival & Persistence

## Scope

Cette page décrit les implications architecturales des systèmes approuvés dans les spécifications de Merge. Les règles détaillées restent dans les specs spécialisées et `specs/SYSTEM_INTEGRATION_MATRIX.md`.

## Principes

- Les systèmes de mouvement, furtivité, combat, survie, maladies, montures et magie restent modulaires.
- Le Backstab consomme les informations du système de furtivité et du positionnement, mais ne fusionne pas les deux systèmes.
- L'écologie simule des populations abstraites ; elle ne crée pas un Actor par individu hors nécessité.
- La persistance appartient au monde et restaure les états de monde nécessaires au gameplay.
- Plusieurs mondes doivent être isolables dans le système de sauvegarde.
- Les phénomènes naturels sont simulés à l'échelle régionale puis matérialisés localement lorsque nécessaire.
- Les besoins hors zone sont résolus par probabilités/agrégats, pas par simulation individuelle à chaque frame.
- Tout système majeur doit disposer d'une stratégie de simulation distante et de tests de charge avant son implémentation complète.

## Domaines

```text
Character
├── Movement
│   ├── Roll
│   ├── BackwardJump
│   ├── SideStep
│   ├── ObstacleTraversal
│   ├── ContextualClimb
│   └── ControlledLanding
├── Stealth / Backstab
├── Combat
│   ├── Targeting
│   ├── Block
│   ├── Parry
│   ├── Dodge / i-frames
│   └── WeaponMastery
├── Progression
│   ├── Endurance
│   ├── Agility
│   ├── Defense
│   ├── Reflex
│   ├── Domptage
│   ├── Medicine
│   └── MagicDomainMastery[*]
├── Survival
│   ├── Hunger
│   ├── Hydration
│   ├── Sleep / Fatigue
│   └── PhysiologicalCondition
├── Disease
├── AquaticMovement
└── Mount / Rider

Social / Magic
├── Party
├── GroupMagic
├── Factions
└── Reputation

World
├── Persistence
├── Ecology
├── Species
├── Population
├── PredatorPrey
├── Resources
├── Migration
├── Destruction
├── Time / Weather
├── NaturalEnvironment
├── Hydrology
├── RegionalDiseaseRisk
└── DynamicHazards
```

## Environnement dynamique

`NaturalEnvironmentSystem` doit pouvoir gérer au minimum :

- tremblements de terre ;
- tornades ;
- feux de forêt ;
- foudre / tonnerre ;
- pluies torrentielles ;
- inondations ;
- glissements de terrain ;
- activité/éruptions volcaniques ;
- coulées de lave.

Les phénomènes peuvent interagir : une foudre peut déclencher un incendie, la destruction de végétation peut fragiliser le sol, une pluie torrentielle peut déclencher un glissement, et un séisme compatible peut augmenter la probabilité de réveil d'un volcan.

## Survie et maladies

Les besoins physiologiques sont progressifs : faim, hydratation et sommeil peuvent conduire à des états de faiblesse ou critiques. Le joueur n'est pas informé automatiquement du nom d'une maladie.

Le diagnostic doit être diégétique :

```text
Symptômes observables
   ├── Médecine du joueur → autodiagnostic
   └── Médecin PNJ       → diagnostic professionnel
```

Les maladies sont dépendantes des conditions régionales et peuvent évoluer avec l'eau, le climat, la faune, l'hygiène et les catastrophes.

## Montures

Deux voies d'acquisition sont prévues :

```text
Éleveur → achat
Nature → domptage
```

Il n'existe pas de système générique de marchand de bêtes. La compétence `Domptage` appartient au joueur et reste distincte du lien/confiance propre à la monture.

## Ciblage et groupe

Le `TargetingSystem` privilégie les cibles proches, puis parcourt les cibles valides selon distance, angle et visibilité.

Le `PartySystem` maintient des PNJ autonomes, et le `GroupMagicSystem` permet des rituels multi-participants avec positionnement, synchronisation, ressources, compatibilité et interruption.

## Eau et hydrologie

Le système aquatique gère eau peu profonde, flottaison, nage, plongée, respiration et noyade. La flottabilité dépend notamment de l'équipement : une armure lourde peut faire couler le personnage ou compliquer fortement la remontée.

La grande colline de la région Light Fantasy possède un lac d'altitude dont les eaux peuvent alimenter des rivières et provoquer des débordements, torrents et inondations en aval.

## Simulation et performance

Tout système majeur suit :

```text
Hors zone joueur
→ probabilité / état régional / agrégat

Entrée zone
→ résolution de l'état
→ matérialisation pertinente

Zone active
→ simulation locale détaillée

Sortie zone
→ agrégation
→ WorldState
```

World Partition, streaming, culling, LOD/HLOD, timers/batches, IA à fréquence adaptée et profiling Unreal sont des contraintes d'architecture, pas uniquement des optimisations de fin de projet.

## Priorité d'implémentation

1. Valider le bootstrap Unreal 5.8.1 et le mouvement de base.
2. Prototyper mouvement, Endurance, roulade, bond arrière, pas de côté et saut.
3. Prototyper accroupissement, furtivité et Backstab.
4. Prototyper CombatResolver, armes, blocage, parade et i-frames.
5. Ajouter Réflexe et familiarité défensive.
6. Prototyper IA/Perception et Targeting.
7. Prototyper inventaire/équipement, survie, Médecine et maladies locales.
8. Prototyper nage, plongée, noyade et dégâts environnementaux.
9. Prototyper montures et Domptage.
10. Prototyper groupe de PNJ et magie collective.
11. Construire les données d'espèces, populations et ressources.
12. Implémenter le temps, météo, hydrologie et catastrophes naturelles.
13. Implémenter simulation écologique régionale et impacts de monde.
14. Implémenter persistance multi-mondes et transformations environnementales.
15. Profiling, tests de charge, streaming et optimisation continue.

Aucun de ces points ne doit être considéré comme implémenté uniquement parce qu'il apparaît dans l'architecture.