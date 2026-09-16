# GAME BIBLE - Merge

---

## 01. Vision du Jeu

**Merge** est un action-RPG en vue à la troisième personne dans le style low-poly PS1 des années 1996-1999.

Le jeu fusionne l'exploration libre et l'immersion narrative des The Elder Scrolls (Morrowind, Oblivion, Skyrim) avec l'esthétique gothique et la mécanique des jeux PS1 originaux comme MediEvil.

**Objectif principal** : Créer une expérience RPG riche, immersive et explorable dans une esthétique intentionnellement rétro et gothique, où chaque système sert l'ambiance générale du monde.

---

## 02. Piliers Fondamentaux

1. **Exploration libre** - Joueur libre de ses choix et de son itinéraire
2. **Immersion narrative** - Monde riche en histoire, lore et secrets
3. **Esthétique rétro intentionnelle** - PS1 low-poly comme choix artistique, pas limitation
4. **Ambiance gothique** - Sombre, mystérieuse, mais avec moments chaleureux
5. **Progression par utilisation** - Learning by doing, pas de niveaux artificiels
6. **Conséquences des actions** - Les choix du joueur importent et marquent le monde
7. **Monde vivant** - PNJ avec routines, cycle jour/nuit, météo, événements

---

## 03. Direction Artistique

### Style Visuel Global
- **Époque** : PS1, années 1996-1999
- **Inspiration principale** : MediEvil
- **Technique** : Low poly avec textures pixelisées
- **Philosophie** : L'esthétique rétro est un choix artistique intentionnel, pas une limitation

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
- **Dominante** : Palette gothique
- **Couleurs principales** : Violets, bleus nuit, ocres et oranges
- **Ambiance générale** : Halloween/gothique permanente
- **Contrastes chauds** : Torches, feux et fenêtres éclairées créent des zones chaleureuses
- **Contraste froid/chaud** : Base froide + sources chaudes pour ambiance contrastée

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
| Royaume de la Light Fantaisie | Êtres de magie (principalement) | Magie pure, lumières, créatures éthérées |

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
- **Royaume de la Light Fantaisie** : peuplé principalement d'êtres de magie, architecture et environnement saturés de magie pure.

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

**Gouvernement** : monarchie. Le roi est fainéant et ne pense qu'à ses intérêts personnels. L'élite dirigeante ressemble à celle de notre monde : des incapables qui se foutent du peuple. Le pouvoir sert d'abord ceux qui le détiennent.

**Esclavage** : légal dans le monde des humains.

**Royaume de la Dark Fantaisie**  
Domaine principalement peuplé de squelettes. Architecture d'ossements, nécropoles, cryptes. Ambiance plus sombre et macabre.

**Gouvernement** : monarchie.  
Le roi est un squelette humain de 2m20, coiffé d'une immense couronne d'or. Il est quasiment toujours assis sur son trône, dans une énorme salle du trône constamment emplie de fumée. Main gauche : un haltère (il fait des répétitions). Main droite : une chicha magique qu'il fume.  
Il considère son peuple comme ses potes. Beaucoup moins égoïste que le roi des humains.

**Origine des squelettes** :  
Le roi est le premier des squelettes vivants et le premier des **Nécromentiens**. C'est lui qui a découvert le sort permettant de devenir squelette après la vie humaine. Les squelettes sont principalement d'anciens humains qui se sont transformés grâce à ce sort *avant* leur mort naturelle.

**Royaume de la Light Fantaisie**  
Territoire dominé par des êtres de magie. Magie pure, créatures éthérées, environnement saturé d'énergie magique. Ambiance plus étrange et lumineuse, en contraste avec le gothique dominant.

**Gouvernement** : conscience collective. Seul le gouvernement forme cette conscience unifiée. Le peuple appartient à la même espèce mais reste indépendant — chaque individu a sa propre volonté. La conscience collective gouverne, elle ne fusionne pas la population.

### Factions et Pouvoirs

#### Royaume de la Fantaisie (humains)
- **Forme** : Monarchie
- **Roi** : fainéant, intérêts personnels uniquement
- **Élite** : incompétente, indifférente au peuple
- **Conséquence** : le pouvoir sert d'abord ceux qui le détiennent
- **Esclavage** : légal

#### Royaume de la Dark Fantaisie (squelettes)
- **Forme** : Monarchie
- **Roi** : squelette humain 2m20, couronne d'or, haltère + chicha magique, salle du trône enfumée
- **Attitude** : considère son peuple comme ses potes, peu égoïste
- **Statut** : premier des squelettes vivants, premier des Nécromentiens
- **Lore clé** : a découvert le sort de transformation en squelette (avant mort naturelle)

#### Royaume de la Light Fantaisie
- **Forme** : Conscience collective (gouvernement uniquement)
- **Peuple** : même espèce, individus indépendants
- **Implication** : le gouvernement agit comme une entité unique, le peuple non

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

#### Religion des êtres de magie (Light Fantaisie)
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

#### Les Êtres de Magie (Light Fantaisie)
- **Apparence** : silhouettes lumineuses
- **Couleur du corps** : change selon leur pouvoir dans la société
- **Aura** : glow autour d'eux, indique leur état mental
- Individus indépendants (seule la conscience collective gouverne)

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

Six caractéristiques fondamentales (échelle **0–20**) :

- **Force**
- **Agilité**
- **Perception**
- **Intelligence**
- **Volonté**
- **Charisme**

Elles progressent **automatiquement** à partir des compétences liées. Voir `specs/CHARACTERISTIC_PROGRESSION.md` et `docs/gameplay/CHARACTER_ATTRIBUTES.md`.

### 07.2 Compétences

**45 compétences canoniques** regroupées en 7 catégories :

- Combat (9)
- Défense / mouvement (6) — *Parade appartient ici, pas au Combat*
- Furtivité (6)
- Magie (7)
- Connaissances (7)
- Artisanat (6)
- Social / communication (4)

Liste complète + liens caractéristiques : `specs/CANONICAL_SKILLS.md`.

Création : toutes démarrent à **5**. Le joueur dispose de **30 points de spécialisation** (max 10 sur une seule compétence → max départ 15).

Après la création : plus aucune répartition manuelle.

### 07.3 Progression

- **Système** : Learning by doing (pas de niveaux artificiels)
- **Mécanique** : action pertinente réussie → progression de la compétence → contribution pondérée aux caractéristiques liées
- **Formule de base** (voir baseline 2026-09-16) :
  `P = 0.9 × max(0, (D - S + 15) / 50) × 1 / (1 + 0.012 × S) × (0.75 + 0.025 × I)`
  où `I` = Intelligence (0–20)
- **Échelle** : compétence 50 = déjà niveau superhumain
- **Réinitialisation** : non prévue

Référence : `specs/PROGRESSION_DESIGN_BASELINE_2026-09-16.md`

### 07.4 États

- Besoins physiologiques progressifs : faim, hydratation, fatigue/sommeil
- Maladies régionales (diagnostic diégétique uniquement)
- États temporaires (poison, blessures, etc.) gérés par le système d'effets data-driven

Détails : `specs/FOOD_MEDICINE_AND_NONMAGICAL_HEALING_SPEC.md` et docs associées.

---

## 08. Combat

### Système de Base
- **Type** : Combat temps réel (pas de tour par tour)
- **Perspective** : Vue à la troisième personne
- **Contrôle** : Libre et direct

### Méchaniques Offensives
- Attaques légères
- Attaques lourdes (coûtent plus d'endurance)
- Combinaisons d'attaques
- Visée libre possible
- Différents types de dégâts (tranchant, contondant, perçant, magie)

### Méchaniques Défensives
- Esquive (dodge) avec timing
- Parade (block) avec arme/bouclier
- Roulement d'esquive
- Durabilité du blocage

### Calcul des Dégâts
À DÉCIDER :
- Formule exacte
- Rôle des attributs
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
À COMPLÉTER :
- Nombre d'écoles
- Noms et thèmes
- Sorts de chaque école

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
- État écologique sauvegardé
- Création de nouveaux mondes indépendants
- Possibilité de continuer dans un monde fortement détruit

---

## 15. Survie

- Faim
- Hydratation
- Fatigue
- Sommeil
- Maladies
- Médecine
- Effets environnementaux

---

## 16. Système Aquatique

- Eau peu profonde
- Nage
- Plongée
- Respiration
- Noyade

---

## 17. Catastrophes Naturelles

- Tremblements de terre
- Tornades
- Feux de forêt
- Foudre
- Pluies torrentielles
- Inondations
- Glissements de terrain
- Volcan
- Coulées de lave

---

## 18. Montures

- Acquisition
- Domptage
- Confiance
- Endurance
- Déplacement
- Interactions avec le terrain

---

## 19. Économie

À COMPLÉTER :
- Monnaies par peuple
- Commerce
- Prix
- Ressources
- Contrebande
- Commerce inter-royaumes

---

## 20. Quêtes

- Quêtes à embranchements
- Solutions multiples
- Conséquences persistantes
- Indices environnementaux
- Absence de marqueurs obligatoires
- Cartes achetables pour faciliter la navigation

---

## 21. Direction du Monde

À COMPLÉTER :
- Noms définitifs des trois royaumes
- Répartition géographique des royaumes dans les 40 km²
- Biomes détaillés
- Villes et villages
- Donjons
- Routes
- Points d'intérêt
- Frontières internes

---

## 22. Audio

À COMPLÉTER :
- Musique
- Ambiances
- Bruitages
- Voix
- Sons de créatures
- Sons environnementaux

---

## 23. Technique

- Unreal Engine 5.8.1
- C++20
- Blueprint complémentaire
- World Partition
- Mass Framework selon besoin
- Niagara
- Sauvegarde persistante

---

## 24. Performance

- Streaming World Partition
- Simulation hors zone probabiliste
- Budget CPU/GPU/mémoire
- LOD
- Optimisation IA
- Optimisation VFX

---

## 25. Principes de Design

- Liberté du joueur
- Conséquences durables
- Monde cohérent
- Pas de barrières invisibles
- Navigation naturelle
- Systèmes interconnectés

---

**Dernière mise à jour : 2026-09-16**
