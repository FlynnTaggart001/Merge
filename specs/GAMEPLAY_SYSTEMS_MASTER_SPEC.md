# Merge — Master Gameplay Systems Specification

**Statut** : APPROUVÉ — architecture de pré-implémentation
**Engine** : Unreal Engine 5.8.1
**Langage principal** : C++20
**Blueprint** : présentation, contenu éditable et prototypage ciblé

## 1. Objectif

Ce document relie les systèmes de gameplay de Merge avant leur implémentation Unreal. Il fixe les dépendances, les responsabilités et les règles d'intégration sans figer prématurément les valeurs d'équilibrage ni les contenus encore en conception.

## 2. Architecture événementielle

Les systèmes communiquent principalement par événements de gameplay et interfaces/composants, plutôt que par dépendances directes entre systèmes.

Exemple :

```text
Combat
  ↓
GameplayEvent: CreatureKilled
  ├── Progression
  ├── Ecology
  ├── Quest
  ├── Faction
  └── WorldHistory
```

Règle : un système producteur ne doit pas connaître les détails internes de tous les systèmes consommateurs.

## 3. Progression

Le personnage progresse principalement par utilisation réelle :

```text
Endurance ← course / combat / saut / effort
Agilité   ← esquives réussies / sauts / mobilité
Défense   ← dégâts réellement subis
Arme X    ← utilisation significative de la famille X
Magie X   ← utilisation effective du domaine magique X
```

Les gains passent par un système de progression commun et peuvent être validés par des règles anti-farming.

Les statistiques dérivées doivent être calculées à partir des attributs/maîtrises et non stockées comme des valeurs arbitrairement dupliquées lorsque cela n'est pas nécessaire.

## 4. Combat et dégâts

Le combat physique utilise des définitions data-driven d'armes et de familles. Le système central doit gérer :

- dégâts ;
- types de dégâts ;
- résistances ;
- armure ;
- blocage ;
- parade si retenue ;
- stagger / équilibre ;
- hit reactions ;
- attaques légères/lourdes ;
- combos ;
- récupération ;
- interruptions ;
- mort ;
- effets et états.

Les valeurs finales seront équilibrées pendant le prototype.

## 5. Effets et statuts

Prévoir un système d'effets réutilisables pour éviter de coder un comportement particulier dans chaque arme, sort ou créature.

Catégories conceptuelles :

```text
Damage / Heal / Buff / Debuff / Poison / Bleed / Stun / Slow / Elemental / Custom
```

Les effets sont data-driven et peuvent être appliqués par plusieurs systèmes.

## 6. Équipement et inventaire

L'équipement doit être séparé de l'inventaire.

```text
Inventory
├── Weapons
├── Armor
├── Accessories
├── Consumables
├── QuestItems
└── Materials

Equipment
├── MainHand
├── OffHand
├── Head
├── Chest
├── Hands
├── Legs
├── Feet
└── Accessories[*]
```

Les objets peuvent avoir poids, statistiques, effets, compatibilités et autres propriétés selon leur catégorie.

Le poids doit pouvoir influencer l'endurance/mobilité si cette règle est retenue par le game design final.

## 7. IA et perception

La perception doit être un système commun pouvant servir aux ennemis et PNJ :

```text
Perception
├── Vision
├── Hearing
├── Light / Visibility
├── Noise
├── Awareness
└── Future senses
```

La furtivité du joueur exploite cette couche. Les états de détection restent progressifs :

```text
Calme → Soupçon → Recherche → Alerte → Combat
```

Les IA peuvent ensuite utiliser Behavior Trees, State Trees ou autres outils UE selon le prototype, sans imposer prématurément une solution unique.

## 8. Bestiaire et écologie

Le bestiaire fonctionne avec des populations abstraites lorsque les individus ne sont pas matérialisés.

```text
Species
├── Population
├── Reproduction
├── Mortality
├── Food needs
├── Predators / Prey
├── Territory
├── CarryingCapacity
└── Migration
```

Les Actors Unreal matérialisés sont une représentation locale de la simulation et non la simulation elle-même.

## 9. Monde persistant

Le monde ne respawn pas artificiellement. Les morts, destructions et consommations définitives persistent.

La simulation peut toutefois produire de nouvelles générations, croissance, migration et évolution naturelle.

Les données persistantes doivent distinguer au minimum :

```text
WorldState
├── EcologyState
├── DestructionState
├── ResourceState
├── NPCState
├── FactionState
├── QuestState
├── WorldEventHistory
└── TimeState
```

## 10. Factions et réputation

Prévoir un système data-driven de factions et de relations :

- réputation du joueur ;
- relations inter-factions ;
- alliances/hostilité ;
- territoire ;
- membres et dirigeants ;
- conséquences de morts ou destructions.

Une faction peut être durablement affaiblie ou disparaître si le game design le permet.

## 11. Quêtes et dialogues réactifs

Les quêtes et dialogues doivent consulter l'état du monde plutôt que supposer que les PNJ, créatures et objets existent toujours.

Exemples de conditions :

```text
NPC_DEAD
FACTION_DESTROYED
CREATURE_EXTINCT_LOCALLY
LOCATION_DESTROYED
OBJECT_ALREADY_CONSUMED
WORLD_EVENT_OCCURRED
```

Une quête doit pouvoir échouer, évoluer ou changer de contexte lorsqu'un événement permanent rend son état initial impossible.

## 12. Temps et environnement

Prévoir un système de temps mondial pouvant alimenter :

- cycle jour/nuit ;
- routines PNJ ;
- reproduction ;
- migration ;
- événements ;
- comportement des créatures.

Prévoir également une couche météo/environnement extensible pouvant influencer visibilité, bruit, navigation et comportements.

Les saisons restent optionnelles et ne doivent pas être codées comme une dépendance obligatoire.

## 13. Événements mondiaux

Un `WorldEventSystem` doit permettre de diffuser des événements persistants ou temporaires :

```text
CreatureKilled
FactionLeaderKilled
FactionDestroyed
LocationDestroyed
PopulationCollapse
Migration
WorldDiscovery
QuestCompleted
```

Les événements importants peuvent alimenter un historique du monde pour les sauvegardes et futurs systèmes narratifs.

## 14. Sauvegarde et multi-mondes

La sauvegarde est divisée en état du joueur et état du monde. Chaque monde possède un identifiant unique et ses propres données persistantes.

```text
World_001
World_002
World_003
```

Créer un nouveau monde ne réinitialise ni ne détruit les anciens mondes.

Le chargement doit restaurer les conséquences persistantes avant ou pendant la matérialisation des Actors concernés.

## 15. Streaming et performance

World Partition est prévu pour le monde ouvert. Les populations hors zone active restent abstraites lorsque possible.

La simulation écologique doit être tickée à une fréquence adaptée ou par événements/batches, pas nécessairement chaque frame.

Mass Framework reste optionnel et doit être adopté seulement si les profils de performance justifient son utilisation.

## 16. Tests

Les systèmes critiques doivent être conçus pour être testables indépendamment du rendu 3D :

- progression ;
- calcul de dégâts ;
- sauvegarde/chargement ;
- évolution de population ;
- prédateur/proie ;
- persistance de destruction ;
- événements mondiaux ;
- conditions de quêtes.

Les tests de performance et de gameplay réels dans Unreal restent nécessaires après implémentation.

## 17. Ce qui reste volontairement ouvert

Ne pas figer dans cette architecture :

- domaines magiques définitifs ;
- nombre exact de familles d'armes ;
- valeurs de dégâts ;
- courbes de progression ;
- nombre définitif de factions ;
- bestiaire final ;
- contenu des quêtes ;
- valeurs de météo/temps ;
- règles d'équilibrage finales.

Ces éléments sont des données de game design, pas des contraintes du cœur technique.

## 18. Ordre recommandé d'implémentation Unreal

```text
1. Core / GameInstance / GameMode / PlayerCharacter
2. Input + Third Person Movement
3. Attributes + Progression Events
4. Combat + Damage + Effects
5. Weapons + Weapon Mastery
6. Dodge / Crouch / Stealth / Backstab
7. Inventory + Equipment
8. AI + Perception
9. Save/Load + World Persistence
10. Time + World Events
11. Ecology + Population Simulation
12. Factions + Reputation
13. Quests + Reactive Dialogue
14. Streaming + Profiling + Optimization
```

Chaque étape doit produire un prototype testable avant d'augmenter la complexité.
