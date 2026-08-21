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

Le Réflexe et l'Agilité sont volontairement séparés :

```text
Agilité → capacité physique / qualité des mouvements et esquives du joueur
Réflexe → expérience de combat / capacité à réagir automatiquement
```

### 3.2 Familiarité de combat et parade réflexe

Le Réflexe influence également la **tolérance de timing des parades**, sans déclencher la parade à la place du joueur.

Le joueur doit toujours effectuer l'input de parade. Le Réflexe permet au personnage expérimenté d'anticiper légèrement l'impact :

```text
Réflexe faible → fenêtre de parade très exigeante
Réflexe moyen → fenêtre légèrement plus permissive
Réflexe élevé → fenêtre nettement plus permissive
```

Cette assistance peut être modulée par une **familiarité de combat** acquise à force d'affronter réellement certaines familles d'attaques.

L'assistance de parade est différente de l'esquive automatique :

```text
Esquive automatique → le système peut déclencher une esquive selon le Réflexe et les conditions.
Parade réflexe → le système ne déclenche rien ; il améliore uniquement la fenêtre de timing après l'input du joueur.
```

### 3.3 Réflexe et invulnérabilité de roulade

La roulade accorde une **fenêtre temporaire d'invulnérabilité (i-frames)** pendant son exécution. Cette protection fait partie du système de défense de la roulade et non d'une invulnérabilité générale du personnage.

Le **Réflexe** influence la durée de cette fenêtre : plus le personnage est expérimenté, plus il peut exploiter précisément le moment où l'attaque passe à proximité.

```text
Réflexe faible
→ i-frames courtes, timing très exigeant

Réflexe moyen
→ i-frames plus tolérantes

Réflexe élevé
→ i-frames nettement plus longues
```

Règles :

- les i-frames ne commencent qu'à une phase définie de la roulade ;
- elles cessent avant la fin complète de l'animation ;
- le Réflexe augmente la fenêtre d'invulnérabilité, mais ne rend pas toute la roulade invulnérable ;
- la roulade conserve son coût en Endurance ;
- l'espace disponible, les collisions et l'état du personnage restent déterminants ;
- certaines attaques spéciales, attaques imparables ou effets explicitement définis peuvent ignorer les i-frames ;
- le système doit empêcher le spam de roulades de créer une invulnérabilité quasi permanente ;
- les valeurs exactes de durée, seuils et courbes restent des paramètres d'équilibrage data-driven.

La **familiarité de combat** peut améliorer l'anticipation contre des familles d'attaques réellement connues, mais ne doit pas créer une immunité automatique contre un nouvel ennemi.

Le modèle défensif devient donc :

```text
                 Réflexe
                    │
       ┌────────────┼─────────────┐
       ↓            ↓             ↓
  Esquive auto   Parade        Roulade
  probabilité    fenêtre       durée des i-frames
       │          timing             │
       └──── Familiarité ────────────┘
```

Le Réflexe améliore ainsi les automatismes et la tolérance défensive sans supprimer l'importance du joueur.

## 4. Mouvement et esquives

Le déplacement à la troisième personne comprend le saut, l'accroupissement et les esquives.

Les esquives doivent supporter plusieurs variantes selon le contexte de déplacement.

### Saut arrière

Le joueur doit pouvoir effectuer un **saut arrière** comme mouvement d'esquive/mobilité distinct de la roulade.

Le saut arrière doit pouvoir :

- être déclenché par une combinaison d'input dédiée ;
- propulser le personnage vers l'arrière selon le design final ;
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

### 4.1 Roulade et i-frames

La roulade possède une fenêtre d'invulnérabilité temporaire, calculée par le `DodgeSystem` à partir de la progression de Réflexe et des paramètres de l'attaque.

Le système doit exposer une fenêtre de protection exploitable par le `CombatResolver` plutôt que d'ajouter un booléen global `IsInvincible` au personnage.

Ainsi, une attaque peut demander au système :

```text
CanAttackHit(Target, AttackContext)
        ↓
Target possède-t-il une DefensiveWindow active ?
        ↓
Oui → vérifier si l'attaque ignore cette fenêtre
Non → résolution normale
```

Cela permet de conserver une architecture propre pour la roulade, les esquives futures et les attaques spéciales.

## 5. Combat et dégâts

Le combat physique utilise des définitions data-driven d'armes et de familles. Le système central doit gérer :

- dégâts ;
- types de dégâts ;
- résistances ;
- armure ;
- blocage ;
- parade active à timing précis ;
- riposte après parade réussie ;
- attaques imparables/non parables définies par données ;
- stagger / équilibre ;
- hit reactions ;
- attaques légères/lourdes ;
- combos ;
- récupération ;
- interruptions ;
- mort ;
- effets et états.

### 5.1 Défense active

Le système distingue trois réponses défensives :

```text
Blocage → absorbe/réduit l'attaque selon les règles d'équipement.
Parade  → timing précis avant impact, pouvant annuler/réduire le coup et ouvrir une riposte.
Esquive → évitement spatial via le DodgeSystem, avec i-frames pour la roulade.
```

La parade doit être résolue par le même `CombatResolver` que les autres interactions et produire des événements comme `SuccessfulParry` ou `ParryFailed`.

Une parade réussie ne doit pas être déclenchée automatiquement par le système de Réflexe.

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

Prévoir un système data-driven de factions et de relations : réputation du joueur, relations inter-factions, alliances/hostilité, territoire, membres et conséquences des morts ou destructions.

## 12. Quêtes et dialogues réactifs

Les quêtes et dialogues doivent consulter l'état du monde plutôt que supposer que les PNJ, créatures et objets existent toujours.

## 13. Temps et environnement

Prévoir un système de temps mondial pouvant alimenter cycle jour/nuit, routines PNJ, reproduction, migration, événements et comportement des créatures. Une couche météo/environnement reste extensible.

## 14. Événements mondiaux

Un `WorldEventSystem` doit permettre de diffuser des événements persistants ou temporaires, dont `CreatureKilled`, `FactionDestroyed`, `LocationDestroyed`, `SuccessfulParry`, `ParryFailed` et les événements défensifs nécessaires au suivi de progression.

## 15. Sauvegarde et multi-mondes

Chaque monde possède un identifiant unique et ses propres données persistantes. Créer un nouveau monde ne réinitialise ni ne détruit les anciens mondes.

## 16. Streaming et performance

World Partition est prévu pour le monde ouvert. Les populations hors zone active restent abstraites lorsque possible. La simulation écologique doit être tickée à une fréquence adaptée ou par événements/batches.

## 17. Tests

Les systèmes critiques doivent être testables indépendamment du rendu 3D : progression, dégâts, sauvegarde, écologie, persistance, événements, quêtes, Réflexe, esquives, saut arrière, fenêtre de parade, familiarité, et **durée des i-frames de roulade selon le Réflexe**.

## 18. Ce qui reste volontairement ouvert

Les domaines magiques, familles d'armes, dégâts, courbes de progression, probabilité exacte du Réflexe, durée exacte des i-frames, fenêtre exacte de parade, familiarité, factions, bestiaire, quêtes et valeurs d'équilibrage restent des données de game design à régler pendant les prototypes.

## 19. Ordre recommandé d'implémentation Unreal

```text
1. Core / GameInstance / GameMode / PlayerCharacter
2. Input + Third Person Movement
3. Attributes + Progression Events
4. Combat + Damage + Effects
5. Weapons + Weapon Mastery
6. Dodge / Roll / BackwardJump / Crouch / Stealth / Backstab
7. Parry / Block / Defense reactions
8. Reflex System + automatic reaction + reflex-scaled i-frames
9. Inventory + Equipment
10. AI + Perception
11. Save/Load + World Persistence
12. Time + World Events
13. Ecology + Population Simulation
14. Factions + Reputation
15. Quests + Reactive Dialogue
16. Streaming + Profiling + Optimization
```

Chaque étape doit produire un prototype testable avant d'augmenter la complexité.
