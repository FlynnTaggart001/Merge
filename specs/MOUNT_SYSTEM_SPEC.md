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
├── MountMovement
├── MountCombat
├── MountAI
├── MountStamina
└── MountPersistence
```

## 2. Acquisition et interaction

Le système doit pouvoir gérer :

- approche d'une monture ;
- interaction / montée ;
- refus ou impossibilité de monter ;
- démontage ;
- interruption forcée ;
- perte de la monture ou séparation ;
- retour du joueur sur la monture lorsque le contexte le permet.

Les règles d'apprivoisement, recrutement, achat, capture ou élevage restent ouvertes et dépendront du game design des montures.

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

Exemples :

```text
Marche      → coût faible ou nul
Course      → coût progressif
Sprint      → coût élevé
Saut        → coût d'impulsion
Charge      → coût spécifique
```

Une monture épuisée doit pouvoir ralentir, refuser certaines actions ou nécessiter une récupération selon le design final.

## 5. Terrain et environnement

Les montures doivent interagir avec les systèmes de terrain déjà prévus :

- pente ;
- boue ;
- neige ;
- feu ;
- zones volcaniques ;
- eau ;
- falaises ;
- obstacles ;
- catastrophes naturelles.

Une monture peut posséder des résistances et capacités spécifiques.

Exemple : certaines montures pourraient traverser l'eau, alors que d'autres paniquent, flottent, coulent ou refusent certaines profondeurs.

## 6. Combat monté

Le système doit pouvoir supporter le combat depuis une monture lorsque la monture et l'arme le permettent.

Le joueur doit pouvoir, selon le design :

- attaquer depuis la monture ;
- utiliser certaines armes ;
- utiliser certaines magies ;
- être désarçonné ;
- subir des attaques visant le joueur ou la monture ;
- descendre volontairement pour combattre à pied.

Le combat monté doit utiliser le `CombatResolver` commun et ne pas créer un deuxième système de dégâts.

## 7. Montures et progression

Le système doit pouvoir supporter une progression propre à la monture sans la rendre obligatoire.

Possibilités extensibles :

- maîtrise de conduite ;
- familiarité du joueur avec une famille de montures ;
- endurance de la monture ;
- vitesse ;
- maniabilité ;
- confiance / lien joueur-monture.

Aucune statistique supplémentaire n'est imposée tant que le game design n'est pas décidé.

La conduite et l'utilisation d'une monture peuvent contribuer à l'expérience appropriée du joueur si le système de progression le confirme.

## 8. IA et comportement

Une monture autonome doit conserver une IA distincte du joueur :

- déplacement ;
- évitement ;
- peur ;
- combat ou fuite ;
- réactions aux catastrophes ;
- retour vers le joueur ;
- routines dans son environnement.

Les mêmes règles de simulation distante s'appliquent : hors zone active, une monture non pertinente ne doit pas avoir une IA complète exécutée à chaque frame.

## 9. Montures et groupe

Une monture peut appartenir au groupe du joueur sans être considérée comme un PNJ de groupe classique.

Elle doit pouvoir être intégrée aux commandes de groupe, au déplacement et aux événements de combat lorsque nécessaire.

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
├── Status
└── WorldRelationship
```

La mort d'une monture persistante doit respecter les règles du monde non régénératif si le design final retient la mortalité permanente.

Une monture tuée ne doit pas réapparaître artificiellement par un simple respawn global.

## 11. Optimisation

Les montures suivent les mêmes règles de simulation que les autres créatures :

```text
Hors zone
→ état abstrait / simulation probabiliste

À proximité
→ Actor + IA adaptée

Joueur monté
→ simulation complète
```

Une monture contrôlée par le joueur doit être traitée comme un élément gameplay critique et recevoir la précision nécessaire au mouvement, à la collision et à l'animation.

## 12. Architecture cible

```text
MountSystem
├── MountDefinition
│   ├── Species / Type
│   ├── MovementProfile
│   ├── StaminaProfile
│   ├── TerrainCapabilities
│   ├── CombatCapabilities
│   └── InteractionRules
│
├── MountComponent / MountActor
├── RiderComponent
├── MountMovement
├── MountInteraction
├── MountCombatAdapter
├── MountAI
└── MountPersistence
```

## 13. Tests prioritaires

- monter / descendre ;
- blocage de montée dans une situation invalide ;
- déplacement monté ;
- course / sprint ;
- endurance de la monture ;
- terrain pentu ;
- obstacles ;
- eau selon les capacités ;
- interaction avec une catastrophe ;
- combat monté ;
- désarçonnement ;
- sauvegarde / chargement ;
- mort permanente si activée ;
- simulation distante probabiliste ;
- streaming et déplacement du joueur monté entre cellules.

## 14. Ce qui reste volontairement ouvert

Les espèces de montures, leur nombre, leurs statistiques, leurs méthodes d'acquisition, leurs capacités spéciales, leur reproduction éventuelle, leur mortalité et leurs systèmes de progression restent des décisions de game design.

Le cœur technique doit être prêt à recevoir ces choix sans refonte majeure.
