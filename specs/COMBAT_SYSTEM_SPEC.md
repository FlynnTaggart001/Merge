# Merge — Système de combat

**Statut :** BROUILLON À VALIDER  
**Moteur cible :** Unreal Engine 5.8.1  
**Rôle :** spécification de référence du fonctionnement du combat avant implémentation Unreal.

---

## 1. Objectif

Le combat de Merge est un système d'action-RPG en troisième personne fondé sur les compétences, le placement, le timing et les caractéristiques du personnage.

Le système doit rester lisible, réactif et compatible avec le style rétro PS1 du jeu sans transformer le combat en système arcade complexe.

Les règles de ce document décrivent le fonctionnement général. Les valeurs numériques marquées **À VALIDER** sont des propositions de départ et peuvent être modifiées avant implémentation.

---

## 2. Compétences utilisées

Les compétences de combat et de défense sont celles définies dans `specs/CANONICAL_SKILLS.md`.

### Combat

- Épée
- Hache
- Masse
- Lance
- Dague
- Arme à deux mains
- Arc
- Arbalète
- Combat à mains nues

### Défense / mouvement

- Esquive
- Parade
- Blocage
- Acrobatie

**Important :** Parade appartient à Défense / mouvement et non à Combat.

Le combat ne crée aucune compétence supplémentaire non présente dans la liste canonique.

---

## 3. Caractéristiques impliquées

Les six caractéristiques restent les caractéristiques générales de Merge :

- Force
- Agilité
- Perception
- Intelligence
- Volonté
- Charisme

Le calcul initial des compétences reste exclusivement défini par `specs/CANONICAL_SKILLS.md`.

Pendant le combat, les caractéristiques peuvent être utilisées comme modificateurs secondaires lorsque cela est explicitement défini par le système.

Aucune nouvelle formule de progression des caractéristiques n'est créée ici.

---

## 4. Principe d'une attaque

Une attaque suit le pipeline :

`Entrée joueur → validation → sélection de l'action → animation → fenêtre d'impact → détection de cible → résolution → dégâts/effet → récupération`

Une attaque ne doit infliger des dégâts qu'à l'intérieur de sa fenêtre d'impact validée.

Le système doit permettre :

- attaque légère ;
- attaque lourde ;
- attaque chargée si retenue ;
- attaque à distance ;
- attaque furtive ;
- attaques propres à certaines armes.

La liste exacte des attaques disponibles par arme reste à définir avec les données d'armes.

---

## 5. Types d'armes

Les familles d'armes actuellement reconnues par les compétences sont :

| Famille | Compétence |
|---|---|
| Épée | Épée |
| Hache | Hache |
| Masse | Masse |
| Lance | Lance |
| Dague | Dague |
| Arme à deux mains | Arme à deux mains |
| Arc | Arc |
| Arbalète | Arbalète |
| Mains nues | Combat à mains nues |

Une arme possède au minimum :

- identifiant ;
- famille ;
- dégâts de base ;
- portée ;
- vitesse d'attaque ;
- type de dégâts ;
- coût éventuel en endurance ;
- poids éventuel ;
- conditions d'utilisation ;
- paramètres de coups critiques si le système les conserve.

Les armes utilisent des données plutôt que des valeurs codées directement dans le comportement.

---

## 6. Résolution d'une attaque

Chaque attaque crée un contexte de résolution appelé provisoirement `DamageContext`.

Il contient au minimum :

- attaquant ;
- défenseur ;
- arme ou source ;
- compétence utilisée ;
- puissance de l'attaque ;
- type de dégâts ;
- position de l'impact ;
- état de l'attaquant ;
- état du défenseur ;
- informations de critique éventuel ;
- modificateurs actifs.

Pipeline :

`Attack → Hit Detection → Defense Resolution → Damage Resolution → Secondary Effects`

La détection du contact et le calcul des dégâts doivent rester séparés.

---

## 7. Défense

Une attaque reçue est résolue dans cet ordre logique :

1. cible réellement touchée ;
2. défense active de la cible ;
3. éventuelle esquive ;
4. éventuelle parade ;
5. éventuel blocage ;
6. dégâts résiduels ;
7. effets secondaires ;
8. réaction/impact.

L'ordre exact entre esquive, parade et blocage devra être validé pendant le prototype.

---

## 8. Esquive

L'Esquive est une action volontaire du joueur.

Elle dépend principalement de la compétence **Esquive**.

Une esquive réussie doit permettre d'éviter complètement ou partiellement une attaque selon :

- position ;
- timing ;
- portée de l'attaque ;
- direction ;
- fenêtre d'invulnérabilité ;
- compétence d'Esquive.

### i-frames

La roulade possède une courte fenêtre d'invulnérabilité.

**Durée : À VALIDER.**

L'invulnérabilité ne doit pas être permanente pendant toute l'animation.

La compétence Esquive doit influencer la qualité de l'action, mais ne doit pas rendre le joueur automatiquement intouchable.

---

## 9. Parade

La Parade est une action défensive basée sur le timing.

Une parade réussie :

- annule ou réduit les dégâts ;
- produit une réaction d'impact ;
- peut ouvrir une fenêtre de riposte.

Une parade ratée laisse l'attaquant toucher normalement ou selon les règles de récupération de la défense.

La compétence utilisée est **Parade**.

### Riposte

Une parade réussie peut ouvrir une courte fenêtre de riposte.

**Durée de la fenêtre : À VALIDER.**

La riposte utilise la compétence d'arme correspondante.

---

## 10. Blocage

Le Blocage est une défense maintenue ou déclenchée selon l'arme/équipement.

Il réduit les dégâts plutôt que de garantir une annulation complète.

Le résultat dépend notamment :

- de la compétence Blocage ;
- de l'équipement ;
- de la puissance de l'attaque reçue ;
- de la direction de l'attaque.

Un blocage peut provoquer :

- perte d'endurance ;
- recul ;
- stagger ;
- garde brisée.

Les formules exactes sont **À VALIDER**.

---

## 11. Endurance

L'Endurance représente la ressource physique utilisée par certaines actions.

Elle peut être consommée par :

- sprint ;
- roulade ;
- parade selon la règle retenue ;
- blocage selon la règle retenue ;
- attaques lourdes ;
- attaques chargées ;
- certaines actions physiques.

La régénération d'Endurance dépend de l'état du personnage.

**Valeurs numériques : À VALIDER.**

Le système doit empêcher les actions défensives d'être utilisées sans limite.

---

## 12. Dégâts

Les dégâts finaux sont calculés à partir de :

`Dégâts finaux = dégâts de l'attaque × modificateurs offensifs × modificateurs défensifs`

La formule exacte reste à définir.

Le système doit au minimum distinguer :

- dégâts physiques ;
- dégâts magiques ;
- dégâts environnementaux si applicable.

Les résistances et protections doivent être data-driven.

---

## 13. Armure et protection

L'équipement défensif peut fournir :

- protection physique ;
- résistances spécifiques ;
- poids ;
- pénalités éventuelles de mobilité.

La formule exacte de réduction des dégâts est **À VALIDER**.

Il faut éviter une formule qui permette d'atteindre une invulnérabilité permanente simplement en empilant de l'armure.

---

## 14. Coups critiques

Les coups critiques sont **À VALIDER**.

Si conservés, ils devront dépendre de règles explicites plutôt que d'un hasard opaque.

Paramètres possibles :

- probabilité ;
- multiplicateur ;
- conditions ;
- attaques spécifiques ;
- bonus liés à certaines compétences.

Aucune valeur canonique n'est fixée dans ce brouillon.

---

## 15. Stagger et réactions

Les impacts peuvent provoquer une réaction selon la puissance du coup.

États possibles :

- aucun stagger ;
- léger recul ;
- stagger court ;
- garde brisée ;
- chute ;
- mise à terre.

La réaction dépend notamment :

- puissance de l'attaque ;
- poids/taille de la cible ;
- posture ;
- défense ;
- état actuel.

Les boss et certaines créatures peuvent avoir des règles spécifiques empêchant certains contrôles.

---

## 16. Mort et état critique

Une entité atteint l'état critique lorsque ses points de vie atteignent le seuil défini.

Règle de base proposée :

`PV ≤ 0 → mort ou état spécial`

Certaines entités peuvent avoir un comportement particulier :

- joueur ;
- PNJ ;
- créature normale ;
- boss ;
- créature immortelle.

Les règles d'immortalité propres aux créatures uniques doivent rester dans `specs/BESTIARY.md`.

Le système de combat ne doit donc pas supposer que toutes les cibles meurent simplement lorsque leurs PV atteignent zéro.

---

## 17. Attaque furtive / Backstab

Le Backstab est une mécanique conditionnelle.

Une attaque furtive peut être déclenchée lorsque les conditions de furtivité sont satisfaites.

Conditions potentielles :

- attaquant non détecté ;
- position derrière la cible ;
- distance correcte ;
- arme compatible ;
- cible vulnérable.

La compétence **Élimination furtive** est utilisée pour la résolution de la compétence furtive.

Le multiplicateur ou bonus de dégâts est **À VALIDER**.

Le Backstab doit rester compatible avec les règles de furtivité définies dans le système de furtivité.

---

## 18. Combat à distance

Les arcs et arbalètes utilisent respectivement :

- **Arc**
- **Arbalète**

Une attaque à distance suit :

`Entrée → visée → projectile → collision → résolution des dégâts`

Les paramètres d'un projectile peuvent inclure :

- vitesse ;
- gravité ;
- portée ;
- dégâts ;
- type de dégâts ;
- pénétration éventuelle.

Les valeurs sont data-driven.

---

## 19. Portée et collision

Les attaques de mêlée utilisent des volumes de détection correspondant à leur animation.

La collision de combat ne doit pas dépendre uniquement du modèle visuel.

Chaque attaque peut définir :

- forme du volume ;
- taille ;
- position ;
- durée ;
- nombre maximum de cibles ;
- angle ;
- règles de multi-hit.

Le système doit empêcher une même attaque de toucher continuellement la même cible à chaque frame.

---

## 20. Ciblage

Le ciblage est géré par le système de ciblage global.

Le combat doit pouvoir fonctionner :

- sans lock-on ;
- avec lock-on ;
- contre une cible unique ;
- contre plusieurs cibles.

Le système de ciblage reste indépendant du calcul des dégâts.

---

## 21. Groupe et magie

Le combat doit pouvoir recevoir des actions provenant :

- du joueur ;
- d'un allié ;
- d'un PNJ ;
- d'une créature ;
- d'un sort individuel ;
- d'un sort de groupe.

La magie collective et les rituels sont définis par leurs propres systèmes.

Le système de combat doit seulement fournir les interfaces nécessaires pour recevoir leurs dégâts, effets et interruptions.

---

## 22. IA et combat

L'IA ne doit pas posséder une version parallèle du système de dégâts.

Un PNJ ou une créature utilise les mêmes règles générales de résolution que le joueur :

`AI Decision → Combat Action → Combat Resolver`

L'IA choisit l'action.

Le système de combat résout l'action.

Cela évite les différences artificielles entre joueur et PNJ.

---

## 23. Compétence et Learning by Doing

Lorsqu'une action de combat est réellement pratiquée et validée, elle peut générer une progression de compétence selon les règles de `specs/SKILL_PROGRESSION.md`.

Exemples :

- attaque à l'épée → Épée ;
- attaque à la hache → Hache ;
- parade réussie/pratiquée → Parade ;
- blocage valide → Blocage ;
- esquive valide → Esquive ;
- tir à l'arc → Arc.

Une action répétée artificiellement doit être soumise aux règles anti-farming.

Le combat ne crée pas une seconde méthode de progression indépendante.

---

## 24. Architecture technique proposée

Le système est prévu pour être principalement implémenté en C++.

Composants proposés :

`UCombatComponent`
- état de combat ;
- actions disponibles ;
- exécution des attaques ;
- consommation des ressources.

`UCombatResolver`
- résolution des touches ;
- défense ;
- dégâts ;
- réactions ;
- effets.

`FDamageContext`
- données d'une résolution individuelle.

`UWeaponData`
- données d'arme.

`UAttackData`
- données d'une attaque.

`UDefenseData`
- paramètres défensifs.

Les noms sont provisoires et peuvent être modifiés lors de l'architecture C++.

---

## 25. Séparation C++ / Blueprint

### C++

À mettre dans le cœur du système :

- règles de résolution ;
- dégâts ;
- défense ;
- ressources ;
- états ;
- validation ;
- anti-exploit ;
- interfaces système.

### Blueprint

Peut être utilisé pour :

- montage d'animations ;
- tuning de valeurs ;
- effets visuels ;
- sons ;
- configuration d'armes ;
- prototypes ;
- feedback de combat.

Blueprint ne doit pas devenir la source parallèle des règles fondamentales.

---

## 26. États de combat

État général provisoire :

- Exploration
- Combat
- Attaque
- Défense
- Stagger
- À terre
- Mort

Ces états devront être affinés si le prototype montre qu'une machine d'états plus précise est nécessaire.

---

## 27. Feedback

Chaque résultat important doit fournir un feedback cohérent :

- impact ;
- son ;
- animation ;
- réaction ;
- effet visuel ;
- éventuellement indicateur de dégâts.

Le feedback ne doit pas modifier directement les règles de résolution.

---

## 28. Cas particuliers

Le système doit pouvoir gérer :

- cible immunisée ;
- cible résistante ;
- attaque bloquée ;
- attaque parée ;
- esquive réussie ;
- attaque interrompue ;
- attaquant interrompu ;
- cible morte avant résolution ;
- projectile manqué ;
- projectile bloqué ;
- multi-cibles ;
- dégâts sur alliés si le friendly fire est activé ;
- créature immortelle ;
- boss avec immunités spécifiques.

---

## 29. Règles de conception à préserver

1. Le combat utilise les compétences canoniques.
2. Aucune nouvelle compétence ne doit être créée uniquement pour le combat sans validation.
3. La progression passe par le Learning by Doing existant.
4. Joueur et IA utilisent le même résolveur de combat.
5. La détection des touches est séparée de la résolution des dégâts.
6. Les données d'armes et d'attaques sont data-driven.
7. Les valeurs de balance ne doivent pas être dispersées dans le code.
8. Les règles fondamentales sont en C++.
9. Blueprint sert principalement au contenu, au tuning et au feedback.
10. Les règles propres aux créatures particulières restent dans le bestiaire.

---

## 30. Questions à valider avant implémentation

Les points suivants sont volontairement laissés ouverts pour validation :

- [ ] dégâts de base des armes ;
- [ ] formule exacte de dégâts ;
- [ ] formule d'armure ;
- [ ] types de dégâts définitifs ;
- [ ] durée des i-frames ;
- [ ] coût en Endurance des actions ;
- [ ] récupération d'Endurance ;
- [ ] fonctionnement exact du Blocage ;
- [ ] fonctionnement exact de la Parade ;
- [ ] durée de la fenêtre de riposte ;
- [ ] existence et fonctionnement des coups critiques ;
- [ ] système de stagger ;
- [ ] attaques chargées ;
- [ ] friendly fire ;
- [ ] gestion précise de la mort du joueur ;
- [ ] règles de résistance/immunité ;
- [ ] attaques spéciales propres aux familles d'armes.

**Principe :** tant que ces points ne sont pas validés, ils ne doivent pas être considérés comme des valeurs canoniques.

---

## 31. Résumé du pipeline

`Entrée`
→ `Action de combat`
→ `Validation`
→ `Animation`
→ `Fenêtre d'impact`
→ `Hit Detection`
→ `Defense Resolution`
→ `Damage Resolution`
→ `Effets / Stagger`
→ `Feedback`
→ `Learning by Doing si action valide`

Ce pipeline constitue la base technique du système de combat de Merge avant son implémentation dans Unreal Engine 5.8.1.
