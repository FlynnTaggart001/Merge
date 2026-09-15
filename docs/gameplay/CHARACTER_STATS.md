# Système de caractéristiques — Merge

## 1. Objectif

Les caractéristiques représentent les capacités fondamentales du personnage. Elles sont distinctes des compétences : une caractéristique décrit une capacité générale du personnage, tandis qu'une compétence représente ce qu'il sait faire dans un domaine précis.

Le système suit le principe fondamental de **Merge** : progression par utilisation (*learning by doing*).

Les caractéristiques suivent également une règle de puissance importante : **un personnage avec une caractéristique basse reste un être humain ou une créature normalement fonctionnelle. Le dépassement de 50 marque progressivement l'entrée dans le domaine surhumain.**

## 2. Caractéristiques de base

Le personnage possède six caractéristiques de base :

- **Force**
- **Agilité**
- **Intelligence**
- **Perception**
- **Volonté**
- **Charisme**

Chaque caractéristique possède une valeur comprise entre **0 et 100**.

Le maximum définitif est **100**.

## 3. Points de départ

Tous les personnages reçoivent le **même nombre de points de caractéristiques lors de la création**.

Le joueur répartit librement ces points entre les six caractéristiques.

La race peut ensuite modifier les caractéristiques initiales en fonction de ses aptitudes naturelles.

Le nombre exact de points de départ et les valeurs minimales restent à définir.

## 4. Progression par utilisation directe

Les caractéristiques progressent lorsque le joueur réalise réellement des actions qui sollicitent la capacité correspondante.

Une même action peut faire progresser plusieurs caractéristiques si elle sollicite réellement plusieurs capacités. Chaque progression doit cependant correspondre à ce que le personnage est effectivement en train de faire.

Principes :

- Une action doit réellement solliciter la caractéristique pour pouvoir la faire progresser.
- La difficulté et l'intensité de l'action influencent la progression.
- Une action insignifiante ou beaucoup trop facile par rapport au niveau actuel peut donner **0 progression**.
- Plus la caractéristique est élevée, plus la progression ralentit naturellement.
- Il n'existe pas de pénalité artificielle destinée à empêcher la répétition d'une activité réellement difficile : une réussite légitime peut toujours faire progresser la caractéristique si l'action reste suffisamment exigeante.
- La progression est plafonnée à **100**.
- Les valeurs sont stockées avec des décimales en interne afin de permettre une progression fine.
- Les caractéristiques ne diminuent pas avec le temps ou l'absence d'utilisation.

La sensation générale recherchée reste comparable à celle de **Skyrim** sur le plan de la progression par utilisation, sans reprendre ses formules exactes.

## 5. Formule universelle de progression

La progression d'une caractéristique utilise une formule unique pour toutes les caractéristiques et toutes les actions.

### Variables

- `C` = valeur actuelle de la caractéristique, de 0 à 100.
- `D_c` = difficulté ou intensité de l'action pour cette caractéristique, sur une échelle de 0 à 100.
- `M` = multiplicateur de sollicitation propre à l'action.
- `P_c` = progression obtenue après l'action.

### Formule

```text
P_c = 0.35 × max(0, (D_c - C + 15) / 50) × 1 / (1 + 0.012 × C) × M
```

La valeur finale est limitée à un minimum de 0 et ne peut jamais faire dépasser la caractéristique au-delà de 100.

### Interprétation

**Écart de difficulté :**

```text
max(0, (D_c - C + 15) / 50)
```

Plus l'action est difficile par rapport au niveau actuel, plus elle apporte de progression. Si l'action est suffisamment en dessous du niveau actuel, le résultat devient nul.

**Ralentissement avec le niveau :**

```text
1 / (1 + 0.012 × C)
```

La progression ralentit continuellement lorsque la caractéristique augmente. Il n'existe donc pas de paliers artificiels dans la progression elle-même.

**Sollicitation de l'action :**

`M` permet de représenter la part réelle de la caractéristique sollicitée par l'action. Une caractéristique fortement sollicitée peut recevoir une progression plus importante qu'une caractéristique seulement secondairement sollicitée.

Le multiplicateur `M` doit être défini par le système de gameplay en fonction de l'action et ne doit pas servir à contourner les règles générales de progression.

## 6. Échelle de puissance des caractéristiques

Les valeurs de caractéristiques ne correspondent pas à des classes de personnage fixes. Elles décrivent une progression continue des capacités.

### 0–19 — Faible, mais normalement fonctionnel

Le personnage est relativement faible dans cette caractéristique, mais reste un être humain ou une créature normalement fonctionnelle.

Une valeur de 10 ou 20 ne signifie pas que le personnage est incapable d'accomplir les actions ordinaires liées à cette caractéristique. Elle indique simplement qu'il est moins performant que la moyenne dans ce domaine.

### 20–39 — Domaine normal

Le personnage se situe dans une plage normale pour un être humain ou une créature comparable.

Il peut accomplir les activités ordinaires sans capacités fantastiques. Les différences de valeur modifient progressivement son efficacité sans lui retirer artificiellement des actions normales.

### 40–49 — Excellence humaine

Le personnage commence à se rapprocher des meilleurs niveaux naturellement accessibles à un être humain exceptionnel.

Il peut être un athlète remarquable, un individu extrêmement observateur, un apprenant exceptionnel, un combattant très doué ou posséder une présence sociale impressionnante selon la caractéristique concernée.

### 50–59 — Début du domaine surhumain

À partir de 50, la caractéristique commence progressivement à dépasser les capacités humaines ordinaires.

Le personnage peut commencer à accomplir des exploits qui seraient extrêmement difficiles ou impossibles pour un humain normal.

Exemples physiques :

- sauts nettement plus hauts ;
- mouvements plus rapides et plus explosifs ;
- force permettant de manipuler des charges anormalement lourdes ;
- enchaînements physiques plus complexes.

Pour les caractéristiques mentales ou sociales, le dépassement est également progressif : apprentissage exceptionnellement rapide, perception de détails difficiles à remarquer, résistance mentale remarquable ou influence sociale inhabituelle.

### 60–69 — Surhumain confirmé

Les capacités dépassent clairement le domaine humain normal.

Le personnage peut réaliser régulièrement des exploits qui paraîtraient extraordinaires à une personne ordinaire.

### 70–79 — Très surhumain

Le personnage possède des capacités suffisamment élevées pour réaliser des exploits spectaculaires.

Dans les caractéristiques physiques, cela peut permettre des mouvements et des enchaînements rappelant les héros d'action ou de fantasy.

### 80–89 — Niveau héroïque extrême

Les capacités deviennent exceptionnellement puissantes.

Le personnage peut accomplir des actions qui seraient normalement considérées comme impossibles pour un humain ordinaire et qui peuvent avoir une forte dimension spectaculaire en jeu.

### 90–99 — Niveau exceptionnel

Le personnage approche de la limite supérieure du système.

Ses exploits peuvent devenir légendaires selon la caractéristique concernée.

### 100 — Maximum

100 représente le maximum définitif de la caractéristique dans le système de **Merge**.

Il s'agit de la limite supérieure des capacités accessibles par la progression normale du personnage.

## 7. Règle fondamentale : pas de paliers artificiels de puissance

Les catégories ci-dessus servent à définir la **sensation générale de puissance**, pas à créer des compétences automatiquement débloquées à chaque tranche de dix points.

Le système ne doit pas fonctionner ainsi :

> « Force 50 = double saut débloqué. »

Il doit fonctionner ainsi :

> « Plus la Force augmente, plus le personnage devient physiquement capable, jusqu'à dépasser progressivement les limites humaines. »

Les effets ordinaires sont donc calculés continuellement.

Les seuils fixes sont réservés à des situations exceptionnelles où une interaction nécessite réellement une condition minimale de faisabilité.

Exemples :

- une porte particulièrement lourde peut nécessiter une Force minimale pour être déplacée ;
- une prise ou une trajectoire particulière peut nécessiter une Agilité minimale ;
- un mécanisme extrêmement complexe peut nécessiter une Intelligence minimale ;
- un détail pratiquement impossible à percevoir peut nécessiter une Perception minimale ;
- un effet mental particulièrement puissant peut nécessiter une Volonté minimale ;
- une interaction sociale exceptionnelle peut nécessiter un Charisme minimal.

Ces seuils ne remplacent jamais le calcul continu.

## 8. Force

La Force représente la puissance physique brute du personnage.

Elle influence continuellement :

- la puissance des attaques physiques ;
- la capacité à porter une charge ;
- la capacité à pousser, tirer ou soulever des objets ;
- la capacité à déplacer certains éléments du monde ;
- les actions physiques exigeantes ;
- l'efficacité des armes nécessitant une importante puissance physique ;
- certaines actions d'escalade et d'athlétisme ;
- la capacité à produire des mouvements physiques explosifs.

Une Force basse n'empêche pas un personnage de vivre et d'agir normalement. Une Force élevée augmente progressivement ses performances, puis permet des exploits surhumains au-delà de 50.

### Exemple de sensation

- **Force 20** : humain relativement peu puissant mais parfaitement fonctionnel.
- **Force 40** : humain physiquement très capable.
- **Force 50+** : dépassement progressif des limites humaines.
- **Force 70+** : exploits physiques spectaculaires possibles.
- **Force 90+** : puissance proche du maximum fantastique du système.

### Surcharge d'inventaire

Le simple fait de posséder beaucoup d'objets ne fait pas progresser la Force.

Lorsque le poids de l'inventaire dépasse la capacité de transport du personnage :

- le personnage devient **surchargé** ;
- ses déplacements sont ralentis en fonction de la surcharge ;
- maintenir cette surcharge pendant un effort réel peut progressivement développer la Force.

La capacité de transport augmente continuellement avec la Force.

## 9. Agilité

L'Agilité représente la capacité à contrôler rapidement et précisément le corps.

Elle influence continuellement :

- la rapidité d'exécution des mouvements ;
- l'accélération et les changements de direction ;
- la précision des mouvements ;
- l'esquive ;
- l'acrobatie ;
- les déplacements sur des surfaces difficiles ;
- l'utilisation d'armes demandant rapidité et précision ;
- la manipulation fine ;
- certaines actions d'escalade et de furtivité.

Une Agilité basse correspond toujours à un personnage fonctionnel. Au-delà de 50, elle peut progressivement produire des mouvements dépassant les capacités humaines ordinaires.

À des valeurs élevées, elle peut permettre des enchaînements spectaculaires, des esquives rapides, des sauts et des changements de direction impossibles pour un humain normal.

## 10. Intelligence

L'Intelligence représente la capacité à apprendre, comprendre, raisonner et mémoriser.

Elle influence continuellement :

- la vitesse d'apprentissage des compétences ;
- la compréhension des mécanismes ;
- l'analyse des problèmes ;
- l'assimilation des connaissances ;
- la compréhension des langues ;
- l'artisanat complexe ;
- l'étude de la magie ;
- la mémorisation et l'exploitation d'informations.

Une Intelligence basse reste compatible avec une vie normale. Une Intelligence élevée améliore progressivement les capacités cognitives et, au-delà de 50, peut représenter des capacités d'apprentissage et d'analyse dépassant clairement les limites humaines ordinaires.

L'Intelligence intervient notamment comme modificateur de la progression des compétences, conformément au système défini dans `CHARACTER_SKILLS.md`.

## 11. Perception

La Perception représente la capacité à observer, remarquer et interpréter les éléments présents dans l'environnement.

Elle influence continuellement :

- la détection des ennemis ;
- la détection des ressources ;
- l'observation des détails ;
- la recherche d'indices ;
- la détection des pièges ;
- la perception des mouvements ;
- la précision à distance ;
- la capacité à remarquer des éléments dissimulés.

Une Perception basse signifie seulement que le personnage remarque moins facilement certaines informations. Elle ne doit pas rendre artificiellement aveugle un personnage normalement fonctionnel.

Au-delà de 50, la capacité d'observation peut progressivement dépasser les capacités humaines ordinaires, jusqu'à permettre la détection de détails extrêmement difficiles à remarquer.

## 12. Volonté

La Volonté représente la force mentale, la maîtrise de soi et la capacité à rester concentré malgré la pression.

Elle influence continuellement :

- la résistance au contrôle mental ;
- la résistance à certaines influences magiques ;
- la concentration ;
- la capacité à maintenir une action exigeant une forte concentration ;
- la résistance à la peur ;
- la maîtrise des réactions émotionnelles ;
- la résistance à certaines provocations, tentations ou pressions psychologiques.

Une Volonté basse correspond à une personne plus facilement perturbée, mais reste compatible avec une vie mentale normale. Au-delà de 50, la résistance et la maîtrise de soi peuvent progressivement devenir surhumaines.

## 13. Charisme

Le Charisme représente la capacité à influencer les autres et à interagir efficacement avec eux.

Il influence continuellement :

- la persuasion ;
- l'intimidation ;
- l'éloquence ;
- le marchandage ;
- la capacité à établir une relation ;
- l'influence exercée sur un groupe ;
- la résolution de conflits par la communication ;
- certaines premières impressions et réactions sociales.

Une valeur basse ne signifie pas que le personnage est socialement incapable. Elle indique une influence plus faible ou une présence moins marquante.

Au-delà de 50, le Charisme peut progressivement produire une influence exceptionnellement forte, jusqu'à des niveaux presque légendaires à très haute valeur.

Le Charisme ne force jamais automatiquement un PNJ à accepter une demande. Il modifie progressivement les chances et la qualité d'une interaction, en combinaison avec le contexte, les relations, la réputation, la langue et les compétences sociales.

## 14. Combinaison des caractéristiques

Les caractéristiques peuvent produire des capacités très différentes lorsqu'elles sont combinées.

Exemple physique :

**Force 75 + Agilité 80 + Épée 85**

Le personnage peut devenir extrêmement puissant, rapide et techniquement compétent, permettant des enchaînements de combat spectaculaires.

À l'inverse :

**Force 75 + Agilité 25 + Épée 85**

Le personnage reste très puissant et techniquement compétent, mais ses mouvements sont beaucoup moins rapides et acrobatiques.

Les caractéristiques ne donnent donc pas automatiquement une « capacité spéciale ». Elles déterminent progressivement les possibilités physiques, mentales et sociales du personnage.

## 15. Exemple — Escalade

Un personnage possède :

- Force = 40
- Agilité = 55

Il escalade une paroi dont l'intensité physique est élevée, avec une difficulté de 70.

L'action peut solliciter :

- fortement la Force ;
- l'Agilité de manière secondaire.

Le jeu calcule alors séparément la progression de chaque caractéristique avec sa difficulté et son multiplicateur propres.

La Force et l'Agilité peuvent donc progresser simultanément, mais pas automatiquement les quatre autres caractéristiques.

## 16. Exemple — Mécanisme complexe

Un mécanisme difficile peut avoir par exemple :

- difficulté Crochetage = 70 ;
- sollicitation Perception = 30 ;
- sollicitation Intelligence = 50 ;
- sollicitation Agilité = 45.

Le système peut alors faire progresser séparément :

- **Crochetage** ;
- **Perception** ;
- **Intelligence** ;
- **Agilité**.

Une action peut donc développer simultanément une compétence et plusieurs caractéristiques lorsque cela correspond réellement à l'activité effectuée.

## 17. Progression multi-caractéristiques

Une action peut développer plusieurs caractéristiques simultanément lorsqu'elle sollicite réellement plusieurs capacités.

Exemple :

Un joueur découvre une plante rare dans une forêt :

- la repérer → **Perception** ;
- la récolter → **Perception** et éventuellement **Agilité** si la récolte demande de la précision ;
- identifier ses propriétés → **Intelligence** ;
- mémoriser son environnement de pousse → **Intelligence** ;
- traverser une zone escarpée pour l'atteindre → **Agilité** ;
- continuer malgré une situation effrayante → **Volonté** ;
- expliquer ensuite ses propriétés à un herboriste → **Charisme**.

Le système ne donne donc pas automatiquement un bonus arbitraire à une caractéristique : chaque progression doit découler de l'activité réellement effectuée.

## 18. Relation avec les compétences

Les caractéristiques et les compétences restent deux systèmes distincts.

> **Caractéristique = ce dont le personnage est capable.**
>
> **Compétence = ce que le personnage sait particulièrement bien faire.**

Une action peut donc :

- développer une ou plusieurs caractéristiques ;
- développer une compétence ;
- développer simultanément plusieurs caractéristiques et une compétence lorsque l'action le justifie.

Exemples :

- **Force 80 / Épée 35** : personnage très puissant physiquement, mais encore peu compétent à l'épée.
- **Force 35 / Épée 85** : excellent épéiste techniquement, mais disposant de moins de puissance physique.

## 19. Relation avec les classes

Les classes utilisent les caractéristiques comme base de spécialisation.

Une classe possède certaines caractéristiques principales. Le joueur peut débloquer une autre classe en développant suffisamment les caractéristiques requises et en dépassant les seuils définis pour cette classe.

Les seuils exacts et les effets précis des caractéristiques sur les classes seront définis dans la documentation dédiée aux classes.

## 20. Principe fondamental

> **Le personnage devient progressivement ce que le joueur lui fait réellement pratiquer.**
>
> **En dessous de 50, les caractéristiques décrivent principalement des différences humaines ou naturelles. Au-dessus de 50, elles permettent progressivement de dépasser les limites humaines et d'entrer dans le domaine surhumain et fantastique.**

La progression doit donc rester organique, continue et directement liée aux actions du joueur plutôt qu'à un système de niveaux global imposant une progression prédéterminée.

## 21. Éléments restant à définir

- nombre exact de points de départ ;
- valeurs minimales ;
- influence numérique précise de chaque caractéristique sur les actions ;
- définition détaillée des multiplicateurs `M` selon les actions ;
- interaction numérique exacte entre caractéristiques et compétences ;
- interaction exacte avec les races ;
- interaction exacte avec les classes.
