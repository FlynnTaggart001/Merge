# Gameplay — Merge

Cette documentation synthétise les mécaniques de gameplay actuellement approuvées. La spécification détaillée et normative se trouve dans `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md`.

## Mouvement

Merge est un Action-RPG à la troisième personne. Le joueur dispose d'un déplacement direct, du saut, de l'accroupissement et d'une roulade/esquive.

La roulade est un état de gameplay et pourra intégrer endurance, invulnérabilité et restrictions d'actions.

## Furtivité

L'accroupissement améliore la furtivité. La détection est progressive et dépend de la posture, vitesse, distance, ligne de vue, luminosité, bruit, terrain, équipement et état de l'ennemi.

États conceptuels :

`Calme → Soupçon → Recherche → Alerte → Combat`

## Backstab

Le Backstab est une action d'assassinat dépendant de la furtivité et du positionnement. Être simplement derrière un ennemi ne suffit pas : distance, angle, état de l'ennemi et détection doivent être compatibles.

## Monde vivant

Le bestiaire utilise des populations simulées. Les espèces peuvent se reproduire et leurs populations sont influencées par la prédation, les ressources, la concurrence, la mortalité, la migration et les actions du joueur.

Une forte réduction d'un prédateur peut donc provoquer une augmentation de ses proies, suivie d'effets secondaires sur les ressources et les autres espèces.

## Conséquences permanentes

Le monde ne se régénère pas artificiellement. Les morts, destructions et ressources définitivement supprimées persistent. Le monde peut néanmoins évoluer naturellement par reproduction, croissance, migration et autres processus écologiques.

## Mondes persistants

Une partie correspond à un monde persistant. Une nouvelle partie doit permettre de créer un nouveau monde sans supprimer les anciens. Le joueur pourra revenir à un monde précédemment sauvegardé et retrouver son état exact.

Pour la conception technique détaillée, voir `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md`.
