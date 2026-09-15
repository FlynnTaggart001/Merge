# Système de compétences — Merge

## 1. Objectif

Les compétences représentent les savoir-faire spécifiques du personnage. Elles sont distinctes des caractéristiques : une caractéristique représente une capacité générale, tandis qu'une compétence représente un domaine de pratique précis.

Le système suit le principe fondamental de **Merge** : progression par utilisation (*learning by doing*).

Une action peut développer une compétence ainsi qu'une ou plusieurs caractéristiques lorsque l'activité le justifie réellement.

## 2. Principes généraux

- Les compétences sont spécialisées et indépendantes les unes des autres.
- Les compétences utilisent une échelle de **0 à 100**.
- Le personnage progresse en pratiquant réellement la compétence concernée.
- **Seules les réussites accordent une progression de compétence.** Une tentative échouée accorde 0 progression.
- Il n'existe **aucune pénalité artificielle anti-répétition** : si le joueur réussit réellement plusieurs actions difficiles, chacune peut faire progresser la compétence.
- La difficulté et la complexité de l'action influencent la progression.
- La difficulté d'une action est **prédéfinie pour cette action ou cet objet**. Elle n'est pas automatiquement augmentée ou diminuée selon le niveau du personnage.
- Une action devenue trop facile par rapport au niveau actuel peut donner **0 progression**.
- La progression devient progressivement plus lente lorsque le niveau de compétence augmente.
- L'Intelligence accélère l'apprentissage, mais ne donne pas de progression sans pratique et ne garantit pas la réussite.
- Les compétences sont **permanentes** : elles ne diminuent pas simplement parce qu'elles ne sont pas utilisées.
- La valeur réelle d'une compétence est conservée avec des **décimales** en interne. L'interface peut afficher une valeur arrondie.
- Les compétences ne sont pas limitées par la classe actuelle du personnage.
- Les classes représentent une orientation et non une restriction définitive des savoir-faire.
- Les caractéristiques peuvent soutenir une compétence, mais ne la remplacent pas.

### 2.1 Échelle de difficulté

Chaque action pouvant faire progresser une compétence reçoit une difficulté prédéfinie sur une échelle de 0 à 100 :

| Niveau de difficulté | Valeur de référence |
|---|---:|
| Très facile | 10 |
| Facile | 25 |
| Moyenne | 50 |
| Difficile | 70 |
| Très difficile | 85 |
| Exceptionnelle | 100 |

Cette échelle constitue une base commune à toutes les compétences. Des valeurs intermédiaires peuvent être utilisées lorsqu'une action se situe entre deux catégories.

Une difficulté supérieure à 100 peut être utilisée pour des situations **exceptionnelles** qui dépassent le niveau normal de la compétence, mais la progression de la compétence reste plafonnée à 100.

### 2.2 Progression selon la difficulté

La progression dépend de l'écart entre la difficulté de l'action et le niveau actuel de la compétence.

- Une action **beaucoup trop facile** par rapport au niveau actuel : 0 progression.
- Une action légèrement plus facile que le niveau actuel : progression faible.
- Une action adaptée au niveau : progression normale.
- Une action nettement plus difficile : progression importante.
- Une action exceptionnellement difficile : progression très importante, dans les limites du système.

Le jeu ne pénalise donc pas artificiellement le joueur pour avoir trouvé plusieurs actions difficiles du même type. Une réussite réelle reste une expérience d'apprentissage valide.

### 2.3 Exemple — Crochetage

Un personnage possède **Crochetage 80** :

- serrure difficulté 25 → **0 progression** ;
- serrure difficulté 50 → **0 progression** ;
- serrure difficulté 70 → **0 progression** ;
- serrure difficulté 85 → progression ;
- serrure difficulté 100 → progression plus importante.

Le personnage doit donc progressivement rencontrer des serrures réellement plus complexes pour continuer à développer un niveau élevé de Crochetage.

## 3. Formule universelle de progression

La même formule est utilisée pour **toutes les compétences**. Elle ne dépend pas du nom de la compétence : seules les valeurs de niveau, de difficulté et d'Intelligence changent.

On définit :

- `S` = niveau actuel de la compétence, compris entre 0 et 100 ;
- `D` = difficulté prédéfinie de l'action ;
- `I` = Intelligence du personnage, comprise entre 0 et 100 ;
- `P` = progression accordée par une réussite.

Pour une action réussie :

```text
P = 0.9 × max(0, (D − S + 15) / 50) × 1 / (1 + 0.012 × S) × (0.75 + 0.005 × I)
```

La nouvelle valeur de la compétence est ensuite :

```text
S_nouveau = min(100, S + P)
```

Une tentative échouée applique directement :

```text
P = 0
```

### 3.1 Interprétation de la formule

#### A. Écart entre difficulté et compétence

```text
max(0, (D − S + 15) / 50)
```

Cette partie mesure à quel point l'action représente un défi pour le personnage.

Si l'action est au moins **15 points plus facile** que la compétence actuelle (`D ≤ S − 15`), cette partie devient 0 et l'action ne donne aucune progression.

#### B. Ralentissement avec le niveau

```text
1 / (1 + 0.012 × S)
```

Plus la compétence est élevée, moins une réussite individuelle apporte de progression. Le ralentissement est continu et ne repose pas sur des paliers artificiels.

#### C. Influence de l'Intelligence

```text
0.75 + 0.005 × I
```

L'effet de l'Intelligence est volontairement modéré :

| Intelligence | Multiplicateur d'apprentissage |
|---:|---:|
| 0 | ×0,75 |
| 25 | ×0,875 |
| 50 | ×1,00 |
| 75 | ×1,125 |
| 100 | ×1,25 |

L'Intelligence permet donc d'apprendre plus rapidement, sans permettre de progresser sans pratiquer.

### 3.2 Progression interne avec décimales

La compétence est stockée avec sa précision réelle en interne.

Exemple :

```text
Crochetage = 47.35
Réussite → +0.42
Crochetage = 47.77
```

L'interface peut afficher simplement `47`, tandis que le système conserve `47.77`.

### 3.3 Exemples de progression

Avec Intelligence = 50 :

| Compétence actuelle | Difficulté | Progression approximative |
|---:|---:|---:|
| 20 | 25 | +0,29 |
| 20 | 70 | +0,94 |
| 40 | 50 | +0,30 |
| 40 | 70 | +0,55 |
| 60 | 70 | +0,26 |
| 60 | 85 | +0,42 |
| 80 | 85 | +0,18 |
| 80 | 100 | +0,32 |
| 90 | 100 | +0,22 |

Ces valeurs sont des exemples de comportement de la formule ; le moteur doit calculer la valeur exacte sans arrondir la progression interne.

## 4. Résolution des actions

Le système distingue deux grandes catégories d'actions : **les actions contre une difficulté fixe** et **les actions opposées à un autre personnage**.

### 4.1 Actions contre une difficulté fixe

Pour une action qui ne s'oppose pas directement aux capacités d'un autre personnage, le résultat est déterminé à partir de :

- la ou les caractéristiques réellement sollicitées ;
- la compétence concernée ;
- la difficulté prédéfinie de l'action.

Toutes les circonstances qui rendent l'action plus ou moins difficile sont intégrées dans **la difficulté de l'action**. Il n'existe pas de coefficient séparé de « circonstance ».

Exemples : crochetage, fabrication, escalade d'une paroi, identification d'une plante ou certaines interactions sociales.

### 4.2 Actions opposées

Lorsqu'une action est directement opposée aux capacités d'un autre personnage, il n'existe pas de difficulté fixe artificielle.

Le résultat dépend de la comparaison entre les capacités des deux personnages.

Le principe général est :

> **Plus l'écart entre les capacités de l'attaquant et celles du défenseur est important, plus le personnage inférieur a de difficultés à réussir son action.**

L'écart produit un effet **progressif** sur les probabilités : il ne doit pas créer de seuil arbitraire où une action devient soudainement impossible.

Même avec un très grand désavantage, une faible possibilité de réussite peut subsister lorsque le contexte le permet. À l'inverse, une supériorité importante rend l'action adverse de plus en plus difficile.

### 4.3 Exemple — Combat à l'épée

Une attaque à l'épée n'a pas de « difficulté 40 », « difficulté 70 », etc. L'attaque est opposée aux capacités défensives de l'adversaire.

Pour une attaque, le système distingue notamment :

1. **L'attaque touche ou ne touche pas.**
2. **Le défenseur peut tenter d'esquiver, de parer ou de bloquer selon ses capacités et la situation.**
3. **Si l'attaque passe, les dégâts sont ensuite calculés.**

Les capacités offensives et défensives utilisent les caractéristiques et compétences pertinentes.

Par exemple, l'Agilité peut participer à la capacité à placer ou éviter un mouvement, tandis que **Épée** représente la maîtrise technique de l'arme et **Esquive**, **Parade** ou **Blocage** représentent les compétences défensives correspondantes.

### 4.4 Toucher et dégâts sont séparés

Un personnage peut avoir une faible compétence d'attaque et néanmoins toucher son adversaire.

Si l'attaque passe, elle inflige des dégâts selon les paramètres pertinents de l'attaque, notamment la puissance physique, l'arme et la maîtrise technique. Une faible maîtrise ne transforme donc pas automatiquement une attaque réussie en attaque sans dégâts.

La différence entre un combattant faible et un combattant extrêmement puissant doit principalement se traduire par la **fréquence de réussite, la qualité des mouvements, la maîtrise technique et l'efficacité des attaques**, et non par une règle binaire « assez de niveau = dégâts / pas assez de niveau = aucun dégât ».

## 5. Écart de puissance et stratégie

Un écart important entre deux personnages ne doit pas rendre le combat frontal artificiellement impossible. Il doit rendre le combat direct **de plus en plus défavorable** au personnage inférieur.

Lorsqu'un personnage affronte un adversaire largement supérieur :

- ses attaques ont une probabilité beaucoup plus faible de toucher ;
- l'adversaire peut esquiver plus facilement ;
- ses capacités de parade ou de blocage sont plus difficiles à surpasser ;
- ses attaques restent dangereuses même lorsqu'elles sont rares ;
- le combat frontal devient progressivement une mauvaise stratégie.

Le joueur doit pouvoir compenser un désavantage direct en utilisant ses autres compétences, l'environnement ou la préparation.

### 5.1 Subterfuges et préparation

Un personnage nettement inférieur peut chercher à réduire ou contourner l'avantage de l'adversaire au lieu de l'affronter directement.

Les solutions possibles comprennent notamment :

- poser un piège pour immobiliser ou gêner l'adversaire ;
- utiliser du poison ou une préparation alchimique ;
- préparer une embuscade ;
- exploiter le terrain ou l'environnement ;
- utiliser la furtivité ;
- utiliser la magie ;
- obtenir l'aide d'alliés ou de PNJ ;
- manipuler une situation sociale ;
- utiliser ses connaissances du monde ou de la cible.

Ces solutions ne constituent pas des « niveaux requis » alternatifs. Elles permettent au joueur de **résoudre un problème de puissance par la préparation, la connaissance et la stratégie**.

Un adversaire très supérieur peut donc rester dangereux tout en étant vaincu par un personnage beaucoup plus faible qui prépare correctement son approche.

## 6. Compétences de combat

- **Épée** — Force + Agilité
- **Hache** — Force + Agilité
- **Masse** — Force
- **Lance** — Force + Agilité
- **Dague** — Agilité
- **Arme à deux mains** — Force + Agilité
- **Arc** — Agilité + Perception
- **Arbalète** — Perception + Agilité
- **Combat à mains nues** — Force + Agilité
- **Parade** — Agilité + Perception

## 7. Compétences de défense et mouvement

- **Esquive** — Agilité + Perception
- **Parade** — Agilité + Perception
- **Blocage** — Force + Agilité
- **Acrobatie** — Agilité
- **Escalade** — Force + Agilité
- **Athlétisme** — Force + Agilité

La **Parade** représente la capacité à dévier une attaque avec un timing précis. Le **Blocage** représente l'arrêt ou l'absorption d'une attaque, notamment avec un bouclier ou une arme. L'**Esquive** repose sur le déplacement et le timing pour éviter l'attaque.

## 8. Compétences de furtivité

- **Discrétion** — Agilité + Perception
- **Élimination furtive** — Agilité + Perception
- **Pickpocket** — Agilité + Perception
- **Crochetage** — Agilité + Intelligence
- **Camouflage** — Perception + Intelligence

La **Discrétion** inclut également la capacité à suivre une personne sans être repéré. La **Filature** n'est donc pas une compétence distincte.

## 9. Compétences de magie

- **Invocation** — Intelligence + Volonté
- **Nécromancie** — Intelligence + Volonté
- **Contrôle mental** — Intelligence + Volonté
- **Magie élémentaire** — Intelligence + Volonté
- **Magie physique** — Intelligence + Volonté
- **Magie de groupe** — Intelligence + Volonté
- **Magie de pacte** — Intelligence + Volonté

### 9.1 Magie physique

La Magie physique comprend notamment :

- le renforcement physique ;
- les soins ;
- la modification des capacités physiques.

### 9.2 Magie de groupe

La Magie de groupe ne désigne pas simplement une magie affectant plusieurs cibles. Elle représente une **forme de magie à très grande échelle et d'une puissance exceptionnelle**.

Elle peut notamment permettre :

- avec l'Invocation, d'invoquer des créatures extrêmement puissantes, comme une Hydre ;
- avec la Nécromancie, de produire des phénomènes nécromantiques d'une ampleur exceptionnelle ;
- avec le Contrôle mental, d'exercer une influence sur un très grand nombre d'individus ;
- avec la Magie élémentaire, de provoquer des phénomènes naturels majeurs, pouvant aller jusqu'à des catastrophes naturelles.

La Magie de groupe constitue donc un niveau de puissance supérieur pouvant avoir des conséquences importantes sur le monde.

### 9.3 Magie de pacte

La Magie de pacte repose sur des pactes, contrats ou liens magiques avec des entités. Ses règles détaillées, conditions et contreparties restent à définir.

## 10. Compétences de connaissances

- **Alchimie** — Intelligence + Perception
- **Botanique** — Intelligence + Perception
- **Médecine** — Intelligence + Perception
- **Histoire** — Intelligence
- **Géographie** — Intelligence + Perception
- **Créatures** — Intelligence + Perception
- **Linguistique** — Intelligence + Perception

La **Médecine** inclut l'Anatomie. Il n'existe pas de compétence séparée d'Anatomie.

La **Linguistique** couvre l'apprentissage et la compréhension des langues. Elle reste une compétence de Connaissances et n'est pas dupliquée dans le domaine social.

## 11. Compétences d'artisanat

- **Forge** — Force + Intelligence
- **Travail de la matière** — Intelligence + Agilité
- **Couture** — Agilité + Perception
- **Fabrication d'armes** — Intelligence + Force
- **Fabrication d'armures** — Intelligence + Force
- **Réparation** — Intelligence + Perception

Le **Travail de la matière** regroupe notamment le travail du bois, du cuir et d'autres matériaux ne nécessitant pas une compétence spécialisée distincte.

La Forge, la Fabrication d'armes et la Fabrication d'armures restent des compétences distinctes.

## 12. Compétences sociales et communication

- **Persuasion** — Charisme + Intelligence
- **Intimidation** — Charisme + Force
- **Éloquence** — Charisme + Intelligence
- **Marchandage** — Charisme + Intelligence

Il n'existe pas de compétence d'**Étiquette**. Les comportements sociaux et la manière dont les PNJ réagissent au personnage sont notamment gérés par le système de réputation et les autres systèmes sociaux du jeu.

## 13. Caractéristiques et compétences

Les caractéristiques associées à chaque compétence indiquent les capacités générales principalement sollicitées par cette pratique. Elles ne remplacent pas la compétence elle-même.

Par exemple :

- utiliser une épée développe la compétence **Épée** et peut solliciter Force et Agilité ;
- apprendre une langue développe **Linguistique** et sollicite notamment Intelligence ;
- négocier dans une langue étrangère peut solliciter **Linguistique**, **Marchandage** et Charisme ;
- réussir une parade développe **Parade** et sollicite Agilité et Perception.

Une même action peut donc développer plusieurs éléments du système lorsqu'elle exerce réellement plusieurs capacités.

## 14. Structure actuelle

Le système contient actuellement **45 compétences** réparties en 7 domaines :

| Domaine | Nombre |
|---|---:|
| Combat | 10 |
| Défense / mouvement | 6 |
| Furtivité | 5 |
| Magie | 7 |
| Connaissances | 7 |
| Artisanat | 6 |
| Social / communication | 4 |
| **Total** | **45** |

## 15. Éléments restant à définir

- valeur initiale des compétences ;
- effets précis des différents niveaux ;
- influence numérique exacte des caractéristiques sur chaque compétence ;
- formule numérique précise des actions opposées ;
- calcul détaillé des dégâts ;
- influence exacte de l'équipement ;
- éventuels prérequis ;
- interactions détaillées avec les races ;
- interactions détaillées avec les classes ;
- fonctionnement précis des compétences magiques ;
- règles détaillées de chaque compétence ;
- paramètres d'équilibrage de la formule si les tests en jeu montrent qu'un ajustement est nécessaire.
