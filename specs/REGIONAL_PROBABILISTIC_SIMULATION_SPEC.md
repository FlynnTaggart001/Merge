# Merge — Regional Probabilistic Simulation Specification

**Statut** : APPROUVÉ — architecture de performance
**Engine** : Unreal Engine 5.8.1
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
```

Le système ne doit pas nécessairement simuler chaque journée individuellement si une résolution statistique ou analytique donne un résultat cohérent.

## 6. Entrée dans une zone

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

## 7. Simulation locale

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

## 8. Catastrophes naturelles

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

## 9. Écologie

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
- ressources ;
- capacité écologique.

Il ne doit pas créer les 1 038 animaux comme Actors Unreal hors besoin.

## 10. PNJ et factions

Les PNJ hors zone peuvent être représentés par des états abstraits :

- emplacement régional ;
- activité ;
- faction ;
- état de santé/mort ;
- objectifs ;
- relations importantes ;
- événements déjà vécus.

Lorsqu'une zone devient active, les PNJ nécessaires sont matérialisés et reprennent leur comportement local.

## 11. Cohérence et déterminisme

Chaque région doit pouvoir utiliser un état pseudo-aléatoire déterministe ou un seed persistant afin que la résolution ne produise pas des incohérences lors des sauvegardes/rechargements.

Le système doit enregistrer les résultats des événements importants plutôt que de rejouer le hasard différemment à chaque chargement.

## 12. Distances de simulation

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

## 13. Persistance

Les résultats d'une résolution hors zone sont enregistrés dans `WorldState`.

Exemples :

```text
Population change
FireSpreadResult
VolcanoState
LandslideState
FloodState
ResourceChange
FactionEvent
TerrainChange
```

Le joueur doit retrouver le même état du monde après sauvegarde/chargement.

## 14. Règles

1. Ne jamais simuler chaque créature du monde en permanence.
2. Ne jamais faire tourner les catastrophes détaillées hors des zones pertinentes.
3. Utiliser des probabilités conditionnelles et des résolutions agrégées hors zone.
4. Activer la simulation détaillée lorsque le joueur entre dans la zone.
5. Conserver les résultats dans le WorldState.
6. Utiliser des états/seed déterministes pour éviter les incohérences.
7. La simulation locale peut devenir beaucoup plus précise sans changer l'état abstrait global.
8. Les résultats doivent rester cohérents avec l'écologie, les factions, les quêtes et la persistance.
