# Merge — Canonical Skills

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

- Chacune des 6 caractéristiques commence à **6**.
- Le joueur reçoit **26 points de caractéristiques supplémentaires** à distribuer librement.
- Une caractéristique ne peut pas dépasser **14** lors de la création du personnage.
- Le total initial est donc de **62 points** (`6 × 6 + 26`).
- Aucune caractéristique ne peut être réduite sous sa valeur de base de 6.

### Calcul initial des compétences

La direction du système est volontairement **inversée entre la création du personnage et le jeu normal** :

**Lors de la création du personnage :**

`Caractéristiques → Compétences initiales`

La valeur initiale de chaque compétence est calculée à partir des caractéristiques liées à cette compétence. La formule mathématique exacte n'est **pas encore finalisée** et doit être définie avant l'implémentation. Elle doit utiliser les liens caractéristiques-compétences canoniques ci-dessous et respecter l'échelle de progression du jeu.

**Après la création du personnage :**

`Compétences → Caractéristiques`

Le joueur ne distribue pas manuellement de points de compétence ou de caractéristique. Les compétences progressent grâce au **Learning by Doing**, et la progression validée des compétences alimente automatiquement les caractéristiques liées.

La formule de création et la formule de progression après la création sont deux systèmes distincts et ne doivent pas être confondus.

**Règle importante de progression :** une caractéristique peut contribuer au calcul d'une compétence sans que cette compétence puisse augmenter cette caractéristique pendant le jeu. Les relations **caractéristique → compétence** utilisées pour le calcul initial n'impliquent **pas automatiquement** une relation inverse **compétence → caractéristique** pour la progression.

## Combat — 9

| Compétence | Caractéristiques |
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

| Compétence | Caractéristiques |
|---|---|
| Esquive | Agilité + Perception |
| Parade | Agilité + Perception |
| Blocage | Force + Agilité |
| Acrobatie | Agilité |
| Escalade | Force + Agilité |
| Athlétisme | Force + Agilité |

**Parade appartient à Défense / mouvement. Ce n'est pas une compétence de Combat.**

## Furtivité — 6

| Compétence | Caractéristiques |
|---|---|
| Discrétion | Agilité + Perception |
| Élimination furtive | Agilité + Perception |
| Pickpocket | Agilité + Perception |
| Crochetage | Agilité + Intelligence |
| Camouflage | Perception + Intelligence |
| Filature | Perception + Agilité |

## Magie — 7

| Compétence | Caractéristiques |
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

| Compétence | Caractéristiques |
|---|---|
| Alchimie | Intelligence + Perception |
| Botanique | Intelligence + Perception |
| Médecine | Intelligence + Perception |
| Histoire | Intelligence |
| Géographie | Intelligence + Perception |
| Créatures | Intelligence + Perception |
| Linguistique | Intelligence + Perception |

## Artisanat — 6

| Compétence | Caractéristiques |
|---|---|
| Forge | Force + Intelligence |
| Travail de la matière | Intelligence + Agilité |
| Couture | Agilité + Perception |
| Fabrication d'armes | Intelligence + Force |
| Fabrication d'armures | Intelligence + Force |
| Réparation | Intelligence + Perception |

## Social / communication — 4

| Compétence | Caractéristiques |
|---|---|
| Persuasion | Charisme + Intelligence |
| Intimidation | **Charisme + Force** |
| Éloquence | Charisme + Intelligence |
| Marchandage | Charisme + Intelligence |

**L'Intimidation utilise à la fois le Charisme et la Force pour le calcul de sa valeur initiale lors de la création du personnage. Cependant, augmenter l'Intimidation par le Learning by Doing n'augmente pas automatiquement la Force. La progression de l'Intimidation ne doit pas alimenter la progression de la Force ; la Force ne peut progresser que grâce aux compétences explicitement désignées comme contribuant à sa progression.**

## Terminologie canonique

- **Lutte n'est pas une compétence ou une caractéristique de Merge.**
- **Parade** est le nom canonique et appartient à **Défense / mouvement**.
- Aucun nom de compétence manquant ne doit être inventé.

## Relation de progression après la création du personnage

La progression des compétences alimente la progression des caractéristiques :

`ProgressionCaractéristique += ProgressionCompétence × Weight`

Chaque caractéristique possède sa propre réserve de progression cachée et son propre seuil. Lorsqu'un seuil est atteint, la caractéristique augmente de +1 et la progression excédentaire est conservée pour le seuil suivant.

Cette progression est automatique. Le joueur ne peut pas attribuer manuellement de points de caractéristiques après la création du personnage.

**Le `Weight` utilisé pour la progression après la création est spécifique à la relation entre chaque compétence et chaque caractéristique. Le fait qu'une caractéristique soit liée à une compétence pour son calcul initial ne signifie pas automatiquement que cette compétence peut faire progresser cette caractéristique après la création.**

Cette distinction permet par exemple à l'Intimidation de dépendre de la Force pour son calcul initial, tout en empêchant la progression de l'Intimidation d'augmenter la Force.

## Échelle

Le niveau de compétence **50 correspond déjà à un niveau de maîtrise extrêmement élevé / surhumain**. Le calcul initial des compétences comme leur progression doivent respecter cette échelle.

## Règle de conception

Le système doit conserver le cycle suivant :

`Création du personnage : Caractéristiques → Compétences`

`Jeu : Compétences → Caractéristiques`

La conversion mathématique utilisée lors de la création reste **À DÉFINIR** et doit être approuvée avant d'être considérée comme une donnée d'implémentation canonique.
