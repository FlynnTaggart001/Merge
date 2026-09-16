# Caractéristiques du personnage — Merge

## 1. Caractéristiques fondamentales

Le personnage joueur possède six caractéristiques fondamentales :

- **Force**
- **Agilité**
- **Perception**
- **Intelligence**
- **Volonté**
- **Charisme**

Les caractéristiques représentent les capacités générales du personnage. Elles sont distinctes des compétences, qui représentent les savoir-faire acquis par la pratique.

## 2. Échelle

Les caractéristiques utilisent une échelle de **0 à 20**.

| Valeur | Interprétation générale |
|---:|---|
| 0 | Incapacité ou potentiel extrêmement faible dans le domaine |
| 1–4 | Très faible |
| 5–7 | Faible à ordinaire |
| 8–10 | Humain compétent |
| 11–13 | Humain très compétent / exceptionnel |
| 14–16 | Exceptionnel, au-delà de la norme humaine courante |
| 17–19 | Surhumain |
| 20 | Sommet absolu de la caractéristique |

Les compétences utilisent une échelle indépendante. **Le niveau 50 d'une compétence correspond déjà à une maîtrise extrêmement élevée / surhumaine.**

## 3. Relation avec les compétences

Les caractéristiques et les compétences restent deux systèmes distincts.

- **Caractéristique** : capacité générale du personnage.
- **Compétence** : maîtrise acquise par la pratique.

La progression d'une compétence validée alimente automatiquement les caractéristiques qui lui sont liées. Les poids numériques sont data-driven.

Exemples :

- Épée → Force + Agilité
- Arc → Agilité + Perception
- Crochetage → Agilité + Intelligence
- Invocation → **Volonté + Intelligence**
- Persuasion → Charisme + Intelligence

### Magie

Pour les sept compétences de Magie, **Volonté est la caractéristique principale**. Elle représente la force mentale nécessaire pour imposer, maintenir et contrôler la magie.

**Intelligence est secondaire** : elle représente notamment la compréhension et l'apprentissage des principes magiques, mais ne constitue pas la source principale de la puissance magique.

Les poids numériques exacts restent data-driven.

## 4. Intelligence et progression

L'Intelligence est comprise entre **0 et 20**. Dans la formule de progression des compétences, son modificateur d'apprentissage est :

```text
Multiplicateur d'apprentissage = 0.75 + 0.025 × I
```

où `I` est l'Intelligence.

Ainsi :

| Intelligence | Multiplicateur |
|---:|---:|
| 0 | ×0,75 |
| 5 | ×0,875 |
| 10 | ×1,00 |
| 15 | ×1,125 |
| 20 | ×1,25 |

## 5. Création du personnage

Les règles canoniques de création des compétences sont :

- les **45 compétences** commencent à 5 ;
- **30 points de spécialisation** sont disponibles ;
- maximum **10 points** investis dans une même compétence ;
- maximum de départ d'une compétence : **15** ;
- après la création, aucune répartition manuelle de points de compétence ou de caractéristique.

Les caractéristiques progressent ensuite automatiquement à partir des compétences selon `specs/CHARACTERISTIC_PROGRESSION.md`.

## 6. Progression des caractéristiques

Les caractéristiques progressent automatiquement à partir de la progression validée des compétences liées :

```text
CharacteristicProgress += SkillProgress × Weight
```

Chaque caractéristique possède son propre pool de progression caché et sa courbe de seuils. Lorsqu'un seuil est atteint, la caractéristique augmente de +1 et le surplus est conservé.

Voir `specs/CHARACTERISTIC_PROGRESSION.md` pour la règle complète.

## 7. Classes et voies

Les classes ne sont pas choisies directement à la création. Les compétences et caractéristiques développées déterminent progressivement les voies accessibles.

Lorsqu'une nouvelle voie devient accessible, le joueur est averti et le nom de la classe est révélé.

Les classes normales sont fondamentales. **Déité** constitue une voie spéciale distincte.

Les conditions numériques exactes de Déité et des classes fondamentales ne sont pas encore fixées dans cette documentation. Elles devront être définies dans la spécification dédiée aux classes avant toute implémentation.
