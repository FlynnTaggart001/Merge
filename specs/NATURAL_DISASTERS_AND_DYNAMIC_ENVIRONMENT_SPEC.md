# Merge — Natural Disasters & Dynamic Environment Specification

**Statut** : APPROUVÉ — architecture de pré-implémentation
**Engine** : Unreal Engine 5.8.1
**Langage principal** : C++20

## Volcan et éruption

Merge peut contenir des volcans en zones montagneuses. Un volcan possède des états de sommeil, activité accrue, signes précurseurs, éruption, phase post-éruptive et refroidissement.

## Coulées de lave

Une éruption peut produire plusieurs coulées de lave qui suivent autant que possible la topographie. Elles peuvent ralentir selon pente et obstacles, produire chaleur et dégâts extrêmes, détruire des éléments compatibles, obstruer des passages, remplir des creux et fonds de ravins, puis refroidir et créer de nouvelles surfaces dangereuses ou modifier des itinéraires.

```text
Éruption
  ↓
Coulée de lave
  ├── chaleur / dégâts
  ├── incendie
  ├── obstruction de passage
  ├── remplissage de ravin / dépression
  └── refroidissement → nouvelle surface
```

La lave peut déclencher et alimenter le système de feux de forêt.

## Zones de danger

Les coulées peuvent créer des `DynamicHazardZone` persistantes utilisables par combat, IA, navigation, quêtes et sauvegarde :

```text
DynamicHazardZone
├── BurnDamage
├── ExtremeHeat
├── NavigationRestriction
├── FirePropagation
└── TerrainChange
```

## Interactions naturelles

Les catastrophes peuvent former des chaînes systémiques :

```text
Séisme → instabilité → glissement de terrain
Éruption → lave → incendie
Pluie torrentielle → terrain saturé → glissement / inondation
Foudre → végétation inflammable → incendie
```

## Monde et écologie

Les catastrophes peuvent modifier terrain, routes, bâtiments, végétation, ressources, populations animales, migrations, territoires, factions, PNJ et quêtes. Les conséquences durables sont enregistrées dans le `WorldState` et ne sont pas annulées par le temps ou un rechargement.

Exemple :

```text
Éruption → forêt détruite → herbivores déplacés/morts → prédateurs déplacés → nouvel équilibre écologique
```

## Architecture

```text
NaturalEventSystem
├── Earthquake
├── Tornado
├── Wildfire
├── Lightning
├── TorrentialRain
├── Flood
├── Landslide
├── VolcanicEruption
└── FutureNaturalEvents[*]

VolcanoSystem
├── VolcanoState
├── Precursors
├── EruptionEvent
├── LavaFlowSimulation
├── HeatZones
├── Ash / Smoke
└── Cooling / Solidification
```

La simulation hors zone active doit pouvoir rester abstraite et régionale ; les effets détaillés ne sont matérialisés que lorsque nécessaire.

## Tests prioritaires

Éruption en montagne, suivi de topographie, coulée dans un ravin, accumulation en dépression, déclenchement d'incendie, zone de danger, refroidissement, changement de navigation, impact écologique et persistance après sauvegarde/chargement.

Les valeurs d'intensité, vitesse, durée, portée et dégâts restent des paramètres data-driven à équilibrer dans Unreal.
