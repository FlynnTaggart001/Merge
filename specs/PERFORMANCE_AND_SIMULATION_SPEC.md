# Merge — Performance & Simulation Specification

**Statut** : APPROUVÉ — contrainte d'architecture
**Moteur** : Unreal Engine 5.8.1
**Langage principal** : C++20

## 1. Principe fondamental

Merge doit être conçu avec une règle stricte : **ne jamais simuler à pleine précision l'intégralité du monde en permanence**.

Les systèmes du monde utilisent trois niveaux :

```text
MONDE HORS ZONE JOUEUR
        ↓
Probabilités / états agrégés / simulation abstraite
        ↓
ENTRÉE DANS LA ZONE
        ↓
Résolution de l'état courant
        ↓
Simulation locale détaillée
        ↓
SORTIE DE LA ZONE
        ↓
Résultat agrégé dans le WorldState
```

La simulation détaillée est donc déclenchée principalement lorsque le joueur entre dans une zone ou lorsqu'un événement global exige une résolution.

## 2. Simulation probabiliste hors zone

Lorsqu'une région n'est pas active près du joueur, les systèmes suivants ne doivent normalement pas fonctionner comme des simulations temps réel complètes :

- populations animales ;
- reproduction et mortalité ;
- prédateur/proie ;
- IA et routines individuelles ;
- incendies ;
- eau locale ;
- catastrophes naturelles détaillées ;
- lave détaillée ;
- météo locale détaillée ;
- navigation individuelle ;
- physique des objets ;
- effets visuels.

À la place, chaque région conserve un état abstrait et des paramètres permettant d'estimer son évolution.

Exemple :

```text
RegionState
├── PopulationSummary
├── ResourceState
├── WeatherState
├── HazardState
├── EcologicalState
├── FactionState
├── TerrainState
└── LastResolvedTime
```

Le moteur peut appliquer des résultats probabilistes/batchés pour la période écoulée sans exécuter chaque seconde de simulation.

## 3. Résolution à l'entrée d'une zone

Lorsque le joueur approche ou entre dans une région inactive :

```text
ZoneActivated
      ↓
Read RegionState
      ↓
Calculate elapsed time
      ↓
Apply probabilistic / aggregate evolution
      ↓
Resolve current state
      ↓
Spawn / materialize relevant Actors
```

Le résultat doit être cohérent avec les événements précédemment enregistrés : une région ne doit pas simplement revenir à son état initial.

## 4. Simulation locale détaillée

Une zone active proche du joueur peut utiliser une simulation beaucoup plus précise :

```text
Zone active
├── Actors / AI
├── Animations
├── Perception
├── Combat
├── Physics when needed
├── Fire propagation
├── Water interaction
├── Wildlife behavior
├── Local disaster effects
└── Visual effects
```

La précision doit augmenter selon la proximité et la pertinence gameplay, pas selon une règle globale identique partout.

## 5. Niveaux de simulation

Prévoir au minimum :

```text
LOD 0 — Player Critical
→ pleine simulation / gameplay / collision / perception

LOD 1 — Local Active
→ simulation simplifiée, fréquence réduite

LOD 2 — Regional
→ agrégats et événements locaux probabilistes

LOD 3 — Distant / Dormant
→ état statistique minimal
```

Ces niveaux doivent s'appliquer aux systèmes de gameplay, pas seulement au rendu graphique.

## 6. Événements naturels hors zone

Une catastrophe lointaine ne doit pas nécessiter la simulation détaillée de chaque élément qu'elle touche.

Exemple :

```text
Région hors zone
    ↓
Probabilité de feu
    ↓
Résultat régional : 18 % forêt détruite
    ↓
Population herbivore -12 %
    ↓
Migration estimée
    ↓
WorldState mis à jour
```

Quand le joueur entre dans la région, ces résultats deviennent les conditions de départ de la simulation locale détaillée.

Pour les événements majeurs (éruption, séisme important, destruction d'une ville), le système peut enregistrer un événement mondial précis sans simuler tous les objets individuellement.

## 7. Écologie

L'écologie hors zone doit utiliser des populations abstraites et des transitions probabilistes.

Exemple :

```text
2000 sangliers
+ conditions favorables
→ résultat probabiliste après période
→ 2230 sangliers estimés
```

Lors de l'activation d'une zone, seuls les individus réellement nécessaires sont matérialisés en Actors.

## 8. IA

Les PNJ et créatures hors zone active ne doivent pas conserver une IA complète exécutée à chaque frame.

Le système peut résumer leurs activités :

```text
Hunt
Travel
Sleep
Patrol
CombatOutcome
Migration
SocialState
```

À l'activation de la zone, l'état est converti en comportement et position locale cohérents.

## 9. Catastrophes

Les catastrophes naturelles utilisent le même principe :

```text
Hors zone
→ probabilité / progression abstraite

À l'entrée
→ résolution de l'événement
→ matérialisation locale
```

Exemples :

- probabilité de déclenchement d'un séisme ;
- probabilité de réveil volcanique ;
- progression abstraite d'un feu de forêt ;
- estimation d'une zone inondée ;
- résolution d'un glissement de terrain ;
- état régional d'une coulée de lave.

Une fois active, la catastrophe peut devenir une simulation locale détaillée.

## 10. Gestion du temps

Chaque région doit conserver au minimum un `LastResolvedTime`.

Lorsqu'elle est activée :

```text
ElapsedTime = CurrentWorldTime - LastResolvedTime
```

Le système utilise ce temps uniquement pour résoudre les changements pertinents. Il ne rejoue pas seconde par seconde les événements qui se seraient produits hors écran.

## 11. Persistance

Après la simulation locale, le système doit résumer les résultats nécessaires :

```text
LocalSimulation
      ↓
StateAggregator
      ↓
WorldState / RegionState
```

Cela réduit le coût des sauvegardes et évite de conserver des milliers d'états intermédiaires inutiles.

## 12. Performance des Actors

Règles obligatoires :

1. Aucun Actor ne doit posséder un `Tick` permanent sans justification mesurée.
2. Les événements, timers, batches et systèmes centralisés sont préférés lorsque possible.
3. Les AI/perceptions utilisent des fréquences adaptées au niveau de simulation.
4. La physique est activée uniquement quand nécessaire.
5. Les VFX détaillés sont locaux au joueur.
6. Les systèmes de particules et effets massifs doivent avoir des budgets de qualité.
7. Les créatures éloignées restent abstraites.
8. Les objets inactifs doivent être dormants ou non matérialisés lorsque possible.

## 13. World Partition et streaming

Le monde doit être compatible avec World Partition et le streaming de cellules.

Les systèmes de simulation ne doivent pas supposer qu'une cellule non chargée contient des Actors actifs.

Lors du chargement d'une cellule :

```text
Stream In
→ Read persistent regional state
→ Resolve required state
→ Spawn relevant Actors
```

Lors du déchargement :

```text
Collect relevant state
→ Aggregate
→ Save regional state
→ Stream Out
```

## 14. Budgets et profilage

Les budgets définitifs seront mesurés sur le matériel cible, mais le projet doit suivre au minimum :

- FPS cible ;
- frame time CPU ;
- frame time GPU ;
- mémoire RAM ;
- mémoire VRAM ;
- nombre d'Actors actifs ;
- coût IA ;
- coût physique ;
- coût VFX ;
- temps de streaming ;
- taille et temps des sauvegardes.

Les régressions de performance doivent être détectées pendant le développement, pas uniquement avant la sortie.

## 15. Profiling Unreal

Les phases d'optimisation doivent utiliser les outils de profiling d'Unreal appropriés, notamment :

- Unreal Insights ;
- `stat unit` ;
- `stat game` ;
- `stat gpu` ;
- `stat memory` ;
- traces CPU/GPU lorsque nécessaires ;
- profils de streaming ;
- tests de montée en charge.

Les outils exacts seront utilisés selon la version et les besoins du prototype.

## 16. Tests de montée en charge

Prévoir des scénarios de test dédiés :

```text
Test A — population élevée
Test B — grande bataille
Test C — plusieurs PNJ + magie collective
Test D — incendie de forêt
Test E — tempête / pluie torrentielle
Test F — séisme + catastrophe secondaire
Test G — réveil volcanique + lave
Test H — zone avec eau + nage + IA
Test I — chargement/déchargement de régions
Test J — monde ancien fortement modifié
```

Un système n'est pas considéré comme prêt si son cas nominal fonctionne mais qu'il détruit les budgets lors des tests de charge.

## 17. Sauvegardes

Les sauvegardes doivent privilégier l'état persistant et les différences significatives plutôt que des snapshots complets de milliers d'Actors inutiles.

Exemple :

```text
RegionState
├── ChangedObjects
├── PopulationSummary
├── TerrainChanges
├── HazardState
└── EventHistory
```

## 18. Principes non négociables

1. **Pas de simulation détaillée globale permanente.**
2. Hors zone du joueur, privilégier probabilités, agrégats et événements.
3. À l'entrée d'une zone, résoudre l'état puis matérialiser uniquement ce qui est nécessaire.
4. Après sortie, agréger la simulation locale dans le WorldState.
5. Aucun système ne doit imposer un coût par frame global sans justification.
6. Tout système majeur doit disposer d'une stratégie de simulation distante avant son implémentation complète.
7. Les performances doivent être profilées régulièrement sur le matériel cible.
8. L'optimisation ne doit pas être reportée à la fin du projet.
