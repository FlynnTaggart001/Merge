# GAME BIBLE - Merge

---

## 01. Vision du Jeu

**Merge** est un action-RPG en vue à la troisième personne dans le style low-poly PS1 des années 1996-1999.

Le jeu fusionne l'exploration libre et l'immersion narrative des The Elder Scrolls (Morrowind, Oblivion, Skyrim) avec l'esthétique gothique et la mécanique des jeux PS1 originaux comme MediEvil.

**Objectif principal** : créer une expérience RPG riche, immersive et explorable dans une esthétique intentionnellement rétro et gothique, où chaque système sert l'ambiance générale du monde.

---

## 02. Piliers Fondamentaux

1. **Exploration libre** - Joueur libre de ses choix et de son itinéraire
2. **Immersion narrative** - Monde riche en histoire, lore et secrets
3. **Esthétique rétro intentionnelle** - PS1 low-poly comme choix artistique, pas limitation
4. **Ambiance gothique** - Sombre, mystérieuse, mais avec moments chaleureux
5. **Progression par utilisation** - Learning by doing, sans niveau global artificiel
6. **Conséquences des actions** - Les choix du joueur importent et marquent le monde
7. **Monde vivant** - PNJ avec routines, cycle jour/nuit, météo, événements

---

## 03. Direction Artistique

### Style Visuel Global
- **Époque** : PS1, années 1996-1999
- **Inspiration principale** : MediEvil
- **Technique** : Low poly avec textures pixelisées
- **Philosophie** : l'esthétique rétro est un choix artistique intentionnel, pas une limitation

### Caractéristiques Techniques
- Silhouettes anguleuses et géométriques
- Textures pixelisées (résolution basse intentionnelle)
- Filtrage nearest-neighbor (pas de lissage bilinéaire)
- Affine texture warping discret
- Vertex jittering discret
- Brouillard de distance marqué (fog limit court)
- Éclairage vertex-lit low-fi (pas de bump mapping moderne)
- Pas d'éclairage dynamique complexe
- Nombre de polygones limité par zone

### Palette de Couleurs
- **Dominante** : palette gothique
- **Couleurs principales** : violets, bleus nuit, ocres et oranges
- **Ambiance générale** : Halloween/gothique permanente
- **Contrastes chauds** : torches, feux et fenêtres éclairées créent des zones chaleureuses
- **Contraste froid/chaud** : base froide + sources chaudes pour ambiance contrastée

### Architecture et Environnement
- Architecture médiévale-fantastique (pas de technologie avancée)
- Villages en bois rustiques avec toits de chaume
- Cimetières et zones sombres
- Cryptes souterraines labyrinthiques
- Églises gothiques
- Forêts sombres et denses
- Ambiance sombre avec touches de chaleur et vie

---

## 04. Direction Sonore

À COMPLÉTER :
- Types de musique (ambiance, combat, exploration, etc.)
- Instruments et style musical (gothique, médiéval, orchestral, etc.)
- Effets sonores (ambiance, actions, feedback)
- Conception sonore immersive

---

## 05. Monde

### Structure générale
Le monde est divisé en **trois grands royaumes** distincts mais interconnectés. Leurs noms officiels ne sont pas encore fixés.

| Royaume (provisoire) | Population principale | Ambiance |
|---|---|---|
| Royaume de la Fantaisie | Humains (majorité) | Fantaisie classique, villages, forêts, châteaux |
| Royaume de la Dark Fantaisie | Squelettes (principalement) | Gothique, nécropole, ossements, cimetières |
| Royaume de la Light Fantaisie | **Kima Vé** (principalement) | Magie pure, lumières, créatures éthérées |

### Échelle et Géographie
- **Surface totale de la carte : 40 km²**
- **Dimension de référence : environ 6,32 × 6,32 km** pour une carte carrée
- Les **40 km² comprennent l'ensemble des trois royaumes** et de leurs zones naturelles.
- La répartition précise de la surface entre les trois royaumes reste à définir.
- La taille de la première région jouable reste à définir.

### Limites naturelles du monde
Les limites extérieures du monde ne sont pas matérialisées par des barrières invisibles ou des murs artificiels.

- **Océan** : une partie des limites extérieures est constituée par un océan vaste et infranchissable dans le cadre du jeu.
- **Montagnes** : les autres limites sont formées par de hautes chaînes de montagnes escarpées et infranchissables.
- Les limites naturelles doivent être intégrées à la géographie et ne doivent pas donner au joueur l'impression d'une limite technique.
- Le joueur peut explorer librement les **40 km² accessibles**.
- Les limites naturelles donnent l'impression que le monde se poursuit au-delà de la zone jouable.

### Régions Principales
- **Royaume de la Fantaisie** : zone de départ probable, majorité humaine, architecture médiévale-fantastique classique.
- **Royaume de la Dark Fantaisie** : peuplé principalement de squelettes, ambiance nécropolitaine, cryptes, ossuaires.
- **Royaume de la Light Fantaisie** : peuplé principalement de **Kima Vé**, architecture et environnement saturés de magie pure.

Détails géographiques, biomes et points d'intérêt majeurs : À COMPLÉTER une fois les noms et frontières stabilisés.

### Connexions et Navigation
- Monde ouvert interconnecté
- Pas de chargement invisible
- Déplacement libre à pied ou via système de transport
- Zones dangereuses / zones sûres
- Frontières entre royaumes : nature encore à définir (passages naturels, portails, zones frontalières hostiles, etc.)

---

## 06. Lore

### Histoire du Monde
À COMPLÉTER :
- Mythologie générale
- Histoire ancienne (origine des trois royaumes)
- Événements récents
- État actuel du monde et relations entre les trois royaumes

### Les Trois Royaumes (base)

**Royaume de la Fantaisie**  
Territoire principal des humains. Cœur « classique » du monde : villages, fermes, forêts, châteaux. La plupart des humains y vivent. Ambiance médiévale-fantastique standard, contrastée par l'esthétique gothique globale du jeu.

**Gouvernement** : monarchie. Le roi est fainéant et ne pense qu'à ses intérêts personnels. L'élite dirigeante ressemble à celle de notre monde : des personnes privilégiant leurs intérêts au détriment du peuple. Le pouvoir sert d'abord ceux qui le détiennent.

**Esclavage** : légal dans le monde des humains.

**Royaume de la Dark Fantaisie**  
Domaine principalement peuplé de squelettes. Architecture d'ossements, nécropoles, cryptes. Ambiance plus sombre et macabre.

**Gouvernement** : monarchie.  
Le roi est un squelette humain de 2m20, coiffé d'une immense couronne d'or. Il est quasiment toujours assis sur son trône, dans une énorme salle du trône constamment emplie de fumée. Main gauche : un haltère (il fait des répétitions). Main droite : une chicha magique qu'il fume.  
Il considère son peuple comme ses potes. Beaucoup moins égoïste que le roi des humains.

**Origine des squelettes** :  
Le roi est le premier des squelettes vivants et le premier des **Nécromentiens**. C'est lui qui a découvert le sort permettant de devenir squelette après la vie humaine. Les squelettes sont principalement d'anciens humains qui se sont transformés grâce à ce sort *avant* leur mort naturelle.

**Royaume de la Light Fantaisie**  
Territoire dominé par les **Kima Vé**. Magie pure, créatures éthérées, environnement saturé d'énergie magique. Ambiance plus étrange et lumineuse, en contraste avec le gothique dominant.

**Gouvernement** : le **Kiyeka** (conscience collective). Seul le gouvernement forme cette conscience unifiée. Le peuple appartient à la même espèce mais reste indépendant — chaque individu a sa propre volonté. Le Kiyeka gouverne, il ne fusionne pas la population.

### Factions et Pouvoirs

#### Royaume de la Fantaisie (humains)
- **Forme** : Monarchie
- **Roi** : fainéant, intérêts personnels uniquement
- **Élite** : privilégie ses intérêts au détriment du peuple
- **Conséquence** : le pouvoir sert d'abord ceux qui le détiennent
- **Esclavage** : légal

#### Royaume de la Dark Fantaisie (squelettes)
- **Forme** : Monarchie
- **Roi** : squelette humain 2m20, couronne d'or, haltère + chicha magique, salle du trône enfumée
- **Attitude** : considère son peuple comme ses potes, peu égoïste
- **Statut** : premier des squelettes vivants, premier des Nécromentiens
- **Lore clé** : a découvert le sort de transformation en squelette (avant mort naturelle)

#### Royaume de la Light Fantaisie (Kima Vé)
- **Forme** : **Kiyeka** (conscience collective, gouvernement uniquement)
- **Peuple** : Kima Vé, individus indépendants
- **Implication** : le Kiyeka agit comme une entité unique, le peuple non

### Quartiers sensibles (rivaux)

Deux quartiers se détestent et se livrent souvent à des rixes.

#### Quartier humain (Royaume de la Fantaisie)
- Vend de la **poudre d'os** (drogue)
- Vend des **squelettes esclaves**
- L'esclavage est légal chez les humains

#### Quartier squelette (Royaume de la Dark Fantaisie)
- Vend des **goûts magiques** pour chicha magique
- Organise des **jeux d'argent**

**Relation** : rivalité ouverte, rixes fréquentes entre les deux quartiers.

Noms des quartiers et localisation précise : À DÉCIDER.

### Squelettes des égouts (Royaume de la Fantaisie)
- Présents dans les égouts du royaume des humains
- Tous sont d'**anciens esclaves en fuite**, partis chercher une vie meilleure
- Incapables de sortir de la ville pour l'instant → ils survivent en **volant** et en gagnant de l'argent comme ils peuvent en attendant une solution
- Tiennent un **casino illégal** et forment une **bande de voleurs compétents**
- Lien avec le quartier squelette de Dark Fantaisie : **pas automatique** — ça dépend de chaque individu

### Religions

Chaque peuple a sa propre religion. Détails encore à développer.

#### Religion des humains (Royaume de la Fantaisie)
- Structure centrée sur des **prophètes**
- **Prophète actuel** : **Hessad**
- Nom de la religion, dogmes, rites, temples : À COMPLÉTER

#### Religion des squelettes / Nécromentiens
À COMPLÉTER

#### Religion des Kima Vé (Light Fantaisie)
À COMPLÉTER

#### Religion des Gork (si distincte)
À COMPLÉTER

### Cultures et Civilisations

#### Les Squelettes / Nécromentiens
- Principalement d'anciens humains transformés par le sort du roi *avant* leur mort naturelle
- Le roi est le premier d'entre eux
- Culture encore à détailler (traditions, rapports aux humains, etc.)

#### Les Gork
- Équivalent des orcs, appelés **Gork** dans le jeu
- Vivent en **tribus séparées**
- Très hostiles aux humains
- Localisation, culture détaillée, rapports aux autres espèces : À COMPLÉTER

#### Les Kima Vé (Light Fantaisie)
- **Apparence** : silhouettes lumineuses
- **Couleur du corps** :
  - Change selon leur pouvoir dans la société pour les individus ordinaires
  - **Dorée** pour les membres du **Kiyeka**
- **Aura (glow)** :
  - Pour les individus ordinaires : indique leur état mental personnel
  - Pour les membres du **Kiyeka** : l’aura reflète **toujours l’état mental du gouvernement** (le Kiyeka)
- Individus indépendants (seul le **Kiyeka** gouverne)

À COMPLÉTER pour les humains.

### Faune notable

#### Sangliers laineux
- Élevés en agriculture par les humains (nourriture, vêtements, etc.)
- Peu de troupeaux sauvages en dehors du Royaume de la Fantaisie
- Ont peur des hommes, des squelettes et des Gork (leurs prédateurs)

### Personnages Importants

#### Sylva the Wise Tree
- **Apparence** : un arbre comme les autres, à quelques exceptions près. Sur son tronc : une paire d'yeux de bois et une bouche de bois (il parle).
- **Personnalité** : très intelligent, très sage — comme un philosophe.
- **Capacités** : utilise la magie.
- **Rôle** : personnage important (conseiller, source de savoir, quêtes possibles — à préciser).
- **Localisation** : À DÉCIDER.

#### Hessad
- **Rôle** : prophète actuel de la religion des humains
- Détails (personnalité, pouvoir, influence politique) : À COMPLÉTER

---

## 07. Personnage Joueur

### 07.1 Caractéristiques

Les six caractéristiques fondamentales de Merge sont :

- **Force**
- **Agilité**
- **Perception**
- **Intelligence**
- **Volonté**
- **Charisme**

La référence numérique actuelle est une échelle **0–20**. Ces caractéristiques ne sont pas réparties manuellement après la création : elles progressent automatiquement à partir de la progression validée des compétences qui leur sont liées.

Relation canonique :

`CharacteristicProgress += SkillProgress × Weight`

Chaque caractéristique possède sa propre réserve de progression et ses seuils. Lorsqu'un seuil est atteint, la caractéristique augmente de +1 et le surplus est conservé.

Les poids, seuils et limites numériques détaillées sont data-driven et ne doivent pas être dupliqués avec des valeurs contradictoires dans d'autres documents.

### 07.2 Compétences

**45 compétences canoniques** regroupées en 7 catégories :

- Combat (9)
- Défense / mouvement (6) — **Parade appartient ici, pas au Combat**
- Furtivité (6)
- Magie (7)
- Connaissances (7)
- Artisanat (6)
- Social / communication (4)

La liste exacte des 45 compétences et leurs caractéristiques liées est définie exclusivement dans `specs/CANONICAL_SKILLS.md`.

### 07.3 Création du personnage

- Les **45 compétences commencent à 5**.
- Le joueur reçoit **30 points de spécialisation**.
- Maximum investi dans une seule compétence : **10 points**.
- Maximum de départ d'une compétence : **15**.
- Ces points servent à spécialiser le profil initial du personnage.

Après la création, le joueur **ne répartit plus manuellement de points de compétence ou de caractéristique**. La progression se fait par le jeu.

### 07.4 Progression

Merge utilise le **Learning by Doing** : une action pertinente et validée fait progresser la compétence concernée. Cette progression validée alimente ensuite automatiquement les caractéristiques liées.

Il n'existe **pas de niveau global de personnage** servant de progression principale.

Pour une action valide, la formule de base actuelle est :

`P = 0.9 × max(0, (D - S + 15) / 50) × 1 / (1 + 0.012 × S) × (0.75 + 0.025 × I)`

avec :
- `P` = progression gagnée par l'action ;
- `D` = difficulté de l'action ;
- `S` = niveau actuel de la compétence ;
- `I` = Intelligence, sur l'échelle canonique 0–20.

La progression doit être validée selon le contexte de l'action. Les actions répétitives réalisées uniquement pour farmer la progression ne donnent pas la progression normale.

Courbe de seuil actuelle de référence :

`XP_required(level) = 100 × level^1.5`

Cette courbe est une **baseline de tuning**, distincte de la formule de progression par action.

**Échelle de maîtrise : le niveau 50 d'une compétence représente déjà une maîtrise extrêmement élevée / surhumaine.** Les difficultés d'action et l'anti-farming doivent préserver cette signification.

### 07.5 Classes et voies

Les classes ne sont pas choisies comme un simple choix arbitraire indépendant de la progression.

- Le profil du personnage est déterminé par la distribution de ses **caractéristiques**.
- Une voie / classe devient disponible lorsque le personnage atteint les caractéristiques et seuils requis pour cette voie.
- Si le personnage n'a pas suffisamment progressé dans les caractéristiques nécessaires, aucune classe correspondante n'est attribuée.
- Lorsque les conditions d'une nouvelle voie sont atteintes, **le joueur est averti et le nom de la classe est révélé**.
- Le joueur peut donc continuer à évoluer avant de satisfaire les conditions d'une classe.
- Le jeu comporte des **classes fondamentales** et une voie **Déité**, qui constitue un cas particulier.
- Les noms et conditions numériques détaillés des classes restent à définir dans une spécification dédiée ; ils ne doivent pas être inventés ici.

### 07.6 États

- Besoins physiologiques progressifs : faim, hydratation, fatigue/sommeil
- Maladies régionales (diagnostic diégétique uniquement)
- États temporaires (poison, blessures, etc.) gérés par le système d'effets data-driven

Détails : `specs/FOOD_MEDICINE_AND_NONMAGICAL_HEALING_SPEC.md` et docs associées.

---

## 08. Combat

### Système de Base
- **Type** : combat temps réel (pas de tour par tour)
- **Perspective** : vue à la troisième personne
- **Contrôle** : libre et direct

### Mécaniques Offensives
- Attaques légères
- Attaques lourdes (coûtent plus d'endurance)
- Combinaisons d'attaques
- Visée libre possible
- Différents types de dégâts (tranchant, contondant, perçant, magie)

### Mécaniques Défensives
- **Esquive** with timing, utilisant la compétence Esquive
- **Parade** with arme/bouclier, utilisant la compétence Parade
- Roulement d'esquive
- Blocage, utilisant la compétence Blocage selon le contexte
- Les coûts d'endurance sont des coûts de gameplay et **ne constituent pas une caractéristique ou une compétence canonique supplémentaire**

### Calcul des Dégâts
À DÉCIDER :
- Formule exacte
- Rôle des caractéristiques
- Rôle de l'arme
- Rôle de l'armure
- Critique et précision

### Statut de Combat
- Détection des ennemis
- Aggression et fuite
- Regroupement d'ennemis
- IA basique (À COMPLÉTER en détail)

---

## 09. Magie

### Écoles de Magie

Les compétences magiques canoniques sont définies dans `specs/CANONICAL_SKILLS.md` :

- Invocation
- Nécromancie
- Contrôle mental
- Magie élémentaire
- Magie physique
- Magie de groupe
- Magie de pacte

Toutes reposent principalement sur la **Volonté**, avec l'**Intelligence** comme caractéristique secondaire. Volonté représente la force mentale, le contrôle et le maintien de la magie ; Intelligence représente la compréhension et l'apprentissage.

### Ressource Magique
À DÉCIDER :
- Mana, Énergie, Essence, ou autre
- Régénération automatique ou non
- Consommation par sort
- Limitations (surcharge, fatigue, etc.)

### Apprentissage des Sorts
- Livres de sorts trouvables
- Entraînement auprès de maîtres
- Pratique et progression par utilisation

### Magie Collective
- Rituels à plusieurs lanceurs
- Formation d'un groupe nécessaire
- Puissance dépendante du nombre de participants
- Synchronisation des lanceurs
- Interruption possible

---

## 10. Furtivité

- Détection basée sur bruit, visibilité et contexte
- Détection progressive
- Indicateurs non intrusifs
- Backstab conditionnel
- Progression via les compétences canoniques de Furtivité, notamment Discrétion et Élimination furtive

---

## 11. IA & PNJ

- PNJ avec routines quotidiennes
- Cycle jour/nuit
- Réactions aux événements
- Fuite / combat / recherche
- Mémoire simplifiée
- Réputation

---

## 12. Monde Vivant

- Météo dynamique
- Événements aléatoires
- Factions réactives
- Écosystème prédateur/proie
- Populations dynamiques
- Migration
- Ressources régionales

---

## 13. Écologie

- Reproduction des créatures
- Population dépendante des ressources et des prédateurs
- Extinction locale possible
- Actions du joueur ayant des conséquences durables
- Simulation probabiliste hors zone pour limiter le coût CPU

---

## 14. Monde Persistant

- Destruction persistante
- PNJ morts définitivement
- Ressources consommées non régénérées artificiellement
- État du monde sauvegardé
