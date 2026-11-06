# Merge — Targeting & Party / Group Magic Specification

**Statut** : APPROUVÉ — architecture de pré-implémentation
**Engine** : Unreal Engine 5.8.4
**Langage principal** : C++20

## 1. Objectif

Merge possède deux systèmes complémentaires :

1. un système de ciblage intelligent permettant de sélectionner et parcourir les ennemis pertinents autour du joueur ;
2. un système de groupe permettant au joueur de voyager avec des PNJ et de réaliser certaines magies collectives.

Les deux systèmes doivent rester modulaires et communiquer avec le CombatSystem sans lui être fortement couplés.

## 2. TargetingSystem

Le joueur dispose d'un bouton dédié au ciblage.

À l'activation, le système recherche les cibles valides autour du joueur et sélectionne en priorité les ennemis proches et pertinents.

### 2.1 Pipeline de sélection

```text
Target Input
    ↓
TargetDetection
    ↓
TargetValidation
    ├── vivant
    ├── hostile / ciblable
    ├── portée valide
    ├── visibilité / ligne de vue selon règle
    └── état compatible
    ↓
TargetPriority
    ├── distance
    ├── angle par rapport à la caméra / orientation joueur
    ├── menace / pertinence
    └── visibilité
    ↓
CurrentTarget
```

La proximité constitue la priorité principale demandée : une cible proche doit normalement être choisie avant une cible très éloignée, toutes choses égales par ailleurs.

L'angle devant le joueur permet d'éviter qu'un ennemi légèrement plus proche mais situé derrière le joueur soit systématiquement choisi au détriment d'une cible clairement présente devant lui.

### 2.2 Parcours des cibles

Le bouton dédié doit permettre de parcourir les cibles valides.

```text
Cible proche A
    ↓ input
Cible proche B
    ↓ input
Cible moyenne C
    ↓ input
...
    ↓
Cible la plus éloignée encore valide
```

Le système ne doit jamais sélectionner une cible invalide uniquement pour poursuivre le cycle.

Le parcours peut être ordonné par score de priorité plutôt que par distance brute afin de conserver une sélection naturelle devant le joueur.

### 2.3 Validité et changement automatique

La cible actuelle devient invalide si elle est notamment :

- morte ;
- détruite ;
- hors des limites de ciblage ;
- devenue non ciblable ;
- inaccessible selon les règles de visibilité ;
- dans un état excluant le ciblage.

Lorsque la cible actuelle devient invalide, le système doit pouvoir sélectionner automatiquement la meilleure cible restante.

Le système doit aussi permettre au joueur de quitter volontairement le lock-on.

### 2.4 Compatibilité

Le ciblage doit fonctionner avec :

- armes physiques ;
- attaques de mêlée ;
- magie ;
- capacités ;
- esquives et mouvements de combat ;
- PNJ et créatures lorsque le design le permet.

Le TargetingSystem fournit une référence de cible au système consommateur mais ne décide pas des dégâts ni de l'issue du combat.

## 3. Architecture TargetingSystem

```text
TargetingSystem
├── TargetDetection
├── TargetValidation
├── TargetScoring
├── TargetPriority
├── TargetLock
├── TargetCycling
├── TargetLossHandling
└── TargetSettings
```

Les paramètres de portée, angle, poids de distance, poids d'angle, visibilité et nombre maximal de cibles analysées doivent être data-driven.

## 4. PartySystem

Le joueur peut constituer un groupe avec des PNJ compatibles.

Un groupe représente un ensemble de personnages coopérant temporairement ou durablement avec le joueur.

```text
Party
├── Player
├── Member[*]
├── Formation
├── PartyState
├── Commands
└── GroupMagic
```

Les PNJ restent des personnages autonomes : leur IA, leur perception, leurs relations et leur personnalité ne doivent pas être remplacées par une simple logique de suiveur.

### 4.1 Membres

Chaque membre possède notamment :

- identité ;
- état ;
- position ;
- santé ;
- mana / ressources magiques ;
- domaines magiques maîtrisés ;
- niveau de maîtrise ;
- disponibilité pour une magie collective ;
- relation avec le joueur et les autres membres.

La composition du groupe peut dépendre du contexte narratif, des relations, des quêtes, des factions et des choix du joueur.

## 5. Formation et coordination

Le PartySystem doit gérer une formation souple afin que les membres puissent se déplacer avec le joueur sans se bloquer mutuellement.

La formation peut influencer les magies collectives lorsque le sort exige un positionnement précis.

Les commandes de groupe restent extensibles : suivre, attendre, défendre, rejoindre le joueur, se positionner pour un rituel, etc.

## 6. GroupMagicSystem

Certaines magies peuvent nécessiter plusieurs participants.

Un sort collectif ne doit pas être simplement une version plus puissante d'un sort individuel. Il constitue une mécanique de coopération nécessitant coordination et conditions spécifiques.

### 6.1 Participants

Chaque magie collective définit dans ses données :

- nombre minimal de participants ;
- nombre maximal ;
- domaines requis ou compatibles ;
- niveau de maîtrise requis ;
- mana demandé à chaque participant ;
- positionnement requis ;
- durée d'incantation ;
- fenêtre de synchronisation ;
- conditions d'interruption ;
- effets résultants.

### 6.2 Exemple conceptuel

```text
Feu + Vent
    ↓
Magie collective compatible
    ↓
Tempête de flammes
```

```text
Feu + Terre
    ↓
Magma / fusion élémentaire possible
```

```text
Feu + Vent + Terre
    ↓
Rituel majeur possible
```

Les domaines magiques définitifs ne sont pas encore figés. Le système doit donc rester extensible et ne pas coder ces combinaisons directement.

## 7. Synchronisation

Une magie collective peut nécessiter que les participants :

- soient suffisamment proches ;
- soient dans une position compatible ;
- lancent leur composante dans une fenêtre de timing ;
- disposent des ressources nécessaires ;
- restent capables de maintenir leur concentration.

La qualité du résultat peut dépendre de la maîtrise et de la synchronisation.

## 8. Interruption et risque

Un rituel peut être interrompu par :

- dégâts ;
- stagger ;
- mort ou incapacité d'un participant ;
- éloignement ;
- perte de concentration ;
- manque de mana ;
- événement défini par le sort.

L'interruption doit produire un résultat cohérent défini par les données du sort : annulation, effet partiel, perte de ressources, effet instable ou autre conséquence.

Le joueur peut donc être obligé de **protéger ses mages** pendant un rituel au lieu de simplement déclencher une attaque surpuissante.

## 9. Contribution des participants

Chaque participant peut contribuer selon :

```text
Contribution
├── Domaine magique
├── Maîtrise
├── Mana disponible
├── État
├── Affinité / compatibilité
└── Synchronisation
```

La puissance finale ne doit pas être une simple addition de statistiques. Le système doit pouvoir calculer des synergies, incompatibilités et pertes d'efficacité.

## 10. Relation avec le combat

```text
PartySystem
      ↓
GroupMagicSystem
      ↓
CombatSystem
      ↓
Effect / Damage / WorldEvent
```

Le GroupMagicSystem demande au CombatSystem d'appliquer le résultat du sort. Il ne doit pas implémenter directement la résolution des dégâts.

## 11. IA et perception

Les membres du groupe continuent d'utiliser le système commun de perception et d'IA.

```text
Party role
    ↓
AI / Behavior
    ↓
Positioning
    ↓
GroupMagic participation
```

Un PNJ ne doit pas rester immobile artificiellement uniquement parce qu'il participe à un groupe. Le comportement de formation et les rôles doivent être compatibles avec ses priorités propres.

## 12. Sauvegarde

L'état du groupe doit pouvoir être sauvegardé lorsqu'il est pertinent : membres présents, état de relation, position/formation si nécessaire, progression de certaines interactions et état des rituels uniquement lorsqu'un rituel persistant est explicitement prévu.

Les PNJ morts ou disparus dans un monde persistant doivent être traités selon les règles globales de persistance et ne doivent pas réapparaître artificiellement simplement parce qu'ils étaient membres du groupe.

## 13. Tests

Les tests doivent couvrir :

### Targeting
- sélection de la cible proche prioritaire ;
- influence de l'angle ;
- filtrage des cibles invalides ;
- parcours jusqu'à une cible éloignée ;
- perte de cible ;
- mort/destruction de la cible ;
- sortie volontaire du lock ;
- compatibilité mêlée/magie.

### Party / Group Magic
- création et dissolution d'un groupe ;
- recrutement d'un membre compatible ;
- comportement de formation ;
- ressources des participants ;
- conditions de positionnement ;
- synchronisation ;
- interruption ;
- contribution individuelle ;
- combinaison de domaines ;
- résolution du résultat par le CombatSystem ;
- persistance des membres dans le monde.

## 14. Ordre d'intégration Unreal

Les systèmes seront implémentés après les fondations Core, Movement, Combat et AI :

```text
Core
 ↓
Player Movement
 ↓
Combat
 ↓
AI / Perception
 ↓
TargetingSystem
 ↓
PartySystem
 ↓
GroupMagicSystem
```

Le ciblage peut être prototypé avant la magie collective afin de valider rapidement les interactions joueur/cible.
