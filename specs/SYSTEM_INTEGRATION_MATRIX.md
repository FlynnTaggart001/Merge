# Merge — System Integration Matrix

**Statut** : APPROUVÉ — référence d'intégration
**Engine** : Unreal Engine 5.8.1
**Langage principal** : C++20

Ce document sert de contrôle de cohérence entre les spécifications de gameplay de Merge. Une règle détaillée reste dans sa spécification spécialisée ; cette matrice indique les dépendances et les contrats entre systèmes.

## 1. Joueur et mouvement

```text
PlayerMovement
├── Walk / Run / Sprint
├── Jump
├── Crouch
├── Roll
├── BackwardJump
├── SideStep
├── ObstacleTraversal
├── ContextualClimb
└── ControlledLanding
```

Connexions :
- Endurance : tous les mouvements physiques significatifs ont un coût data-driven.
- Agilité : mobilité, esquives, saut, franchissement, escalade et réceptions pertinentes peuvent faire progresser l'Agilité.
- Réflexe : influence les automatismes défensifs, mais pas la maîtrise physique de base.
- Combat : mouvements défensifs et fenêtres d'impact utilisent le même pipeline de résolution.

## 2. Défense et Réflexe

```text
Blocage
Parade
Esquive
Roulade i-frames
Saut arrière
Pas de côté
Esquive réflexe
```

Le Réflexe :
- peut déclencher probabilistiquement une esquive automatique ;
- élargit la fenêtre de timing de parade après l'input du joueur ;
- augmente la fenêtre d'i-frames de la roulade ;
- peut être modulé par la familiarité avec des familles d'attaques ;
- ne doit jamais déclencher automatiquement une parade complète ;
- ne doit jamais créer une invulnérabilité permanente.

## 3. Combat et dégâts environnementaux

Tous les dégâts utilisent un `CombatResolver`/`DamageContext` commun lorsque la source est compatible.

Sources prévues :
- attaques physiques ;
- magie ;
- brûlure ;
- chute ;
- noyade ;
- dangers environnementaux ;
- chaleur extrême ;
- autres sources futures.

La roulade utilise une fenêtre défensive temporelle, et non un booléen global d'invincibilité.

## 4. Survie, sommeil et médecine

```text
SurvivalNeeds
├── Hunger
├── Hydration
├── Sleep / Fatigue
└── PhysiologicalCondition

Medicine
├── Diagnosis
├── Treatment
├── Stabilization
└── MedicalProgression

Disease
├── RegionalDiseasePool
├── Exposure
├── Incubation
├── Transmission
├── Symptoms
├── Severity
├── Diagnosis
└── Treatment
```

Règles :
- faim, déshydratation et manque de sommeil produisent des états physiologiques progressifs ;
- les maladies sont dépendantes des conditions régionales ;
- aucune maladie n'est révélée automatiquement par du texte au joueur ;
- diagnostic professionnel par médecin ou autodiagnostic selon la compétence Médecine ;
- un traitement mal adapté peut être inefficace ;
- Médecine et magie de soin restent des voies distinctes.

## 5. Maladies et monde dynamique

Les risques sanitaires peuvent dépendre de :
- climat ;
- humidité ;
- température ;
- qualité de l'eau ;
- marais ;
- faune / vecteurs ;
- végétation ;
- hygiène ;
- densité de population ;
- catastrophes récentes.

Exemple :

```text
Inondation
  ↓
Eau contaminée
  ↓
Risque d'exposition ↑
  ↓
Maladie potentielle
  ↓
Incubation
  ↓
Symptômes
  ↓
Diagnostic
```

## 6. Montures

```text
Acquisition
├── Achat auprès d'un éleveur uniquement
└── Domptage selon compatibilité de l'espèce
```

Le système ne doit pas contenir de catégorie générique de marchand de bêtes.

`Domptage` est une compétence du joueur distincte de :
- Réflexe ;
- Agilité ;
- Maîtrises d'armes ;
- Médecine ;
- magie.

Les montures peuvent également avoir :
- faim ;
- hydratation ;
- repos ;
- blessures ;
- maladies spécifiques ;
- confiance ;
- Endurance propre.

## 7. Ciblage et groupe

```text
TargetingSystem
      ↓
Combat / Magic

PartySystem
      ↓
GroupMagicSystem
      ↓
Combat / Effect / WorldEvent
```

Le ciblage donne priorité aux ennemis proches puis parcourt les cibles valides jusqu'aux plus éloignées, sans ignorer les contraintes d'angle, visibilité et validité.

Les groupes de PNJ conservent leur IA propre. Les magies collectives utilisent la position, la synchronisation, le mana, les maîtrises et les compatibilités des participants.

## 8. Aquatique

```text
ShallowWater
→ Float
→ Swim
→ Dive
→ AirCritical
→ Drowning
```

La flottabilité dépend du personnage et de l'équipement. Une armure lourde peut faire couler le personnage ou rendre la remontée difficile.

Endurance et réserve d'air sont deux ressources différentes.

## 9. Monde naturel

```text
Weather
  ↓
NaturalEvents
  ↓
Propagation / Transformation
  ↓
WorldImpact
```

Événements prévus :
- séisme ;
- tornade ;
- feu de forêt ;
- foudre/tonnerre ;
- pluie torrentielle ;
- inondation ;
- glissement de terrain ;
- éruption volcanique ;
- coulée de lave.

Un séisme compatible peut augmenter la probabilité de réveil d'un volcan sans rendre l'éruption automatique.

Les coulées de lave peuvent suivre le relief, remplir des dépressions/ravins, créer des zones dangereuses et déclencher des incendies.

## 10. Monde en trois grandes régions

Le découpage géographique actuel est une **direction de conception**, pas encore un layout Unreal définitif :

1. **Dark Fantasy** : montagnes, falaises, volcan, ravins et environnement plus dangereux.
2. **Light Fantasy** : grande colline verte d'échelle comparable à la montagne, avec une dépression d'altitude contenant un grand lac ; le relief doit permettre au réseau d'eau de descendre vers l'aval et de provoquer éventuellement des inondations.
3. **Fantasy classique** : forêts, plaines, reliefs, routes, villages et environnements de transition.

Les frontières doivent rester progressives plutôt que parfaitement nettes.

La grande colline et son lac ne sont pas une zone sûre par défaut : débordements, pluies torrentielles, ruissellements, ruptures de berges ou autres événements hydrologiques peuvent créer des zones dangereuses en aval.

## 11. Performance

Tous les systèmes majeurs doivent respecter `PERFORMANCE_AND_SIMULATION_SPEC.md` :

```text
Hors zone joueur
→ probabilité / état régional / agrégat

Entrée zone
→ résolution de l'état
→ matérialisation pertinente

Zone active
→ simulation locale détaillée

Sortie zone
→ agrégation
→ WorldState
```

Aucun système majeur ne doit supposer qu'un monde entier est simulé à pleine précision en permanence.

## 12. Persistance

Les conséquences définitives ne sont pas réinitialisées artificiellement :
- morts ;
- destructions ;
- ressources supprimées ;
- changements de terrain ;
- catastrophes durables ;
- populations déplacées ;
- conséquences de maladies ou pénuries lorsque pertinentes.

Un nouveau monde possède un état indépendant.

## 13. Règle de cohérence

Avant toute nouvelle implémentation système dans Unreal, vérifier :

1. sa spécification spécialisée ;
2. sa place dans cette matrice ;
3. les dépendances `CombatResolver`, `ProgressionSystem`, `WorldState`, `EffectSystem` et `Performance` ;
4. sa stratégie hors zone ;
5. ses conséquences de sauvegarde ;
6. ses tests de montée en charge ;
7. l'absence de contradiction avec les systèmes existants.
