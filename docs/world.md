# World Systems — Merge

## Principe fondamental

Le monde de Merge est persistant et non régénératif. Le jeu ne restaure pas artificiellement l'état initial d'une région après le passage du temps ou les actions du joueur.

## Écosystème

Les populations animales sont simulées à l'échelle des régions. Chaque espèce possède des caractéristiques de reproduction, mortalité, alimentation, territoire et relations avec les autres espèces.

Les relations prédateur/proie influencent les populations. Les actions du joueur peuvent donc provoquer des cascades écologiques.

## Extinction et recolonisation

Une population locale tombée à zéro est éteinte localement. Elle ne réapparaît pas par respawn artificiel. Une recolonisation ne peut provenir que d'une population source existante et d'un mécanisme de migration compatible.

## Catastrophes naturelles

Le monde peut développer naturellement des phénomènes environnementaux et catastrophes régionales :

- tremblements de terre ;
- tornades ;
- feux de forêt ;
- foudre et orages ;
- pluies torrentielles ;
- inondations et ruissellements ;
- glissements de terrain ;
- autres phénomènes futurs compatibles avec le système.

Ces phénomènes ne sont pas de simples scripts isolés. Ils peuvent émerger de conditions régionales, se propager, interagir entre eux et modifier l'environnement.

Exemple :

```text
Foudre
  ↓
Feu de forêt
  ↓
Végétation détruite
  ↓
Sol fragilisé
  ↓
Pluie torrentielle
  ↓
Glissement de terrain
```

Les catastrophes peuvent également perturber les populations animales, les ressources, les PNJ, les factions, les routes et les quêtes.

## Destruction

Les individus tués, PNJ morts, bâtiments détruits et ressources définitivement supprimées conservent leur état dans la sauvegarde du monde.

Les catastrophes naturelles qui provoquent des modifications durables suivent la même règle : une forêt brûlée, une route ensevelie, un bâtiment détruit ou un terrain modifié ne revient pas magiquement à son état initial.

Le monde peut cependant changer naturellement : les individus survivants peuvent se reproduire et de nouvelles ressources biologiques peuvent apparaître par croissance naturelle. Cela ne restaure pas les objets ou individus précédemment détruits.

## Persistance multi-mondes

Chaque monde possède un état indépendant. Une nouvelle partie crée un nouveau monde sans supprimer les mondes précédents. Le joueur peut sélectionner un monde existant pour continuer son histoire et ses conséquences.

## Performance

La population simulée n'est pas équivalente au nombre d'Actors Unreal. Les catastrophes et phénomènes hors zone active peuvent également être résolus à l'échelle régionale puis matérialisés autour du joueur lorsque nécessaire.

Voir `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md`, `specs/AQUATIC_AND_ENVIRONMENTAL_DAMAGE_SPEC.md` et `specs/NATURAL_DISASTERS_AND_DYNAMIC_ENVIRONMENT_SPEC.md` pour les spécifications détaillées.
