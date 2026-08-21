# Gameplay — Merge

Cette documentation synthétise les mécaniques de gameplay actuellement approuvées. Les spécifications détaillées et normatives se trouvent dans `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md`, `specs/PLAYER_PROGRESSION.md` et `specs/GAMEPLAY_SYSTEMS_MASTER_SPEC.md`.

## Mouvement

Merge est un Action-RPG à la troisième personne. Le joueur dispose d'un déplacement direct, du saut, de l'accroupissement, d'une roulade/esquive et d'un **saut arrière**.

La roulade et le saut arrière sont des variantes du même système d'esquive afin de partager les règles de coût d'Endurance, collision, récupération et invulnérabilité lorsqu'elles sont retenues.

## Combat

Le combat physique distingue trois réponses défensives :

- **Blocage** : défense plus permissive qui réduit/absorbe une attaque selon l'équipement et les règles de défense.
- **Parade** : défense active fondée sur une fenêtre de timing précise avant l'impact. Une réussite peut annuler/réduire le coup, déséquilibrer l'attaquant et ouvrir une fenêtre de riposte.
- **Esquive** : évitement spatial via roulade, saut arrière ou autres variantes futures.

La parade n'est pas un simple blocage et n'est pas déclenchée automatiquement par le Réflexe. Les attaques non parables et les paramètres de fenêtre seront définis dans le prototype.

## Progression

La progression est organique et liée à l'utilisation réelle :

- Endurance : course, combat, sauts et efforts physiques ;
- Agilité : esquives, roulades, sauts et mobilité ;
- Défense : dégâts réellement subis ;
- Réflexe : expérience de combat réelle ;
- maîtrise d'arme : utilisation significative de la famille correspondante ;
- magie : utilisation du domaine magique correspondant.

## Réflexe

Le Réflexe est différent de l'Agilité. Il représente les automatismes acquis par l'expérience du combat.

À mesure que le Réflexe augmente, le personnage peut obtenir une chance de déclencher automatiquement une esquive lorsqu'une attaque ennemie est sur le point de le toucher et que les conditions sont réunies.

Cette esquive automatique reste limitée : elle ne garantit pas l'évitement, ne remplace pas l'esquive manuelle et doit respecter l'espace disponible, l'état du personnage, l'Endurance et les règles normales du système d'esquive.

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

Pour la conception technique détaillée, voir `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md`, `specs/PLAYER_PROGRESSION.md` et `specs/GAMEPLAY_SYSTEMS_MASTER_SPEC.md`.
