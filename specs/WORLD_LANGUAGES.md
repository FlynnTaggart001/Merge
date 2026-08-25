# Merge — Système des langues et communication

## Objectif

Les peuples de **Merge** ne partagent pas nécessairement une langue commune. Chaque peuple possède sa propre langue, liée à son histoire, sa culture et son territoire.

La langue doit être un véritable élément du monde et non simplement un changement cosmétique de texte.

## Principes

- Chaque peuple majeur possède une langue principale.
- Certains individus peuvent connaître plusieurs langues.
- La connaissance d'une langue dépend du personnage, de son origine, de son éducation et de son vécu.
- Les PNJ ne doivent pas automatiquement comprendre le joueur si celui-ci ne parle pas leur langue.
- Les langues peuvent évoluer ou présenter des dialectes selon les régions et tribus.
- Les traductions parfaites ne sont pas garanties : certains termes culturels, noms propres, insultes, expressions ou concepts peuvent rester difficiles à traduire.
- Le joueur peut apprendre progressivement de nouvelles langues.
- La maîtrise d'une langue peut débloquer des dialogues, quêtes, informations, livres, commerces ou interactions spécifiques.

## Langues par peuple

### Humains — Royaume de la Fantaisie

- Langue principale : **à nommer**.
- Variantes/dialectes régionaux : possibles.
- Langue la plus répandue dans les zones humaines.

### Squelettes / Nécromentiens — Royaume de la Dark Fantaisie

- Langue principale : **à nommer**.
- Peut avoir conservé certains éléments de l'ancienne langue humaine en raison de l'origine des Nécromentiens.
- Vocabulaire spécifique lié à la mort, à la transformation et à leur culture.

### Êtres de Magie — Royaume de la Light Fantaisie

- Langue principale : **à nommer**.
- Structure potentiellement très différente des langues humaines et nécromentiennes.
- Certains concepts magiques peuvent ne pas avoir d'équivalent direct dans les autres langues.

### Gork

- Langue principale : **à nommer**.
- Les tribus Gork étant séparées, des dialectes ou variantes tribales peuvent exister.
- Certains Gork peuvent également connaître la langue humaine, notamment ceux ayant eu des contacts avec les humains.

## Apprentissage des langues

L'apprentissage d'une langue ne se fait pas instantanément. Le joueur doit **prendre des cours de linguistique** auprès de personnes capables d'enseigner la langue concernée.

### Cours de linguistique

Les cours constituent le moyen principal et structuré d'apprendre une nouvelle langue.

- Des **professeurs de linguistique** peuvent être trouvés dans différentes villes, royaumes et communautés.
- Un professeur doit lui-même maîtriser la langue qu'il enseigne.
- Les cours peuvent avoir un coût en argent, en ressources ou en temps selon le professeur.
- Certains enseignants peuvent exiger une réputation minimale, une quête préalable ou une relation particulière avec le joueur.
- Les langues rares ou difficiles peuvent nécessiter plusieurs enseignants ou plusieurs étapes d'apprentissage.
- Le joueur peut interrompre une formation puis la reprendre plus tard.
- Les cours ne donnent pas nécessairement une maîtrise parfaite : ils font progresser le niveau de connaissance de la langue.

### Progression linguistique

Chaque langue possède une progression indépendante. Les cours permettent de franchir progressivement plusieurs niveaux :

1. **Incompréhension totale** — aucun mot compris.
2. **Initiation** — mots et expressions très simples compris.
3. **Compréhension partielle** — phrases simples et conversations courtes comprises.
4. **Conversation basique** — possibilité de communiquer dans des situations courantes.
5. **Maîtrise courante** — compréhension et expression normales.
6. **Maîtrise avancée** — compréhension des nuances, expressions, dialectes et concepts complexes.

La progression ne doit pas être purement abstraite : le niveau de langue doit modifier concrètement ce que le joueur comprend et peut faire dans le monde.

### Autres moyens de progresser

Les cours sont le moyen principal, mais l'apprentissage peut être renforcé par :

- conversations répétées avec des locuteurs ;
- immersion dans une communauté ;
- lecture de livres et documents ;
- quêtes et événements impliquant la langue ;
- observation et écoute de conversations ;
- pratique régulière de la langue après les cours.

Ces méthodes peuvent compléter les cours sans les remplacer totalement pour les langues complexes.

## Conséquences gameplay

Une langue inconnue peut provoquer :

- dialogues incompréhensibles ou partiellement compris ;
- informations manquantes ou ambiguës ;
- impossibilité de négocier correctement ;
- mauvaises interprétations ;
- accès limité à certaines quêtes ou factions ;
- réactions différentes des PNJ selon les efforts du joueur pour communiquer.

La maîtrise d'une langue peut au contraire permettre :

- dialogues complets ;
- négociation ;
- lecture de textes ;
- compréhension des traditions locales ;
- accès à des secrets ;
- nouvelles options de résolution de quêtes ;
- meilleure réputation auprès du peuple concerné.

## Traduction et interprétation

Certains PNJ peuvent servir d'interprètes. Un interprète peut toutefois avoir ses propres intérêts et ne pas toujours traduire fidèlement.

Les objets, livres, inscriptions et documents doivent également respecter la langue du peuple qui les a produits.

## Architecture technique prévue

Le système devra être **data-driven** afin de permettre l'ajout de nouvelles langues sans modifier profondément le code.

Chaque langue devra pouvoir définir notamment :

- identifiant unique ;
- peuple(s) associé(s) ;
- dialectes ;
- niveau de maîtrise du personnage ;
- textes/dialogues associés ;
- règles de compréhension partielle ;
- relations avec les autres langues ;
- données nécessaires à l'apprentissage ;
- professeurs et lieux où la langue peut être étudiée ;
- coûts et prérequis des cours ;
- progression associée aux cours et à la pratique.

Le système de dialogue devra pouvoir vérifier la capacité du personnage à comprendre une langue avant de déterminer le texte ou l'option de dialogue présentée.

## À définir ultérieurement

- Noms officiels de toutes les langues.
- Alphabet et systèmes d'écriture.
- Dialectes régionaux et tribaux.
- Niveau de différence entre les langues.
- Liste des professeurs de linguistique.
- Prix, durée et prérequis des cours.
- Effets précis de chaque niveau de maîtrise.
- Langues anciennes ou mortes.
- Langue commune éventuelle utilisée pour faciliter les échanges entre peuples.
- Traitement audio : vrais doublages, sons incompréhensibles, sous-titres, ou combinaison de plusieurs systèmes.
