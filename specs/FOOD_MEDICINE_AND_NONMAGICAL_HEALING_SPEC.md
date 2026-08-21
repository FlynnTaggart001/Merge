# Merge — Food, Medicine & Non-Magical Healing Specification

**Statut** : APPROUVÉ — architecture de pré-implémentation
**Engine** : Unreal Engine 5.8.1
**Langage principal** : C++20

## 1. Principe

Merge doit distinguer trois grandes voies de récupération :

```text
Récupération
├── Nourriture / hydratation
├── Médecine / soins non magiques
└── Magie de soin
```

La magie ne doit pas remplacer les besoins physiques du personnage. Les soins non magiques restent importants même dans un monde où la magie existe.

## 2. Système de nourriture et besoins physiologiques

Le personnage dispose d'un système de faim, d'alimentation et d'hydratation.

La faim et l'hydratation ne sont pas seulement des jauges d'interface : leur niveau influence progressivement **l'état physiologique du personnage**.

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

Conséquences potentielles, à équilibrer :
- récupération physique réduite ;
- Endurance maximale ou récupération diminuée ;
- faiblesse générale ;
- capacité d'effort réduite ;
- résistance aux blessures éventuellement diminuée ;
- progression physique temporairement moins efficace ;
- à un stade critique, perte de santé ou incapacité prolongée.

Les effets doivent progresser graduellement plutôt que passer brutalement de normal à critique.

### 2.2 Déshydratation

Lorsque le personnage reste trop longtemps sans boire, il peut entrer dans un état `Dehydrated` ou dans des paliers équivalents.

Conséquences potentielles, à équilibrer :
- récupération d'Endurance réduite ;
- consommation d'Endurance augmentée ;
- efficacité des déplacements réduite ;
- faiblesse générale ;
- récupération des blessures ralentie ;
- à un stade critique, dégâts progressifs ou incapacité.

La déshydratation doit être plus rapidement dangereuse que la faim lorsque le game design le confirme, mais les valeurs sont à équilibrer par le prototype.

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

Le système doit éviter une simple addition aveugle des pénalités : les effets combinés doivent être définis par un resolver d'états pour éviter des multiplicateurs incohérents.

### 2.4 Récupération

La récupération d'un état physiologique suit la consommation de ressources adaptées et le temps nécessaire au retour à l'équilibre.

```text
Faim
 ↓ alimentation
 ↓
Récupération progressive
 ↓
État normal

Déshydratation
 ↓ hydratation
 ↓
Récupération progressive
 ↓
État normal
```

Une seule consommation ne doit pas forcément annuler immédiatement plusieurs niveaux d'état critique.

## 3. Nourriture

La nourriture peut :

- restaurer progressivement l'énergie ou la condition physique ;
- réduire la faim ;
- fournir des effets temporaires ;
- contribuer à la récupération naturelle ;
- transporter et stocker ;
- avoir une durée de conservation selon le game design.

```text
FoodDefinition
├── NutritionalValue
├── Hydration
├── RecoveryEffect
├── Buffs / Debuffs
├── Spoilage
└── PreparationRequirements
```

La nourriture ne doit pas être une obligation punitive permanente ; les paramètres de fréquence et de conséquences seront équilibrés dans le prototype.

## 4. Nourriture et monde vivant

La nourriture doit être liée au monde : chasse, agriculture, récolte, pêche, élevage et ressources locales.

Les catastrophes, destructions et variations écologiques peuvent influencer la disponibilité de nourriture.

```text
Feu de forêt
→ récoltes / gibier réduits
→ nourriture disponible ↓
→ pression sur populations / villages
```

## 5. Médecine

Le personnage possède une compétence indépendante appelée **Médecine**.

La Médecine progresse avec l'utilisation réelle de soins non magiques pertinents.

```text
Médecine
├── Premiers secours
├── Traitement des blessures
├── Pansements
├── Potions non magiques / préparations
├── Stabilisation
└── Soins avancés futurs
```

Le contenu exact des techniques dépendra du game design et du monde.

## 6. Soins non magiques

Les soins non magiques peuvent prendre différentes formes : bandages, pansements, médicaments/préparations, plantes médicinales, antidotes, soins de plaies, immobilisation et autres traitements futurs.

Les soins sont data-driven et utilisent un système commun d'effets.

## 7. Blessures et récupération

Le système de soins peut distinguer la simple perte de santé des **blessures** plus persistantes.

```text
Damage
  ↓
Condition / Injury
  ↓
Recovery
  ├── repos / nourriture
  ├── soins Médecine
  └── magie de soin
```

Les blessures détaillées restent optionnelles et doivent être activées uniquement si elles apportent une vraie valeur de gameplay.

## 8. Médecine et progression

La progression de Médecine doit être organique : diagnostic pertinent, utilisation correcte de traitements, stabilisation, soins réussis et préparation/application de traitements selon le game design.

Les mêmes règles anti-farming que les autres compétences s'appliquent.

Un soin répété sans véritable besoin médical ne doit pas fournir une progression importante.

## 9. Séparation avec la magie

```text
Médecine
→ soins physiques, traitements, stabilisation, préparations

Magie de soin
→ récupération magique et effets surnaturels
```

Un sort de soin ne doit pas augmenter Médecine. Une action médicale ne doit pas augmenter une maîtrise magique. Les deux peuvent agir sur la même cible via l'EffectSystem commun.

## 10. Ressources et inventaire

```text
Inventory
├── Food
├── MedicalSupplies
├── Ingredients
├── Weapons
├── Armor
└── OtherItems
```

Les aliments et traitements sont des objets data-driven.

## 11. PNJ et monde

Les PNJ et factions peuvent consommer ou produire nourriture et traitements selon le niveau de simulation.

Hors zone joueur : besoins alimentaires et hydriques agrégés, risques de pénurie et résultats probabilistes. À proximité, les PNJ pertinents peuvent être matérialisés avec une simulation détaillée.

## 12. Montures

Le système peut supporter les besoins alimentaires, hydriques et soins des montures si le game design les active.

Une monture peut avoir faim, nécessiter de l'eau, subir des blessures, recevoir des traitements et voir son état de confiance influencé par les soins.

Les besoins restent data-driven selon l'espèce.

## 13. Interaction avec les catastrophes

```text
Incendie → brûlure
Chute → blessure
Noyade → état critique
Catastrophe → pénurie alimentaire / hydrique possible
```

La disponibilité des ingrédients médicaux peut elle-même changer avec l'état du monde.

## 14. Performance

La faim, l'hydratation, les besoins et la récupération hors zone suivent `PERFORMANCE_AND_SIMULATION_SPEC.md`.

Aucun PNJ lointain ne doit manger, boire ou se soigner individuellement à chaque frame.

## 15. Architecture

```text
SurvivalNeedsSystem
├── Hunger
├── Hydration
├── NutritionState
├── HydrationState
├── PhysiologicalCondition
└── Recovery

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

ConditionStateSystem
├── WellNourished
├── Hungry
├── Malnourished
├── Hydrated
├── Thirsty
├── Dehydrated
└── CriticalCondition
```

## 16. Tests prioritaires

- faim et récupération ;
- consommation de nourriture ;
- hydratation ;
- accumulation progressive d'un état de malnutrition ;
- accumulation progressive de déshydratation ;
- effets sur Endurance et récupération ;
- cumul faim + déshydratation ;
- retour progressif à l'état normal ;
- soin avec Médecine faible ;
- amélioration de Médecine ;
- traitement d'une blessure ;
- progression anti-farming ;
- séparation Médecine / magie ;
- soins d'une monture si activés ;
- pénurie alimentaire/hydrique régionale ;
- disponibilité des ingrédients après catastrophe ;
- sauvegarde / chargement de l'état physiologique.

## 17. Ce qui reste ouvert

Les règles exactes de faim, hydratation, seuils des états, durée des paliers, blessures détaillées, médicaments, effets nutritionnels, aliments, plantes et traitements restent des décisions de game design. La compétence **Médecine**, les besoins physiologiques et la séparation avec la magie sont des contraintes d'architecture.
