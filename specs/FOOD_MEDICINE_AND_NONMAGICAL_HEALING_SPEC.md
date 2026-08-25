# Merge — Food, Medicine, Sleep & Non-Magical Healing Specification

**Statut** : APPROUVÉ — architecture de pré-implémentation
**Engine** : Unreal Engine 5.8.1
**Langage principal** : C++20

## 1. Principe

Merge doit distinguer plusieurs voies de récupération et d'état physiologique :

```text
Récupération / État physiologique
├── Nourriture / hydratation
├── Sommeil / fatigue
├── Médecine / soins non magiques
└── Magie de soin
```

La magie ne doit pas remplacer les besoins physiques du personnage. Les soins non magiques et les besoins physiologiques restent importants même dans un monde où la magie existe.

## 2. Système de nourriture et besoins physiologiques

Le personnage dispose d'un système de faim, d'alimentation et d'hydratation.

La faim et l'hydratation ne sont pas seulement des jauges d'interface : leur niveau influence progressivement l'état physiologique du personnage.

```text
Besoin satisfait
      ↓
État normal
      ↓
Besoin faible
      ↓
Mal nourri / déshydraté
      ↓
État sévère
      ↓
État critique
```

Les seuils, durées et effets exacts sont data-driven.

### 2.1 Malnutrition / faim prolongée

Lorsque le personnage reste trop longtemps sans alimentation suffisante, il peut entrer dans un état `Malnourished` ou dans des paliers équivalents.

Conséquences potentielles, à équilibrer : récupération physique réduite, Endurance maximale ou récupération diminuée, faiblesse générale, capacité d'effort réduite, résistance aux blessures éventuellement diminuée, progression physique temporairement moins efficace et, à un stade critique, perte de santé ou incapacité prolongée.

Les effets doivent progresser graduellement plutôt que passer brutalement de normal à critique.

### 2.2 Déshydratation

Lorsque le personnage reste trop longtemps sans boire, il peut entrer dans un état `Dehydrated` ou dans des paliers équivalents.

Conséquences potentielles, à équilibrer : récupération d'Endurance réduite, consommation d'Endurance augmentée, efficacité des déplacements réduite, faiblesse générale, récupération des blessures ralentie et, à un stade critique, dégâts progressifs ou incapacité.

### 2.3 Combinaison faim + déshydratation

Les deux états peuvent se cumuler.

```text
Mal nourri + déshydraté
        ↓
Fatigue / faiblesse accrue
        ↓
Récupération dégradée
        ↓
Risque critique augmenté
```

Le système doit éviter une simple addition aveugle des pénalités : les effets combinés passent par un resolver d'états.

### 2.4 Récupération

La récupération suit la consommation de ressources adaptées et le temps nécessaire au retour à l'équilibre. Une seule consommation ne doit pas forcément annuler immédiatement plusieurs niveaux d'état critique.

## 3. Sommeil et fatigue

Le personnage possède un **besoin de sommeil** distinct de la faim et de l'hydratation.

Le sommeil se comporte comme un état physiologique progressif plutôt qu'un simple bouton « dormir » :

```text
Repos suffisant
      ↓
Éveillé / reposé
      ↓
Fatigue légère
      ↓
Fatigue importante
      ↓
Épuisement
      ↓
État critique / risque d'effondrement
```

### 3.1 Effets du manque de sommeil

Selon le niveau de fatigue, le personnage peut subir progressivement : récupération d'Endurance réduite, régénération ou récupération physique diminuée, performances de mouvement légèrement réduites, concentration moins efficace, perception et temps de réaction affectés, efficacité en combat réduite, récupération des blessures ralentie et, à un stade extrême, incapacité temporaire à maintenir certaines actions.

Les effets précis restent à équilibrer et doivent éviter de rendre le jeu inutilement punitif.

### 3.2 Sommeil

Le joueur doit pouvoir récupérer dans des contextes permettant réellement le repos, par exemple : lit, campement, refuge ou autres emplacements définis par le game design.

Les conditions de repos peuvent influencer la qualité du sommeil : sécurité, confort, environnement, perturbations, météo ou événements à proximité.

Le sommeil peut restaurer progressivement fatigue, Endurance, certains états de récupération et éventuellement certaines blessures, selon leur nature.

### 3.3 Sommeil et environnement

```text
Zone sûre + lit
→ récupération optimale

Zone exposée / météo défavorable
→ sommeil perturbé

Danger imminent / attaque
→ sommeil interrompu
```

Les règles exactes de qualité de sommeil sont data-driven.

### 3.4 Sommeil et montures

Certaines montures peuvent posséder leurs propres besoins de repos ou de récupération. Leur comportement reste dépendant de l'espèce.

## 4. Nourriture

La nourriture peut restaurer progressivement l'énergie ou la condition physique, réduire la faim, fournir des effets temporaires, contribuer à la récupération naturelle, être transportée et stockée et avoir une durée de conservation selon le game design.

```text
FoodDefinition
├── NutritionalValue
├── Hydration
├── RecoveryEffect
├── Buffs / Debuffs
├── Spoilage
└── PreparationRequirements
```

## 5. Nourriture et monde vivant

La nourriture doit être liée au monde : chasse, agriculture, récolte, pêche, élevage et ressources locales. Les catastrophes, destructions et variations écologiques peuvent influencer sa disponibilité.

## 6. Médecine

Le personnage possède une compétence indépendante appelée **Médecine**.

La Médecine progresse avec l'utilisation réelle de soins non magiques pertinents.

```text
Médecine
├── Premiers secours
├── Diagnostic
├── Traitement des blessures
├── Pansements
├── Préparations médicales
├── Antidotes
├── Stabilisation
└── Soins avancés futurs
```

## 7. Soins non magiques

Les soins non magiques peuvent prendre différentes formes : bandages, pansements, médicaments/préparations, plantes médicinales, antidotes, soins de plaies, immobilisation et autres traitements futurs.

Les soins utilisent un système commun d'effets et restent data-driven.

## 8. Blessures et récupération

Le système peut distinguer la simple perte de santé des **blessures** plus persistantes.

```text
Damage
  ↓
Condition / Injury
  ↓
Recovery
  ├── repos / sommeil / nourriture
  ├── soins Médecine
  └── magie de soin
```

Les blessures détaillées restent optionnelles tant qu'elles n'apportent pas une vraie valeur de gameplay.

## 9. Maladies régionales

Merge possède un système de **maladies dépendantes des zones**. Une maladie n'est pas nécessairement présente partout : sa probabilité d'apparition dépend de l'environnement et des conditions locales.

```text
Region
├── Climate
├── WaterQuality
├── Temperature
├── Humidity
├── Fauna
├── Vegetation
├── Sanitation
├── RecentEvents
└── DiseasePool
```

### 9.1 Déclencheurs possibles

Une zone peut augmenter le risque de certaines maladies selon : eau contaminée ou de mauvaise qualité, climat chaud/humide, froid extrême, marécages, forte densité animale, parasites, insectes/vecteurs, mauvaises conditions sanitaires, cadavres ou décomposition, événements écologiques ou catastrophes, proximité d'une population infectée lorsque la transmission est prévue.

### 9.2 Maladies liées aux régions

Chaque région peut posséder un **pool de maladies** avec probabilité d'exposition, conditions d'apparition, délai d'incubation, contagiosité éventuelle, durée, symptômes/états, gravité, résistance ou immunité, traitements possibles et moyens de prévention.

```text
Zone A
→ maladie X fréquente
→ maladie Y rare

Zone B
→ maladie X absente
→ maladie Z fréquente
```

Une maladie peut également apparaître ou disparaître d'une région en fonction des changements du monde.

### 9.3 Évolution dynamique

Les maladies doivent pouvoir évoluer avec le monde :

```text
Inondation
 ↓
Eau contaminée
 ↓
Risque sanitaire ↑
 ↓
Maladie régionale
 ↓
Transmission possible
```

Ou :

```text
Feu de forêt
 ↓
Destruction d'habitat
 ↓
Migration de faune
 ↓
Nouveaux vecteurs / nouvelles zones d'exposition
```

Une catastrophe n'ajoute donc pas artificiellement une maladie : elle modifie les **conditions qui déterminent le risque**.

### 9.4 Diagnostic diégétique — aucune indication directe de la maladie

Le jeu ne doit **jamais afficher directement au joueur le nom de la maladie dont il souffre** dans une notification, une étiquette de HUD, une fenêtre automatique ou un texte système du type `Maladie : X`.

L'état réel existe dans les données du personnage, mais le joueur n'en connaît pas automatiquement l'identité exacte.

Le joueur peut obtenir un diagnostic par deux voies :

```text
Symptômes observables
        ↓
      Joueur
     ↙       ↘
Médecine     Médecin
   ↓             ↓
Diagnostic     Diagnostic
personnel      professionnel
```

#### Autodiagnostic

Le joueur peut tenter de reconnaître lui-même la maladie grâce à la compétence **Médecine**.

Plus la compétence est élevée :
- plus les symptômes pertinents sont faciles à interpréter ;
- plus le nombre de maladies possibles est réduit ;
- plus le diagnostic est fiable ;
- plus les maladies rares ou atypiques deviennent identifiables.

Une compétence faible peut produire un diagnostic incertain ou erroné. Le système doit permettre un résultat du type « hypothèse » plutôt qu'une révélation certaine.

#### Diagnostic par un médecin

Un PNJ médecin peut examiner le personnage et fournir un diagnostic. La qualité du diagnostic peut dépendre de sa propre compétence, de son expérience, de ses connaissances disponibles et des informations observables.

Un médecin peut donc être plus fiable que l'autodiagnostic d'un personnage peu compétent.

#### Symptômes

Les symptômes doivent être présentés **par le gameplay et le monde**, pas par une notification de diagnostic :
- fièvre ou état de chaleur ;
- faiblesse ;
- toux ;
- vomissements ;
- douleurs ;
- vertiges ;
- fatigue inhabituelle ;
- altérations de perception ;
- autres symptômes spécifiques définis par chaque maladie.

La présentation exacte peut combiner animation, comportement, effets visuels/sonores, restrictions d'action ou feedback contextuel, sans révéler automatiquement l'identité de la maladie.

#### Traitement et incertitude

Le traitement doit pouvoir être tenté avant diagnostic complet, mais un mauvais traitement peut être inefficace, perdre des ressources ou retarder la guérison selon le design final.

Le joueur doit donc pouvoir choisir entre :

```text
Observer les symptômes
→ tenter son propre diagnostic
→ consulter un médecin
→ choisir un traitement
```

Le système reste entièrement data-driven.

### 9.5 Prévention

Le système peut prévoir des moyens de prévention : eau potable, cuisson, hygiène, protection contre les vecteurs, vêtements adaptés, éviter certaines zones et traitements préventifs futurs.

## 10. Séparation avec la magie

```text
Médecine
→ diagnostic, soins physiques, traitements, stabilisation, maladies

Magie de soin
→ récupération magique et effets surnaturels
```

Un sort de soin ne doit pas augmenter directement Médecine. Une action médicale ne doit pas augmenter une maîtrise magique.

La magie peut toutefois traiter certaines maladies si un domaine ou un sort le permet ; cela reste un effet magique distinct de la compétence Médecine.

## 11. Ressources et inventaire

```text
Inventory
├── Food
├── Water
├── MedicalSupplies
├── Ingredients
├── Weapons
├── Armor
└── OtherItems
```

Les aliments, l'eau et les traitements sont data-driven.

## 12. PNJ et monde

Les PNJ et factions peuvent consommer, produire nourriture et traitements et être exposés aux maladies selon leur niveau de simulation.

Hors zone joueur : besoins et propagation sont agrégés/probabilistes. À proximité, les PNJ pertinents peuvent être matérialisés avec une simulation détaillée.

Les maladies peuvent modifier les populations, les comportements, les déplacements, les demandes de soins et certains événements de faction/quête.

## 13. Montures

Le système peut supporter les besoins alimentaires, hydriques, de repos et de soins des montures si le game design les active. Des maladies spécifiques aux espèces peuvent également être définies.

## 14. Interaction avec les catastrophes

```text
Incendie → brûlure / fumées
Chute → blessure
Noyade → état critique
Inondation → eau contaminée → maladie possible
Froid extrême → risque physiologique accru
Catastrophe → pénurie alimentaire / hydrique possible
```

La disponibilité des ingrédients médicaux et la fréquence des maladies peuvent elles-mêmes changer avec l'état du monde.

## 15. Performance

La faim, l'hydratation, le sommeil, les maladies et la récupération hors zone suivent `PERFORMANCE_AND_SIMULATION_SPEC.md`.

Aucun PNJ lointain ne doit manger, boire, dormir, tomber malade ou se soigner individuellement à chaque frame. Les états régionaux sont résolus probabilistiquement puis matérialisés localement lorsque nécessaire.

## 16. Architecture

```text
SurvivalNeedsSystem
├── Hunger
├── Hydration
├── Sleep
├── Fatigue
├── NutritionState
├── HydrationState
├── SleepState
├── PhysiologicalCondition
└── Recovery

DiseaseSystem
├── RegionalDiseasePool
├── ExposureResolver
├── Incubation
├── Transmission
├── SymptomState
├── Severity
├── HiddenDiagnosisState
├── SelfDiagnosis
├── PhysicianDiagnosis
├── TreatmentResolver
└── Prevention

MedicineSystem
├── MedicineSkill
├── Diagnosis
├── Treatment
├── Stabilization
├── MedicalItemResolver
└── MedicalProgression

FoodSystem
├── FoodDefinition
├── Consumption
├── Nutrition
├── Hydration
├── Spoilage
└── Preparation
```

## 17. Tests prioritaires

- faim et récupération ;
- consommation de nourriture ;
- hydratation ;
- accumulation progressive de malnutrition ;
- accumulation progressive de déshydratation ;
- sommeil insuffisant ;
- récupération par sommeil ;
- qualité de sommeil selon le contexte ;
- cumul faim + déshydratation + fatigue ;
- soin avec Médecine faible ;
- amélioration de Médecine ;
- symptômes visibles sans révélation directe du nom ;
- autodiagnostic avec Médecine faible ;
- autodiagnostic avec Médecine élevée ;
- diagnostic fiable par un médecin ;
- maladie propre à une région ;
- absence d'une maladie hors de ses conditions ;
- incubation et transmission ;
- impact d'une inondation sur le risque sanitaire ;
- traitement correct vs incorrect ;
- séparation Médecine / magie ;
- besoins et maladies d'une monture si activés ;
- pénurie alimentaire/hydrique régionale ;
- disponibilité des ingrédients après catastrophe ;
- sauvegarde / chargement de l'état physiologique.

## 18. Ce qui reste ouvert

Les règles exactes de faim, hydratation, sommeil, seuils, durées, maladies, symptômes, probabilités, méthodes de traitement, degré d'incertitude du diagnostic, qualité des médecins, blessures détaillées, médicaments, effets nutritionnels, aliments, plantes et traitements restent des décisions de game design. La compétence **Médecine**, les besoins physiologiques, le diagnostic diégétique et la séparation avec la magie sont des contraintes d'architecture.
