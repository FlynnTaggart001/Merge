# Merge — Compétences canoniques

**Statut :** APPROUVÉ — liste canonique
**Moteur :** Unreal Engine 5.8.4

Merge possède **46 compétences uniques**.

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
- Le joueur reçoit **20 points de caractéristiques supplémentaires** à distribuer librement.
- Une caractéristique ne peut pas dépasser **14/20** lors de la création du personnage.
- Le total initial est donc de **56 points** (`6 × 6 + 20`).
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

Le joueur ne distribue plus manuellement de points de caractéristique. Les activités pratiquées par le joueur génèrent des **points de progression de compétence** lorsqu'elles sont validées par le système de Learning by Doing.

Ces mêmes points de progression de compétence alimentent automatiquement la progression des caractéristiques auxquelles la compétence contribue.

Le pipeline canonique est :

`Activité validée → points de compétence → augmentation de la compétence → contribution pondérée à la caractéristique → seuil → caractéristique +1`

La progression des caractéristiques utilise une **réserve de progression cachée**, des **poids** et des **seuils data-driven**, définis dans `specs/CHARACTERISTIC_PROGRESSION.md`.

Lorsqu'un seuil est atteint, la caractéristique augmente de +1 et le surplus de progression est conservé.

Il n'existe donc **pas de recalcul direct de la caractéristique à partir de la moyenne des compétences** pendant le jeu. La formule `moyenne(compétences) / 4` n'est pas une règle runtime de progression.

### Important : liens de création et liens de progression

Les deux types de relations sont volontairement distincts :

1. **Liens de création :** quelles caractéristiques déterminent la valeur initiale d'une compétence.
2. **Liens de progression :** quelles compétences font progresser une caractéristique pendant le jeu.

Une compétence peut donc utiliser plusieurs caractéristiques pour être calculée à la création, puis ne faire progresser qu'une seule caractéristique pendant le jeu.

#### Cas canonique : Intimidation

L'**Intimidation** est calculée à la création à partir de **Charisme + Force** :

`Intimidation initiale = moyenne(Charisme, Force) × 4`

Mais après la création, lorsqu'un joueur améliore son **Intimidation** par le **Learning by Doing** :

`Intimidation → Charisme`

`Intimidation ↛ Force`

Autrement dit : **la Force et le Charisme servent tous les deux à déterminer le niveau initial d'Intimidation, mais la progression de l'Intimidation augmente uniquement le Charisme. Elle n'augmente jamais automatiquement la Force.**

Cette distinction est canonique et doit être conservée dans les données de progression du jeu.

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

## Social / communication — 5

| Compétence | Caractéristiques pour le calcul initial |
|---|---|
| Persuasion | Charisme + Intelligence |
| Intimidation | **Charisme + Force** |
| Éloquence | Charisme + Intelligence |
| Marchandage | Charisme + Intelligence |
| Domptage | Perception + Charisme |

## Terminologie canonique

- **Lutte n'est pas une compétence ou une caractéristique de Merge.**
- **Domptage est une compétence canonique.**
- **Parade** est le nom canonique et appartient à **Défense / mouvement**.
- Aucun nom de compétence manquant ne doit être inventé.

## Progression des compétences vers les caractéristiques

Pour chaque caractéristique, seules les compétences explicitement désignées comme contributrices pendant le jeu alimentent sa réserve de progression.

Les points de progression gagnés par une activité validée font donc deux choses dans le même événement :

1. ils augmentent la progression de la compétence pratiquée ;
2. ils alimentent la progression cachée des caractéristiques auxquelles cette compétence contribue, selon son poids.

`CharacteristicProgress += SkillProgress × Weight`

Lorsque le seuil suivant est atteint :

`while CharacteristicProgress >= Threshold(C + 1):`

`    CharacteristicProgress -= Threshold(C + 1)`

`    C += 1`

Les poids, seuils et limites sont data-driven.

**Il n'y a pas de recomposition directe de la caractéristique à partir de la moyenne des compétences.** Une compétence peut donc continuer à progresser sans provoquer immédiatement +1 dans une caractéristique : elle accumule une contribution jusqu'au prochain seuil.

Pour l'**Intimidation** :
- création : `moyenne(Charisme, Force) × 4` ;
- progression : les points gagnés en Intimidation contribuent au **Charisme uniquement** ;
- Intimidation ne contribue jamais automatiquement à la Force.

## Règle d'activité

Toute activité pertinente ne donne pas automatiquement de progression : elle doit être validée par les règles de contexte et d'anti-farming de `specs/SKILL_PROGRESSION.md`. Une activité réellement pratiquée et validée génère des points de compétence ; ces mêmes points alimentent la progression des caractéristiques selon les liens de progression.

## Règle de conception

Le système doit conserver le cycle suivant :

`Création du personnage : Caractéristiques → Compétences`

`Jeu : Compétences → Caractéristiques`

La formule de création est canonique :

`Compétence initiale (%) = moyenne(Caractéristiques liées) × 4`

Après la création, la règle canonique est un pipeline de progression :

`Points de compétence gagnés → progression de compétence → contribution pondérée → seuil de caractéristique`

La moyenne des compétences n'est pas utilisée comme formule runtime de recalcul des caractéristiques.

Les liens utilisés pour le calcul initial et ceux utilisés pour la progression après création restent deux ensembles de données distincts.
