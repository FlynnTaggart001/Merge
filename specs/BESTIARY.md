# BESTIAIRE — Merge

Ce document contient les descriptions et comportements canoniques des animaux et créatures du monde de **Merge**. Les systèmes généraux d'écologie restent définis dans les spécifications de gameplay ; les informations propres aux espèces sont centralisées ici.

---

## Vouivre

### Description
La vouivre est une grande créature reptilienne volante, rare et mystérieuse. Malgré son apparence imposante, elle n'est pas naturellement agressive envers les êtres qui l'approchent. Elle vit généralement près d'une étendue d'eau isolée et suit un rituel nocturne très particulier.

Son trait le plus remarquable est sa capacité à produire des sifflements capables d'attirer les serpents présents dans les environs. La vouivre ne se contente donc pas d'être un prédateur volant : son environnement peut devenir une partie de sa défense.

### Cycle quotidien
- **Jour** : la vouivre dort dans son repaire.
- **Nuit** : elle sort et se rend à son étendue d'eau pour se baigner.
- Avant d'entrer dans l'eau, elle retire la **pierre précieuse incrustée sur son front** et la dépose à proximité de son lieu de baignade.

### Comportement
- La vouivre n'attaque pas spontanément un individu qui la laisse tranquille.
- Elle attaque si elle est attaquée en premier.
- Elle devient immédiatement hostile si sa pierre précieuse est volée.
- Elle ressent **instantanément** le vol de sa pierre, quelle que soit la distance qui la sépare de celle-ci.
- Dès que la pierre est volée, elle devient **extrêmement brûlante**.
- Si sa pierre est volée pendant sa baignade, elle sort immédiatement de l'eau et poursuit le voleur.

### Sifflement et serpents
La vouivre possède une capacité particulière lui permettant d'appeler les serpents présents dans les environs grâce à des sifflements spécifiques.
- Elle peut attirer les serpents autour de son lieu de baignade.
- Lorsqu'un voleur prend sa pierre, elle appelle les serpents environnants pour l'aider à poursuivre le voleur.
- Les serpents suivent le joueur de très près tant que celui-ci possède la pierre.

### Pierre précieuse
- La pierre est extrêmement précieuse et peut être vendue très cher.
- Elle est normalement portée sur le front de la vouivre.
- La vouivre la dépose volontairement avant chaque baignade nocturne.
- Lorsqu'un joueur possède la pierre dans son inventaire, celle-ci lui inflige des **dégâts de brûlure continus**.
- Les dégâts de brûlure et la poursuite des serpents cessent lorsque le joueur lâche la pierre.

### Particularité de gameplay
La vouivre ne constitue pas nécessairement un combat obligatoire. Le joueur peut observer son rituel nocturne sans l'agresser, ou tenter de voler sa pierre au prix d'une poursuite dangereuse par la vouivre et les serpents qu'elle appelle.

---

## Gargouille

### Description
La gargouille est une créature de pierre extrêmement lourde qui s'intègre directement aux bâtiments sur lesquels elle est installée. Elle ressemble à une statue architecturale tant qu'aucun danger n'est détecté dans son périmètre.

Les gargouilles servent principalement de gardiennes. Leur présence dissuade les agressions et contribue à faire baisser le taux de criminalité dans les endroits où elles sont installées.

### Position et déplacement
- La gargouille est fixée à un bâtiment et reste immobile lorsqu'aucun danger n'est détecté.
- Son poids est trop important pour lui permettre de voler.
- Lorsqu'elle intervient, elle se détache du bâtiment et tombe vers l'initiateur de l'agression.
- Une fois son intervention terminée, elle **grimpe le long du bâtiment** jusqu'à retrouver exactement son emplacement d'origine.
- Elle ne vole jamais, y compris lors de son retour à son emplacement.

### Intervention contre les agressions
La gargouille surveille les agressions qui se produisent dans son périmètre.
- Si le joueur attaque un PNJ, la gargouille considère **le joueur comme l'initiateur** et intervient contre lui.
- Si un PNJ attaque le joueur, elle considère **ce PNJ comme l'initiateur** et intervient contre lui.
- Elle ne prend donc pas automatiquement parti pour le joueur ou pour les PNJ : elle intervient contre celui qui a déclenché l'altercation.

### Chute et onde de choc
Lorsque la gargouille intervient :
- Elle tombe directement sur l'initiateur de l'agression.
- **Les dégâts de l'impact sont infligés uniquement à la personne sur laquelle elle tombe.**
- La chute produit également une **onde de choc** autour du point d'impact.
- L'onde de choc ne sert pas à infliger des dégâts de zone : elle **propulse les personnes présentes autour de la gargouille**.
- Cette propulsion sépare les participants et permet de mettre fin à l'altercation.

### Neutralisation de l'agresseur
La gargouille cherche à arrêter la violence, pas à tuer.
- Elle réduit l'initiateur de l'agression au **minimum de PV possible** sans l'achever.
- Le PNJ agressé prend la fuite, ce qui sépare physiquement les deux protagonistes.
- Si l'agresseur cesse son attaque, la gargouille n'a aucune raison de le tuer.
- Si l'agresseur continue volontairement d'attaquer malgré son état critique et l'intervention de la gargouille, celle-ci peut finalement **le tuer**.

### Rôle dans la société
La gargouille constitue une force de dissuasion locale. Les habitants et les individus susceptibles de commettre des agressions savent qu'une violence déclenchée dans son périmètre peut provoquer son intervention. La présence de gargouilles dans un lieu contribue donc directement à **réduire le taux de criminalité et les agressions** dans la zone qu'elles surveillent.

---

## Basilicoq

### Description
Le basilicoq est une créature mythologique hybride à l'apparence particulièrement étrange. Il possède une **tête de coq**, un **corps reptilien couvert d'écailles**, des **pattes terminées par de puissantes griffes**, une **longue queue reptilienne** et des **ailes membraneuses rappelant celles d'une chauve-souris**.

### Attaques
- **Coups de griffes** : le basilicoq attaque directement ses adversaires avec ses puissantes serres.
- **Flaques de poison** : lorsqu'il poursuit le joueur, il crache du poison derrière lui. Le poison reste au sol sous forme de flaques et inflige des dégâts à ceux qui les traversent.
- Les flaques servent également à **empêcher ou limiter la fuite du joueur**, en réduisant progressivement les trajectoires disponibles.

### Cri du basilicoq
Le cri du basilicoq possède un effet surnaturel particulier :
- Son cri **inverse aléatoirement les contrôles du joueur**.
- L'inversion peut concerner les directions de déplacement, notamment avancer/reculer et gauche/droite.
- La combinaison inversée est aléatoire lors de chaque cri.
- L'effet est temporaire et les contrôles reviennent ensuite à leur fonctionnement normal.
- Le basilicoq peut utiliser son cri plusieurs fois pendant un affrontement.

### Comportement en combat
Le basilicoq utilise ses différentes capacités de manière complémentaire. Il peut poursuivre le joueur en laissant des flaques de poison derrière lui afin de limiter ses possibilités de fuite, puis utiliser son cri pour perturber ses contrôles et provoquer des déplacements involontaires. Il peut ensuite profiter de la confusion pour attaquer avec ses griffes.

---

## Hydre

### Description
L'hydre est une créature monstrueuse massive dont le corps est surmonté de plusieurs têtes. Elle constitue un prédateur extrêmement dangereux, notamment parce que sa force ne dépend pas d'une seule tête : même lorsqu'une partie de la créature est neutralisée, les autres peuvent continuer à attaquer.

### Particularités
- **Plusieurs têtes** capables d'attaquer simultanément.
- **Régénération** : lorsqu'une tête est tranchée, l'hydre peut la faire repousser selon les règles propres à son espèce.
- Créature particulièrement dangereuse lors des combats prolongés.
- Son comportement et son cycle biologique restent spécifiques à l'espèce et suivent les cycles saisonniers généraux du monde.

---

## Sanglier laineux

- Principalement utilisé comme **bétail par les humains**.
- Élevé notamment pour la **nourriture** et le **vêtement / pelage**.
- Quelques troupeaux sauvages existent, mais ils sont minoritaires et se trouvent surtout en dehors des zones fortement occupées par les humains.
- Les populations sauvages sont généralement méfiantes envers les humains, les squelettes et les Gork.
- Leur comportement et leur population suivent les cycles saisonniers propres à leur espèce.

---

## Faune et animaux du monde

Les animaux et créatures de Merge suivent des cycles biologiques propres à leur espèce.

### Saison des amours
La période de reproduction peut modifier :
- les comportements ;
- les déplacements ;
- la territorialité ;
- les rassemblements ;
- la reproduction et les naissances.

### Saison d'hivernage
Selon l'espèce, l'hiver peut entraîner :
- une baisse d'activité ;
- la recherche d'abris ;
- des regroupements ;
- une migration ;
- une hibernation.

Les hydres, les sangliers laineux et les autres espèces disposent d'un cycle saisonnier cohérent avec leur physiologie. Ces cycles peuvent influencer la présence des animaux, les migrations, les naissances, l'agressivité, les ressources disponibles et l'écosystème local.

---

## Règles générales de la faune

- Les espèces possèdent des comportements propres et ne partagent pas toutes les mêmes cycles.
- Les populations dépendent des ressources et des prédateurs.
- Les espèces peuvent se reproduire.
- Une population peut disparaître localement.
- Les actions du joueur peuvent avoir des conséquences durables sur les populations.
- Une partie de la simulation peut être effectuée de manière probabiliste hors de la zone active afin de limiter le coût CPU.
