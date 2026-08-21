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
Réflexe   ← expérience de combat significative / situations de combat réellement vécues
Arme X    ← utilisation significative de la famille X
Magie X   ← utilisation effective du domaine magique X
```

Les gains passent par un système de progression commun et peuvent être validés par des règles anti-farming.

Les statistiques dérivées doivent être calculées à partir des attributs/maîtrises et non stockées comme des valeurs arbitrairement dupliquées lorsque cela n'est pas nécessaire.

### 3.1 Réflexe de combat

Le personnage possède une jauge/compétence de **Réflexe** distincte de l'Agilité.

Le Réflexe représente l'expérience et les automatismes acquis au combat. Il augmente progressivement grâce à l'expérience de combat significative, notamment lorsque le personnage survit et apprend de situations où il doit réagir à des attaques réelles.

Le Réflexe peut donner une **chance passive d'esquive automatique** lorsqu'une attaque ennemie est détectée et que les conditions de réaction sont réunies, sans input direct du joueur.

Principes :

- le Réflexe ne remplace jamais l'esquive manuelle ;
- une forte maîtrise doit améliorer la fiabilité, pas rendre le joueur invulnérable ;
- l'esquive automatique doit être limitée par le contexte, la direction, l'espace disponible, l'état du personnage et le coût éventuel en Endurance ;
- les attaques impossibles à éviter, les situations sans espace et certains effets spéciaux peuvent ignorer l'automatisme ;
- l'automatisme doit respecter les mêmes règles de collision, animation et invulnérabilité que l'esquive manuelle ;
- le système doit empêcher le farming artificiel de Réflexe sur des attaques répétées sans danger réel.

Le calcul exact de la probabilité, des seuils et des exceptions sera équilibré pendant le prototype.

Le Réflexe et l'Agilité sont volontairement séparés :

```text
Agilité → capacité physique / qualité des mouvements et esquives du joueur
Réflexe → expérience de combat / capacité à réagir automatiquement
```

## 4. Mouvement et esquives

Le déplacement à la troisième personne comprend le saut, l'accroupissement et les esquives.

Les esquives doivent supporter plusieurs variantes selon le contexte de déplacement.

### Saut arrière

Le joueur doit pouvoir effectuer un **saut arrière** comme mouvement d'esquive/mobilité distinct de la roulade.

Le saut arrière doit pouvoir :

- être déclenché par une combinaison d'input dédiée ;
- propulser le personnage vers l'arrière par rapport à son orientation ou à la direction de déplacement selon le design final ;
- être intégré au système d'Endurance ;
- contribuer à la progression d'Agilité lorsqu'il est utilisé de manière pertinente ;
- interagir avec le combat, la furtivité et les animations ;
- être soumis aux mêmes contraintes de collision et d'espace que les autres mouvements.

L'architecture doit permettre plusieurs variantes d'esquive sans créer une logique indépendante pour chaque animation.

```text
DodgeSystem
├── Roll
├── Backstep / BackwardJump
├── DirectionalDodge
└── FutureDodgeTypes[*]
```

Le nom gameplay définitif entre « saut arrière », « backstep » ou une variante pourra être choisi pendant le prototype sans modifier l'architecture centrale.

## 5. Combat et dégâts

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

Le système d'esquive automatique du Réflexe utilise le même pipeline de résolution que les esquives manuelles et ne doit pas créer une seconde mécanique de combat incompatible.

Les valeurs finales seront équilibrées pendant le prototype.

## 6. Effets et statuts

Prévoir un système d'effets réutilisables pour éviter de coder un comportement particulier dans chaque arme, sort ou créature.

Catégories conceptuelles :

```text
Damage / Heal / Buff / Debuff / Poison / Bleed / Stun / Slow / Elemental / Custom
```

Les effets sont data-driven et peuvent être appliqués par plusieurs systèmes.

## 7. Équipement et inventaire

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

## 8. IA et perception

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

## 9. Bestiaire et écologie

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

## 10. Monde persistant

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

## 11. Factions et réputation

Prévoir un système data-driven de factions et de relations :

- réputation du joueur ;
- relations inter-factions ;
- alliances/hostilité ;
- territoire ;
- membres et dirigeants ;
- conséquences de morts ou destructions.

Une faction peut être durablement affaiblie ou disparaître si le game design le permet.

## 12. Quêtes et dialogues réactifs

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

## 13. Temps et environnement

Prévoir un système de temps mondial pouvant alimenter :

- cycle jour/nuit ;
- routines PNJ ;
- reproduction ;
- migration ;
- événements ;
- comportement des créatures.

Prévoir également une couche météo/environnement extensible pouvant influencer visibilité, bruit, navigation et comportements.

Les saisons restent optionnelles et ne doivent pas être codées comme une dépendance obligatoire.

## 14. Événements mondiaux

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

## 15. Sauvegarde et multi-mondes

La sauvegarde est divisée en état du joueur et état du monde. Chaque monde possède un identifiant unique et ses propres données persistantes.

```text
World_001
World_002
World_003
```

Créer un nouveau monde ne réinitialise ni ne détruit les anciens mondes.

Le chargement doit restaurer les conséquences persistantes avant ou pendant la matérialisation des Actors concernés.

## 16. Streaming et performance

World Partition est prévu pour le monde ouvert. Les populations hors zone active restent abstraites lorsque possible.

La simulation écologique doit être tickée à une fréquence adaptée ou par événements/batches, pas nécessairement chaque frame.

Mass Framework reste optionnel et doit être adopté seulement si les profils de performance justifient son utilisation.

## 17. Tests

Les systèmes critiques doivent être conçus pour être testables indépendamment du rendu 3D :

- progression ;
- calcul de dégâts ;
- sauvegarde/chargement ;
- évolution de population ;
- prédateur/proie ;
- persistance de destruction ;
- événements mondiaux ;
- conditions de quêtes ;
- Réflexe et probabilité d'esquive automatique ;
- variantes d'esquive dont le saut arrière.

Les tests de performance et de gameplay réels dans Unreal restent nécessaires après implémentation.

## 18. Ce qui reste volontairement ouvert

Ne pas figer dans cette architecture :

- domaines magiques définitifs ;
- nombre exact de familles d'armes ;
- valeurs de dégâts ;
- courbes de progression ;
- courbe et probabilité exactes du Réflexe ;
- nombre définitif de factions ;
- bestiaire final ;
- contenu des quêtes ;
- valeurs de météo/temps ;
- règles d'équilibrage finales.

Ces éléments sont des données de game design, pas des contraintes du cœur technique.

## 19. Ordre recommandé d'implémentation Unreal

```text
1. Core / GameInstance / GameMode / PlayerCharacter
2. Input + Third Person Movement
3. Attributes + Progression Events
4. Combat + Damage + Effects
5. Weapons + Weapon Mastery
6. Dodge / BackwardJump / Crouch / Stealth / Backstab
7. Reflex System + automatic reaction prototype
8. Inventory + Equipment
9. AI + Perception
10. Save/Load + World Persistence
11. Time + World Events
12. Ecology + Population Simulation
13. Factions + Reputation
14. Quests + Reactive Dialogue
15. Streaming + Profiling + Optimization
```

Chaque étape doit produire un prototype testable avant d'augmenter la complexité.
