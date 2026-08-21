# Merge — Mount System Specification

**Statut** : APPROUVÉ — architecture de pré-implémentation
**Engine** : Unreal Engine 5.8.1
**Langage principal** : C++20

## 1. Objectif

Le joueur doit pouvoir monter sur des montures terrestres, aquatiques ou autres catégories futures définies par le game design.

Les espèces et types de montures ne sont volontairement **pas figés**. Le système doit permettre d'ajouter une nouvelle monture par données sans réécrire le système central.

```text
MountSystem
├── MountDefinition
├── MountState
├── MountInteraction
├── MountAcquisition
├── TamingSystem
├── MountMovement
├── MountCombat
├── MountAI
├── MountStamina
└── MountPersistence
```

## 2. Acquisition et interaction

Le joueur dispose de deux voies principales d'acquisition selon la monture et les règles du monde :

### 2.1 Achat auprès d'un éleveur

L'achat de montures se fait **exclusivement auprès d'éleveurs**. Le jeu ne possède pas de catégorie générique de « marchand de bêtes ».

Un éleveur peut proposer des montures selon :
- espèce / famille ;
- disponibilité ;
- qualité de l'animal ;
- âge ou caractéristiques ;
- prix ;
- région ;
- réputation ;
- relations avec la faction ou l'éleveur ;
- éventuelles conditions de quête.

L'éleveur doit être traité comme une source cohérente de créatures élevées ou préparées pour la monte, et non comme un vendeur générique d'animaux.

L'achat crée une association persistante entre la monture et le joueur lorsqu'elle devient sa monture.

### 2.2 Domptage / capture

Certaines montures peuvent être obtenues sans achat grâce à une compétence de **Domptage**.

Le joueur doit pouvoir :

```text
Repérer une créature compatible
        ↓
S'approcher / l'approcher sans la faire fuir
        ↓
Déclencher une tentative de domptage
        ↓
Calcul de la difficulté
        ↓
Résolution progressive
   ┌────┴────┐
   ↓         ↓
Succès     Échec
   ↓         ↓
Créature   fuite / résistance /
acceptée   tentative à reprendre
```

La compétence de Domptage est une compétence de progression distincte des maîtrises d'armes et du Réflexe.

### 2.3 Compétence de Domptage

Le **Domptage** progresse avec des tentatives et réussites de domestication réellement pertinentes.

Le système doit pouvoir prendre en compte :

- difficulté de l'espèce ;
- tempérament ;
- niveau de peur/agression ;
- état de la créature ;
- familiarité avec l'espèce ;
- expérience du joueur en Domptage ;
- contexte et approche ;
- qualité des interactions précédentes ;
- éventuels objets ou techniques d'aide.

La compétence doit réduire progressivement la difficulté effective et augmenter la fiabilité, sans transformer automatiquement toute créature en monture.

```text
Domptage faible
→ espèces dociles / faciles
→ forte probabilité d'échec sur créatures sauvages difficiles

Domptage moyen
→ plus d'espèces accessibles
→ meilleure tolérance aux erreurs

Domptage élevé
→ créatures plus rares / sauvages potentiellement domptables
→ meilleure fiabilité
```

Les espèces intrinsèquement incompatibles avec le domptage doivent pouvoir être déclarées **non domptables** dans leurs données.

### 2.4 Familles et familiarité

La familiarité avec une espèce ou une famille de montures peut être enregistrée séparément ou comme modificateur du Domptage.

Exemple : un joueur ayant beaucoup de pratique avec les équidés peut mieux gérer une nouvelle créature de la même famille qu'une créature complètement inconnue.

La familiarité ne doit pas remplacer la compétence générale de Domptage.

### 2.5 Relation et confiance

Après l'acquisition, la monture peut posséder un état de relation avec le joueur :

```text
Nouvellement domptée / achetée
        ↓
Confiance faible
        ↓
Utilisation / soins / interactions positives
        ↓
Confiance accrue
```

Le niveau de confiance peut, selon le game design final, influencer :
- réponse aux commandes ;
- stress / peur ;
- obéissance ;
- stabilité en combat ;
- comportement face aux catastrophes ;
- performances de certaines capacités.

La confiance ne doit pas être obligatoire pour toutes les montures et reste data-driven.

## 3. Mouvement

Une monture possède ses propres paramètres :

- vitesse de marche ;
- course ;
- accélération ;
- freinage ;
- saut éventuel ;
- capacité à franchir certains obstacles ;
- rotation ;
- maniabilité ;
- endurance ;
- interaction avec le terrain.

Le joueur ne doit pas simplement remplacer son CharacterMovement par une vitesse multiplicative : la monture est une entité de mouvement distincte.

## 4. Endurance et montures

La monture peut posséder sa propre Endurance.

```text
Monture
├── Stamina
├── Recovery
├── MovementCost
└── FatigueState
```

Les coûts doivent être data-driven et varier selon le type de déplacement.

## 5. Terrain et environnement

Les montures doivent interagir avec les systèmes de terrain déjà prévus : pente, boue, neige, feu, zones volcaniques, eau, falaises, obstacles et catastrophes naturelles.

Une monture peut posséder des résistances et capacités spécifiques.

## 6. Combat monté

Le système doit pouvoir supporter le combat depuis une monture lorsque la monture et l'arme le permettent.

Le joueur doit pouvoir, selon le design : attaquer depuis la monture, utiliser certaines armes, utiliser certaines magies, être désarçonné ou descendre volontairement.

Le combat monté doit utiliser le `CombatResolver` commun.

## 7. Montures et progression

Le système peut supporter une progression propre à la monture sans la rendre obligatoire : maîtrise de conduite, familiarité, endurance, vitesse, maniabilité, confiance/lien joueur-monture.

La **compétence de Domptage** appartient au joueur et reste distincte de ces éventuelles caractéristiques de la monture.

L'utilisation effective de montures peut contribuer aux événements de progression pertinents si le game design le confirme.

## 8. IA et comportement

Une monture autonome doit conserver une IA distincte du joueur : déplacement, évitement, peur, combat/fuite, réactions aux catastrophes, retour vers le joueur et routines.

## 9. Montures et groupe

Une monture peut appartenir au groupe du joueur sans être considérée comme un PNJ de groupe classique.

## 10. Persistance

Lorsque les montures sont persistantes, leur état doit pouvoir être sauvegardé :

```text
MountState
├── Identity
├── Region
├── Health
├── Stamina
├── Equipment
├── CurrentOwner / Association
├── AcquisitionMethod
├── TamingProgress / TamingHistory
├── TrustState
├── Status
└── WorldRelationship
```

La mort d'une monture persistante doit respecter les règles du monde non régénératif si le design final retient la mortalité permanente.

## 11. Optimisation

Les montures suivent les mêmes règles de simulation que les autres créatures :

```text
Hors zone → état abstrait / simulation probabiliste
À proximité → Actor + IA adaptée
Joueur monté → simulation complète
```

## 12. Architecture cible

```text
MountSystem
├── MountDefinition
│   ├── Species / Type
│   ├── MovementProfile
│   ├── StaminaProfile
│   ├── TerrainCapabilities
│   ├── CombatCapabilities
│   ├── AcquisitionRules
│   └── InteractionRules
│
├── MountComponent / MountActor
├── RiderComponent
├── MountInteraction
├── TamingComponent
├── MountMovement
├── MountCombatAdapter
├── MountAI
└── MountPersistence
```

## 13. Tests prioritaires

- achat auprès d'un éleveur ;
- conditions d'achat chez un éleveur ;
- absence de système générique de marchand de bêtes ;
- tentative de domptage d'une monture facile ;
- tentative sur une monture difficile ;
- échec de domptage ;
- réussite de domptage ;
- espèce déclarée non domptable ;
- progression de Domptage ;
- familiarité par famille ;
- montée / descente ;
- déplacement monté ;
- endurance de la monture ;
- terrain et eau ;
- combat monté ;
- désarçonnement ;
- sauvegarde / chargement ;
- mortalité persistante si activée ;
- simulation distante probabiliste ;
- streaming entre cellules.

## 14. Ce qui reste volontairement ouvert

Les espèces de montures, leur nombre, leurs statistiques, leurs capacités spéciales, leurs prix, leurs méthodes exactes de domptage, leurs difficultés de domptage, leur reproduction éventuelle, leur mortalité et leurs systèmes de progression restent des décisions de game design.

Le cœur technique doit être prêt à recevoir ces choix sans refonte majeure.
