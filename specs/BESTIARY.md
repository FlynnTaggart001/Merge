# BESTIAIRE — Merge

Ce document contient les descriptions et comportements canoniques des animaux et créatures du monde de **Merge**. Les systèmes généraux d'écologie restent définis dans les spécifications de gameplay ; les informations propres aux espèces sont centralisées ici.

> **État du bestiaire : EN COURS — NON TERMINÉ.**
> Les fiches ci-dessous constituent une base de conception. Les valeurs précises de vitesse, reproduction, dégâts, endurance et autres paramètres restent à équilibrer et pourront être ajustées avant l'implémentation dans Unreal Engine.

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
- Son cri **inverse aléatoirement tous les contrôles du joueur**.
- L'inversion concerne aussi bien les déplacements que les contrôles utilisés pour attaquer et toutes les autres actions contrôlées par le joueur.
- La combinaison des contrôles inversés est aléatoire lors de chaque cri.
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

## Phoenix

### Statut
- **Créature unique** : un seul Phoenix existe dans le monde de Merge.
- **Immortel** : il ne peut pas mourir définitivement.
- Il possède néanmoins une **barre de vie** et peut être vaincu temporairement.
- Il ne se reproduit pas et ne pond pas d'œufs.

### Habitat
- Le Phoenix vit au **sommet de l'immense volcan du monde squelette**.
- Son **nid** se trouve au sommet du volcan.
- Le nid est uniquement son lieu de repos et son territoire : **aucun objet récupérable n'y est placé**.

### Comportement
- Le Phoenix est **pacifiste par nature**.
- Il n'attaque pas spontanément le joueur.
- C'est une créature **intelligente** capable d'observer et d'interpréter le comportement du joueur.
- Son comportement peut varier en fonction des **statistiques du joueur**, de ses actions et du contexte de la rencontre.
- Le détail précis de l'influence de chaque caractéristique reste à définir.
- Même lorsqu'il devient défensif, il ne doit pas être considéré comme une créature naturellement hostile.

### Marchandises
Le Phoenix peut **marchander avec le joueur** et vendre certaines marchandises particulières, notamment :
- **Cendre de Phoenix** ;
- **Plume de feu**.

Ces marchandises ne sont pas à récupérer dans son nid.

### Renaissance
- Lorsqu'il est vaincu, le Phoenix entre dans son cycle de renaissance.
- Sa mort apparente n'est donc jamais définitive.
- Les modalités précises de sa renaissance et son impact sur son état restent à détailler.

---

## Léviathan

### Statut
- **Créature unique** : un seul Léviathan existe dans le monde de Merge.
- **Immortel** : il ne peut pas mourir.
- Il possède une **barre de vie**.
- Le joueur peut théoriquement lui infliger des dégâts, mais son immense taille et sa quantité de vie rendent impossible de vider normalement sa barre de vie.

### Taille
- **Longueur : environ 8 km**.
- **Largeur maximale : environ 1 km**.
- Sa taille est telle que le joueur ne peut pratiquement jamais percevoir son corps entier comme celui d'une créature classique.

### Territoire
- Le Léviathan est lié à l'**océan situé à l'est de la carte**.
- Il constitue une **frontière naturelle vivante** du monde.
- Il ne cherche pas à négocier, comprendre ou évaluer les intentions des intrus.

### Comportement
Le Léviathan détruit tout ce qui s'approche trop près de sa frontière, notamment :
- les bateaux ;
- les embarcations ;
- les personnes qui nagent trop près ;
- les créatures ou objets volants qui passent trop près ;
- le joueur ;
- toute autre présence suffisamment proche pour pénétrer dans son territoire.

Son comportement **ne dépend pas des statistiques du joueur**.

### Fonction dans le monde
- Le Léviathan n'est pas un boss classique.
- Il sert à rendre la limite orientale du monde naturelle et crédible.
- Plus le joueur s'approche de son territoire, plus il doit comprendre qu'il entre dans une zone qu'il ne peut pas franchir normalement.
- Sa puissance et son échelle doivent faire comprendre que le joueur fait face à une **force gigantesque du monde**, et non à une créature conçue pour un combat conventionnel.

---

## Spraseed

### Description
Le Spraseed est une créature très frêle et chétive dont la dangerosité repose presque entièrement sur sa vitesse et sa maîtrise de l'espace. Sa faible résistance physique le rend très facile à faire chanceler ou projeter dans les airs. Cette apparente faiblesse est toutefois trompeuse : le Spraseed peut exploiter sa propre projection pour se repositionner et contre-attaquer.

### Mobilité et téléportation
- Le Spraseed peut se téléporter lui-même.
- Il peut créer des portails dans l'espace afin de modifier instantanément sa position.
- Ses attaques de base sont très rapides.
- Pendant une attaque, il peut ouvrir un portail et modifier son angle d'attaque en réapparaissant à un autre endroit tout en poursuivant le même mouvement.
- Il peut enchaîner des attaques et des téléportations afin d'attaquer successivement depuis des directions différentes.

### Manipulation de la position du joueur
Le Spraseed peut également créer un portail directement sous le joueur afin de déplacer celui-ci.

Il peut notamment préparer une attaque qui semble devoir manquer sa cible, puis ouvrir au dernier moment un portail sous le joueur et le faire apparaître sur la trajectoire de l'attaque.

### Contre lors d'une projection
Lorsqu'un joueur fait valser ou projette le Spraseed :
1. le Spraseed ouvre un portail devant lui, dans la direction de sa projection ;
2. il ouvre un second portail derrière le joueur ;
3. il traverse le premier portail ;
4. il ressort du second portail derrière le joueur ;
5. il peut immédiatement attaquer depuis cette nouvelle position.

Ainsi, sa fragilité physique ne signifie pas qu'une projection est systématiquement sans danger pour le joueur.

### Renvoi des attaques à distance
Lorsqu'une attaque à distance est dirigée vers le Spraseed, notamment une flèche ou un projectile magique, il peut utiliser un portail pour intercepter l'attaque et la renvoyer vers son lanceur.

Le principe est le suivant :
**joueur → projectile → portail du Spraseed → portail près du joueur → joueur**.

Le Spraseed n'est donc pas simplement capable d'éviter les attaques à distance : il peut transformer l'attaque du joueur en menace contre celui-ci.

### Identité de gameplay
Le Spraseed est un ennemi de harcèlement et de manipulation spatiale. Ses comportements doivent être cohérents et observables afin que le joueur puisse progressivement comprendre son fonctionnement et découvrir lui-même comment l'affronter. Aucune solution spécifique à une classe ou à un style de personnage n'est imposée par cette fiche.

# Faune normale et gothique — base de conception

Cette section constitue la base actuelle pour les **14 animaux normaux et gothiques**. Elle n'est **pas terminée** : les valeurs numériques et certains comportements devront encore être détaillés et équilibrés.

## Loup

- **Régime** : carnivore, chasse principalement en meute.
- **Proies** : cerfs, sangliers laineux et petits animaux.
- **Prédateurs** : aucun prédateur naturel majeur établi à ce stade.
- **Vitesse maximale indicative** : ~55 km/h.
- **Fuite** : endurance moyenne ; peut abandonner une poursuite si elle devient trop longue.
- **Attaques** : morsure, attaques coordonnées en groupe.
- **Comportement** : territorial, peut défendre sa meute et ses petits.
- **Particularité** : privilégie les proies faibles, jeunes ou isolées.

## Renard

- **Régime** : omnivore.
- **Proies** : poulets, rats et petits animaux.
- **Prédateurs** : loups.
- **Vitesse maximale indicative** : ~50 km/h.
- **Fuite** : très rapide et généralement privilégiée face au danger.
- **Attaques** : morsure.
- **Comportement** : solitaire ; évite normalement les humains.
- **Particularité** : peut s'approcher des villages la nuit et voler des poules.

## Cerf

- **Régime** : herbivore.
- **Proies** : aucune.
- **Prédateurs** : loups.
- **Vitesse maximale indicative** : ~60 km/h.
- **Fuite** : très rapide ; fuite immédiate lorsqu'un prédateur est détecté.
- **Attaques** : bois, ruade.
- **Comportement** : peut vivre en troupeaux dont la taille varie selon la saison.
- **Particularité** : les mâles peuvent devenir territoriaux pendant la période de reproduction ; un cerf acculé peut charger.

## Sanglier laineux

- **Régime** : omnivore.
- **Proies / alimentation** : végétaux, racines, fruits et petits animaux.
- **Prédateurs** : loups ; les individus sauvages peuvent également être exposés à d'autres créatures.
- **Vitesse maximale indicative** : ~40 km/h.
- **Fuite** : moyenne ; préfère fuir mais peut charger lorsqu'il est coincé.
- **Attaques** : charge, morsure.
- **Comportement** : les individus sauvages sont méfiants envers les humains, les squelettes et les Gork.
- **Particularité** : une femelle accompagnée de ses petits devient particulièrement agressive.

### Rôle domestique
- Principalement utilisé comme **bétail par les humains**.
- Élevé notamment pour la **nourriture** et le **vêtement / pelage**.
- Quelques troupeaux sauvages existent, mais ils sont minoritaires et se trouvent surtout en dehors des zones fortement occupées par les humains.

## Cheval

- **Régime** : herbivore.
- **Proies** : aucune.
- **Prédateurs** : peut être attaqué par des loups.
- **Vitesse maximale indicative** : ~65 km/h.
- **Fuite** : élevée ; peut fuir en groupe.
- **Attaques** : ruade.
- **Comportement** : normalement calme, mais peut paniquer face à certains prédateurs ou créatures fantastiques.
- **Particularité** : une ruade peut blesser involontairement un individu qui se trouve derrière lui.

## Chèvre

- **Régime** : herbivore.
- **Proies** : aucune.
- **Prédateurs** : loups.
- **Vitesse maximale indicative** : ~30 km/h.
- **Fuite** : élevée.
- **Attaques** : coups de corne.
- **Comportement** : grégaire.
- **Particularité** : peut se déplacer et grimper facilement sur les terrains escarpés.

## Mouton

- **Régime** : herbivore.
- **Proies** : aucune.
- **Prédateurs** : loups.
- **Vitesse maximale indicative** : ~25 km/h.
- **Fuite** : faible individuellement mais fortement influencée par le troupeau.
- **Attaques** : coup de tête.
- **Comportement** : très grégaire.
- **Particularité** : lorsqu'un individu fuit, les autres peuvent avoir tendance à le suivre.

## Bovin

- **Régime** : herbivore.
- **Proies** : aucune.
- **Prédateurs** : peu de prédateurs naturels établis à ce stade.
- **Vitesse maximale indicative** : ~35 km/h.
- **Fuite** : moyenne.
- **Attaques** : charge, coup de tête.
- **Comportement** : généralement calme.
- **Particularité** : un taureau peut devenir territorial ; la charge est puissante mais demande une phase de déclenchement.

## Poulet

- **Régime** : omnivore.
- **Alimentation** : graines, insectes et petites ressources au sol.
- **Prédateurs** : renards, serpents et autres petits prédateurs.
- **Vitesse maximale indicative** : ~15 km/h.
- **Fuite** : très élevée en réaction à une menace ; déplacements parfois imprévisibles.
- **Attaques** : coups de bec.
- **Comportement** : se déplace en groupe et panique facilement.
- **Particularité** : peut se percher pour échapper à certains prédateurs.

## Serpent

- **Régime** : carnivore.
- **Proies** : rats, poulets et petits animaux.
- **Prédateurs** : peut notamment être chassé par la vouivre.
- **Vitesse maximale indicative** : ~10–20 km/h selon l'espèce.
- **Fuite** : élevée ; préfère généralement éviter le combat.
- **Attaques** : morsure, venin pour certaines espèces.
- **Comportement** : peut rester immobile longtemps avant de frapper.
- **Particularité** : attaque principalement lorsqu'il se sent menacé.

## Corbeau

- **Régime** : omnivore et charognard.
- **Alimentation** : charognes, insectes, graines et petites ressources.
- **Prédateurs** : peut être chassé par des créatures plus grandes.
- **Vitesse maximale indicative** : ~50 km/h.
- **Fuite** : très élevée.
- **Attaques** : coups de bec, coups d'ailes.
- **Comportement** : intelligent et opportuniste ; peut suivre les événements attirant de la nourriture.
- **Particularité** : peut voler de petits objets ou de la nourriture.

## Chauve-souris

- **Régime** : principalement insectivore.
- **Proies** : insectes.
- **Prédateurs** : certains serpents et autres prédateurs.
- **Vitesse maximale indicative** : ~30 km/h.
- **Fuite** : très élevée.
- **Attaques** : morsure.
- **Comportement** : principalement nocturne, vit en colonies.
- **Particularité** : utilise l'écholocation.

## Rat

- **Régime** : omnivore.
- **Alimentation** : déchets, graines et petites ressources.
- **Prédateurs** : renards, serpents et autres prédateurs.
- **Vitesse maximale indicative** : ~15 km/h.
- **Fuite** : très élevée.
- **Attaques** : morsure.
- **Comportement** : vit en colonies importantes, notamment dans les villes et les égouts.
- **Particularité** : reproduction rapide ; devient agressif lorsqu'il est acculé.

## Araignée

- **Régime** : carnivore.
- **Proies** : insectes et petits animaux.
- **Prédateurs** : corbeaux, serpents et autres prédateurs selon l'espèce.
- **Vitesse** : très variable selon l'espèce.
- **Fuite** : moyenne.
- **Attaques** : morsure, toile.
- **Comportement** : préfère tendre des toiles plutôt que poursuivre ses proies.
- **Particularité** : certaines espèces peuvent vivre en colonies, d'autres sont solitaires.

---

# Règles générales de la faune

- Les espèces possèdent des comportements propres et ne partagent pas toutes les mêmes cycles.
- Les animaux normaux doivent rester cohérents avec une biologie animale crédible.
- Les populations dépendent des ressources et des prédateurs.
- Les espèces peuvent se reproduire.
- Une population peut disparaître localement.
- Les actions du joueur peuvent avoir des conséquences durables sur les populations.
- Une partie de la simulation peut être effectuée de manière probabiliste hors de la zone active afin de limiter le coût CPU.

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
