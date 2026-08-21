# Merge — Player Progression Specification

**Statut** : APPROUVÉ — conception / architecture
**Moteur** : Unreal Engine 5.8.1
**Langage principal** : C++

## 1. Principe

La progression de Merge est principalement **organique et liée à l'utilisation**. Le personnage améliore une aptitude en pratiquant réellement les actions correspondant à cette aptitude.

Il ne s'agit pas d'un système où toutes les statistiques augmentent uniquement grâce à un niveau global.

## 2. Endurance

L'Endurance progresse progressivement avec les efforts physiques répétés :

- course / sprint ;
- combat ;
- saut ;
- roulade / esquive ;
- bond en arrière ;
- pas de côté ;
- franchissement d'obstacles ;
- escalade ;
- autres activités physiques pertinentes.

Toutes ces actions ont un **coût d'Endurance** lorsqu'elles représentent un effort physique significatif. Les coûts sont data-driven et peuvent varier selon l'action, sa durée, son intensité, l'équipement et le contexte.

Le système doit mesurer l'effort utile plutôt que compter aveuglément chaque input.

Une action nécessitant de l'Endurance ne doit normalement pas être exécutée lorsque la ressource est insuffisante. Le comportement exact en cas d'Endurance faible sera équilibré dans le prototype.

Objectifs : récompenser l'activité physique réelle, éviter le farming artificiel et permettre un équilibrage du gain selon l'intensité et la durée de l'effort.

### 2.1 Coûts par mouvement

Les coûts sont volontairement **paramétrables individuellement** :

```text
Course / Sprint          → coût selon durée et intensité
Saut                     → coût par impulsion
Roulade                  → coût par utilisation
Bond en arrière          → coût par utilisation
Pas de côté              → coût par utilisation
Franchissement           → coût selon l'obstacle / effort
Escalade                 → coût progressif selon durée et effort
```

Une escalade peut donc drainer l'Endurance progressivement plutôt que d'appliquer un coût unique. Les mouvements courts utilisent principalement un coût à l'activation.

Le système doit exposer ces coûts comme données d'équilibrage et ne doit pas coder des valeurs fixes directement dans les animations ou le personnage.

## 3. Agilité

L'Agilité progresse avec les actions nécessitant mobilité, timing et évitement :

- esquive / roulade réussie ;
- saut ;
- bond en arrière ;
- pas de côté ;
- franchissement d'obstacles ;
- escalade / déplacement vertical ;
- réception contrôlée après une chute ;
- autres actions acrobatiques futures.

Le système de mouvement doit distinguer les actions de mobilité des simples inputs répétés. Une utilisation significative en situation réelle doit être davantage valorisée qu'un spam sans contexte.

### 3.1 Bond en arrière

Le bond en arrière est une action de mouvement et d'esquive distincte de la roulade. Il peut contribuer à l'Agilité lorsqu'il est utilisé dans un contexte pertinent de mouvement ou de combat.

Il est intégré au même système de Dodge que la roulade pour partager les règles communes de coût, collision et récupération lorsque celles-ci sont retenues, mais ses paramètres de déplacement et ses propriétés défensives restent distincts.

### 3.2 Pas de côté

Le pas de côté est une esquive/mobilité latérale rapide. Il doit permettre d'éviter une attaque ou de modifier rapidement la position du personnage sans utiliser la roulade.

Il peut contribuer à l'Agilité lorsqu'il est utilisé de façon pertinente et doit respecter l'Endurance, les collisions, l'espace disponible et les règles de récupération.

### 3.3 Réception de chute

Une chute modérée peut être résolue par une réception contrôlée lorsque le personnage dispose de suffisamment de mobilité et que les conditions sont réunies.

La qualité de la réception peut dépendre de l'Agilité et du contexte :

```text
Chute
  ↓
Évaluation de la hauteur / vitesse / état
  ↓
Réception possible ?
  ├── Oui → réception contrôlée / dégâts réduits
  └── Non → chute normale
```

Cette mécanique ne doit pas supprimer les conséquences d'une chute importante.

La réception contrôlée peut avoir un coût d'Endurance faible ou contextuel si elle implique une action physique active ; elle ne doit pas consommer systématiquement une ressource lorsqu'aucun effort distinct n'est effectué.

## 4. Défense

La Défense progresse avec les dégâts réellement subis par le personnage.

Le système devra comptabiliser l'exposition réelle au danger et empêcher les boucles artificielles de progression, par exemple dégâts auto-infligés volontairement, sources triviales répétées ou exploitation d'un événement répétable.

## 5. Réflexe de combat

Le **Réflexe** est une compétence distincte de l'Agilité. Il représente l'expérience pratique accumulée lors de combats réels et la capacité du personnage à développer des automatismes défensifs.

Le Réflexe progresse avec l'XP/expérience de combat pertinente : combats réellement engagés, attaques rencontrées, situations de danger, survie et répétition de situations variées.

### 5.1 Esquive réflexe automatique

Lorsque le personnage est suffisamment expérimenté, le Réflexe lui donne une **probabilité passive d'effectuer automatiquement une esquive** lorsqu'une attaque ennemie va réellement le toucher.

L'automatisme utilise le même système de Dodge que l'esquive commandée par le joueur et respecte collisions, espace, Endurance, états, animation, cooldowns et attaques intrinsèquement inévitables.

### 5.2 Différence Agilité / Réflexe

```text
Agilité → capacités physiques et efficacité des mouvements/esquives.
Réflexe → expérience de combat et capacité à réagir automatiquement.
```

## 6. Magie

La progression magique est séparée par domaine de magie. Chaque domaine possède sa propre maîtrise et progresse principalement avec son utilisation effective. Les domaines restent extensibles et ne sont pas figés dans l'architecture centrale.

## 7. Événements de progression

Les systèmes de gameplay envoient des événements génériques au système de progression :

```text
PhysicalEffort      → Endurance
SuccessfulDodge     → Agilité
BackwardJump        → Agilité
SideStep            → Agilité
Jump                → Agilité / Endurance selon contexte
ObstacleTraversal   → Agilité / Endurance selon contexte
Climb               → Agilité / Endurance selon contexte
ControlledLanding   → Agilité
ReceivedDamage      → Défense
CombatExperience    → Réflexe
MagicUsage(Domain)  → Maîtrise du domaine
```

Chaque événement doit pouvoir être validé par des règles anti-farming.

## 8. Anti-abus

Chaque source de progression doit pouvoir définir : contexte requis, fréquence maximale, intensité minimale, rendement décroissant, répétition détectée et récompense uniquement pour une action réellement pertinente.

## 9. Architecture cible

```text
PlayerMovementSystem
├── Walk / Run / Sprint
├── Jump
├── Crouch
├── Roll
├── BackwardJump
├── SideStep
├── ObstacleTraversal
├── ContextualClimb
└── ControlledLanding

ProgressionSystem
├── AttributeProgression
│   ├── Endurance
│   ├── Agility
│   └── Defense
├── CombatExperience
│   └── Reflex
│       └── AutomaticDodgeChance
├── PhysicalEffort
│   └── EnduranceCost[*]
├── MagicProgression
│   └── MagicDomainMastery[*]
└── ProgressionRules
    ├── Validation
    ├── AntiAbuse
    └── GainCalculation
```

## 10. Règles

1. La progression doit être principalement liée à l'utilisation réelle.
2. Une action doit progresser l'aptitude à laquelle elle correspond.
3. Les systèmes gameplay ne doivent pas modifier directement toutes les statistiques sans passer par une logique de progression cohérente.
4. La roulade, le bond en arrière et le pas de côté sont des mécaniques d'esquive distinctes.
5. Les actions physiques significatives — course, saut, roulade, bond en arrière, pas de côté, franchissement et escalade — ont un coût d'Endurance data-driven.
6. Une action nécessitant de l'Endurance ne doit normalement pas être exécutée lorsque le coût ne peut pas être payé.
7. Le Réflexe est distinct de l'Agilité.
8. Le Réflexe peut déclencher une esquive automatique avec une probabilité limitée lorsque les conditions sont réunies.
9. L'esquive automatique ne doit jamais rendre l'esquive manuelle inutile.
10. Les mouvements d'exploration doivent rester contextuels et ne pas transformer Merge en système de parkour intégral sans décision de game design ultérieure.
11. Les mécanismes anti-farming sont nécessaires et seront équilibrés au prototype.
12. La progression doit être persistante avec le personnage et compatible avec la persistance du monde.
