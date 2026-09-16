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

Le **domptage** peut exister comme mécanique d'acquisition pour certaines espèces, mais **Domptage n'est pas une compétence canonique du joueur** et ne doit pas être ajouté aux 45 compétences sans décision explicite dans `specs/CANONICAL_SKILLS.md`.

## 2. Acquisition et interaction

Le joueur dispose de deux voies principales d'acquisition selon la monture et les règles du monde :

### 2.1 Achat auprès d'un éleveur

L'achat de montures se fait **auprès d'éleveurs**. Le jeu ne possède pas de catégorie générique de « marchand de bêtes ».

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

### 2.2 Acquisition naturelle / domptage

Certaines montures peuvent être obtenues sans achat lorsque les règles de l'espèce le permettent.

```text
Repérer une créature compatible
        ↓
S'approcher / l'approcher sans la faire fuir
        ↓
Interaction de domptage ou d'acquisition
        ↓
Résolution selon les règles de l'espèce
   ┌────┴────┐
   ↓         ↓
Succès     Échec
   ↓         ↓
Créature   fuite / résistance /
acceptée   tentative à reprendre
```

Le système de domptage est une **mécanique**, pas une compétence canonique supplémentaire. Sa difficulté et ses conditions sont déterminées par les données de la créature et par le contexte du monde.

### 2.3 Règles d'acquisition

Le système doit pouvoir prendre en compte :

- difficulté propre à l'espèce ;
- tempérament ;
- niveau de peur/agression ;
- état de la créature ;
- familiarité éventuelle du personnage avec l'espèce ;
- contexte et approche ;
- qualité des interactions précédentes ;
- éventuels objets ou techniques d'aide ;
- conditions de quête ou de monde.

Aucune compétence « Domptage » ne doit être utilisée pour déterminer directement le résultat.

Les espèces intrinsèquement incompatibles avec l'acquisition par domptage doivent pouvoir être déclarées **non domptables** dans leurs données.

### 2.4 Familles et familiarité

Une familiarité avec une espèce ou une famille de montures peut être enregistrée comme état ou modificateur propre au système de montures.

La familiarité ne constitue pas une compétence ou une caractéristique canonique supplémentaire du joueur.

### 2.5 Relation et confiance

Après l'acquisition, la monture peut posséder un état de relation avec le joueur :

```text
Nouvellement acquise
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

L'Endurance de la monture est une ressource/paramètre de la monture et ne crée pas une caractéristique canonique **Endurance** pour le joueur.

## 5. Terrain et environnement

Les montures doivent interagir avec les systèmes de terrain déjà prévus : pente, boue, neige, feu, zones volcaniques, eau, falaises, obstacles et catastrophes naturelles.

Une monture peut posséder des résistances et capacités spécifiques.

## 6. Combat monté

Le système doit pouvoir supporter le combat depuis une monture lorsque la monture et l'arme le permettent.

Le joueur doit pouvoir, selon le design : attaquer depuis la monture, utiliser certaines armes, utiliser certaines magies, être désarçonné ou descendre volontairement.

Le combat monté doit utiliser le `CombatResolver` commun.

## 7. Montures et progression

Le système peut supporter une progression propre à la monture sans la rendre obligatoire : maîtrise de conduite, familiarité, endurance, vitesse, maniabilité, confiance/lien joueur-monture.

Ces valeurs concernent le système de montures et ne constituent pas de nouvelles compétences ou caractéristiques canoniques du joueur.

L'utilisation effective de montures peut contribuer à une compétence canonique uniquement lorsqu'une compétence existante est réellement concernée et que l'action passe les règles normales de validation de progression. Aucune compétence dédiée « Domptage » ne doit être créée implicitement.

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
├── AcquisitionHistory
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

`TamingComponent` représente une mécanique d'acquisition éventuelle. Il ne représente pas une compétence canonique du joueur.

## 13. Tests prioritaires

- achat auprès d'un éleveur ;
- conditions d'achat chez un éleveur ;
- absence de système générique de marchand de bêtes ;
- acquisition d'une monture compatible ;
- tentative d'acquisition d'une monture difficile ;
- échec d'acquisition ;
- réussite d'acquisition ;
- espèce déclarée non domptable ;
- absence de progression d'une compétence « Domptage » inexistante ;
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

Les espèces de montures, leur nombre, leurs statistiques, leurs capacités spéciales, leurs prix, leurs méthodes exactes d'acquisition, leurs difficultés d'acquisition, leur reproduction éventuelle, leur mortalité et leurs systèmes de progression restent des décisions de game design.

Le cœur technique doit être prêt à recevoir ces choix sans refonte majeure.
