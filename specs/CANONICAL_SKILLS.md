# Merge — Compétences canoniques

**Statut :** APPROUVÉ — liste canonique
**Moteur :** Unreal Engine 5.8.1

Merge possède **45 compétences uniques**.

## Caractéristiques

Les six caractéristiques canoniques sont :

- Force
- Agilité
- Perception
- Intelligence
- Volonté
- Charisme

### Création du personnage

Lors de la création du personnage, le joueur distribue les points de caractéristiques **manuellement**. C'est la seule phase durant laquelle le joueur attribue directement des points de caractéristiques.

Règles actuelles de création :

- Chacune des 6 caractéristiques commence à **6/20**.
- Le joueur reçoit **26 points de caractéristiques supplémentaires** à distribuer librement.
- Une caractéristique ne peut pas dépasser **14/20** lors de la création du personnage.
- Le total initial est donc de **62 points** (`6 × 6 + 26`).
- Aucune caractéristique ne peut être réduite sous sa valeur de base de 6.

### Conversion mathématique caractéristique → compétence à la création

La création du personnage utilise volontairement le chemin inverse de la progression en jeu :

`Caractéristiques → Compétences`

Chaque caractéristique est exprimée sur **20** et chaque compétence sur **100 %**.

La conversion canonique est :

`Pourcentage de compétence = Caractéristique × 4`

Pour une compétence liée à plusieurs caractéristiques, on utilise la moyenne arithmétique des caractéristiques liées :

`Compétence initiale (%) = moyenne(Caractéristiques liées) × 4`

Cette formule donne notamment :

| Caractéristique | Niveau initial correspondant de compétence |
|---:|---:|
| 6/20 | 24 % |
| 7/20 | 28 % |
| 8/20 | 32 % |
| 9/20 | 36 % |
| 10/20 | 40 % |
| 11/20 | 44 % |
| 12/20 | 48 % |
| 13/20 | 52 % |
| 14/20 | 56 % |
| 15/20 | 60 % |
| 16/20 | 64 % |
| 17/20 | 68 % |
| 18/20 | 72 % |
| 19/20 | 76 % |
| 20/20 | 80 % |

Ainsi, au début de la création, les 6/20 de base donnent **24 %** aux compétences qui dépendent entièrement de cette caractéristique.

Exemple : une compétence liée à **Force + Agilité** avec Force = 14/20 et Agilité = 6/20 commence à :

`((14 + 6) / 2) × 4 = 40 %`

Les points de caractéristiques distribués par le joueur modifient donc directement les valeurs initiales des compétences avant le début du jeu.

### Progression après la création : compétence → caractéristique

Après la création du personnage, le système est inversé :

`Compétences → Caractéristiques`

Le joueur ne distribue plus manuellement de points de caractéristique. Les compétences progressent par **Learning by Doing**, et cette progression alimente automatiquement les caractéristiques qui leur sont associées pour la progression.

La conversion inverse utilise la même relation mathématique :

`Caractéristique = moyenne(Compétences contributrices) / 4`

La valeur est limitée au maximum de **20/20** :

`Caractéristique finale = min(20, moyenne(Compétences contributrices) / 4)`

Cela signifie qu'une caractéristique atteint **20/20 lorsque la moyenne cumulée des compétences qui la font progresser atteint au moins 80 %**.

Exemple :

- Compétence A : 79 %
- Compétence B : 81 %
- Moyenne : `(79 + 81) / 2 = 80 %`
- Caractéristique : `80 / 4 = 20/20`

Une compétence individuelle peut donc être inférieure à 80 % sans empêcher la caractéristique d'atteindre 20/20, à condition que les autres compétences contributrices compensent cette valeur.

Autre exemple :

- Compétence A : 70 %
- Compétence B : 90 %
- Compétence C : 80 %
- Compétence D : 80 %
- Moyenne : `80 %`
- Caractéristique : `20/20`

### Relation exacte entre les deux systèmes

Les deux conversions sont mathématiquement inverses sur l'échelle normale :

`Caractéristique → Compétence : C × 4 = S`

`Compétences → Caractéristique : moyenne(S) / 4 = C`

La correspondance fondamentale est donc :

`6/20 ↔ 24 %`

`10/20 ↔ 40 %`

`14/20 ↔ 56 %`

`20/20 ↔ 80 %`

Les compétences peuvent continuer à progresser au-delà de 80 % jusqu'à **100 %**. Une fois que la moyenne des compétences contributrices atteint 80 %, la caractéristique est déjà à son plafond de 20/20 et ne dépasse pas cette valeur.

Cette règle permet aux compétences de conserver une progression indépendante jusqu'à 100 %, tout en faisant de **20/20 le plafond des caractéristiques**.

### Important : liens de création et liens de progression

Une caractéristique peut contribuer au calcul initial d'une compétence sans que cette compétence puisse nécessairement augmenter cette caractéristique après la création.

Les relations **caractéristique → compétence** utilisées à la création ne définissent donc pas automatiquement les relations **compétence → caractéristique** utilisées pour la progression.

La liste des compétences qui alimentent réellement chaque caractéristique pendant le jeu doit être définie explicitement dans les données de progression.

Cette distinction permet par exemple à l'**Intimidation** de dépendre de **Charisme + Force** pour son calcul initial, tout en empêchant la progression de l'Intimidation d'augmenter automatiquement la Force.

## Combat — 9

| Compétence | Caractéristiques pour le calcul initial |
|---|---|
| Épée | Force + Agilité |
| Hache | Force + Agilité |
| Masse | Force |
| Lance | Force + Agilité |
| Dague | Agilité |
| Arme à deux mains | Force + Agilité |
| Arc | Agilité + Perception |
| Arbalète | Perception + Agilité |
| Combat à mains nues | Force + Agilité |

## Défense / mouvement — 6

| Compétence | Caractéristiques pour le calcul initial |
|---|---|
| Esquive | Agilité + Perception |
| Parade | Agilité + Perception |
| Blocage | Force + Agilité |
| Acrobatie | Agilité |
| Escalade | Force + Agilité |
| Athlétisme | Force + Agilité |

**Parade appartient à Défense / mouvement. Ce n'est pas une compétence de Combat.**

## Furtivité — 6

| Compétence | Caractéristiques pour le calcul initial |
|---|---|
| Discrétion | Agilité + Perception |
| Élimination furtive | Agilité + Perception |
| Pickpocket | Agilité + Perception |
| Crochetage | Agilité + Intelligence |
| Camouflage | Perception + Intelligence |
| Filature | Perception + Agilité |

## Magie — 7

| Compétence | Caractéristiques pour le calcul initial |
|---|---|
| Invocation | **Volonté + Intelligence** |
| Nécromancie | **Volonté + Intelligence** |
| Contrôle mental | **Volonté + Intelligence** |
| Magie élémentaire | **Volonté + Intelligence** |
| Magie physique | **Volonté + Intelligence** |
| Magie de groupe | **Volonté + Intelligence** |
| Magie de pacte | **Volonté + Intelligence** |

**La magie repose principalement sur la Volonté. L'Intelligence est secondaire et représente la compréhension et l'apprentissage plutôt que la force magique elle-même.** Les pondérations numériques des caractéristiques restent définies par les données et ne sont pas fixées dans ce document.

## Connaissances — 7

| Compétence | Caractéristiques pour le calcul initial |
|---|---|
| Alchimie | Intelligence + Perception |
| Botanique | Intelligence + Perception |
| Médecine | Intelligence + Perception |
| Histoire | Intelligence |
| Géographie | Intelligence + Perception |
| Créatures | Intelligence + Perception |
| Linguistique | Intelligence + Perception |

## Artisanat — 6

| Compétence | Caractéristiques pour le calcul initial |
|---|---|
| Forge | Force + Intelligence |
| Travail de la matière | Intelligence + Agilité |
| Couture | Agilité + Perception |
| Fabrication d'armes | Intelligence + Force |
| Fabrication d'armures | Intelligence + Force |
| Réparation | Intelligence + Perception |

## Social / communication — 4

| Compétence | Caractéristiques pour le calcul initial |
|---|---|
| Persuasion | Charisme + Intelligence |
| Intimidation | **Charisme + Force** |
| Éloquence | Charisme + Intelligence |
| Marchandage | Charisme + Intelligence |

**L'Intimidation utilise à la fois le Charisme et la Force pour le calcul de sa valeur initiale lors de la création du personnage. Cependant, augmenter l'Intimidation par le Learning by Doing n'augmente pas automatiquement la Force. La progression de l'Intimidation ne doit alimenter la progression de la Force que si elle est explicitement définie comme compétence contributrice de la Force dans les données de progression.**

## Terminologie canonique

- **Lutte n'est pas une compétence ou une caractéristique de Merge.**
- **Parade** est le nom canonique et appartient à **Défense / mouvement**.
- Aucun nom de compétence manquant ne doit être inventé.

## Progression et compensation entre compétences

Pour chaque caractéristique, seules les compétences explicitement désignées comme contributrices à cette caractéristique sont prises en compte.

La progression utilise leur **moyenne arithmétique**. Il n'est donc pas nécessaire que chaque compétence atteigne individuellement le seuil de 80 %.

`Moyenne = Somme des niveaux des compétences contributrices / Nombre de compétences contributrices`

`Caractéristique = min(20, Moyenne / 4)`

Le système permet ainsi la compensation entre compétences : une compétence à 79 % peut être compensée par une autre à 81 %, donnant une moyenne de 80 % et donc une caractéristique à 20/20.

Aucune attribution manuelle de points de caractéristiques n'est possible après la création du personnage.

## Échelle

Le niveau de compétence **50 correspond déjà à un niveau de maîtrise extrêmement élevé / surhumain**. Le calcul initial des compétences comme leur progression doivent respecter cette échelle.

## Règle de conception

Le système doit conserver le cycle suivant :

`Création du personnage : Caractéristiques → Compétences`

`Jeu : Compétences → Caractéristiques`

La formule mathématique de création et sa formule inverse de progression sont désormais canoniques :

`Compétence initiale (%) = moyenne(Caractéristiques liées) × 4`

`Caractéristique après progression = min(20, moyenne(Compétences contributrices) / 4)`

Les liens utilisés pour le calcul initial et ceux utilisés pour la progression après création restent deux ensembles de données distincts.