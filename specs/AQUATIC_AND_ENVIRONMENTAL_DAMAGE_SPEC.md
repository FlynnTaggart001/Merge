# Merge — Aquatic & Environmental Damage Specification

**Statut** : APPROUVÉ — architecture de pré-implémentation
**Engine** : Unreal Engine 5.8.4
**Langage principal** : C++20

## 1. Objectif

Les dégâts environnementaux et les interactions avec l'eau doivent être des systèmes génériques et data-driven. Ils ne doivent pas être codés comme des exceptions isolées dans le personnage.

```text
EnvironmentalDamageSystem
├── Fire / Burn
├── Fall
├── Drowning
├── Hazard
└── FutureEnvironmentalDamage[*]
```

## 2. Brûlure

Le feu applique un état de brûlure pouvant infliger des dégâts sur la durée.

Le système doit permettre :
- durée configurable ;
- intensité configurable ;
- résistances/immunités ;
- extinction selon les conditions ;
- propagation ou interaction environnementale si le gameplay le permet ;
- événements de dégâts exploitables par le système de combat et la progression.

## 3. Dégâts de chute

Les chutes constituent une source de dégâts distincte des attaques classiques.

Le calcul doit pouvoir tenir compte de :
- hauteur ;
- vitesse d'impact ;
- état du personnage ;
- équipement ;
- capacité de réception ;
- éventuels modificateurs de terrain.

Une **réception contrôlée** peut réduire les conséquences d'une chute lorsque les conditions sont réunies. Une chute importante ne doit jamais être annulée simplement par une statistique élevée.

## 4. Système aquatique

L'eau possède plusieurs états de déplacement :

```text
Sol
 ↓
Eau peu profonde
 ↓
Flottaison
 ↓
Nage
 ↓
Plongée
 ↓
Air critique
 ↓
Noyade
```

Le personnage doit réellement interagir avec la profondeur, la flottabilité, l'équipement et ses ressources physiques.

### 4.1 Eau peu profonde

Le personnage peut marcher dans l'eau lorsque la profondeur le permet. La résistance de l'eau peut modifier vitesse et coût d'Endurance.

### 4.2 Flottaison et nage

Lorsque la profondeur empêche le déplacement normal, le personnage passe à un état de flottaison ou de nage.

La nage :
- possède une vitesse propre ;
- consomme de l'Endurance ;
- dépend de l'état physique et de l'équipement ;
- permet de rejoindre une surface ou un point de sortie ;
- doit gérer les collisions et volumes d'eau ;
- peut progresser avec l'utilisation réelle.

### 4.3 Flottabilité et équipement

La flottabilité effective est calculée à partir des caractéristiques du personnage et de ce qu'il porte.

```text
EffectiveBuoyancy
├── CharacterBody
├── Armor
├── Clothing
├── Equipment
├── CarriedWeight
└── Modifiers
```

Principe de gameplay :

```text
Équipement léger → flotte plus facilement
Équipement moyen → nage normale, effort accru possible
Armure lourde → tendance à couler et nage fortement pénalisée
Équipement extrêmement lourd → difficulté majeure à remonter / risque de couler
```

L'armure lourde ne doit donc pas être traitée comme un simple malus abstrait de vitesse : sa masse influence réellement le comportement aquatique.

Le calcul reste paramétrable afin que certains équipements, accessoires ou capacités puissent modifier la flottabilité.

### 4.4 Plongée

Le joueur peut descendre sous la surface lorsque les conditions le permettent. La plongée doit gérer :
- profondeur ;
- déplacement vertical ;
- coût d'Endurance ;
- réserve d'air ;
- visibilité et environnement ;
- remontée vers la surface.

Une armure lourde peut rendre la remontée beaucoup plus difficile.

### 4.5 Respiration

La réserve d'air est distincte de l'Endurance.

```text
Surface
 ↓
Air restauré
 ↓
Plongée / immersion
 ↓
Air diminue
 ↓
Air critique
 ↓
Noyade
```

La réserve d'air doit être data-driven et pouvoir être modifiée par les caractéristiques du personnage, les états, l'équipement ou de futures capacités.

## 5. Noyade

Lorsque la réserve d'air arrive à zéro, le personnage entre dans un état de noyade et subit des dégâts selon les paramètres du système.

Le système doit permettre :
- dégâts progressifs ;
- état critique ;
- récupération immédiate à la remontée ;
- interruption de certaines actions ;
- conséquences adaptées à l'état du personnage.

La noyade ne doit pas être un simple type de dégâts appliqué indépendamment du système aquatique : elle dépend de l'immersion et de la gestion de l'air.

## 6. Endurance et eau

La nage, la plongée et les déplacements aquatiques physiquement exigeants consomment de l'Endurance.

```text
Nage       → coût selon durée / intensité
Plongée    → coût selon durée / effort
Remontée   → coût selon effort / flottabilité
```

Une Endurance insuffisante doit limiter les actions exigeantes conformément aux règles générales de mouvement. La réserve d'air reste cependant indépendante : être épuisé et manquer d'air sont deux problèmes différents.

## 7. Progression

L'utilisation réelle du système aquatique peut contribuer à la progression :

```text
Nage / effort aquatique → Endurance
Mouvements précis / mobilité aquatique → Agilité selon contexte
Réceptions contrôlées → Agilité
```

Le système anti-farming s'applique également aux actions aquatiques.

## 8. Architecture

```text
AquaticMovementSystem
├── ShallowWaterMovement
├── Buoyancy
├── Swimming
├── Diving
├── SurfaceDetection
├── BreathSystem
├── WaterExit
└── EquipmentInteraction

EnvironmentalDamageSystem
├── BurnDamage
├── FallDamage
├── DrowningDamage
├── HazardDamage
└── FutureDamageTypes[*]
```

Les systèmes doivent communiquer avec `CombatResolver`, `ProgressionSystem`, `EquipmentSystem`, `CharacterMovement` et les systèmes de sauvegarde lorsque l'état aquatique doit persister.

## 9. Tests prioritaires

- nage sans équipement lourd ;
- nage avec armure ;
- armure lourde entraînant une tendance à couler ;
- remontée avec équipement lourd ;
- épuisement pendant la nage ;
- plongée ;
- restauration de l'air à la surface ;
- noyade ;
- dégâts de chute ;
- réception contrôlée ;
- brûlure et dégâts sur la durée ;
- résistances et immunités ;
- interaction eau/feu selon les règles environnementales futures.

## 10. Principes de conception

1. L'eau est un véritable système de mouvement, pas une simple animation.
2. Endurance et réserve d'air sont deux ressources différentes.
3. Le poids de l'équipement influence réellement la flottabilité.
4. Une armure lourde peut faire couler le personnage et rendre la remontée difficile.
5. Les dégâts environnementaux sont extensibles et data-driven.
6. Les valeurs exactes de flottabilité, coûts, vitesse, air et dégâts seront équilibrées pendant le prototype Unreal.
