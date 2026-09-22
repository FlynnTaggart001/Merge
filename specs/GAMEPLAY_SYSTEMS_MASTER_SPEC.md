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

Le personnage progresse selon le système canonique **Learning by Doing**. Il n'existe pas de niveau global de personnage servant à distribuer des points.

```text
Action de gameplay
      ↓
Validation de l'action
      ↓
Compétence canonique concernée
      ↓
Progression de la compétence
      ↓
Contribution pondérée aux caractéristiques liées
```

Le modèle canonique comprend **45 compétences** et **6 caractéristiques**. La liste et les relations compétence → caractéristique sont définies exclusivement dans `specs/CANONICAL_SKILLS.md`.

À la création :
- les 6 caractéristiques commencent à **6/20** ;
- 26 points de caractéristiques sont disponibles ;
- maximum d'une caractéristique à la création : **14/20** ;
- les compétences ne reçoivent aucun point manuellement.

Après la distribution des caractéristiques, les 45 compétences sont calculées automatiquement selon `specs/CANONICAL_SKILLS.md`.

Après la création, aucune répartition manuelle de points de compétence ou de caractéristique.

La progression par action utilise le baseline de `specs/SKILL_PROGRESSION.md` :

```text
P = 0.9 × max(0, (D - S + 15) / 50)
    × 1 / (1 + 0.012 × S)
    × (0.75 + 0.025 × I)
```

La progression doit être validée par le contexte de jeu. Les actions répétitives réalisées uniquement pour farmer ne constituent pas une source normale de progression.

### 3.1 Progression automatique des caractéristiques

Les caractéristiques progressent uniquement à partir de la progression validée des compétences qui leur sont liées :

```text
CharacteristicProgress += SkillProgress × Weight
```

Chaque caractéristique possède son propre pool caché et ses seuils. Lorsqu'un seuil est atteint :

```text
while CharacteristicProgress >= Threshold(C + 1):
    CharacteristicProgress -= Threshold(C + 1)
    C += 1
```

Le surplus est conservé. Les poids, seuils et limites sont data-driven.

### 3.2 Classes et voies

Les classes/voies sont déterminées par le **profil de caractéristiques** du personnage.

- Les caractéristiques sont la base de qualification d'une classe/voie.
- Les compétences influencent les classes indirectement puisqu'elles alimentent les caractéristiques.
- Si les caractéristiques requises sont insuffisantes, la classe/voie correspondante n'est pas encore disponible.
- Lorsque les conditions d'une nouvelle voie sont atteintes, le joueur est averti et le nom de la classe est révélé.
- Les classes normales sont des **classes fondamentales**.
- **Déité** est une voie spéciale distincte des classes fondamentales.
- Les noms et conditions numériques détaillés doivent être définis dans une spécification dédiée avant implémentation.

### 3.3 Échelle de maîtrise

Le niveau **50 d'une compétence représente déjà une maîtrise extrêmement élevée / surhumaine**. Les difficultés d'action et l'anti-farming doivent préserver cette signification.

## 4. Mouvement et esquives

Le déplacement à la troisième personne comprend le saut, l'accroupissement et les esquives.

Les esquives doivent supporter plusieurs variantes selon le contexte de déplacement.

### Saut arrière

Le joueur doit pouvoir effectuer un **saut arrière** comme mouvement d'esquive/mobilité distinct de la roulade.

Le saut arrière doit pouvoir :

- être déclenché par une combinaison d'input dédiée ;
- propulser le personnage vers l'arrière selon le design final ;
- être intégré au système d'Endurance ;
- générer une progression de compétence uniquement lorsqu'il correspond à une compétence canonique et que l'action est validée ;
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

La roulade possède une fenêtre d'invulnérabilité temporaire. Cette protection est une mécanique défensive du `DodgeSystem` et non une caractéristique ou compétence supplémentaire.

La durée exacte de la fenêtre est un paramètre d'équilibrage data-driven. Elle ne doit pas dépendre d'une progression **Réflexe**, puisque Réflexe n'est pas une caractéristique ou compétence canonique actuelle.

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

Une parade réussie doit toujours résulter de l'input du joueur et du timing de la compétence **Parade** ; aucun système de Réflexe ne doit la déclencher ou en modifier automatiquement la fenêtre.

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

Un `WorldEventSystem` doit permettre de diffuser des événements persistants ou temporaires, dont `CreatureKilled`, `FactionDestroyed`, `LocationDestroyed`, `SuccessfulParry`, `ParryFailed` et les événements nécessaires au suivi de progression des compétences canoniques.

## 15. Sauvegarde et multi-mondes

Chaque monde possède un identifiant unique et ses propres données persistantes. Créer un nouveau monde ne réinitialise ni ne détruit les anciens mondes.

## 16. Streaming et performance

World Partition est prévu pour le monde ouvert. Les populations hors zone active restent abstraites lorsque possible. La simulation écologique doit être tickée à une fréquence adaptée ou par événements/batches.

## 17. Tests

Les systèmes critiques doivent être testables indépendamment du rendu 3D : progression des compétences, progression des caractéristiques, validation anti-farming, classes/voies, dégâts, sauvegarde, écologie, persistance, événements, esquives, saut arrière, fenêtre de parade, familiarité éventuelle de gameplay et durée des i-frames.

## 18. Ce qui reste volontairement ouvert

Les domaines magiques, familles d'armes, dégâts, courbes de progression, durée exacte des i-frames, fenêtre exacte de parade, familiarité, factions, bestiaire, quêtes et valeurs d'équilibrage restent des données de game design à régler pendant les prototypes.

Les conditions exactes des classes fondamentales et de **Déité** restent également à définir. Aucun nom ou seuil de classe non validé ne doit être inventé.

## 19. Ordre recommandé d'implémentation Unreal

```text
1. Core / GameInstance / GameMode / PlayerCharacter
2. Input + Third Person Movement
3. Attributes + Progression Events
4. Combat + Damage + Effects
5. Weapons + Weapon Mastery
6. Dodge / Roll / BackwardJump / Crouch / Stealth / Backstab
7. Parry / Block / Defense reactions
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
