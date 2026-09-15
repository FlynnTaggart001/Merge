# Système de caractéristiques — Merge

## 1. Objectif

Les caractéristiques représentent les capacités fondamentales du personnage. Elles sont distinctes des compétences : une caractéristique décrit une capacité générale du personnage, tandis qu'une compétence représente ce qu'il sait faire dans un domaine précis.

Le système suit le principe fondamental de **Merge** : progression par utilisation (*learning by doing*).

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

La progression ralentit continuellement lorsque la caractéristique augmente. Il n'existe donc pas de paliers artificiels entre les niveaux.

**Sollicitation de l'action :**

`M` permet de représenter la part réelle de la caractéristique sollicitée par l'action. Une caractéristique fortement sollicitée peut recevoir une progression plus importante qu'une caractéristique seulement secondairement sollicitée.

Le multiplicateur `M` doit être défini par le système de gameplay en fonction de l'action et ne doit pas servir à contourner les règles générales de progression.

## 6. Effets continus des caractéristiques

Les valeurs de caractéristiques ont des effets **continus** sur les capacités du personnage. Il n'existe pas de tableau de bonus fixes du type « 50 = +10 % » ou « 75 = nouveau pouvoir » pour les actions ordinaires.

À mesure que la valeur augmente, l'efficacité correspondante augmente progressivement. Une différence de quelques points peut donc avoir un effet mesurable, sans créer artificiellement un nouveau palier de puissance.

Les seuils fixes sont réservés à des situations exceptionnelles où une interaction nécessite une condition minimale clairement définie par le gameplay.

Exemples :

- une porte particulièrement lourde peut nécessiter une Force minimale pour être déplacée ;
- une zone ou une prise peut nécessiter une Agilité minimale pour être franchie ;
- un mécanisme extrêmement complexe peut nécessiter un niveau minimal d'Intelligence pour être compris ;
- un détail pratiquement impossible à percevoir peut nécessiter une Perception minimale ;
- un effet mental particulièrement puissant peut nécessiter une Volonté minimale ;
- une interaction sociale exceptionnelle peut nécessiter un Charisme minimal.

Ces seuils ne remplacent pas le calcul continu : ils représentent uniquement des conditions de faisabilité.

## 7. Force

La Force représente la puissance physique brute du personnage.

Son effet est calculé continuellement et peut notamment influencer :

- la puissance des attaques physiques ;
- la capacité à porter une charge ;
- la capacité à pousser, tirer ou soulever des objets ;
- la capacité à déplacer certains éléments du monde ;
- les actions physiques exigeantes ;
- l'efficacité des armes nécessitant une importante puissance physique ;
- certaines actions d'escalade et d'athlétisme.

Plus la Force augmente, plus ces capacités deviennent efficaces. Le jeu ne doit pas imposer de paliers arbitraires pour les actions ordinaires.

### Surcharge d'inventaire

Le simple fait de posséder beaucoup d'objets ne fait pas progresser la Force.

Lorsque le poids de l'inventaire dépasse la capacité de transport du personnage :

- le personnage devient **surchargé** ;
- ses déplacements sont ralentis en fonction de la surcharge ;
- maintenir cette surcharge pendant un effort réel peut progressivement développer la Force.

La capacité de transport augmente progressivement avec la Force. Un inventaire restant sous la capacité normale du personnage ne produit pas de progression de Force liée au poids transporté.

## 8. Agilité

L'Agilité représente la capacité à contrôler rapidement et précisément le corps.

Son effet est calculé continuellement et peut notamment influencer :

- la rapidité d'exécution des mouvements ;
- la précision des mouvements ;
- l'esquive ;
- l'acrobatie ;
- les déplacements sur des surfaces difficiles ;
- l'utilisation d'armes demandant rapidité et précision ;
- la manipulation fine ;
- certaines actions d'escalade et de furtivité.

Une Agilité plus élevée améliore progressivement la coordination et la réactivité sans créer automatiquement de nouvelles capacités à chaque palier.

## 9. Intelligence

L'Intelligence représente la capacité à apprendre, comprendre, raisonner et mémoriser.

Son effet est calculé continuellement et peut notamment influencer :

- la vitesse d'apprentissage des compétences ;
- la compréhension des mécanismes ;
- l'analyse des problèmes ;
- l'assimilation des connaissances ;
- la compréhension des langues ;
- l'artisanat complexe ;
- l'étude de la magie ;
- la mémorisation et l'exploitation d'informations.

L'Intelligence intervient notamment comme modificateur de la progression des compétences, conformément au système défini dans `CHARACTER_SKILLS.md`.

## 10. Perception

La Perception représente la capacité à observer, remarquer et interpréter les éléments présents dans l'environnement.

Son effet est calculé continuellement et peut notamment influencer :

- la détection des ennemis ;
- la détection des ressources ;
- l'observation des détails ;
- la recherche d'indices ;
- la détection des pièges ;
- la perception des mouvements ;
- la précision à distance ;
- la capacité à remarquer des éléments dissimulés.

Plus la Perception augmente, plus les éléments difficiles à remarquer deviennent progressivement accessibles à l'observation du personnage.

## 11. Volonté

La Volonté représente la force mentale, la maîtrise de soi et la capacité à rester concentré malgré la pression.

Son effet est calculé continuellement et peut notamment influencer :

- la résistance au contrôle mental ;
- la résistance à certaines influences magiques ;
- la concentration ;
- la capacité à maintenir une action exigeant une forte concentration ;
- la résistance à la peur ;
- la maîtrise des réactions émotionnelles ;
- la résistance à certaines provocations, tentations ou pressions psychologiques.

Une Volonté plus élevée améliore progressivement la résistance mentale, tandis que les effets exceptionnellement puissants peuvent utiliser un seuil minimal de faisabilité.

## 12. Charisme

Le Charisme représente la capacité à influencer les autres et à interagir efficacement avec eux.

Son effet est calculé continuellement et peut notamment influencer :

- la persuasion ;
- l'intimidation ;
- l'éloquence ;
- le marchandage ;
- la capacité à établir une relation ;
- l'influence exercée sur un groupe ;
- la résolution de conflits par la communication ;
- certaines premières impressions et réactions sociales.

Le Charisme ne force pas automatiquement un PNJ à accepter une demande. Il modifie progressivement les chances et la qualité d'une interaction, en combinaison avec le contexte, les relations, la réputation, la langue et les compétences sociales.

## 13. Exemple — Escalade

Un personnage possède :

- Force = 40
- Agilité = 55

Il escalade une paroi dont l'intensité physique est élevée, avec une difficulté de 70.

L'action peut solliciter :

- fortement la Force ;
- l'Agilité de manière secondaire.

Le jeu calcule alors séparément la progression de chaque caractéristique avec sa difficulté et son multiplicateur propres.

La Force et l'Agilité peuvent donc progresser simultanément, mais pas automatiquement les quatre autres caractéristiques.

## 14. Exemple — Mécanisme complexe

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

## 15. Exemple — différence entre caractéristiques et compétences

Les effets continus permettent de conserver une séparation nette entre aptitude générale et maîtrise technique.

- **Force 80 / Épée 35** : personnage très puissant physiquement, mais encore peu compétent à l'épée.
- **Force 35 / Épée 85** : excellent épéiste techniquement, mais disposant de moins de puissance physique.

Le premier peut produire des attaques naturellement puissantes grâce à sa Force, mais manque de technique. Le second maîtrise très bien les gestes et techniques de l'épée, mais dispose de moins de puissance physique brute.

## 16. Progression multi-caractéristiques

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

## 17. Relation avec les compétences

Les caractéristiques et les compétences restent deux systèmes distincts.

Une caractéristique représente une capacité générale. Une compétence représente un savoir-faire particulier.

Une action peut donc :

- développer une ou plusieurs caractéristiques ;
- développer une compétence ;
- développer simultanément plusieurs caractéristiques et une compétence lorsque l'action le justifie.

Exemple : apprendre une langue développe l'Intelligence et la compétence Linguistique. Utiliser cette langue pour convaincre un marchand peut ensuite solliciter le Charisme et la compétence Linguistique.

## 18. Relation avec les classes

Les classes utilisent les caractéristiques comme base de spécialisation.

Une classe possède certaines caractéristiques principales. Le joueur peut débloquer une autre classe en développant suffisamment les caractéristiques requises et en dépassant les seuils définis pour cette classe.

Les seuils exacts et les effets précis des caractéristiques sur les classes seront définis dans la documentation dédiée aux classes.

## 19. Principe fondamental

> **Le personnage devient progressivement ce que le joueur lui fait réellement pratiquer.**

La progression doit donc être organique, cohérente et directement liée aux actions du joueur plutôt qu'à un système de niveaux global imposant une progression prédéterminée.

## 20. Éléments restant à définir

- nombre exact de points de départ ;
- valeurs minimales ;
- influence numérique précise de chaque caractéristique sur les actions ;
- définition détaillée des multiplicateurs `M` selon les actions ;
- interaction numérique exacte entre caractéristiques et compétences ;
- interaction exacte avec les races ;
- interaction exacte avec les classes.
