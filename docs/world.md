# World Systems — Merge

## Principe fondamental

Le monde de Merge est persistant et non régénératif. Le jeu ne restaure pas artificiellement l'état initial d'une région après le passage du temps ou les actions du joueur.

## Écosystème

Les populations animales sont simulées à l'échelle des régions. Chaque espèce possède des caractéristiques de reproduction, mortalité, alimentation, territoire et relations avec les autres espèces.

Les relations prédateur/proie influencent les populations. Les actions du joueur peuvent donc provoquer des cascades écologiques.

## Extinction et recolonisation

Une population locale tombée à zéro est éteinte localement. Elle ne réapparaît pas par respawn artificiel. Une recolonisation ne peut provenir que d'une population source existante et d'un mécanisme de migration compatible.

## Destruction

Les individus tués, PNJ morts, bâtiments détruits et ressources définitivement supprimées conservent leur état dans la sauvegarde du monde.

Le monde peut cependant changer naturellement : les individus survivants peuvent se reproduire et de nouvelles ressources biologiques peuvent apparaître par croissance naturelle. Cela ne restaure pas les objets ou individus précédemment détruits.

## Persistance multi-mondes

Chaque monde possède un état indépendant. Une nouvelle partie crée un nouveau monde sans supprimer les mondes précédents. Le joueur peut sélectionner un monde existant pour continuer son histoire et ses conséquences.

## Performance

La population simulée n'est pas équivalente au nombre d'Actors Unreal. Les régions non chargées peuvent être simulées abstraitement et seules les créatures pertinentes sont matérialisées lorsque nécessaire.

Voir `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md` pour la spécification normative.
