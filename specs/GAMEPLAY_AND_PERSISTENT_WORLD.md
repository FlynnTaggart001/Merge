# Merge — Gameplay & Persistent World Specification

**Statut** : APPROUVÉ — conception / architecture
**Moteur** : Unreal Engine 5.8.4
**Langage principal** : C++20

---

## 1. Objectif

Cette spécification formalise les systèmes de déplacement, furtivité, Backstab, écologie dynamique et persistance du monde.

Les règles de progression du joueur ne sont pas redéfinies ici. Elles sont centralisées dans :

1. `specs/CANONICAL_SKILLS.md`
2. `specs/SKILL_PROGRESSION.md`
3. `specs/CHARACTERISTIC_PROGRESSION.md`
4. `specs/PLAYER_PROGRESSION.md`

Cela évite qu'un système secondaire crée ses propres caractéristiques ou compétences.

Ces systèmes sont spécifiés mais pas encore entièrement implémentés.

---

## 2. Mouvement du joueur

Le joueur évolue en troisième personne.

Les états de mouvement prévus comprennent notamment :

- debout ;
- déplacement ;
- course / sprint ;
- accroupissement ;
- roulade / esquive ;
- saut ;
- saut arrière ;
- pas de côté ;
- franchissement contextuel ;
- escalade contextuelle ;
- réception contrôlée ;
- nage / plongée selon le contexte.

La roulade est une mécanique de gameplay à part entière et non une simple animation. Elle devra intégrer :

- direction basée sur l'input ;
- coût éventuel en Endurance ;
- fenêtre d'invulnérabilité temporaire à équilibrer ;
- restrictions d'actions pendant l'esquive ;
- transitions cohérentes avec combat et furtivité.

La roulade utilise la compétence canonique **Esquive** lorsqu'une action de progression est validée. Elle ne dépend d'aucune caractéristique ou compétence « Réflexe ».

---

## 3. Accroupissement et furtivité

L'accroupissement améliore la furtivité du joueur.

La furtivité n'est pas un booléen. Elle résulte de plusieurs facteurs :

- posture ;
- vitesse de déplacement ;
- distance ;
- ligne de vue ;
- luminosité / environnement ;
- bruit ;
- terrain ;
- équipement ;
- compétence **Discrétion** ;
- état de l'ennemi.

Le système de détection est progressif :

`Calme → Soupçon → Recherche → Alerte → Combat`

La compétence **Discrétion** progresse uniquement à partir d'actions de furtivité pertinentes et validées selon le système canonique.

---

## 4. Backstab

Le Backstab est une action de combat dépendant de la furtivité et du positionnement.

La simple condition « joueur derrière l'ennemi » est insuffisante.

Les conditions prévues comprennent :

- ennemi compatible ;
- distance valide ;
- position arrière valide ;
- angle valide ;
- ennemi non pleinement engagé en combat ;
- joueur non détecté ou dans un état permettant l'assassinat.

L'architecture doit permettre différentes armes, animations, compétences et effets sans coupler le Backstab à un seul type d'ennemi.

Un Backstab réussi peut générer un événement de progression pour **Élimination furtive** ou une autre compétence canonique uniquement si la relation est définie et si la validation de progression l'autorise.

---

## 5. Progression et gameplay

Les actions de gameplay produisent des événements de progression lorsqu'elles correspondent à une compétence canonique.

```text
Action réussie
      ↓
Validation contextuelle
      ↓
Compétence canonique
      ↓
Progression de compétence
      ↓
Caractéristiques liées
```

Il n'existe pas de progression directe de « Endurance », « Défense », « Réflexe » ou d'une autre aptitude non présente dans les 46 compétences / 6 caractéristiques canoniques.

**Endurance** peut être utilisée comme ressource de gameplay pour les efforts physiques, sans être une caractéristique canonique.

**Agilité** ne progresse pas directement parce qu'un mouvement est effectué : elle progresse automatiquement via les compétences liées lorsqu'une progression de compétence validée est générée.

Les règles détaillées sont celles des spécifications canoniques de progression.

---

## 6. Magie

Les domaines magiques progressent par l'utilisation des **sept compétences canoniques de Magie** :

- Invocation ;
- Nécromancie ;
- Contrôle mental ;
- Magie élémentaire ;
- Magie physique ;
- Magie de groupe ;
- Magie de pacte.

Toutes sont liées à **Volonté + Intelligence**, avec Volonté comme caractéristique principale.

Aucun système de progression magique parallèle ne doit être créé.

---

## 7. Bestiaire dynamique

Les espèces possèdent des populations simulées plutôt qu'un nombre fixe d'Actors permanents.

Chaque espèce peut définir notamment :

- taux de reproduction ;
- maturité ;
- durée de vie ;
- besoins alimentaires ;
- capacité du territoire ;
- population minimale / maximale ;
- mobilité ;
- relations écologiques ;
- territoire principal ;
- capacité de migration.

---

## 8. Relations prédateur / proie

Les populations s'influencent mutuellement.

Exemple :

`Prédateurs ↓ → pression de prédation ↓ → proies ↑ → ressources ↓ → reproduction des proies ↓`

Le système ne doit pas utiliser une simple conversion linéaire entre populations.

Il doit prendre en compte autant que possible :

- prédation ;
- reproduction ;
- mortalité naturelle ;
- ressources disponibles ;
- capacité du territoire ;
- concurrence ;
- migration ;
- actions du joueur ;
- saisonnalité et conditions environnementales.

---

## 9. Extinction locale

Une espèce peut disparaître d'une région.

Une population tombée à zéro ne respawn pas artificiellement.

Une recolonisation n'est possible que si une population source existe ailleurs et qu'un mécanisme de migration / déplacement écologique le permet.

Si aucune population source n'existe, l'espèce reste absente.

---

## 10. Monde non régénératif

Règle fondamentale : **le monde ne se réinitialise pas spontanément**.

Les conséquences définitives comprennent notamment :

- PNJ tué : mort persistante ;
- créature tuée : individu définitivement supprimé ;
- bâtiment détruit : destruction persistante ;
- ressource définitivement extraite : pas de respawn artificiel ;
- population exterminée localement : pas de respawn artificiel.

Le monde n'est toutefois pas figé. Il peut évoluer naturellement.

Exemple : un arbre coupé ne revient pas, mais des graines existantes peuvent produire de nouveaux arbres. Un animal tué ne revient pas, mais les survivants peuvent se reproduire.

**Évolution naturelle ≠ restauration de l'état initial.**

---

## 11. Conséquences écologiques en chaîne

Les actions du joueur peuvent produire des effets indirects.

Exemple :

`Prédateurs ↓ → proies ↑ → végétation ↓ → ressources ↓ → reproduction ↓ / migration`

Les systèmes doivent permettre des conséquences émergentes sans nécessiter un script spécifique pour chaque événement.

---

## 12. Simulation abstraite et Actors Unreal

La population simulée est distincte des créatures matérialisées dans le monde.

Exemple :

`Population simulée : 2 000 individus`

ne signifie pas `2 000 Actors Unreal`.

Une région chargée peut ne matérialiser qu'une fraction de la population nécessaire à la présence du joueur.

La simulation écologique doit fonctionner périodiquement, à une granularité adaptée au monde, et ne doit pas être exécutée inutilement à chaque frame.

Architecture conceptuelle :

```text
EcologySystem
├── SpeciesDefinition
├── EcosystemRegion
├── PopulationState
├── PredatorPreyRelationship
├── ResourceState
└── EcosystemSimulation
    ├── Reproduction
    ├── Mortality
    ├── Predation
    ├── Migration
    └── PopulationBalance
```

---

## 13. Persistance du monde

La sauvegarde doit être centrée sur le monde et pas uniquement sur le joueur.

Conceptuellement :

```text
World
├── WorldState
├── EcologyState
├── NPCState
├── QuestState
├── DestructionState
├── ResourceState
└── PlayerState
```

Le chargement doit restaurer les conséquences persistantes du monde.

---

## 14. Plusieurs mondes

Une nouvelle partie ne détruit pas automatiquement les mondes existants.

Le joueur doit pouvoir choisir :

- **Continuer un monde existant** ;
- **Créer un nouveau monde**.

Chaque monde possède son propre état persistant.

Le joueur doit pouvoir revenir dans un ancien monde et retrouver son état antérieur.

---

## 15. Architecture logicielle cible

La progression est découplée des systèmes d'action :

```text
Gameplay System
      ↓
Validated Progression Event
      ↓
ProgressionSystem
      ↓
Canonical Skill
      ↓
CharacteristicProgression
```

Les systèmes de mouvement, combat, furtivité, magie, survie et montures ne doivent pas créer leurs propres compétences ou caractéristiques cachées.

Les systèmes fondamentaux devront être développés en C++ et rester suffisamment découplés pour permettre l'exposition des paramètres de gameplay aux outils data-driven.

---

## 16. Tests prioritaires

Les systèmes critiques doivent être testables indépendamment du rendu 3D :

- validation des événements de progression ;
- progression des compétences canoniques ;
- progression automatique des caractéristiques ;
- anti-farming ;
- détection et furtivité ;
- Backstab ;
- combat ;
- sauvegarde ;
- écologie ;
- persistance ;
- migration ;
- extinction locale ;
- simulation hors zone.

---

## 17. Ce qui reste volontairement ouvert

Les valeurs exactes de combat, furtivité, écologie, migration, reproduction, dégâts, survie, catastrophes et contenu restent data-driven et seront équilibrées pendant les prototypes.

Les conditions exactes des classes fondamentales et de **Déité** restent également à définir dans la spécification dédiée aux classes.

Aucune nouvelle compétence ou caractéristique ne doit être introduite ici sans mise à jour préalable de `specs/CANONICAL_SKILLS.md`.
