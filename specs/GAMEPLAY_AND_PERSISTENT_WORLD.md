# Merge — Gameplay & Persistent World Specification

**Statut** : APPROUVÉ — conception / architecture
**Moteur** : Unreal Engine 5.8.1
**Langage principal** : C++

---

## 1. Objectif

Cette spécification formalise les nouvelles décisions de gameplay concernant le déplacement, la furtivité, le Backstab, l'écologie dynamique et la persistance irréversible du monde.

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

La roulade est une mécanique de gameplay à part entière et non une simple animation. Elle devra pouvoir intégrer ultérieurement :

- direction basée sur l'input ;
- coût d'endurance ;
- fenêtre d'invulnérabilité ;
- restrictions d'actions pendant la roulade ;
- transitions cohérentes avec combat et furtivité.

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
- équipement et compétences futures ;
- état de l'ennemi.

Le système de détection est progressif :

`Calme → Soupçon → Recherche → Alerte → Combat`

Les valeurs exactes seront équilibrées pendant le prototype gameplay.

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

---

## 5. Bestiaire dynamique

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

## 6. Relations prédateur / proie

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

## 7. Extinction locale

Une espèce peut disparaître d'une région.

Une population tombée à zéro ne respawn pas artificiellement.

Une recolonisation n'est possible que si une population source existe ailleurs et qu'un mécanisme de migration / déplacement écologique le permet.

Si aucune population source n'existe, l'espèce reste absente.

---

## 8. Monde non régénératif

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

## 9. Conséquences écologiques en chaîne

Les actions du joueur peuvent produire des effets indirects.

Exemple :

`Hydres ↓ → Sangliers ↑ → végétation ↓ → ressources ↓ → reproduction des Sangliers ↓ / migration`

Les systèmes doivent donc permettre des conséquences émergentes sans nécessiter un script spécifique pour chaque événement.

---

## 10. Simulation abstraite et Actors Unreal

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

## 11. Persistance du monde

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

## 12. Plusieurs mondes

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

## 13. Architecture logicielle cible

La conception doit permettre une séparation claire :

```text
MergeCharacter
├── Movement
│   ├── Standing
│   ├── Crouching
│   ├── Rolling
│   └── Jumping
├── Stealth
│   ├── Visibility
│   ├── Noise
│   ├── Detection
│   └── BackstabEligibility
└── Combat
    ├── Attack
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

Les systèmes fondamentaux devront être développés en C++ et rester suffisamment découplés pour permettre l'exposition de paramètres de gameplay aux outils éditables d'Unreal lorsque pertinent.

---

## 14. Règles de conception

1. Aucun respawn global artificiel ne doit restaurer l'ancien état du monde.
2. Une population simulée n'est pas équivalente à un nombre d'Actors Unreal.
3. Une extinction locale doit être réellement persistante jusqu'à une éventuelle recolonisation naturelle.
4. Les conséquences du joueur doivent pouvoir modifier l'écosystème indirectement.
5. Le Backstab doit dépendre de la furtivité et du positionnement.
6. L'accroupissement doit être intégré au système de furtivité.
7. La roulade doit être un état de gameplay.
8. Les paramètres d'équilibrage ne doivent pas être figés avant le prototype.
9. Aucun système complexe ne doit être implémenté prématurément simplement pour satisfaire cette spécification.

---

## 15. État d'implémentation

| Système | État |
|---|---|
| Troisième personne | Fondation existante |
| Accroupissement | À implémenter |
| Roulade | À implémenter |
| Furtivité | Spécifiée, à prototyper |
| Détection progressive | Spécifiée, à prototyper |
| Backstab | Spécifié, à prototyper |
| Reproduction des espèces | Spécifiée, à architecturer |
| Prédateur / proie | Spécifié, à architecturer |
| Extinction locale | Spécifiée |
| Monde non régénératif | Règle approuvée |
| Persistance du monde | Spécifiée, à architecturer |
| Plusieurs mondes | Spécifié |

**Ce document ne constitue pas une déclaration d'implémentation.**
