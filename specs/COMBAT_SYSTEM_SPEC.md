# Merge — Combat System Specification

**Statut :** APPROUVÉ — système de conception actuel  
**Moteur :** Unreal Engine 5.8.1  
**Référence canonique :** ce fichier est la spécification centrale du combat. Au 2026-10-15, `COMBAT_RESOLUTION.md` n'est pas présent aux chemins historiques vérifiés dans la branche `main`. Ne pas créer un second document concurrent ; toute référence historique doit pointer ici tant que le document historique n'est pas retrouvé.

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

La charge augmente linéairement la puissance pendant **3 secondes maximum**.

- le joueur maintient la commande pour charger ;
- l'attaque est exécutée **immédiatement au relâchement** de la commande ;
- à **1 % de charge**, la puissance correspond à celle d'une attaque de base ;
- à **100 % de charge**, après 3 secondes, la puissance atteint **4× celle d'une attaque de base** ;
- au-delà de 3 secondes, la puissance n'augmente plus.

La progression est linéaire entre 1 % et 100 % de charge :

```text
Charge_Multiplier = 1 + ((Charge_Percent - 1) / 99) × 3
```

Exemples : 1 % = 1× ; 25 % ≈ 1,75× ; 50 % ≈ 2,50× ; 75 % ≈ 3,25× ; 100 % = 4×.

Le coût d'endurance de l'attaque puissante reste de **20 à 40 endurance selon le niveau de charge**.

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

**Fenêtres de timing retenues pour un personnage de référence :**
- fenêtre de parade parfaite : **200 ms** ;
- fenêtre de parade normale : **350 ms au total**, incluant la fenêtre parfaite.

L'Agilité et la compétence Parade modifient la facilité du timing. Leurs coefficients exacts et la manière précise de déplacer ou d'élargir ces fenêtres restent à définir ; ne pas inventer de coefficients avant validation.

Un personnage lourd peut toujours parer, mais peut choisir de privilégier le blocage.

### 3.3 Blocage

Le blocage est une défense plus stable et moins dépendante du timing précis.

**Coût d'endurance :** le simple maintien de la garde ne consomme aucune endurance. L'endurance est consommée uniquement lorsqu'une attaque ennemie est effectivement interceptée par le blocage.

- Garde maintenue sans attaque reçue : **0 endurance**.
- Attaque effectivement bloquée : **10 endurance par impact bloqué** (coût de base canonique actuel).
- Une attaque qui rate le joueur ou ne touche pas la garde : **0 endurance**.
- Aucun modificateur supplémentaire lié au poids de l'armure n'est encore défini. Jusqu'à décision explicite, appliquer uniformément le coût de base de 10 ; ne pas inventer de multiplicateur.

Les personnages lourds ont tendance à privilégier le blocage ; leur armure plus élevée compense une partie des dégâts qui peuvent traverser le blocage.

## 4. Endurance

Merge utilise une seule barre d'endurance de **100 points**.

Elle sert notamment au sprint, à l'esquive, au blocage, aux attaques puissantes et aux attaques spéciales.

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
- armure généralement plus élevée pour compenser une partie des dégâts résiduels ;
- style fondé davantage sur l'endurance et la résistance.

Le coût de base du blocage reste de 10 endurance par impact. Un surcoût lié à l'armure lourde est une décision de design encore ouverte ; aucun surcoût ne doit être implémenté avant que sa valeur et sa règle soient approuvées.

Aucun style n'est imposé au joueur.

## 6. Dégâts

Les deux catégories principales de dégâts sont Physique et Magique.

Tranchant, perforant et contondant sont des propriétés des armes utilisées pour caractériser les attaques physiques. Ils ne constituent pas trois catégories principales indépendantes.

### 6.1 Formule de dégâts physiques

La formule canonique des dégâts physiques est :

```
Damage = Weapon_Base_Damage
       × (1 + Weapon_Mastery × 0.005)
       × (1 + Strength × 0.02)
       × Armor_Modifier
       × Other_Modifiers
```

Où :
- **Weapon_Base_Damage** = dégâts de base fixes de l'arme ;
- **Weapon_Mastery** = maîtrise de la famille d'arme, de 0 à 100 ;
- **Strength** = Force du personnage, de 0 à 20 ;
- **Armor_Modifier** = coefficient de protection correspondant au type de dégâts et au type d'armure ;
- **Other_Modifiers** = modificateurs contextuels éventuels.

La maîtrise maximale apporte donc **+50 %** de dégâts et chaque point de Force apporte **+2 %** de dégâts physiques, soit **+40 % maximum** à 20/20.

### 6.2 Propriétés physiques et armure

Merge ne possède que **deux catégories d'armure : légère et lourde**. Il n'existe pas d'armure moyenne.

Les coefficients ci-dessous représentent la **réduction des dégâts physiques** appliquée par l'armure :

| Type de dégâts | Armure légère | Armure lourde |
|---|---:|---:|
| **Tranchant** | **35 %** | **60 %** |
| **Perforant** | **30 %** | **45 %** |
| **Contondant** | **25 %** | **40 %** |

Ainsi, pour une attaque de 100 dégâts avant armure :
- tranchant contre légère = 65 dégâts ;
- perforant contre légère = 70 dégâts ;
- contondant contre légère = 75 dégâts ;
- tranchant contre lourde = 40 dégâts ;
- perforant contre lourde = 55 dégâts ;
- contondant contre lourde = 60 dégâts.

La hiérarchie recherchée est donc :
- contre l'armure légère, les trois types restent utiles, avec le perforant légèrement favorisé ;
- contre l'armure lourde, le tranchant est le plus pénalisé, le perforant reste sensiblement efficace et le contondant est le plus efficace.

Les armes infligeant principalement des dégâts **contondants sont des armes à deux mains**. Leur avantage contre les armures lourdes est donc associé à une contrainte de maniement et de style de combat.

Ces coefficients sont déterministes et ne sont pas randomisés.

## 7. Armure

L'armure réduit les dégâts reçus selon les coefficients définis à la section 6.2.

Les seules catégories canoniques sont :
- **Armure légère** ;
- **Armure lourde**.

Il n'existe pas de catégorie d'armure moyenne.

L'armure légère fournit une protection significative tout en restant moins résistante que l'armure lourde. L'armure lourde est particulièrement résistante au tranchant, résiste davantage au perforant qu'au tranchant, et reste vulnérable au contondant relativement aux deux autres propriétés.

Les conséquences exactes du poids de l'armure sur la mobilité et l'endurance restent à définir.

## 8. Stagger

**Modèle retenu : stagger équilibré.** La résistance au stagger dépend notamment de la puissance et de l'impact de l'attaque, ainsi que du poids, de la taille et de l'armure de la cible.

- Les petites cibles légères sont généralement plus faciles à déséquilibrer.
- Les créatures massives résistent davantage au déséquilibre.
- Les attaques puissantes et chargées peuvent favoriser le stagger, sans garantir qu'une cible résistante soit interrompue.

La durée du stagger réussi est fixée à **3 secondes**. Les seuils numériques qui déterminent si le stagger réussit et les effets précis pendant ces 3 secondes restent à définir. Les règles d'interruption sont définies séparément à la section 16 ; elles ne doivent pas être modifiées sans décision explicite.

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

Le plafond de la chance de critique est fixé à **15 %**. Le maximum doit être réservé aux personnages disposant de caractéristiques et d'une maîtrise de l'arme élevées.

La formule canonique validée est :

```
Critical_Chance_Percent = min(15, (Agility + Perception) / 4 + Weapon_Mastery / 20)
```

- Agilité et Perception sont chacune notées de 0 à 20.
- Maîtrise de l'arme (ou compétence de combat pertinente) est notée de 0 à 100.
- La chance est plafonnée à **15 %** ; atteindre ce plafond demande des caractéristiques élevées et une maîtrise élevée.
- Les résultats de la formule sont exprimés en pourcentage.

Exemples de référence :

| Agilité | Perception | Maîtrise | Chance de critique |
|---:|---:|---:|---:|
| 6 | 6 | 0 | 3 % |
| 10 | 10 | 50 | 7,5 % |
| 14 | 14 | 80 | 11 % |
| 18 | 18 | 100 | 14 % |
| 20 | 20 | 100 | 15 % |

Les critiques garantis par une parade parfaite ou un backstab restent distincts de cette probabilité aléatoire.

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

### 16.1 Règle canonique d'interruption et de bris de défense

Seuls les événements suivants peuvent interrompre une autre attaque en cours ou briser une défense :

- **Attaque critique** ;
- **Stagger réussi** ;
- **Attaque chargée à 100 %** (charge maximale de 3 secondes).

Une attaque ordinaire ou une attaque chargée à moins de 100 % ne peut pas, à elle seule, interrompre une autre attaque ni briser une défense. Cette règle limite les interruptions aux événements qui ont une importance tactique particulière. Les conditions précises d'application, les priorités en cas d'événements simultanés et les réactions d'animation restent à définir, sans élargir la liste des événements autorisés.

Les valeurs déjà fixées dans les sections précédentes (coûts de base d'endurance, régénération, formule de dégâts physiques, coefficients d'armure, charge maximale et multiplicateur critique) ne sont pas à redéfinir dans une autre spécification sans décision explicite.

- coefficients exacts de l'influence de l'Agilité et de la compétence Parade sur les fenêtres de timing ;
- formule précise du stagger et seuils de réussite (la durée approuvée est de 3 secondes) ;
- détails de résolution des interruptions et du bris de défense, en conservant la règle canonique suivante : seuls un coup critique, un stagger réussi ou une attaque chargée à 100 % peuvent interrompre une autre attaque ou briser une défense ;
- détails des combos spéciaux par arme ;
- comportement exact des réactions automatiques de Réflexe ;
- détails de l'IA de combat ;
- système de magie en combat ;
- influence détaillée des différentes compétences de combat sur la chance de critique lorsqu'une compétence pertinente remplace la Maîtrise de l'arme.

Ces éléments sont des sous-systèmes ou paramètres encore à concevoir, pas des contradictions avec le système approuvé.

**État de validation au 2026-10-15 :** spécification documentaire seulement. La compilation UE 5.8.1, l'intégration C++, les animations/collisions, les tests de dégâts et les tests PIE restent à effectuer localement. L'approbation du document ne signifie pas que le combat est implémenté ou validé.
