# Gameplay — Merge

Cette documentation synthétise les mécaniques de gameplay actuellement approuvées. Les spécifications détaillées et normatives se trouvent dans `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md`, `specs/PLAYER_PROGRESSION.md` et `specs/GAMEPLAY_SYSTEMS_MASTER_SPEC.md`.

## Mouvement du joueur

Merge est un Action-RPG à la troisième personne. Le joueur dispose de :

- déplacement direct ;
- marche et course/sprint ;
- saut ;
- accroupissement ;
- roulade/esquive ;
- **bond en arrière** ;
- **pas de côté** ;
- **franchissement contextuel d'obstacles** ;
- **escalade contextuelle** ;
- **réception contrôlée après une chute**.

### Bond en arrière

Le bond en arrière est une vraie action de mouvement du joueur, et pas uniquement une variante théorique du système de combat. Il permet de prendre rapidement de la distance avec un ennemi et peut être utilisé comme esquive/mobilité. Il possède ses propres paramètres de déplacement, d'animation, de collision, de récupération et de coût en Endurance.

### Pas de côté

Le pas de côté est une esquive latérale rapide permettant de sortir de la trajectoire d'une attaque ou de repositionner le personnage. Il est distinct de la roulade et du bond en arrière et possède ses propres paramètres de déplacement, animation, récupération et coût en Endurance.

### Franchissement et escalade contextuels

Le personnage peut franchir certains obstacles adaptés à sa morphologie : petits murets, fenêtres basses, rochers, clôtures, troncs, tables et petites corniches lorsque la géométrie et le contexte l'autorisent.

L'escalade reste **contextuelle** : Merge ne doit pas devenir un système de parkour où chaque surface est grimpable sans règle de gameplay. Les surfaces, hauteurs et conditions d'accès seront définies par les données du monde.

### Réception contrôlée

Après une chute modérée, le personnage peut effectuer une réception contrôlée lorsque les conditions sont réunies. L'Agilité peut améliorer la qualité de cette réception, réduire les dégâts ou le déséquilibre dans les limites du système de chute. Les chutes importantes restent dangereuses.

La roulade et le bond en arrière sont des variantes du système d'esquive afin de partager les règles communes de défense, tout en conservant des comportements et animations distincts. Le pas de côté utilise également cette architecture commune sans être une simple copie de la roulade.

La roulade possède une fenêtre temporaire d'invulnérabilité (i-frames). La durée de cette fenêtre progresse avec le Réflexe sans rendre toute la roulade invulnérable. Le bond en arrière et le pas de côté n'héritent pas automatiquement des mêmes i-frames : leurs propriétés défensives seront équilibrées séparément.

## Combat

Le combat physique distingue trois réponses défensives :

- **Blocage** : défense plus permissive qui réduit/absorbe une attaque selon l'équipement et les règles de défense.
- **Parade** : défense active fondée sur une fenêtre de timing précise avant l'impact. Une réussite peut annuler/réduire le coup, déséquilibrer l'attaquant et ouvrir une fenêtre de riposte.
- **Esquive** : évitement spatial via roulade, bond en arrière, pas de côté ou autres variantes futures.

La parade n'est pas un simple blocage et n'est pas déclenchée automatiquement par le Réflexe. Les attaques non parables et les paramètres de fenêtre seront définis dans le prototype.

## Progression

La progression est organique et liée à l'utilisation réelle :

- Endurance : course, combat, sauts, esquives, franchissements et autres efforts physiques ;
- Agilité : esquives, roulades, bonds en arrière, pas de côté, sauts, franchissements, escalade et mobilité ;
- Défense : dégâts réellement subis ;
- Réflexe : expérience de combat réelle ;
- maîtrise d'arme : utilisation significative de la famille correspondante ;
- magie : utilisation du domaine magique correspondant.

## Réflexe

Le Réflexe est différent de l'Agilité. Il représente les automatismes acquis par l'expérience du combat.

À mesure que le Réflexe augmente, le personnage peut obtenir une chance de déclencher automatiquement une esquive lorsqu'une attaque ennemie est sur le point de le toucher et que les conditions sont réunies.

Le Réflexe augmente également la tolérance de timing de la parade et la durée des i-frames de la roulade. La familiarité acquise contre certaines familles d'attaques peut améliorer l'anticipation, sans rendre les attaques inconnues triviales.

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
