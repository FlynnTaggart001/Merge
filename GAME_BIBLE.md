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
À DÉCIDER :
- Taille totale du monde
- Étendue de chaque royaume
- Étendue de la première région jouable

### Régions Principales
- **Royaume de la Fantaisie** : zone de départ probable, majorité humaine, architecture médiévale-fantastique classique.
- **Royaume de la Dark Fantaisie** : peuplé principalement de squelettes, ambiance nécropolitaine, cryptes, ossuaires.
- **Royaume de la Light Fantaisie** : peuplé principalement d’êtres de magie, architecture et environnement saturés de magie pure.

Détails géographiques, biomes et points d’intérêt majeurs : À COMPLÉTER une fois les noms et frontières stabilisés.

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
Territoire principal des humains. Cœur « classique » du monde : villages, fermes, forêts, châteaux. La plupart des humains y vivent. Ambiance médiévale-fantastique standard, contrastée par l’esthétique gothique globale du jeu.

**Gouvernement** : monarchie. Le roi est fainéant et ne pense qu’à ses intérêts personnels. L’élite dirigeante ressemble à celle de notre monde : des incapables qui se foutent du peuple. Le pouvoir sert d’abord ceux qui le détiennent.

**Esclavage** : légal dans le monde des humains.

**Royaume de la Dark Fantaisie**  
Domaine principalement peuplé de squelettes. Architecture d’ossements, nécropoles, cryptes. Ambiance plus sombre et macabre.

**Gouvernement** : monarchie.  
Le roi est un squelette humain de 2m20, coiffé d’une immense couronne d’or. Il est quasiment toujours assis sur son trône, dans une énorme salle du trône constamment emplie de fumée. Main gauche : un haltère (il fait des répétitions). Main droite : une chicha magique qu’il fume.  
Il considère son peuple comme ses potes. Beaucoup moins égoïste que le roi des humains.

**Origine des squelettes** :  
Le roi est le premier des squelettes vivants et le premier des **Nécromentiens**. C’est lui qui a découvert le sort permettant de devenir squelette après la vie humaine. Les squelettes sont principalement d’anciens humains qui se sont transformés grâce à ce sort *avant* leur mort naturelle.

**Royaume de la Light Fantaisie**  
Territoire dominé par des êtres de magie. Magie pure, créatures éthérées, environnement saturé d’énergie magique. Ambiance plus étrange et lumineuse, en contraste avec le gothique dominant.

**Gouvernement** : conscience collective. Seul le gouvernement forme cette conscience unifiée. Le peuple appartient à la même espèce mais reste indépendant — chaque individu a sa propre volonté. La conscience collective gouverne, elle ne fusionne pas la population.

### Factions et Pouvoirs

#### Royaume de la Fantaisie (humains)
- **Forme** : Monarchie
- **Roi** : fainéant, intérêts personnels uniquement
- **Élite** : incompétente, indifférente au peuple
- **Conséquence** : le pouvoir sert d’abord ceux qui le détiennent
- **Esclavage** : légal

#### Royaume de la Dark Fantaisie (squelettes)
- **Forme** : Monarchie
- **Roi** : squelette humain 2m20, couronne d’or, haltère + chicha magique, salle du trône enfumée
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
- Vend de la **poudre d’os** (drogue)
- Vend des **squelettes esclaves**
- L’esclavage est légal chez les humains

#### Quartier squelette (Royaume de la Dark Fantaisie)
- Vend des **goûts magiques** pour chicha magique
- Organise des **jeux d’argent**

**Relation** : rivalité ouverte, rixes fréquentes entre les deux quartiers.

Noms des quartiers et localisation précise : À DÉCIDER.

### Squelettes des égouts (Royaume de la Fantaisie)
- Présents dans les égouts du royaume des humains
- Tiennent un **casino illégal**
- Bande de **voleurs compétents**
- Lien éventuel avec le quartier squelette de Dark Fantaisie : À DÉCIDER

### Cultures et Civilisations

#### Les Squelettes / Nécromentiens
- Principalement d’anciens humains transformés par le sort du roi *avant* leur mort naturelle
- Le roi est le premier d’entre eux
- Culture encore à détailler (traditions, rapports aux humains, etc.)

#### Les Gork
- Équivalent des orcs, appelés **Gork** dans le jeu
- Vivent en **tribus séparées**
- Très hostiles aux humains
- Localisation, culture détaillée, rapports aux autres espèces : À COMPLÉTER

#### Les Êtres de Magie (Light Fantaisie)
- **Apparence** : silhouettes lumineuses
- **Couleur du corps** : change selon leur pouvoir dans la société
- **Aura** : glow autour d’eux, indique leur état mental
- Individus indépendants (seule la conscience collective gouverne)

À COMPLÉTER pour les humains.

### Faune notable

#### Sangliers laineux
- Élevés en agriculture par les humains (nourriture, vêtements, etc.)
- Peu de troupeaux sauvages en dehors du Royaume de la Fantaisie
- Ont peur des hommes, des squelettes et des Gork (leurs prédateurs)

### Personnages Importants

#### Sylva the Wise Tree
- **Apparence** : un arbre comme les autres, à quelques exceptions près. Sur son tronc : une paire d’yeux de bois et une bouche de bois (il parle).
- **Personnalité** : très intelligent, très sage — comme un philosophe.
- **Capacités** : utilise la magie.
- **Rôle** : personnage important (conseiller, source de savoir, quêtes possibles — à préciser).
- **Localisation** : À DÉCIDER.

---

## 07. Personnage Joueur

### 07.1 Attributs

À DÉCIDER :
- Liste des attributs (Force, Endurance, Intelligence, Sagesse, Agilité, Charisme, etc.)
- Valeurs min/max
- Impact sur les compétences
- Formules de calcul

### 07.2 Compétences

À COMPLÉTER :
- Liste complète des compétences
- Catégories de compétences
- Progression de chaque compétence
- Effet du niveau de compétence sur les performances

### 07.3 Progression

- **Système** : Learning by doing (pas de niveaux fixes)
- **Mécanique** : Utilisation d’une compétence → progression de cette compétence
- **Plafonné** : Oui, chaque compétence a un maximum
- **Réinitialisation** : À DÉCIDER (possible ou pas)

### 07.4 États

À COMPLÉTER :
- États de base (faim, fatigue, santé mentale, etc.)
- États temporaires (poison, bénédiction, malédiction, etc.)
- Impact sur le gameplay
- Mécaniques de guérison

---

## 08. Combat

### Système de Base
- **Type** : Combat temps réel (pas de tour par tour)
- **Perspective** : Vue à la troisième personne
- **Contrôle** : Libre et direct

### Méchaniques Offensives
- Attaques légères
- Attaques lourdes (coûtent plus d’endurance)
- Combinaisons d’attaques
- Visée libre possible
- Différents types de dégâts (tranchant, contondant, perçant, magie)

### Méchaniques Défensives
- Esquive (dodge) avec timing
- Parade (block) avec arme/bouclier
- Roulement d’esquive
- Durabilité du blocage

### Calcul des Dégâts
À DÉCIDER :
- Formule exacte
- Rôle des attributs
- Rôle de l’arme
- Rôle de l’armure
- Critique et précision

### Statut de Combat
- Détection des ennemis
- Aggression et fuite
- Regroupement d’ennemis
- IA basique (À COMPLÉTER en détail)

---

## 09. Magie

### Écoles de Magie
À COMPLÉTER :
- Nombre d’écoles
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
- Découverte par expérimentation
- Progression : maîtrise → sort plus puissant ou moins coûteux

### Lancer de Sorts
À COMPLÉTER :
- Temps de lancer
- Interruption possible
- Portée
- Rayon d’effet
- Effets spéciaux (knockback, stun, etc.)

### Effets Magiques
À COMPLÉTER :
- Dégâts élémentaires
- Buffs et débuffs
- Transmutation
- Restauration
- Autres effets

---

## 10. Équipement

### Slots d’Équipement
- Tête (casque, couronne, bandeau)
- Torse (armure lourde, légère, robe)
- Mains (gants, mitaines)
- Jambes (chausses, armure de jambes)
- Pieds (bottes, sabots)
- Mains droite/gauche (armes, baguettes, boucliers)
- Accessoires (anneaux, amulettes)

### Armes
À COMPLÉTER :
- Types d’armes (épées, haches, bâtons, arcs, etc.)
- Statistiques (dégâts, poids, portée, vitesse)
- Effets spéciaux (enchantements)
- Durabilité et réparation

### Armures
À COMPLÉTER :
- Types d’armures (plate, cuir, tissu, etc.)
- Statistiques (protection, poids, mobilité)
- Ensemble d’armures cohérents
- Effets visuels distinctifs

### Durabilité
À DÉCIDER :
- Système de durabilité activé
- Réparation possible
- Coût de réparation
- Dégradation progressive

---

## 11. Inventaire

### Système de Poids
- **Actif** : Oui
- **Limite de poids** : À DÉCIDER
- **Impact surcharge** : Mobilité réduite, fatigue accrue
- **Conséquences** : Limitation stratégique des ressources portées

### Gestion des Objets
- Tri par catégorie
- Recherche et filtrage
- Droppable/vendable
- Limite de nombre de certains objets (potions, etc.) : À DÉCIDER

### Types d’Objets
- Armes
- Armures
- Consommables (potions, nourriture)
- Matériaux de craft
- Livres et parchemins
- Clés et objets spéciaux
- Trésors et objets de quête

---

## 12. Alchimie

À COMPLÉTER :
- Système de création de potions
- Ingrédients disponibles
- Recettes
- Effets des potions
- Durée des effets
- Complications possibles (explosion, poison accidentel, etc.)

---

## 13. PNJ & IA

### Types de PNJ
- Civils inoffensifs
- Marchands
- Maîtres de compétences
- Prêtres/Mages
- Gardes/soldats
- Criminels
- Ennemis

### Routines
- Horaires quotidiens (À COMPLÉTER)
- Lieux fréquentés
- Activités typiques
- Variation selon cycle jour/nuit

### Interaction
- Dialogue simple ou arborescent
- Services (achat, vente, entraînement)
- Quêtes
- Réaction aux actions du joueur

### IA Ennemis
À COMPLÉTER :
- Comportement basique (patrouille, attaque)
- Tactiques en combat
- Fuite / poursuite
- Regroupement et communication

---

## 14. Factions

### Nombre de Factions
À DÉCIDER

### Structure des Factions
À COMPLÉTER :
- Noms des factions
- Idéologies
- Zones de contrôle
- Chefs de faction
- Membres notables
- Quartiers généraux

### Relations Inter-Factions
À COMPLÉTER :
- Alliances
- Rivalités
- Guerres
- Négociations

---

## 15. Réputation

### Système de Réputation
- **Type** : Par faction
- **Plage** : À DÉCIDER (0-100, -100 à +100, etc.)
- **Influences** : Accès aux quêtes, prix commerciaux, réactions PNJ, lieux accessibles

### Gain/Perte de Réputation
À COMPLÉTER :
- Actions générant de la réputation
- Quêtes de faction
- Crimes et conséquences
- Rédemption possible

### Seuils de Réputation
À DÉCIDER :
- Points de basculement majeurs
- Conséquences à chaque seuil
- Ennemis / Alliés permanents

---

## 16. Quêtes

### Types de Quêtes
- Quêtes principales (storyline)
- Quêtes de faction
- Quêtes secondaires (side quests)
- Quêtes dynamiques (générées ou contextuelles)
- Quêtes cachées / optionnelles

### Structure des Quêtes
À COMPLÉTER :
- Objectifs clairs
- Marqueurs et tracking
- Récompenses variables
- Conséquences narratives
- Branches et choix alternatifs

### Journal de Quêtes
- Enregistrement automatique
- Notes manuscrites du joueur : À DÉCIDER
- Historique complet
- Quêtes échouées/abandonnées

---

## 17. Dialogue

### Système de Dialogue
- **Type** : Arborescent (branches multiples)
- **Perspective** : Texte ou voix : À DÉCIDER
- **Longueur** : Variable, du court au long

### Options de Dialogue
À COMPLÉTER :
- Ton neutre / agressif / charmant
- Choix basés sur les attributs
- Choix basés sur la réputation
- Choix basés sur les compétences
- Bluff et persuasion

### Conséquences
- Dialogue affecte quêtes
- Dialogue affecte réputation
- Dialogue affecte relations PNJ
- Dialogue affecte fin du jeu : À DÉCIDER

---

## 18. Monde Vivant

### Cycle Jour/Nuit
- **Longueur** : À DÉCIDER (temps de jeu)
- **Jour** : Luminosité normale, activité PNJ maximale
- **Nuit** : Luminosité réduite (brouillard, shadows), PNJ dorment
- **Transitions** : Aube et crépuscule
- **Impact** : Ennemi différents, quêtes disponibles, dangerosité

### Météo
À COMPLÉTER :
- Types de météo
- Durée des changements
- Impact visuel
- Impact gameplay (glissade, visibilité, etc.)
- Impact sur PNJ

### Événements Dynamiques
À COMPLÉTER :
- Apparition d’ennemis
- Catastrophes naturelles
- Événements de faction
- Événements contextuels
- Festivals ou célébrations

### Cycles Saisonniers
À DÉCIDER :
- Variation saisonnière
- Changement visuel
- Changement de contenu
- Durée des saisons

---

## 19. Exploration

### Récompenses d’Exploration
- Trésors cachés
- Raccourcis secrets
- Ennemis redoutables isolés
- Lore découvert
- Zones cachées

### Marqueurs et Indices
À DÉCIDER :
- Système de marqueur (pins, notes)
- Indices contextuels
- Journal d’exploration
- Cartes trouvables

### Danger et Progression
- Zones dangereuses accessibles tôt (avec risque)
- Progression organique en difficulté
- Pas de barrière invisible arbitraire
- Challenge scaling optionnel : À DÉCIDER

---

## 20. Économie

### Monnaie
À DÉCIDER :
- Nom de la devise
- Sources de revenus
- Coûts typiques

### Commerce
- Achat/Vente auprès des marchands
- Prix dynamiques selon réputation : À DÉCIDER
- Négociation possible : À DÉCIDER
- Vol possible : À DÉCIDER

### Économie du Monde
À COMPLÉTER :
- Coûts de base (nourriture, auberge, équipement)
- Salaires des PNJ
- Coûts de services
- Économie dynamique ou statique

---

## 21. Mort & Sauvegarde

### Mort du Joueur
À DÉCIDER :
- Mode : Respawn simple ou conséquences
- Lieu de respawn : À domicile ou dernière auberge
- Perte d’équipement : Oui/Non/Partiel
- Perte d’argent : Oui/Non/Partiel
- Conséquences narratives : À DÉCIDER

### Sauvegarde
- **Type** : Sauvegarde manuelle / auto-save / hybride : À DÉCIDER
- **Slots** : Nombre de sauvegardes : À DÉCIDER
- **Quicksave** : Oui/Non : À DÉCIDER
- **Permadeath** : Mode optionnel : À DÉCIDER

---

## 22. Interface

### Menus Principaux
À COMPLÉTER :
- Menu de démarrage
- Paramètres
- Galerie / Cinématiques

### HUD en Jeu
À COMPLÉTER :
- Barre de vie
- Ressource magique
- Objective tracker
- Minimap ou compas
- Interactifs contextuels

### Sous-Menus
- Inventaire
- Équipement
- Quêtes
- Carte
- Journal
- Compétences/Attributs
- Magie

### Accessibilité
À DÉCIDER :
- Taille du texte adjustable
- Couleurs contrastées
- Sous-titres
- Options de difficulté

---

## 23. Audio

### Musique
À COMPLÉTER :
- Thèmes régionaux
- Musiques de combat
- Musiques d’exploration
- Musiques ambiantes
- Thèmes de faction

### Effets Sonores
À COMPLÉTER :
- Bruits d’ambiance (vent, animaux, eau)
- Bruits d’action (armes, pas, armure)
- Bruits de magie
- Bruits d’interface

### Voix
À DÉCIDER :
- Voix complète ou partielle
- Langues supportées
- Accents régionaux : À DÉCIDER

---

## 24. Caméra

### Perspective
- Vue à la troisième personne
- Position basse et rapprochée du personnage
- Dynamique et réactive

### Comportement
- Suit le personnage naturellement
- Collision simple (évite les murs)
- Zoom avant dans les espacements étroits
- Permet la vue panoramique : À DÉCIDER

### Inspiration
- Caméra PS1 / MediEvil
- Système simple mais efficace
- Pas de complexité inutile moderne
- Priorité à la clarté et à la lisibilité

---

## 25. Architecture Technique

### Moteur
CHOISI : Unreal Engine 5.8.1

### Langage de Programmation
À DÉCIDER (dépend du moteur)

### Infrastructure
À COMPLÉTER :
- Structure du code
- Systèmes modulaires
- Dépendances
- Pipeline de développement

### Streaming et Chargement
À DÉCIDER :
- Chargement de zones
- Streaming en temps réel
- Écrans de chargement

---

## 26. Performance

### Cibles de Performance
À DÉCIDER :
- Résolution cible
- FPS cible (30, 60, 120+)
- Plateforme cible
- Limitations matérielles

### Optimisation
À COMPLÉTER :
- LOD (Level of Detail)
- Culling et frustum
- Texture compression
- Polygon budgets

### Tests de Performance
À DÉCIDER :
- Profiling régulier
- Seuils acceptables
- Gestion des pics

---

## 27. Contraintes PS1

### Limitations Volontaires

**Visuellement** :
- Résolution basse de texture
- Nombre de polygones limité par scène
- Pas de shaders avancés
- Éclairage vertex-lit uniquement
- Brouillard de distance court
- Pas de ray-tracing ou technique moderne

**Techniquement** :
- Pas de physique ultra-réaliste
- IA simple et prévisible
- Pas de streaming infini
- Mémoire limitée simulée

**Narrativement** :
- Aucune limitation (histoire riche et profonde acceptée)

**Ludiquement** :
- Aucune limitation (gameplay peut être complexe)

### Justification
Ces contraintes sont des **choix artistiques** qui créent l’ambiance rétro intentionnelle du jeu.

---

## 28. MVP (Minimum Viable Product)

### Objectif du MVP
Créer un **Vertical Slice** jouable démontrant tous les systèmes essentiels.

### Éléments Requis
- [x] Déplacement du personnage en temps réel
- [ ] Caméra dynamique troisième personne
- [ ] Combat de base (attaque, défense, esquive)
- [ ] Ennemi avec IA simple
- [ ] Armes fonctionnelles
- [ ] Magie basique (2-3 sorts)
- [ ] Inventaire et équipement
- [ ] Compétences et progression
- [ ] PNJ et routines
- [ ] Dialogues simples
- [ ] Une quête du début à la fin
- [ ] Une petite zone explorée (village + forêt)
- [ ] Esthétique PS1 validée
- [ ] Cycle jour/nuit (optionnel mais préféré)

### Durée Estimée
À DÉCIDER

---

## 29. Roadmap

Voir `ROADMAP.md` pour le plan détaillé de développement.

### Phases Majeures
1. **Préproduction** : Vision et planning (EN COURS)
2. **Choix du moteur** : Sélection tech
3. **Prototype technique** : Infra de base
4. **Prototype gameplay** : Mécaniques essentielles
5. **Vertical Slice** : MVP jouable
6. **Première région** : Contenu complet
7. **Expansion du monde** : Régions additionnelles
8. **Contenu** : Quêtes, lore, secrets
9. **Polish** : Affinage et raffinement
10. **Optimisation** : Performance et stabilité
11. **Release** : Lancement final

---

## 30. Règles de Développement

### Principes Généraux
1. **L’esthétique d’abord** : Toute décision technique serve l’esthétique PS1
2. **Cohérence narrative** : Le monde doit être logique et cohérent
3. **Liberté du joueur** : Minimiser les limites invisibles
4. **Ambiance prioritaire** : L’atmosphère dépasse les polygones
5. **Contenu over bling** : Plus de contenu que d’effets visuels modernes

### Collaboration Multi-IA
Voir `AI_RULES.md` pour les responsabilités détaillées.

### Documentation
- Tous les systèmes doivent être documentés
- Changements importants dans CHANGELOG.md
- Décisions justifiées dans le repo

### Source de Vérité
En cas de contradiction :
1. Décision explicite du Game Director
2. GAME_BIBLE.md (ce fichier)
3. specs/ (spécifications détaillées)
4. docs/ (documentation générale)
5. Propositions individuelles des IA

---

**Dernière mise à jour** : 2026-08-24
**Statut** : Phase de préproduction
**Prochaine étape** : Noms des trois royaumes + autres personnages / espèces
