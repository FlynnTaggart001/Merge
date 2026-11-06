# Merge — System Integration Matrix

**Statut** : APPROUVÉ — référence d'intégration
**Engine** : Unreal Engine 5.8.4
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
- **Endurance** : tous les mouvements physiques significatifs peuvent avoir un coût data-driven. Il s'agit d'une ressource de gameplay, pas d'une caractéristique canonique.
- **Compétences** : lorsqu'une action de mouvement correspond à une compétence canonique, elle peut générer une progression validée de cette compétence selon les règles de `SKILL_PROGRESSION.md`.
- **Caractéristiques** : elles ne progressent pas directement à partir du mouvement ; elles progressent automatiquement à partir de la progression validée des compétences liées.
- **Combat** : les mouvements défensifs et fenêtres d'impact utilisent le même pipeline de résolution lorsque pertinent.

## 2. Défense et compétences canoniques

```text
Blocage
Parade
Esquive
Roulade i-frames
Saut arrière
Pas de côté
```

Règles :
- **Blocage** utilise la compétence canonique Blocage lorsque le contexte correspond.
- **Parade** utilise la compétence canonique Parade.
- **Esquive** utilise la compétence canonique Esquive.
- La roulade possède une fenêtre défensive temporelle et peut contribuer à Esquive lorsqu'une progression est validée.
- **Réflexe** est un système défensif automatique, pas une caractéristique ni une compétence. Il peut éviter automatiquement une attaque surprise selon notamment l'Agilité et la Perception du joueur. Sa formule est data-driven et il ne génère aucune progression indépendante.
- Une action défensive ne doit pas créer une source de progression de caractéristique indépendante du pipeline de compétence → caractéristique.

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
└── MedicalSkillProgression

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
- Médecine et magie de soin restent des voies distinctes ;
- la progression de Médecine suit le système canonique des compétences et ses règles de validation.

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
├── Achat auprès d'un éleveur
└── Acquisition naturelle selon les règles propres à l'espèce
```

Le système de montures utilise la compétence canonique **Domptage** pour les situations d'acquisition naturelle compatibles avec l'espèce. L'achat auprès d'un éleveur ne nécessite pas Domptage.

Les montures peuvent également avoir :
- faim ;
- hydratation ;
- repos ;
- blessures ;
- maladies spécifiques ;
- confiance ;
- endurance propre en tant que ressource/paramètre de la monture.

Aucune de ces mécaniques n'ajoute une caractéristique ou une compétence aux **6 caractéristiques / 46 compétences** canoniques du joueur.

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

Endurance et réserve d'air sont deux ressources différentes. Aucune ne constitue une caractéristique canonique supplémentaire.

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
7. l'absence de contradiction avec les systèmes existants ;
8. l'absence d'ajout implicite à la liste canonique des **46 compétences** ou **6 caractéristiques**.
