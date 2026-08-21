# Merge — Natural Disasters & Dynamic Environment Specification

**Statut** : APPROUVÉ — architecture de pré-implémentation
**Engine** : Unreal Engine 5.8.1
**Langage principal** : C++20

## 1. Objectif

Le monde de Merge doit pouvoir subir des phénomènes naturels qui apparaissent, évoluent, interagissent avec les systèmes du monde et laissent des conséquences persistantes.

Ces phénomènes ne doivent pas être de simples événements scriptés isolés. Ils doivent être pilotés par des conditions environnementales, des probabilités, des régions et des événements mondiaux data-driven.

```text
NaturalEnvironmentSystem
├── WeatherSystem
├── HazardSimulation
├── NaturalDisasterSystem
├── EnvironmentalPropagation
└── WorldImpactResolver
```

## 2. Phénomènes naturels à prévoir

Le système doit pouvoir gérer au minimum :

- tremblements de terre ;
- tornades ;
- feux de forêt ;
- foudre / tonnerre ;
- pluies torrentielles ;
- glissements de terrain ;
- autres catastrophes naturelles futures sans modifier le cœur du système.

Les phénomènes peuvent être rares, régionaux, saisonniers ou dépendants de conditions spécifiques. Les valeurs exactes ne sont pas figées.

## 3. Tremblements de terre

Un tremblement de terre peut provoquer :

- secousses de caméra et de monde ;
- perte d'équilibre ;
- dégâts ;
- chute d'objets ;
- fissures / dommages environnementaux ;
- destruction ou affaiblissement de structures ;
- glissements de terrain dans les zones instables ;
- modification temporaire de l'accessibilité.

Les conséquences importantes doivent être persistantes lorsqu'elles modifient réellement le WorldState.

## 4. Tornades

Les tornades doivent être des phénomènes mobiles et localisés.

Elles peuvent :
- se déplacer selon une trajectoire ;
- modifier leur intensité ;
- repousser ou soulever des objets et entités ;
- endommager des structures ;
- modifier localement la navigation et la visibilité ;
- provoquer ou aggraver des dégâts environnementaux.

Le système doit privilégier une simulation abstraite et des effets matérialisés autour du joueur afin de préserver les performances.

## 5. Feux de forêt

Le feu doit être un phénomène **propagatif** plutôt qu'une simple zone de dégâts.

```text
Source d'ignition
      ↓
Combustion
      ↓
Propagation selon vent / sécheresse / végétation
      ↓
Incendie
      ↓
Extinction / manque de combustible
```

Le feu doit pouvoir affecter :
- végétation ;
- créatures ;
- PNJ ;
- bâtiments ;
- ressources ;
- visibilité ;
- qualité de certaines zones ;
- équilibre écologique.

Un incendie important peut modifier durablement une région : habitat détruit, population déplacée, ressources perdues, espèces favorisées ou pénalisées.

Le feu de forêt est donc connecté à `EcologySystem` et `WorldPersistence`.

## 6. Foudre et tonnerre

La foudre doit pouvoir être associée aux conditions météorologiques.

Elle peut :
- causer des dégâts ;
- enflammer certains matériaux ;
- provoquer des feux de forêt ;
- perturber certaines activités ;
- produire des événements environnementaux.

Le tonnerre est un événement sonore et atmosphérique distinct de la résolution des dégâts de foudre.

## 7. Pluies torrentielles

Les pluies fortes peuvent modifier progressivement l'environnement :

```text
Pluie intense
   ↓
Sol saturé
   ↓
Accumulation / ruissellement
   ↓
Zones boueuses / eau montante
   ↓
Érosion / inondation / instabilité
```

Conséquences possibles :
- visibilité réduite ;
- bruit ambiant modifié ;
- déplacement plus difficile ;
- débit des rivières augmenté ;
- inondation locale ;
- terrains fragilisés ;
- déclenchement ou aggravation de glissements de terrain.

## 8. Glissements de terrain

Un glissement de terrain peut être déclenché ou favorisé par :
- pluie intense ;
- tremblement de terre ;
- pente ;
- saturation du sol ;
- modification du terrain ;
- destruction de végétation.

Il peut :
- bloquer une route ;
- ensevelir une zone ;
- détruire des structures ;
- modifier une pente ou un passage ;
- créer ou supprimer un accès.

Le changement du terrain doit être enregistré dans le WorldState lorsqu'il est persistant.

## 9. Interactions entre phénomènes

Les catastrophes doivent pouvoir se déclencher ou se renforcer mutuellement.

Exemple :

```text
Orage
  ↓
Foudre
  ↓
Feu de forêt
  ↓
Végétation détruite
  ↓
Sol fragilisé
  ↓
Pluie torrentielle
  ↓
Glissement de terrain
```

Autre exemple :

```text
Tremblement de terre
  ↓
Terrain instable
  ↓
Rupture / éboulement
  ↓
Rivière obstruée
  ↓
Inondation locale
```

Le système ne doit pas nécessiter un script unique pour chaque chaîne d'événements.

## 10. Relations avec l'écologie

Les catastrophes naturelles peuvent modifier :

- populations animales ;
- zones de reproduction ;
- ressources alimentaires ;
- végétation ;
- migration ;
- prédation ;
- capacité écologique d'une région.

Exemple :

```text
Feu de forêt
   ↓
Habitat détruit
   ↓
Population locale ↓
   ↓
Migration
   ↓
Nouvelle pression écologique ailleurs
```

Ces effets doivent alimenter le système écologique plutôt que d'être simulés indépendamment.

## 11. Relations avec les PNJ et factions

Les catastrophes peuvent provoquer :
- évacuations ;
- déplacements ;
- changements de routes ;
- pénuries ;
- perte de territoire ;
- destruction de villages ;
- changements de réputation ou de pouvoir si le game design le prévoit.

Les quêtes et dialogues réactifs doivent pouvoir consulter les événements naturels importants.

## 12. Persistance

Une catastrophe qui modifie réellement le monde doit pouvoir laisser une trace persistante.

Exemples :
- forêt brûlée ;
- bâtiment détruit ;
- route ensevelie ;
- terrain effondré ;
- ressource détruite ;
- population déplacée.

Le système doit distinguer :

```text
Effet temporaire
→ météo / visibilité / vent / secousses

Effet persistant
→ destruction / terrain modifié / population déplacée / ressources perdues
```

La mort du joueur ne restaure jamais automatiquement ces changements.

## 13. Simulation et performances

Le système doit fonctionner par régions et niveaux de détail.

```text
Simulation abstraite régionale
        ↓
Détermination des zones affectées
        ↓
Matérialisation détaillée autour du joueur
```

Il ne faut pas simuler chaque particule, arbre ou objet du monde en permanence.

Les événements hors zone active peuvent être résolus statistiquement ou par batches lorsque cela ne compromet pas la cohérence du WorldState.

## 14. Architecture cible

```text
NaturalEnvironmentSystem
├── WeatherSystem
│   ├── Rain
│   ├── Storm
│   ├── Wind
│   └── Lightning
│
├── NaturalDisasterSystem
│   ├── Earthquake
│   ├── Tornado
│   ├── Wildfire
│   ├── TorrentialRain
│   └── Landslide
│
├── PropagationSystem
│   ├── FireSpread
│   ├── FloodSpread
│   └── TerrainInstability
│
└── WorldImpactResolver
    ├── Damage
    ├── Destruction
    ├── EcologyImpact
    ├── FactionImpact
    └── Persistence
```

Le système communique avec `WorldEventSystem`, `EcologySystem`, `EnvironmentalDamageSystem`, `AquaticMovementSystem`, `FactionSystem`, `QuestSystem` et `WorldPersistence`.

## 15. Événements à exposer

Prévoir des événements génériques tels que :

```text
WeatherChanged
StormStarted
LightningStrike
EarthquakeStarted
EarthquakeEnded
TornadoStarted
TornadoEnded
WildfireStarted
WildfireSpread
WildfireExtinguished
TorrentialRainStarted
FloodExpanded
LandslideTriggered
TerrainChanged
NaturalDisasterImpact
```

## 16. Tests prioritaires

- déclenchement régional d'un phénomène ;
- propagation d'un feu ;
- interaction vent / feu ;
- foudre pouvant déclencher un incendie ;
- pluie intense augmentant l'humidité du terrain ;
- glissement provoqué par terrain instable ;
- tremblement de terre affectant des structures ;
- catastrophe modifiant une population animale ;
- catastrophe modifiant une route ou une zone ;
- persistance des dégâts environnementaux ;
- cohérence hors zone chargée ;
- absence de simulation inutile à chaque frame.

## 17. Principes de conception

1. Les catastrophes naturelles sont émergentes et data-driven.
2. Elles doivent pouvoir interagir entre elles.
3. Elles peuvent modifier durablement le monde.
4. Elles peuvent modifier l'écosystème et les populations.
5. Elles peuvent modifier le comportement des PNJ et les quêtes.
6. Les effets temporaires et persistants doivent être séparés.
7. Les valeurs de fréquence, intensité et propagation restent des paramètres de game design.
8. La simulation doit être scalable et compatible avec World Partition.
