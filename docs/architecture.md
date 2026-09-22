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
- Les saisons sont un état persistant du temps mondial et modifient les probabilités et conditions régionales sans forcer uniformément tous les événements.
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
│   ├── SurpriseAvoidance (Réflexe)
│   └── WeaponMastery
├── Progression
│   ├── Skills (46 canonical skills)
│   ├── Characteristics (6 canonical characteristics)
│   ├── LearningByDoing
│   ├── CharacteristicContribution
│   └── ClassPathRecognition
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
├── Time
│   ├── Calendar
│   ├── Seasons
│   └── SeasonTransition
├── Weather
├── Ecology
├── Species
├── Population
├── PredatorPrey
├── Resources
├── Migration
├── Destruction
├── NaturalEnvironment
├── Hydrology
├── RegionalDiseaseRisk
└── DynamicHazards
```

## Saison et environnement

`SeasonSystem` est connecté à `TimeSystem` et fournit un profil saisonnier au climat, à la météo, à l'écologie, aux ressources, aux maladies et aux risques naturels.

```text
TimeSystem
   ↓
SeasonSystem
   ├── Climate
   ├── Weather probabilities
   ├── Ecology
   ├── Resources
   ├── Wildlife behavior
   ├── Disease risk
   └── Hazard probability
```

Les saisons standards sont Printemps, Été, Automne et Hiver. Les durées exactes et les profils régionaux sont data-driven.

Une saison n'impose pas automatiquement un événement : elle modifie les probabilités et les conditions.

Exemples :
- Été sec → risque de feu de forêt accru ;
- Printemps / automne humides → ruissellement, inondations et glissements favorisés ;
- Hiver → froid, neige et ressources modifiées ;
- Printemps → croissance végétale et certaines périodes de reproduction ;
- saison + pénurie de proies → excursions de prédateurs plus probables.

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

Les maladies sont dépendantes des conditions régionales et peuvent évoluer avec l'eau, le climat, la faune, l'hygiène, la saison et les catastrophes.

## Montures

Deux voies d'acquisition sont prévues :

```text
Éleveur → achat
Nature → acquisition selon les règles propres à l'espèce
```

`Domptage` est une compétence canonique. Une acquisition naturelle peut utiliser Domptage, ainsi que les règles propres à l'espèce et au système de confiance/lien de la monture.

## Système Réflexe — évitement automatique des attaques surprises

`Réflexe` n'est ni une compétence ni une caractéristique. C'est un système défensif automatique qui peut éviter une attaque surprise avant qu'elle ne touche le joueur.

Son fonctionnement dépend notamment de **l'Agilité et de la Perception** du joueur. La formule exacte est data-driven et ce système ne génère aucune progression indépendante.

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
2. Prototyper mouvement, ressource d'Endurance, roulade, bond arrière, pas de côté et saut.
3. Prototyper accroupissement, furtivité et Backstab.
4. Prototyper CombatResolver, armes, blocage, parade et i-frames.
5. Prototyper progression des 46 compétences et des 6 caractéristiques.
6. Prototyper IA/Perception et Targeting.
7. Prototyper inventaire/équipement, survie, Médecine et maladies locales.
8. Prototyper nage, plongée, noyade et dégâts environnementaux.
9. Prototyper montures, acquisition et système de confiance.
10. Prototyper groupe de PNJ et magie collective.
11. Construire les données d'espèces, populations et ressources.
12. Implémenter le temps, saisons, météo, hydrologie et catastrophes naturelles.
13. Implémenter simulation écologique régionale et impacts de monde.
14. Implémenter persistance multi-mondes et transformations environnementales.
15. Profiling, tests de charge, streaming et optimisation continue.

Aucun de ces points ne doit être considéré comme implémenté uniquement parce qu'il apparaît dans l'architecture.
