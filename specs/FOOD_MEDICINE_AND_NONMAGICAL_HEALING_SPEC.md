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

## 2. Système de nourriture

Le personnage dispose d'un système de faim et d'alimentation. La nourriture peut :

- restaurer progressivement l'énergie ou la condition physique ;
- réduire la faim ;
- fournir des effets temporaires ;
- contribuer à la récupération naturelle ;
- être transportée et stockée ;
- avoir une durée de conservation selon le game design.

Les aliments peuvent être classés par données :

```text
FoodDefinition
├── NutritionalValue
├── Hydration
├── RecoveryEffect
├── Buffs / Debuffs
├── Spoilage
└── PreparationRequirements
```

Le système ne doit pas transformer la faim en obligation punitive permanente : les paramètres de fréquence et de conséquences seront équilibrés dans le prototype.

## 3. Nourriture et monde vivant

La nourriture doit être liée au monde :

- chasse ;
- agriculture ;
- récolte ;
- pêche ;
- élevage ;
- commerce indirect via ressources/établissements du monde.

Les catastrophes, destructions et variations écologiques peuvent donc influencer la disponibilité de nourriture.

Exemple :

```text
Feu de forêt
→ récoltes / gibier réduits
→ nourriture disponible ↓
→ pression sur les populations / villages
```

## 4. Médecine

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

## 5. Soins non magiques

Les soins non magiques peuvent prendre différentes formes :

- bandages ;
- pansements ;
- médicaments / préparations ;
- plantes médicinales ;
- antidotes ;
- soins de plaies ;
- immobilisation ;
- récupération assistée ;
- autres traitements futurs.

Les soins doivent être data-driven et utiliser un système commun d'effets afin de ne pas coder chaque objet comme une exception.

## 6. Blessures et récupération

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

Le jeu pourra ainsi faire varier les conséquences d'une brûlure, d'une chute, d'une coupure ou d'une attaque sans faire de chaque événement un simple retrait de HP.

Les blessures détaillées restent optionnelles et doivent être activées uniquement si elles apportent une vraie valeur de gameplay.

## 7. Médecine et progression

La progression de Médecine doit être organique :

- diagnostic / identification pertinente ;
- utilisation correcte de traitements ;
- stabilisation de blessures ;
- soins réussis ;
- préparation ou application de traitements selon le game design.

Les mêmes règles anti-farming que les autres compétences s'appliquent.

Un soin répété sans véritable besoin médical ne doit pas fournir une progression importante.

## 8. Séparation avec la magie

Le système distingue :

```text
Médecine
→ soins physiques, traitements, stabilisation, préparations

Magie de soin
→ récupération magique et effets surnaturels selon le domaine choisi
```

Un sort de soin ne doit pas augmenter directement la compétence Médecine.

Une action médicale ne doit pas augmenter une maîtrise magique.

Les deux systèmes peuvent toutefois agir sur la même cible et produire des effets compatibles dans le `EffectSystem` commun.

## 9. Ressources et inventaire

La nourriture et les traitements utilisent l'inventaire existant :

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

## 10. PNJ et monde

Les PNJ et factions peuvent également consommer ou produire de la nourriture et des traitements selon le niveau de simulation.

Hors zone joueur :

```text
Population / Village
→ besoins alimentaires agrégés
→ ressources disponibles
→ risque de pénurie
→ résultat probabiliste
```

À proximité du joueur, les établissements et PNJ pertinents peuvent être matérialisés avec une simulation détaillée.

## 11. Montures

Le système doit pouvoir supporter les besoins alimentaires et les soins des montures si le game design les active.

Une monture peut avoir :

- faim ;
- besoins alimentaires spécifiques ;
- blessures ;
- traitements ;
- récupération ;
- état de confiance influencé par les soins et la qualité du traitement.

Ces règles restent data-driven pour ne pas imposer les mêmes besoins à toutes les espèces.

## 12. Interaction avec les catastrophes

Les blessures, la nourriture et les traitements doivent pouvoir réagir aux événements environnementaux :

```text
Incendie → brûlure
Chute → blessure
Noyade → état critique
Catastrophe → pénurie alimentaire possible
```

La disponibilité des ingrédients médicaux peut elle-même changer avec l'état du monde.

## 13. Performance

La faim, les besoins alimentaires et la récupération hors zone doivent suivre la simulation probabiliste déjà définie dans `PERFORMANCE_AND_SIMULATION_SPEC.md`.

Aucun PNJ lointain ne doit manger ou soigner un objet individuellement à chaque frame.

## 14. Architecture

```text
SurvivalNeedsSystem
├── Hunger
├── Hydration
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
├── Spoilage
└── Preparation
```

Les systèmes communiquent avec `InventorySystem`, `EffectSystem`, `ProgressionSystem`, `MountSystem`, `NPCSystem`, `EcologySystem` et `WorldPersistence`.

## 15. Tests prioritaires

- faim et récupération ;
- consommation de nourriture ;
- hydratation ;
- soin avec Médecine faible ;
- amélioration de Médecine ;
- traitement d'une blessure ;
- progression anti-farming ;
- séparation Médecine / magie ;
- soins d'une monture si activés ;
- pénurie alimentaire régionale ;
- disponibilité des ingrédients après catastrophe ;
- sauvegarde / chargement de l'état de récupération.

## 16. Ce qui reste ouvert

Les règles exactes de faim, hydratation, blessures détaillées, types de médicaments, effets nutritionnels, aliments, plantes médicinales et traitements restent des décisions de game design. La compétence **Médecine** et la séparation avec la magie sont, elles, désormais des contraintes d'architecture.
