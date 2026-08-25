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
- **activité et éruptions volcaniques** ;
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
- modification temporaire de l'accessibilité ;
- **perturbation ou activation d'un volcan lorsque les conditions géologiques prévues sont réunies**.

Les conséquences importantes doivent être persistantes lorsqu'elles modifient réellement le WorldState.

## 4. Volcan et réveil volcanique

Le monde peut contenir un ou plusieurs volcans situés dans des régions montagneuses.

Un volcan possède un état pouvant évoluer :

```text
Dormant
  ↓
Dormance active / Pression interne
  ↓
Activité accrue
  ↓
Signes précurseurs
  ↓
Éruption
  ↓
Coulées / projections / fumées / chaleur
  ↓
Phase post-éruptive
  ↓
Refroidissement / nouvelle stabilité
```

### 4.1 Déclenchement par événements naturels

Un volcan ne doit pas forcément se réveiller uniquement selon un timer.

Un **tremblement de terre** suffisamment important, proche et compatible avec l'état du volcan peut augmenter sa pression d'activité et provoquer une transition vers un état plus actif.

```text
Séisme régional
      ↓
Évaluation de la proximité / magnitude / état du volcan
      ↓
Impact géologique
      ↓
Pression volcanique ↑
      ↓
Activité accrue
      ↓
Signes précurseurs
      ↓
Éruption possible
```

La règle ne doit pas être déterministe : un séisme compatible peut **augmenter la probabilité** d'un réveil sans garantir une éruption à chaque fois.

D'autres événements géologiques futurs pourront également influencer l'activité du volcan via le même système d'événements.

### 4.2 Signes précurseurs

Les signes précurseurs peuvent inclure :

- fumées ou vapeur ;
- grondements ;
- secousses locales ;
- chaleur accrue ;
- changements de sources ou d'eau selon le design ;
- comportement inhabituel de la faune ;
- modifications locales de l'environnement.

Ces signes peuvent avertir le joueur et les PNJ sans révéler immédiatement la conséquence finale.

## 5. Coulées de lave

Une éruption peut générer une ou plusieurs **coulées de lave** suivant le relief.

La lave doit :

- suivre la topographie autant que possible ;
- ralentir ou s'arrêter selon la pente, le terrain et les obstacles ;
- produire des zones de chaleur et de danger ;
- détruire ou transformer certains éléments de l'environnement ;
- pouvoir déclencher des incendies ;
- pouvoir obstruer des passages ;
- pouvoir remplir progressivement des creux et certains fonds de ravins ;
- créer de nouvelles surfaces dangereuses après refroidissement.

Le chemin exact de la lave doit être déterminé par les données de terrain/région plutôt que par un tracé arbitraire.

## 6. Lave et incendies

Une coulée de lave peut enflammer la végétation, les structures ou d'autres matériaux combustibles compatibles :

```text
Éruption
   ↓
Lave
   ↓
Contact avec végétation / structures combustibles
   ↓
Incendie
   ↓
Feu de forêt / destruction locale
```

Le système doit fusionner avec la propagation des feux de forêt déjà prévue.

## 7. Lave et ravins

Les ravins, vallées et dépressions du terrain sont des zones importantes pour la simulation des coulées.

Une coulée peut descendre dans un ravin, s'accumuler dans une dépression, former une zone de lave temporairement active, refroidir et solidifier progressivement et modifier durablement certains itinéraires selon les possibilités techniques du prototype.

Le jeu doit distinguer :

```text
Lave active
→ dégâts extrêmes / chaleur / zone interdite

Lave refroidissante
→ danger résiduel / température / accès limité

Roche solidifiée
→ nouvelle surface / modification du terrain
```

## 8. Zones de danger dynamiques

Les catastrophes doivent pouvoir créer des `DynamicHazardZone` persistantes :

```text
Volcan
 ↓
Coulée de lave
 ↓
DynamicHazardZone
 ├── BurnDamage
 ├── ExtremeHeat
 ├── NavigationRestriction
 ├── FirePropagation
 └── TerrainChange
```

Les zones de danger doivent être connues du système d'IA, du système de navigation, du joueur, des quêtes et de la sauvegarde du monde lorsque nécessaire.

## 9. Interactions entre catastrophes

Les phénomènes peuvent se déclencher ou amplifier mutuellement :

```text
Séisme → instabilité du terrain → glissement de terrain
Séisme → impact volcanique → réveil possible du volcan
Éruption → lave → feu de forêt
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

Ces chaînes sont pilotées par des événements et des conditions plutôt que par des scripts uniques.

## 10. Impact sur le monde

Une catastrophe peut modifier :
- terrain et passages ;
- routes ;
- bâtiments ;
- végétation ;
- ressources ;
- populations animales ;
- migration ;
- territoires ;
- factions ;
- PNJ ;
- quêtes ;
- zones de danger ;
- navigation IA.

Les conséquences permanentes doivent être sauvegardées avec le `WorldState` lorsque leur effet est durable.

## 11. Écologie

Les événements naturels doivent être intégrés à l'écologie.
## Monde et écologie

Les catastrophes peuvent modifier terrain, routes, bâtiments, végétation, ressources, populations animales, migrations, territoires, factions, PNJ et quêtes. Les conséquences durables sont enregistrées dans le `WorldState` et ne sont pas annulées par le temps ou un rechargement.

Exemple :

```text
Éruption
 ↓
Forêt détruite
 ↓
Herbivores déplacés / morts
 ↓
Prédateurs déplacés
 ↓
Nouvel équilibre écologique
```

## 12. Architecture
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
├── GeologicalTriggers
│   ├── EarthquakeInfluence
│   └── FutureGeologicalInfluences[*]
├── Precursors
├── EruptionEvent
├── LavaFlowSimulation
├── HeatZones
├── Ash / Smoke
└── Cooling / Solidification

DynamicHazardSystem
├── Burn
├── ExtremeHeat
├── Collapse
├── HazardZone
└── NavigationImpact
```

La simulation des événements hors zone active doit pouvoir être abstraite et régionale. Les effets visuels détaillés peuvent être matérialisés uniquement lorsque la zone est chargée.

## 13. Persistance

Les catastrophes ne doivent pas réinitialiser automatiquement le monde après chargement.

Selon le phénomène, la sauvegarde peut conserver : état du volcan, activité déclenchée par un séisme, zones incendiées, terrain modifié, zones de lave, passages bloqués, nouvelles zones de danger, conséquences écologiques et historique des événements.

## 14. Tests prioritaires

- séisme proche d'un volcan dormant ;
- séisme suffisamment puissant augmentant la probabilité d'activité ;
- absence d'éruption lorsque les conditions ne sont pas remplies ;
- accumulation de plusieurs signaux précurseurs ;
- transition activité → éruption ;
- génération de plusieurs coulées ;
- suivi de la topographie ;
- lave entrant dans un ravin ;
- accumulation dans une dépression ;
- déclenchement d'un feu de forêt ;
- création d'une zone de danger ;
- refroidissement / solidification ;
- modification des chemins et navigation ;
- impact sur une population animale ;
- persistance après sauvegarde/chargement ;
- interaction séisme → glissement ;
- interaction pluie → terrain instable.

## 15. Principes

1. Une catastrophe naturelle est un événement systémique, pas seulement un effet visuel.
2. Les phénomènes doivent pouvoir agir sur le monde de manière émergente.
3. Les coulées de lave suivent autant que possible le relief.
4. La lave peut déclencher des incendies et transformer des ravins/vallées.
5. Un séisme peut augmenter la probabilité de réveil d'un volcan lorsque les conditions régionales sont réunies, sans rendre l'éruption automatique.
6. Les conséquences durables doivent être compatibles avec le monde non régénératif.
7. Les zones de danger doivent être utilisables par les autres systèmes du jeu.
8. Les simulations hors zone active doivent rester abstraites lorsque possible pour préserver les performances.
9. Les valeurs d'intensité, fréquence, vitesse, durée, seuils géologiques et dégâts sont des paramètres de game design à équilibrer dans Unreal.
```

La simulation hors zone active doit pouvoir rester abstraite et régionale ; les effets détaillés ne sont matérialisés que lorsque nécessaire.

## Tests prioritaires

Éruption en montagne, suivi de topographie, coulée dans un ravin, accumulation en dépression, déclenchement d'incendie, zone de danger, refroidissement, changement de navigation, impact écologique et persistance après sauvegarde/chargement.

Les valeurs d'intensité, vitesse, durée, portée et dégâts restent des paramètres data-driven à équilibrer dans Unreal.
