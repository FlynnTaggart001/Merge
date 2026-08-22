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
- autres actions acrobatiques futures.

Le système d'esquive doit être une véritable mécanique de gameplay :

- direction selon l'input ;
- coût d'Endurance ;
- état d'esquive ;
- fenêtre d'invulnérabilité à équilibrer ;
- verrouillage ou interruption de certaines actions ;
- intégration au combat et à la furtivité.

Une esquive ne doit pas automatiquement donner une progression maximale : la progression doit pouvoir distinguer une utilisation significative d'un spam sans danger.

## 4. Défense

La Défense progresse avec les dégâts réellement subis par le personnage.

Le système devra comptabiliser l'exposition réelle au danger et empêcher les boucles artificielles de progression, par exemple :

- dégâts auto-infligés volontairement ;
- sources triviales répétées ;
- dégâts sans risque ni contexte de combat ;
- exploitation d'un événement répétable.

Les règles exactes de validation et les paliers de progression seront déterminés lors du prototype.

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

Les valeurs de gain, paliers et formules ne sont pas encore définitifs.

## 10. Règles

1. La progression doit être principalement liée à l'utilisation réelle.
2. Une action doit progresser l'aptitude à laquelle elle correspond.
3. Les systèmes gameplay ne doivent pas modifier directement toutes les statistiques sans passer par une logique de progression cohérente.
4. L'Esquive est une mécanique de gameplay obligatoire et une source d'Agilité.
5. La Discrétion progresse uniquement via des actions de furtivité réussies et significatives.
6. Les domaines magiques restent extensibles et non figés.
7. Les mécanismes anti-farming sont nécessaires, mais seront équilibrés au prototype.
8. La progression doit être persistante avec le personnage et compatible avec la persistance du monde.
9. Aucun système complet n'est considéré comme implémenté par cette spécification seule.
