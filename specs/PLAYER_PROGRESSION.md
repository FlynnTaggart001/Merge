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
- nage et plongée ;
- autres activités physiques pertinentes.

Toutes ces actions ont un **coût d'Endurance** lorsqu'elles représentent un effort physique significatif. Les coûts sont data-driven et peuvent varier selon l'action, sa durée, son intensité, l'équipement et le contexte.

Une action nécessitant de l'Endurance ne doit normalement pas être exécutée lorsque la ressource est insuffisante. Le comportement exact en cas d'Endurance faible sera équilibré dans le prototype.

### 2.1 Coûts par mouvement

```text
Course / Sprint          → coût selon durée et intensité
Saut                     → coût par impulsion
Roulade                  → coût par utilisation
Bond en arrière          → coût par utilisation
Pas de côté              → coût par utilisation
Franchissement           → coût selon l'obstacle / effort
Escalade                 → coût progressif selon durée et effort
Nage / Plongée           → coût selon durée et intensité
```

Les coûts sont exposés comme données d'équilibrage et ne doivent pas être codés en dur dans les animations ou le personnage.

## 3. Agilité

L'Agilité progresse avec les actions nécessitant mobilité, timing et évitement :

- esquive / roulade réussie ;
- saut ;
- bond en arrière ;
- pas de côté ;
- franchissement d'obstacles ;
- escalade / déplacement vertical ;
- réception contrôlée après une chute ;
- mobilité aquatique pertinente ;
- autres actions acrobatiques futures.

Le système de mouvement doit distinguer les actions de mobilité des simples inputs répétés. Une utilisation significative en situation réelle doit être davantage valorisée qu'un spam sans contexte.

### 3.1 Bond en arrière

Le bond en arrière est une action de mouvement et d'esquive distincte de la roulade. Il peut contribuer à l'Agilité lorsqu'il est utilisé dans un contexte pertinent de mouvement ou de combat.

### 3.2 Pas de côté

Le pas de côté est une esquive/mobilité latérale rapide. Il doit respecter l'Endurance, les collisions, l'espace disponible et les règles de récupération.

### 3.3 Réception de chute

Une chute modérée peut être résolue par une réception contrôlée lorsque les conditions sont réunies. La qualité de la réception peut dépendre de l'Agilité et du contexte.

Une chute importante ne doit pas être annulée simplement par une statistique élevée.

## 4. Défense

La Défense progresse avec les dégâts réellement subis par le personnage.

Le système comptabilise l'exposition réelle au danger et empêche les boucles artificielles de progression : dégâts auto-infligés volontairement, sources triviales répétées et événements sans risque réel.

## 5. Réflexe de combat

Le **Réflexe** est une compétence distincte de l'Agilité. Il représente l'expérience pratique accumulée lors de combats réels et la capacité du personnage à développer des automatismes défensifs.

Le Réflexe progresse avec l'XP/expérience de combat pertinente : combats réellement engagés, attaques rencontrées, situations de danger, survie et répétition de situations variées.

### 5.1 Esquive réflexe automatique

Lorsque le personnage est suffisamment expérimenté, le Réflexe lui donne une **probabilité passive d'effectuer automatiquement une esquive** lorsqu'une attaque ennemie va réellement le toucher.
## 5. Discrétion

La Discrétion progresse avec les actions de furtivité réussies qui permettent d'éviter d'être repéré par les ennemis.

Sources principales de progression :

- déplacement en furtivité sans détection ;
- passage à proximité d'ennemis sans déclencher Soupçon / Recherche / Alerte ;
- backstab réussi ;
- utilisation prolongée de l'accroupissement en zone hostile sans être vu ;
- actions furtives significatives (vol, infiltration, etc. à définir).

Effets attendus de la maîtrise :

- réduction de la visibilité et du bruit générés ;
- meilleure résistance à la détection progressive ;
- fenêtre de backstab plus tolérante ;
- réduction du rayon de détection ennemi contre le joueur.

La progression doit récompenser l'utilisation réelle et réussie de la furtivité, pas le spam d'accroupissement en zone sûre. Les règles anti-abus (contexte, intensité, fréquence) s'appliquent comme pour les autres aptitudes.

La Discrétion s'intègre au système de furtivité déjà spécifié (posture, vitesse, ligne de vue, luminosité, bruit, terrain, équipement, état de l'ennemi).

## 6. Magie

L'automatisme utilise le même système de Dodge que l'esquive commandée par le joueur et respecte collisions, espace, Endurance, états, animation, cooldowns et attaques intrinsèquement inévitables.

### 5.2 Parade réflexe

Le joueur doit toujours effectuer l'input de parade. Le Réflexe améliore uniquement la **tolérance de la fenêtre de timing**.

La familiarité acquise contre certaines familles d'attaques peut améliorer l'anticipation, sans rendre les attaques inconnues triviales.

### 5.3 Roulade et i-frames

Le Réflexe influence la durée de la fenêtre temporaire d'invulnérabilité de la roulade :

```text
Réflexe faible → i-frames courtes
Réflexe moyen → i-frames plus tolérantes
Réflexe élevé → i-frames plus longues
```

Les i-frames ne couvrent jamais automatiquement toute l'animation. Certaines attaques peuvent ignorer cette fenêtre.

## 6. Magie

La progression magique est séparée par domaine de magie. Chaque domaine possède sa propre maîtrise et progresse principalement avec son utilisation effective.

Les domaines restent extensibles et ne sont pas figés dans l'architecture centrale.
## 7. Événements de progression

## 7. Domptage

Le **Domptage** est une compétence distincte destinée à l'acquisition de montures sauvages compatibles.

Elle progresse avec des tentatives de domptage réellement pertinentes et des réussites de domestication.

La progression peut tenir compte :
- difficulté des créatures affrontées ;
- diversité des espèces rencontrées ;
- qualité de l'approche ;
- répétition de situations variées ;
- réussites et échecs instructifs.

Le Domptage peut réduire la difficulté effective ou améliorer la fiabilité des tentatives, sans rendre automatiquement domptable une espèce déclarée incompatible.

La familiarité avec une famille d'animaux peut agir comme modificateur secondaire, sans remplacer la compétence générale.

## 8. Médecine

La **Médecine** est une compétence distincte de la magie de soin.

Elle progresse avec des actions médicales réellement pertinentes :

- diagnostic / identification ;
- premiers secours ;
- stabilisation ;
- traitement de blessures ;
- préparation ou application de traitements ;
- reconnaissance et traitement de maladies.
```text
Action furtive réussie / non-détection
    ↓
ProgressionEvent(SuccessfulStealth)
    ↓
ProgressionSystem
    ↓
Discrétion
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

La progression doit favoriser les situations réelles et variées plutôt qu'un soin répété sans nécessité.

### 8.1 Diagnostic
## 8. Anti-abus

Le joueur peut tenter de diagnostiquer lui-même un problème de santé. Une meilleure compétence de Médecine améliore la précision et réduit l'incertitude.

Le diagnostic d'un médecin PNJ reste une voie distincte et peut être plus fiable selon son expertise.

Le jeu ne doit pas révéler automatiquement le nom d'une maladie avant un diagnostic réussi.

## 9. Événements de progression

Les systèmes de gameplay envoient des événements génériques au système de progression :

```text
PhysicalEffort          → Endurance
SuccessfulDodge         → Agilité
BackwardJump            → Agilité
SideStep                → Agilité
Jump                    → Agilité / Endurance selon contexte
ObstacleTraversal       → Agilité / Endurance selon contexte
Climb                   → Agilité / Endurance selon contexte
ControlledLanding       → Agilité
SwimmingMovement        → Endurance / Agilité selon contexte
ReceivedDamage          → Défense
CombatExperience        → Réflexe
MagicUsage(Domain)      → Maîtrise du domaine
TamingAttempt           → Domptage
TamingSuccess           → Domptage
MedicalDiagnosis        → Médecine
MedicalTreatment        → Médecine
DiseaseTreatment        → Médecine
```

Chaque événement doit être validé par des règles anti-farming.

## 10. Anti-abus

Chaque source de progression doit pouvoir définir : contexte requis, fréquence maximale, intensité minimale, rendement décroissant, répétition détectée et récompense uniquement pour une action réellement pertinente.

## 11. Architecture cible
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
├── ControlledLanding
├── Swimming
└── Diving

ProgressionSystem
├── AttributeProgression
│   ├── Endurance
│   ├── Agility
│   └── Defense
├── CombatExperience
│   └── Reflex
│       └── AutomaticDodgeChance
├── DomptageProgression
│   ├── Attempt
│   ├── Success
│   └── Familiarity
├── MedicineProgression
│   ├── Diagnosis
│   ├── Treatment
│   └── DiseaseTreatment
├── PhysicalEffort
│   └── EnduranceCost[*]
├── MagicProgression
│   └── MagicDomainMastery[*]
│   ├── Defense
│   └── Discretion
│
├── MagicProgression
│   └── MagicDomainMastery[*]
│
├── ProgressionEvent
│   ├── PhysicalEffort
│   ├── SuccessfulDodge
│   ├── Jump
│   ├── ReceivedDamage
│   ├── SuccessfulStealth
│   └── MagicUsage(Domain)
│
└── ProgressionRules
    ├── Validation
    ├── AntiAbuse
    └── GainCalculation
```

## 12. Règles
Les valeurs de gain, paliers et formules ne sont pas encore définitifs.

## 10. Règles

1. La progression doit être principalement liée à l'utilisation réelle.
2. Une action doit progresser l'aptitude à laquelle elle correspond.
3. Les systèmes gameplay ne doivent pas modifier directement toutes les statistiques sans passer par une logique de progression cohérente.
4. La roulade, le bond en arrière et le pas de côté sont des mécaniques d'esquive distinctes.
5. Les actions physiques significatives — course, saut, roulade, bond en arrière, pas de côté, franchissement, escalade, nage et plongée — ont un coût d'Endurance data-driven.
6. Une action nécessitant de l'Endurance ne doit normalement pas être exécutée lorsque le coût ne peut pas être payé.
7. Le Réflexe est distinct de l'Agilité.
8. Le Réflexe peut déclencher une esquive automatique avec une probabilité limitée lorsque les conditions sont réunies.
9. Le Réflexe ne déclenche pas automatiquement une parade complète.
10. Les mouvements d'exploration restent contextuels.
11. Domptage et Médecine sont des compétences de progression distinctes.
12. Le diagnostic de maladie n'est pas révélé automatiquement avant une résolution de diagnostic.
13. Les mécanismes anti-farming sont nécessaires et seront équilibrés au prototype.
14. La progression doit être persistante avec le personnage et compatible avec la persistance du monde.
4. L'Esquive est une mécanique de gameplay obligatoire et une source d'Agilité.
5. La Discrétion progresse uniquement via des actions de furtivité réussies et significatives.
6. Les domaines magiques restent extensibles et non figés.
7. Les mécanismes anti-farming sont nécessaires, mais seront équilibrés au prototype.
8. La progression doit être persistante avec le personnage et compatible avec la persistance du monde.
9. Aucun système complet n'est considéré comme implémenté par cette spécification seule.
