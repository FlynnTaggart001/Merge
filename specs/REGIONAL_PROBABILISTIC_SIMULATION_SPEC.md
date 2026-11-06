# Merge — Regional Probabilistic Simulation Specification

**Statut** : APPROUVÉ — architecture de performance
**Engine** : Unreal Engine 5.8.4
**Langage principal** : C++20

## 1. Principe fondamental

Merge ne doit pas simuler en temps réel l'intégralité du monde.

**Une région éloignée du joueur n'est pas simulée frame par frame.** Son évolution est représentée par un état abstrait et des probabilités conditionnelles.

La simulation détaillée n'est activée que lorsque le joueur entre dans une zone concernée ou suffisamment proche pour que les conséquences deviennent pertinentes.

```text
Joueur éloigné
    ↓
État régional + probabilités
    ↓
Pas de simulation détaillée

Joueur approche
    ↓
Résolution de l'évolution hors caméra
    ↓
Activation de la simulation locale
    ↓
Matérialisation détaillée
```

## 2. Objectifs

Ce modèle doit permettre :

- un monde systémique très vaste ;
- écologie dynamique ;
- catastrophes naturelles ;
- météo ;
- populations animales ;
- factions et PNJ ;
- persistance des conséquences ;
- coût CPU maîtrisé.

## 3. État régional abstrait

Chaque région possède un état compact pouvant contenir :

```text
RegionState
├── TimeState
├── WeatherState
├── EcologyState
├── PopulationState
├── ResourceState
├── FactionState
├── HazardState
├── TerrainChangeState
├── WorldEventHistory
└── RandomSeed / DeterministicState
```

Les valeurs représentent des tendances, populations, réserves, risques et événements persistants, pas une simulation de chaque individu.

## 4. Probabilités conditionnelles

Chaque événement naturel ou écologique utilise des probabilités conditionnées par l'état de la région.

Exemples :

```text
Probabilité de pluie
= climat + saison + météo actuelle + région
```

```text
Probabilité de feu de forêt
= sécheresse + vent + combustible + sources d'ignition
```

```text
Probabilité de glissement
= pente + saturation du sol + pluie + séisme + état du terrain
```

```text
Probabilité d'éruption
= état du volcan + activité + séisme local + autres précurseurs
```

La probabilité ne signifie pas que le phénomène est aléatoire sans logique : elle doit être issue des conditions du monde.

## 5. Résolution hors zone

Lorsque le joueur n'est pas dans une région, le système ne fait pas tourner les phénomènes détaillés.

À la place, lors d'un point de résolution pertinent, il détermine statistiquement ce qui a pu arriver depuis la dernière résolution :

```text
Dernière résolution : Jour 120
Joueur revient : Jour 145

↓

Résolution régionale des 25 jours

↓

- météo agrégée
- probabilité d'événement naturel
- évolution population
- migrations agrégées
- ressources consommées / produites
- changements de faction
- propagation abstraite des risques
- excursions territoriales de prédateurs
```

Le système ne doit pas nécessairement simuler chaque journée individuellement si une résolution statistique ou analytique donne un résultat cohérent.

## 6. Territoires et déplacements des prédateurs

Les prédateurs possèdent un **territoire principal** dans lequel ils passent la majorité de leur temps. Le territoire est une zone écologique préférentielle, pas une frontière invisible impossible à franchir.

```text
Territoire principal
├── déplacements quotidiens
├── recherche de proies
├── repos
└── reproduction / interactions sociales selon l'espèce
```

Les prédateurs peuvent **quitter occasionnellement leur territoire** pour explorer les alentours. Une excursion peut être déclenchée ou favorisée par :

- baisse locale des proies ;
- recherche de nourriture ;
- concurrence entre prédateurs ;
- changement de saison ;
- conditions météorologiques ;
- perturbation du territoire ;
- catastrophe naturelle ;
- recherche d'un partenaire ou comportement social ;
- qualité d'un habitat voisin ;
- caractéristiques propres à l'espèce.

L'excursion reste généralement limitée dans le temps ou la distance, avec une **probabilité de retour** vers le territoire principal. Certaines espèces peuvent toutefois effectuer des déplacements plus longs lorsque leurs données le permettent.

### 6.1 Continuum de migration

Il faut distinguer :

```text
Patrouille / déplacement local
        ↓
Excursion hors territoire
        ↓
Exploration prolongée
        ↓
Déplacement saisonnier
        ↓
Migration / changement de territoire
```

Une simple sortie temporaire ne doit donc pas transformer automatiquement un prédateur en migrant permanent.

### 6.2 Gestion probabiliste hors zone

Hors zone joueur, les excursions sont représentées par des événements agrégés :

```text
Prédateurs d'une région
        ↓
Probabilité d'excursion
        ↓
Région voisine candidate
        ↓
Probabilité d'établissement temporaire / retour
        ↓
Mise à jour des populations régionales
```

Le système peut enregistrer qu'une fraction de la population de prédateurs est momentanément hors territoire sans créer les individus correspondants comme Actors Unreal.

### 6.3 Matérialisation locale

Lorsque le joueur entre dans une zone :

- les prédateurs dont le territoire ou l'excursion intersecte la zone peuvent être matérialisés ;
- leur position de départ est cohérente avec la résolution régionale ;
- leur comportement local reprend à partir de cet état ;
- un prédateur en excursion peut donc être rencontré dans une zone où il n'est normalement pas résident.

Cela permet de conserver des rencontres rares et naturelles sans sacrifier les performances.

## 7. Entrée dans une zone

Lorsque le joueur entre dans une région :

```text
RegionState
    ↓
ResolvePendingSimulation()
    ↓
ApplyRegionalConsequences()
    ↓
Spawn / Materialize relevant actors
    ↓
Enable local simulation
```

La zone devient alors un espace de simulation détaillée.

## 8. Simulation locale

À proximité du joueur, les systèmes peuvent utiliser des simulations plus précises :

- Actors animaux ;
- IA ;
- feu visible ;
- lave ;
- eau ;
- météo locale ;
- dégâts environnementaux ;
- interactions physiques ;
- navigation ;
- effets visuels.

La précision dépend de la distance au joueur et du besoin gameplay.

## 9. Catastrophes naturelles

Une catastrophe éloignée peut exister dans l'état abstrait :

```text
Volcan
→ activité élevée
→ probabilité d'éruption 0.08
```

Si l'événement est tiré lors d'une résolution :

```text
Volcan en éruption
→ 3 coulées estimées
→ zone affectée déterminée par le relief régional
→ feu possible
→ terrain impacté
```

Lorsque le joueur arrive, seuls les résultats nécessaires sont matérialisés.

## 10. Écologie

Les populations hors zone sont traitées comme des distributions ou compteurs :

```text
Sangliers : 420
Hydres : 8
Cerfs : 610
```

Le modèle peut estimer :
- reproduction ;
- mortalité ;
- prédation ;
- migration ;
- excursions territoriales ;
- ressources ;
- capacité écologique.

Il ne doit pas créer les 1 038 animaux comme Actors Unreal hors besoin.

## 11. PNJ et factions

Les PNJ hors zone peuvent être représentés par des états abstraits :

- emplacement régional ;
- activité ;
- faction ;
- état de santé/mort ;
- objectifs ;
- relations importantes ;
- événements déjà vécus.

Lorsqu'une zone devient active, les PNJ nécessaires sont matérialisés et reprennent leur comportement local.

## 12. Cohérence et déterminisme

Chaque région doit pouvoir utiliser un état pseudo-aléatoire déterministe ou un seed persistant afin que la résolution ne produise pas des incohérences lors des sauvegardes/rechargements.

Le système doit enregistrer les résultats des événements importants plutôt que de rejouer le hasard différemment à chaque chargement.

## 13. Distances de simulation

Prévoir plusieurs niveaux :

```text
Niveau 0 — Hors monde / très éloigné
→ résolution statistique minimale

Niveau 1 — Région éloignée
→ simulation abstraite

Niveau 2 — Région proche
→ simulation simplifiée

Niveau 3 — Zone active
→ simulation gameplay détaillée

Niveau 4 — Proximité immédiate
→ précision maximale nécessaire au gameplay
```

Les seuils exacts seront déterminés par profiling.

## 14. Persistance

Les résultats d'une résolution hors zone sont enregistrés dans `WorldState`.

Exemples :

```text
Population change
PredatorExcursionResult
FireSpreadResult
VolcanoState
LandslideState
FloodState
ResourceChange
FactionEvent
TerrainChange
```

Le joueur doit retrouver le même état du monde après sauvegarde/chargement.

## 15. Règles

1. Ne jamais simuler chaque créature du monde en permanence.
2. Ne jamais faire tourner les catastrophes détaillées hors des zones pertinentes.
3. Utiliser des probabilités conditionnelles et des résolutions agrégées hors zone.
4. Les prédateurs ont un territoire principal mais peuvent effectuer des excursions occasionnelles dans des zones voisines.
5. Une excursion ne doit pas être confondue avec une migration permanente.
6. Activer la simulation détaillée lorsque le joueur entre dans la zone.
7. Conserver les résultats dans le WorldState.
8. Utiliser des états/seed déterministes pour éviter les incohérences.
9. La simulation locale peut devenir beaucoup plus précise sans changer l'état abstrait global.
10. Les résultats doivent rester cohérents avec l'écologie, les factions, les quêtes et la persistance.
