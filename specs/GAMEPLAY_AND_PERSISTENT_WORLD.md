# Merge — Gameplay & Persistent World Specification

**Statut** : APPROUVÉ — conception / architecture
**Moteur** : Unreal Engine 5.8.1
**Langage principal** : C++

---

## 1. Objectif

Cette spécification formalise les décisions de gameplay concernant le déplacement, la progression par utilisation, la furtivité, le Backstab, l'écologie dynamique et la persistance irréversible du monde.

Ces systèmes sont **spécifiés mais pas encore entièrement implémentés**. Leur architecture doit être prévue avant leur développement afin d'éviter une refonte ultérieure.

---

## 2. Mouvement du joueur

Le joueur évolue en troisième personne.

Les états de mouvement prévus comprennent :

- Debout
- Déplacement
- Accroupi
- Roulade / esquive
- Saut

La roulade est une mécanique de gameplay à part entière et non une simple animation. Elle devra intégrer :

- direction basée sur l'input ;
- coût d'endurance ;
- fenêtre d'invulnérabilité à équilibrer ;
- restrictions d'actions pendant l'esquive ;
- transitions cohérentes avec combat et furtivité ;
- progression de l'Agilité liée à son utilisation réussie.

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
- équipement et compétences (notamment Discrétion) ;
- état de l'ennemi.

Le système de détection est progressif :

`Calme → Soupçon → Recherche → Alerte → Combat`

Les valeurs exactes seront équilibrées pendant le prototype gameplay.

La compétence **Discrétion** module ces facteurs : plus elle est élevée, plus la visibilité et le bruit du joueur diminuent, et plus la détection progressive est retardée.

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

Un Backstab réussi contribue à la progression de la Discrétion.

---

## 5. Progression par utilisation

Merge utilise une progression organique pour plusieurs aptitudes fondamentales : les compétences progressent principalement parce que le joueur les utilise réellement.

### Endurance

L'Endurance progresse progressivement grâce aux activités physiques du joueur, notamment :

- courir ;
- se battre ;
- sauter ;
- effectuer des efforts physiques répétés.

L'Endurance ne doit pas simplement augmenter parce que le joueur gagne un niveau abstrait. Son évolution doit être liée à l'activité physique réellement effectuée.

### Agilité

L'Agilité progresse progressivement grâce à l'utilisation de mouvements demandant de la mobilité et du timing, notamment :

- esquiver / rouler ;
- sauter ;
- réussir des mouvements d'évitement.

Le système d'esquive est donc une mécanique fondamentale et une source directe de progression de l'Agilité.

### Défense

La Défense progresse progressivement lorsque le joueur subit des dégâts.

L'objectif est de créer une progression cohérente avec l'expérience réelle du personnage face au danger, sans permettre une montée artificielle par des actions sans risque.

Le système devra éviter les abus évidents tels que l'auto-infligement contrôlé de dégâts ou les boucles de farming artificielles.

### Discrétion

La Discrétion progresse avec les actions de furtivité réussies (déplacement non détecté, backstab, infiltration, etc.).

Elle réduit la visibilité, le bruit et la sensibilité à la détection progressive. Voir `specs/PLAYER_PROGRESSION.md` pour le détail.

### Magie

La progression magique est séparée par domaine de magie.

Chaque domaine disposera de sa propre progression et augmentera principalement à force d'utiliser effectivement les capacités appartenant à ce domaine.

Exemple conceptuel :

`Utilisation répétée d'un domaine → maîtrise progressive de ce domaine`

Les domaines de magie sont **encore en cours de définition**. L'architecture doit donc être générique et ne doit pas figer une liste de domaines maintenant.

La progression devra pouvoir supporter plusieurs domaines indépendants sans modifier le code central à chaque ajout d'un nouveau domaine.

### Règle générale

La progression par utilisation doit rester mesurable, équilibrable et persistante. Elle ne doit pas devenir une simple multiplication automatique de statistiques à chaque action.

---

## 6. Relations entre progression et gameplay

Les aptitudes progressives doivent renforcer les comportements qu'elles récompensent.

Exemples :

```text
Course / combat / saut répétés
        ↓
    progression Endurance
        ↓
    meilleure capacité physique
```

```text
Esquives / sauts réussis
        ↓
    progression Agilité
        ↓
    mobilité accrue
```

```text
Dégâts réellement subis
        ↓
    progression Défense
        ↓
    amélioration défensive
```

```text
Actions furtives réussies / non-détection
        ↓
    progression Discrétion
        ↓
    furtivité accrue
```

```text
Utilisation d'un domaine magique
        ↓
    progression de CE domaine
        ↓
    maîtrise accrue
```

Le système doit empêcher une progression incohérente où une action sans rapport ferait progresser une aptitude.

---

## 5. Progression par utilisation

Merge utilise une progression organique pour plusieurs aptitudes fondamentales : les compétences progressent principalement parce que le joueur les utilise réellement.

### Endurance

L'Endurance progresse progressivement grâce aux activités physiques du joueur, notamment :

- courir ;
- se battre ;
- sauter ;
- effectuer des efforts physiques répétés.

L'Endurance ne doit pas simplement augmenter parce que le joueur gagne un niveau abstrait. Son évolution doit être liée à l'activité physique réellement effectuée.

### Agilité

L'Agilité progresse progressivement grâce à l'utilisation de mouvements demandant de la mobilité et du timing, notamment :

- esquiver / rouler ;
- sauter ;
- réussir des mouvements d'évitement.

Le système d'esquive est donc une mécanique fondamentale et une source directe de progression de l'Agilité.

### Défense

La Défense progresse progressivement lorsque le joueur subit des dégâts.

L'objectif est de créer une progression cohérente avec l'expérience réelle du personnage face au danger, sans permettre une montée artificielle par des actions sans risque.

Le système devra éviter les abus évidents tels que l'auto-infligement contrôlé de dégâts ou les boucles de farming artificielles.

### Magie

La progression magique est séparée par domaine de magie.

Chaque domaine disposera de sa propre progression et augmentera principalement à force d'utiliser effectivement les capacités appartenant à ce domaine.

Exemple conceptuel :

`Utilisation répétée d'un domaine → maîtrise progressive de ce domaine`

Les domaines de magie sont **encore en cours de définition**. L'architecture doit donc être générique et ne doit pas figer une liste de domaines maintenant.

La progression devra pouvoir supporter plusieurs domaines indépendants sans modifier le code central à chaque ajout d'un nouveau domaine.

### Règle générale

La progression par utilisation doit rester mesurable, équilibrable et persistante. Elle ne doit pas devenir une simple multiplication automatique de statistiques à chaque action.

---

## 6. Relations entre progression et gameplay

Les aptitudes progressives doivent renforcer les comportements qu'elles récompensent.

Exemples :

```text
Course / combat / saut répétés
        ↓
    progression Endurance
        ↓
    meilleure capacité physique
```

```text
Esquives / sauts réussis
        ↓
    progression Agilité
        ↓
    mobilité accrue
```

```text
Dégâts réellement subis
        ↓
    progression Défense
        ↓
    amélioration défensive
```

```text
Utilisation d'un domaine magique
        ↓
    progression de CE domaine
        ↓
    maîtrise accrue
```

Le système doit empêcher une progression incohérente où une action sans rapport ferait progresser une aptitude.

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
- relations écologiques.

---

## 8. Relations prédateur / proie

Les populations s'influencent mutuellement.

Exemple :

`Hydres → prédation → Sangliers → consommation → Ressources`

Si le joueur élimine une grande partie des Hydres, la pression prédatrice sur les Sangliers diminue. Les Sangliers peuvent alors augmenter jusqu'à ce que d'autres contraintes écologiques deviennent dominantes.

Le système ne doit jamais utiliser une simple conversion linéaire du type « prédateurs -20 % = proies +20 % ».

Il doit prendre en compte autant que possible :

- prédation ;
- reproduction ;
- mortalité naturelle ;
- ressources disponibles ;
- capacité du territoire ;
- concurrence ;
- migration ;
- actions du joueur.

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

`Hydres ↓ → Sangliers ↑ → végétation ↓ → ressources ↓ → reproduction des Sangliers ↓ / migration`

Les systèmes doivent donc permettre des conséquences émergentes sans nécessiter un script spécifique pour chaque événement.

---

## 12. Simulation abstraite et Actors Unreal

La population simulée est distincte des créatures matérialisées dans le monde.

Exemple :

`Population simulée : 2 000 Sangliers`

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

Exemple :

```text
World_001
  état sauvegardé et potentiellement détruit

World_002
  nouveau monde indépendant
```

Chaque monde possède son propre état persistant.

Le joueur doit pouvoir revenir dans un ancien monde et retrouver son état antérieur.

---

## 15. Architecture logicielle cible

La conception doit permettre une séparation claire :

```text
MergeCharacter
├── Movement
│   ├── Standing
│   ├── Crouching
│   ├── Rolling
│   └── Jumping
├── Progression
│   ├── Endurance
│   ├── Agility
│   ├── Defense
│   ├── Discretion
│   └── MagicDomains
├── Stealth
│   ├── Visibility
│   ├── Noise
│   ├── Detection
│   └── BackstabEligibility
└── Combat
    ├── Attack
    ├── Dodge / Roll
    ├── Backstab
    └── Damage

World Systems
├── Persistence
├── Ecology
├── Species
├── Population
├── PredatorPrey
├── Resources
├── Migration
└── Destruction
```

La progression doit être découplée des systèmes d'action afin que les événements de gameplay puissent enregistrer leur utilisation sans que chaque système connaisse les détails internes de progression.

Exemple conceptuel :

```text
Action réussie
    ↓
Progression Event
    ↓
Progression System
    ↓
Aptitude concernée
```

Les systèmes fondamentaux devront être développés en C++ et rester suffisamment découplés pour permettre l'exposition de paramètres de gameplay aux outils éditables d'Unreal lorsque pertinent.

---

## 16. Règles de conception

1. Aucun respawn global artificiel ne doit restaurer l'ancien état du monde.
2. Une population simulée n'est pas équivalente à un nombre d'Actors Unreal.
3. Une extinction locale doit être réellement persistante jusqu'à une éventuelle recolonisation naturelle.
4. Les conséquences du joueur doivent pouvoir modifier l'écosystème indirectement.
5. Le Backstab doit dépendre de la furtivité et du positionnement.
6. L'accroupissement doit être intégré au système de furtivité.
7. La roulade / esquive doit être un état de gameplay et une source de progression de l'Agilité.
8. L'Endurance doit progresser avec les efforts physiques réels : course, combat, saut et activités comparables.
9. La Défense doit progresser avec les dégâts réellement subis, avec des protections contre le farming artificiel.
10. La magie doit progresser indépendamment par domaine, sans figer les domaines avant leur validation.
11. Les paramètres d'équilibrage ne doivent pas être figés avant le prototype.
12. Aucun système complexe ne doit être implémenté prématurément simplement pour satisfaire cette spécification.
10. La Discrétion progresse via les actions de furtivité réussies et module la détection.
11. La magie doit progresser indépendamment par domaine, sans figer les domaines avant leur validation.
12. Les paramètres d'équilibrage ne doivent pas être figés avant le prototype.
13. Aucun système complexe ne doit être implémenté prématurément simplement pour satisfaire cette spécification.

---

## 17. État d'implémentation

| Système | État |
|---|---|
| Troisième personne | Fondation existante |
| Accroupissement | À implémenter |
| Roulade / esquive | À implémenter |
| Furtivité | Spécifiée, à prototyper |
| Détection progressive | Spécifiée, à prototyper |
| Backstab | Spécifié, à prototyper |
| Progression Endurance | Spécifiée, à architecturer |
| Progression Agilité | Spécifiée, à architecturer |
| Progression Défense | Spécifiée, à architecturer |
| Progression Discrétion | Spécifiée, à architecturer |
| Progression par domaines magiques | Spécifiée, domaines à définir |
| Reproduction des espèces | Spécifiée, à architecturer |
| Prédateur / proie | Spécifié, à architecturer |
| Extinction locale | Spécifiée |
| Monde non régénératif | Règle approuvée |
| Persistance du monde | Spécifiée, à architecturer |
| Plusieurs mondes | Spécifié |

**Ce document ne constitue pas une déclaration d'implémentation complète.**
