# Merge — Seasonality & Seasonal Cycle Specification

**Statut** : APPROUVÉ — architecture de pré-implémentation
**Engine** : Unreal Engine 5.8.4
**Langage principal** : C++20

## 1. Objectif

Le monde de Merge possède un cycle saisonnier persistant. Les saisons modifient progressivement le climat, l'écologie, les ressources, les comportements des créatures, les maladies et certains risques environnementaux.

Le système doit rester data-driven afin que chaque région puisse interpréter les saisons différemment.

```text
TimeSystem
   ↓
SeasonSystem
   ├── Climate
   ├── Weather
   ├── Ecology
   ├── Resources
   ├── WildlifeBehavior
   ├── DiseaseRisk
   └── WorldEvents
```

## 2. Cycle saisonnier

Le cycle standard peut utiliser quatre saisons :

```text
Printemps → Été → Automne → Hiver → Printemps
```

La durée exacte des saisons est un paramètre de game design et peut varier selon le monde ou la région si cela apporte une valeur réelle.

Le changement de saison doit être progressif et déterministe dans la sauvegarde du monde.

## 3. Variations régionales

Une saison n'a pas le même effet partout.

```text
Light Fantasy
→ saisons plus tempérées

Fantasy classique
→ cycle équilibré

Dark Fantasy
→ saisons plus rudes / effets plus extrêmes selon le lore

Montagne / volcan
→ températures et conditions spécifiques à l'altitude
```

Une région peut donc avoir son propre profil saisonnier tout en partageant le calendrier mondial.

## 4. Météo et saisons

Les saisons modifient les probabilités météorologiques plutôt que de forcer une météo fixe.

Exemples :

```text
Hiver
→ probabilité de froid / neige ↑
→ végétation active ↓

Printemps
→ pluie ↑
→ croissance végétale ↑

Été
→ chaleur / sécheresse ↑
→ risque de feu de forêt ↑

Automne
→ pluie / vent ↑
→ ressources et migrations modifiées
```

Ces valeurs restent probabilistes et régionales.

## 5. Écologie saisonnière

Les saisons peuvent influencer :

- reproduction ;
- périodes de rut ;
- naissance ;
- mortalité naturelle ;
- disponibilité des proies ;
- migration ;
- territoire ;
- hibernation ou dormance ;
- comportement des prédateurs ;
- croissance et renouvellement de la végétation.

Un prédateur peut par exemple étendre ses excursions lorsque les proies deviennent rares en hiver.

## 6. Ressources et nourriture

La disponibilité des ressources peut varier selon la saison :

- fruits ;
- plantes ;
- gibier ;
- poissons ;
- récoltes ;
- plantes médicinales ;
- eau disponible en surface.

La pénurie peut modifier les déplacements des animaux, les prix des élevages, les ressources d'un village et les choix du joueur.

## 7. Maladies saisonnières

Les saisons modifient les conditions de certaines maladies régionales.

```text
Été chaud + humidité
→ vecteurs / maladies favorisés

Hiver froid
→ certaines infections favorisées
→ autres maladies / parasites réduits

Printemps + pluie
→ eau stagnante / vecteurs possibles
```

Le système de diagnostic diégétique reste inchangé : une maladie n'est jamais révélée automatiquement par un texte.

## 8. Catastrophes et risques saisonniers

Les saisons modifient les probabilités de catastrophes :

```text
Été sec
→ incendies de forêt plus probables

Printemps / automne pluvieux
→ ruissellement / inondations / glissements plus probables

Hiver
→ neige / gel / routes difficiles
```

Les conditions saisonnières peuvent également modifier les risques volcaniques et géologiques, mais sans provoquer artificiellement une catastrophe sans conditions physiques compatibles.

## 9. Faune et excursions

Les territoires des prédateurs restent définis, mais la saison peut influencer la probabilité qu'ils quittent leur zone pour explorer une région voisine.

```text
Territoire principal
      ↓
Saison + nourriture + météo + pression écologique
      ↓
Probabilité d'excursion
      ↓
Zone voisine
      ↓
Retour probable ou déplacement prolongé
```

Une excursion reste distincte d'une migration définitive.

## 10. Joueur et besoins physiologiques

Les saisons peuvent modifier les besoins du joueur :

- hydratation accrue en période chaude ;
- consommation d'énergie modifiée par le froid ;
- qualité du sommeil influencée par température, météo et abri ;
- risque de certaines maladies régionales ;
- disponibilité de nourriture et d'eau.

Ces modifications doivent rester équilibrées et ne pas transformer les saisons en pénalités permanentes.

## 11. Monde persistant

Le changement de saison est une modification du `WorldState`.

```text
WorldState
├── TimeState
│   └── Season
├── WeatherState
├── EcologyState
├── ResourceState
├── DiseaseState
└── HazardState
```

Une sauvegarde/restauration doit préserver la date et la saison afin que les événements futurs restent cohérents.

## 12. Simulation probabiliste

Hors zone active, la saison est intégrée au calcul régional :

```text
RegionState
+ Season
+ Weather
+ Ecology
        ↓
ProbabilisticResolution
```

Le jeu ne simule pas chaque jour de chaque région à haute précision.

Lors de l'entrée du joueur dans une région, les conséquences saisonnières pertinentes sont résolues puis matérialisées localement.

## 13. Architecture

```text
SeasonSystem
├── Calendar
├── CurrentSeason
├── SeasonTransition
├── RegionalSeasonProfile
├── SeasonalClimateResolver
├── SeasonalEcologyResolver
├── SeasonalResourceResolver
├── SeasonalDiseaseResolver
└── SeasonalHazardResolver
```

Le système communique avec `TimeSystem`, `WeatherSystem`, `EcologySystem`, `FoodSystem`, `DiseaseSystem`, `SurvivalNeedsSystem`, `NaturalEnvironmentSystem` et `RegionalProbabilisticSimulation`.

## 14. Tests prioritaires

- passage de saison ;
- sauvegarde / chargement pendant une transition ;
- météo influencée par la saison ;
- reproduction saisonnière ;
- migration/excursions saisonnières ;
- ressources saisonnières ;
- maladies saisonnières ;
- incendie estival ;
- inondation/glissement en période humide ;
- besoins physiologiques influencés par la saison ;
- résolution hors zone ;
- cohérence après retour du joueur dans une région inactive.

## 15. Principes de conception

1. Une saison modifie des probabilités et conditions, elle ne doit pas forcer tous les événements.
2. Les effets saisonniers sont régionaux et data-driven.
3. Les saisons sont persistantes dans le monde.
4. Les saisons alimentent l'écologie, les maladies, les ressources, la météo et les risques naturels.
5. La simulation détaillée reste locale au joueur ; hors zone, les effets sont agrégés.
