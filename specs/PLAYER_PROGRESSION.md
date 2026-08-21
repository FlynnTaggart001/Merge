# Merge — Player Progression Specification

**Statut** : APPROUVÉ — conception / architecture
**Moteur** : Unreal Engine 5.8.1
**Langage principal** : C++

## 1. Principe

La progression de Merge est principalement **organique et liée à l'utilisation**. Le personnage améliore une aptitude en pratiquant réellement les actions correspondant à cette aptitude.

Il ne s'agit pas d'un système où toutes les statistiques augmentent uniquement grâce à un niveau global.

## 2. Endurance

L'Endurance progresse progressivement avec les efforts physiques répétés :

- course ;
- combat ;
- saut ;
- esquive / roulade ;
- autres activités physiques pertinentes à définir.

Le système doit mesurer l'effort utile plutôt que compter aveuglément chaque input.

Objectifs :

- récompenser l'activité physique réelle ;
- éviter le farming artificiel ;
- permettre un équilibrage du gain selon l'intensité et la durée de l'effort ;
- permettre une progression persistante par personnage.

## 3. Agilité

L'Agilité progresse avec les actions nécessitant mobilité, timing et évitement :

- esquive / roulade réussie ;
- saut ;
- saut arrière ;
- autres actions acrobatiques futures.

Le système d'esquive doit être une véritable mécanique de gameplay :

- direction selon l'input ;
- coût d'Endurance ;
- état d'esquive ;
- fenêtre d'invulnérabilité à équilibrer ;
- verrouillage ou interruption de certaines actions ;
- intégration au combat et à la furtivité.

Une esquive ne doit pas automatiquement donner une progression maximale : la progression doit pouvoir distinguer une utilisation significative d'un spam sans danger.

### 3.1 Saut arrière

Le saut arrière est une variante d'esquive/mobilité distincte de la roulade. Il peut contribuer à l'Agilité lorsqu'il est utilisé dans un contexte pertinent de mouvement ou de combat.

Il doit être intégré au même système de Dodge que la roulade afin de partager les règles de coût, collision, invulnérabilité et récupération lorsque celles-ci sont retenues.

## 4. Défense

La Défense progresse avec les dégâts réellement subis par le personnage.

Le système devra comptabiliser l'exposition réelle au danger et empêcher les boucles artificielles de progression, par exemple :

- dégâts auto-infligés volontairement ;
- sources triviales répétées ;
- dégâts sans risque ni contexte de combat ;
- exploitation d'un événement répétable.

Les règles exactes de validation et les paliers de progression seront déterminés lors du prototype.

## 5. Réflexe de combat

Le **Réflexe** est une compétence distincte de l'Agilité. Il représente l'expérience pratique accumulée lors de combats réels et la capacité du personnage à développer des automatismes défensifs.

Le Réflexe progresse avec l'XP/expérience de combat pertinente, notamment :

- combats réellement engagés ;
- attaques ennemies rencontrées ;
- situations de danger ;
- survie et répétition de situations de combat variées.

Le simple fait de répéter artificiellement une même séquence sans danger réel ne doit pas produire une progression normale.

### 5.1 Esquive réflexe automatique

Lorsque le personnage est suffisamment expérimenté, le Réflexe lui donne une **probabilité passive d'effectuer automatiquement une esquive** lorsqu'une attaque ennemie va réellement le toucher.

L'automatisme doit :

- rester une chance et non une garantie ;
- ne jamais supprimer l'intérêt de l'esquive manuelle ;
- utiliser le même système de Dodge que l'esquive commandée par le joueur ;
- respecter les collisions, l'espace disponible et les états du personnage ;
- pouvoir consommer de l'Endurance ;
- être impossible ou fortement réduit dans certaines situations ;
- ne pas permettre d'éviter des attaques intrinsèquement inévitables ;
- respecter les cooldowns, fenêtres d'action et règles d'animation ;
- être clairement équilibrable par données.

Conceptuellement :

```text
Attaque ennemie détectée
        ↓
Vérification du danger réel
        ↓
Vérification état / espace / endurance
        ↓
Test de Réflexe
   ┌────┴────┐
   ↓         ↓
 réussite   échec
   ↓         ↓
Dodge auto  attaque résolue normalement
```

La probabilité exacte ne doit pas être fixée maintenant. Elle sera déterminée par une courbe de progression et testée dans Unreal.

### 5.2 Différence Agilité / Réflexe

```text
Agilité
→ améliore les capacités physiques et l'efficacité des mouvements/esquives.

Réflexe
→ représente l'expérience de combat et la capacité à réagir automatiquement.
```

Un personnage très agile peut donc être excellent avec une esquive manuelle sans avoir un Réflexe élevé. À l'inverse, un vétéran peut posséder de bons automatismes défensifs sans disposer d'une Agilité exceptionnelle.

## 6. Magie

La progression magique est **séparée par domaine de magie**.

Chaque domaine possède sa propre maîtrise :

```text
Domaine A → maîtrise A
Domaine B → maîtrise B
Domaine C → maîtrise C
```

L'utilisation effective d'une capacité appartenant à un domaine fait progresser principalement ce domaine.

Les domaines de magie sont actuellement en cours de définition. Aucun nom, nombre ou liste définitive ne doit être codé en dur dans l'architecture centrale.

L'architecture doit permettre d'ajouter un nouveau domaine par données / configuration lorsque possible, sans réécrire le système de progression.

## 7. Événements de progression

Les systèmes de gameplay doivent pouvoir envoyer des événements de progression génériques au système de progression.

Conceptuellement :

```text
Course réussie
    ↓
ProgressionEvent(PhysicalEffort)
    ↓
ProgressionSystem
    ↓
Endurance
```

```text
Esquive réussie
    ↓
ProgressionEvent(SuccessfulDodge)
    ↓
ProgressionSystem
    ↓
Agilité
```

```text
Dégâts réellement subis
    ↓
ProgressionEvent(ReceivedDamage)
    ↓
ProgressionSystem
    ↓
Défense
```

```text
Combat réellement vécu
    ↓
ProgressionEvent(CombatExperience)
    ↓
ProgressionSystem
    ↓
Réflexe
```

```text
Sort du domaine X utilisé
    ↓
ProgressionEvent(MagicUsage, DomainX)
    ↓
ProgressionSystem
    ↓
Maîtrise DomainX
```

Cette séparation évite de coupler le système de combat, de mouvement ou de magie aux détails internes des statistiques.

## 8. Anti-abus

Chaque source de progression doit pouvoir définir des règles de validation :

- contexte requis ;
- fréquence maximale de contribution ;
- intensité minimale ;
- rendement décroissant ;
- répétition détectée ;
- récompense uniquement pour une action réellement pertinente.

Ces mécanismes seront équilibrés pendant le prototype et ne doivent pas être surconçus maintenant.

## 9. Architecture cible

```text
ProgressionSystem
├── AttributeProgression
│   ├── Endurance
│   ├── Agility
│   └── Defense
│
├── CombatExperience
│   └── Reflex
│       └── AutomaticDodgeChance
│
├── MagicProgression
│   └── MagicDomainMastery[*]
│
├── ProgressionEvent
│   ├── PhysicalEffort
│   ├── SuccessfulDodge
│   ├── BackwardJump
│   ├── Jump
│   ├── ReceivedDamage
│   ├── CombatExperience
│   └── MagicUsage(Domain)
│
└── ProgressionRules
    ├── Validation
    ├── AntiAbuse
    └── GainCalculation
```

Les valeurs de gain, paliers, courbes et probabilités ne sont pas encore définitifs.

## 10. Règles

1. La progression doit être principalement liée à l'utilisation réelle.
2. Une action doit progresser l'aptitude à laquelle elle correspond.
3. Les systèmes gameplay ne doivent pas modifier directement toutes les statistiques sans passer par une logique de progression cohérente.
4. L'Esquive est une mécanique de gameplay obligatoire et une source d'Agilité.
5. Le saut arrière est une variante d'esquive/mobilité intégrée au même système.
6. Le Réflexe est distinct de l'Agilité.
7. Le Réflexe peut déclencher une esquive automatique avec une probabilité limitée lorsque les conditions sont réunies.
8. L'esquive automatique ne doit jamais rendre l'esquive manuelle inutile.
9. Les domaines magiques restent extensibles et non figés.
10. Les mécanismes anti-farming sont nécessaires, mais seront équilibrés au prototype.
11. La progression doit être persistante avec le personnage et compatible avec la persistance du monde.
12. Aucun système complet n'est considéré comme implémenté par cette spécification seule.
