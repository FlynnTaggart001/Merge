# Merge — Combat System Specification

**Statut :** APPROUVÉ — système de conception actuel  
**Moteur :** Unreal Engine 5.8.1

## 1. Principes

Le combat de Merge est un système temps réel à la troisième personne.

- contrôle direct du personnage ;
- combat fondé sur le placement, le timing et les compétences ;
- pas de mécanique de combo de type jeu de combat nécessitant la mémorisation de séquences ;
- chaque famille d'arme possède sa propre identité, ses propres attaques et ses propres animations ;
- lock-on entièrement optionnel ;
- utilisation des compétences canoniques et du Learning by Doing ;
- aucune progression de combat séparée du système de compétences.

## 2. Types d'attaques

### 2.1 Attaque de base

L'attaque de base correspond aux coups normaux de la famille d'arme et sert principalement à infliger les dégâts de base.

Familles concernées : Épée, Hache, Masse, Lance, Dague, Arme à deux mains, Arc, Arbalète et Combat à mains nues.

Les attaques utilisent les propriétés de l'arme, notamment tranchant, perforant ou contondant.

### 2.2 Attaque puissante

L'attaque puissante est une attaque chargée. Le joueur maintient la commande d'attaque pour charger puis relâche pour exécuter l'attaque.

La charge augmente la puissance jusqu'à la limite définie par l'arme.

Les coûts d'endurance, temps de charge et valeurs numériques restent à définir.

### 2.3 Attaque spéciale

L'attaque spéciale est un combo préenregistré propre à la famille d'arme. Le joueur déclenche la spéciale et le personnage exécute automatiquement la séquence prévue.

### 2.4 Spéciale de la dague

La spéciale de la dague consiste en une série de coups rapides. Le dernier mouvement repositionne le joueur derrière l'adversaire lorsque le déplacement est possible.

Un coup porté depuis l'arrière est un backstab, c'est-à-dire simplement un coup critique. Le backstab n'est pas une catégorie de dégâts séparée.

## 3. Défense

Les trois défenses principales sont : Esquive, Parade et Blocage.

### 3.1 Esquive

L'esquive est une défense mobile utilisant la compétence Esquive. Elle bénéficie notamment de l'Agilité et utilise l'endurance.

### 3.2 Parade

La parade utilise un test de timing inspiré du principe des tests de compétence de Dead by Daylight.

Le test ne s'active que lorsqu'une attaque ennemie est réellement susceptible de toucher le joueur. Si l'attaque rate naturellement le joueur, aucun test de parade ne s'active.

Résultats :
- Parade parfaite : aucun dégât + contre automatique + coup critique sur l'ennemi.
- Parade réussie mais non parfaite : aucun dégât, sans contre automatique.
- Parade ratée : le joueur reçoit un coup critique.

Une parade réussie annule donc les dégâts de l'attaque parée.

L'Agilité influence la facilité physique du timing :
- personnage agile : fenêtre plus large ;
- personnage moyen : fenêtre normale ;
- personnage lourd / peu agile : fenêtre plus courte.

La compétence Parade représente la maîtrise technique et influence également la facilité du test.

Un personnage lourd peut toujours parer, mais peut choisir de privilégier le blocage.

### 3.3 Blocage

Le blocage est une défense plus stable et moins dépendante du timing précis.

**Coût d'endurance :** le simple maintien de la garde ne consomme aucune endurance. L'endurance est consommée uniquement lorsqu'une attaque ennemie est effectivement interceptée par le blocage.

- Garde maintenue sans attaque reçue : **0 endurance**.
- Attaque effectivement bloquée : **10 endurance par impact bloqué**.
- Une attaque qui rate le joueur ou ne touche pas la garde : **0 endurance**.

Les personnages lourds ont tendance à privilégier le blocage ; leur armure plus élevée compense une partie des dégâts qui peuvent traverser le blocage.

## 4. Endurance

Merge utilise une seule barre d'endurance de **100 points**.

Elle sert notamment au sprint, à l'esquive, au blocage, aux attaques puissantes et, lorsque défini, aux attaques spéciales.

Les attaques de base n'ont pas de coût d'endurance.

### 4.1 Coûts canoniques

- **Esquive : 20 endurance** par utilisation.
- **Parade réussie : 10 endurance**.
- **Parade parfaite : 5 endurance**.
- **Blocage : 10 endurance par impact effectivement bloqué**, et non par seconde de garde.
- **Attaque puissante : 20 à 40 endurance** selon le niveau de charge.
- **Attaque spéciale : 30 endurance**.
- **Sprint : 5 endurance par seconde**.

### 4.2 Régénération

La régénération est de **15 endurance par seconde**.

Après **0,5 seconde sans action consommant de l'endurance**, la régénération commence.

La barre est plafonnée à 100 points.

## 5. Styles défensifs émergents

Personnage agile :
- parade facilitée par l'Agilité ;
- esquive importante ;
- mobilité élevée ;
- peut rechercher les parades parfaites et leurs contres critiques.

Personnage lourd :
- parade plus difficile ;
- blocage davantage privilégié ;
- blocage plus consommateur d'endurance ;
- armure plus élevée pour compenser les dégâts résiduels ;
- style fondé davantage sur l'endurance et la résistance.

Aucun style n'est imposé au joueur.

## 6. Dégâts

Les deux catégories principales de dégâts sont Physique et Magique.

Tranchant, perforant et contondant sont des propriétés des armes utilisées pour caractériser les attaques physiques. Ils ne constituent pas trois catégories principales indépendantes.

La formule numérique complète des dégâts, le rôle exact des caractéristiques, de l'arme et de l'armure restent à définir.

## 7. Armure

L'armure réduit les dégâts reçus selon le système de protection défini pour l'équipement.

Les catégories et valeurs exactes d'armure, ainsi que ses éventuelles conséquences sur mobilité et endurance, restent à régler.

## 8. Stagger

Le stagger dépend notamment de la puissance et de l'impact de l'attaque ainsi que du poids et de la taille de la cible.

Une petite cible légère peut donc être déséquilibrée plus facilement qu'une créature massive.

Les seuils et résultats exacts restent à définir.

## 9. Critiques

### 9.1 Critiques de situation (automatiques)

Les coups critiques de situation se déclenchent automatiquement dans des contextes définis, **sans tirage aléatoire** :

- **Parade parfaite** → contre-attaque automatique avec coup critique sur l'ennemi.
- **Backstab** (attaque depuis l'arrière) → coup critique automatique.

Ces critiques se déclenchent toujours dans les conditions appropriées et ne dépendent pas d'une probabilité aléatoire générale.

D'autres conditions contextuelles pourront être définies ultérieurement selon le même principe.

### 9.2 Chance de critique basée sur les caractéristiques

Une attaque normale peut également devenir critique selon la **chance de critique** du personnage attaquant.

La chance de critique dépend de :

- **Agilité** du personnage attaquant ;
- **Perception** du personnage attaquant ;
- **Maîtrise de l'arme** (ou compétence de combat pertinente) du personnage attaquant.

La formule exacte et les poids de chaque facteur : À DÉFINIR.

### 9.3 Multiplicateur de critique

Tout coup critique inflige un multiplicateur de **2.0×** sur les dégâts calculés (voir `specs/WEAPONS_AND_EQUIPMENT_SPEC.md`, section 10.1).

```
Critical_Damage = Normal_Damage × 2.0
```

## 10. Furtivité et combat

Les attaques furtives peuvent être réalisées avec les armes de mêlée et avec l'arc.

Chaîne de détection :
Discrétion de l'attaquant → détection par la Perception de la cible → Réflexe de la cible si une réaction est possible.

- Discrétion : capacité de l'attaquant à approcher sans être détecté.
- Perception : capacité de la cible à détecter l'approche.
- Réflexe : système automatique de réaction à une menace soudaine ; ce n'est ni une compétence ni une caractéristique.

Si le joueur atteint l'arrière de la cible sans être détecté, une attaque dans le dos constitue un backstab critique.

Une cible disposant d'un Réflexe suffisamment élevé peut, lorsque les conditions permettent une réaction, se retourner ou éviter automatiquement le coup critique.

Réflexe est basé sur les caractéristiques Agilité + Perception.

La Discrétion de la cible n'est pas utilisée pour éviter un backstab : elle sert à sa propre capacité de furtivité.

## 11. Lock-on

Le verrouillage de cible est optionnel et dépend entièrement de la volonté du joueur.

Le combat doit rester jouable sans lock-on.

## 12. Armes à distance

Arc :
- tir normal ;
- attaque furtive possible ;
- identité fondée notamment sur mobilité et cadence ;
- compétence Arc.

Arbalète :
- tir normal ;
- comportement distinct de l'arc ;
- recharge et puissance propres ;
- compétence Arbalète.

Les trajectoires, collisions, vitesses de projectile et valeurs de dégâts restent à définir.

## 13. Mains nues

Le Combat à mains nues est une famille de combat canonique avec :
- attaques de base ;
- attaques puissantes chargées ;
- combos spéciaux préenregistrés ;
- propriétés et animations propres.

## 14. Learning by Doing et anti-farming

Le combat n'utilise pas de progression séparée.

Les actions pertinentes et validées peuvent alimenter les compétences correspondantes : Épée, Hache, Masse, Lance, Dague, Arme à deux mains, Arc, Arbalète, Combat à mains nues, Esquive, Parade, Blocage, Discrétion, Élimination furtive.

Une parade contre une attaque qui ne pouvait pas toucher n'existe pas dans le système : aucun test de parade ne s'active et aucune progression de Parade ne peut être accordée par ce cas.

Les règles générales de validation et d'anti-farming de specs/SKILL_PROGRESSION.md restent prioritaires. Une action répétée artificiellement ou non pertinente ne fournit pas la progression normale.

## 15. Mort et exceptions

Le système de combat standard peut amener une cible à 0 PV et à l'état mort.

Les exceptions propres aux créatures uniques ou immortelles restent définies par leurs systèmes ou le bestiaire respectifs. Le système de combat générique ne doit pas intégrer en dur les règles d'immortalité.

## 16. Éléments encore à définir

- formule exacte des dégâts ;
- valeurs d'armure ;
- formule précise du stagger ;
- valeurs des fenêtres de parade ;
- règles précises d'interruption ;
- détails des combos spéciaux par arme ;
- comportement exact des réactions automatiques de Réflexe ;
- détails de l'IA de combat ;
- système de magie en combat ;
- formule exacte de la chance de critique incorporant Agilité, Perception et Maîtrise de l'arme.

Ces éléments sont des sous-systèmes ou paramètres encore à concevoir, pas des contradictions avec le système approuvé.
