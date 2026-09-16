# Résolution des actions de combat — Merge

## 1. Principe général

Le combat de **Merge** utilise des actions opposées entre les capacités de l'attaquant et celles du défenseur.

Une attaque de mêlée n'utilise pas une difficulté fixe artificielle. La probabilité de réussite dépend de la comparaison entre les capacités pertinentes des deux personnages.

Les circonstances qui rendent l'action plus ou moins favorable font partie de la situation de combat et doivent être représentées par les valeurs pertinentes du système plutôt que par un coefficient générique de « circonstance ».

Le principe fondamental est :

> **Plus l'écart entre les capacités de l'attaquant et celles du défenseur est important, plus le personnage ayant les capacités les plus faibles a de difficultés à réussir son action.**

L'effet de l'écart est progressif. Un très grand désavantage rend une réussite très rare, mais ne crée pas automatiquement une impossibilité absolue.

## 2. Attaque contre esquive

Pour une attaque à l'épée, le calcul de la capacité offensive utilise principalement la compétence d'arme, l'Agilité et la Perception.

### 2.1 Score d'attaque

```text
A = 0.50 × Épée + 0.30 × Agilité + 0.20 × Perception
```

- `A` = score offensif utilisé pour l'opposition contre l'Esquive ;
- `Épée` = compétence Épée, 0–100 ;
- `Agilité` = caractéristique Agilité, 0–100 ;
- `Perception` = caractéristique Perception, 0–100.

La **Force n'entre pas dans le score de chance de toucher** dans cette première définition. Elle intervient principalement dans le calcul des dégâts après une touche.

La même logique sera adaptée aux autres compétences d'attaque : la compétence spécifique reste le facteur principal, avec les caractéristiques réellement pertinentes pour l'action.

### 2.2 Score d'esquive

```text
E = 0.50 × Esquive + 0.35 × Agilité + 0.15 × Perception
```

- `E` = score défensif utilisé contre l'attaque ;
- `Esquive` = compétence Esquive, 0–100 ;
- `Agilité` = caractéristique Agilité, 0–100 ;
- `Perception` = caractéristique Perception, 0–100.

La compétence **Esquive** constitue donc le facteur principal, tandis que l'Agilité et la Perception représentent les capacités physiques et perceptives nécessaires pour éviter le mouvement adverse.

## 3. Écart entre attaque et esquive

On définit l'écart :

```text
Δ = A − E
```

- `Δ < 0` : le défenseur possède un avantage ;
- `Δ = 0` : les capacités sont équilibrées ;
- `Δ > 0` : l'attaquant possède un avantage.

## 4. Probabilité de toucher

La probabilité de toucher utilise une courbe logistique afin que l'influence de l'écart soit progressive et non binaire.

```text
P_toucher = 5 + 90 / (1 + e^(−Δ / 15))
```

La valeur finale est bornée entre **5 % et 95 %**.

### 4.1 Référence de comportement

| Écart `Δ` | Probabilité approximative de toucher |
|---:|---:|
| -60 | 6,6 % |
| -40 | 11,1 % |
| -30 | 15,7 % |
| -20 | 23,3 % |
| -10 | 39,1 % |
| 0 | 50 % |
| +10 | 60,9 % |
| +20 | 76,7 % |
| +30 | 84,3 % |
| +40 | 88,9 % |
| +60 | 93,4 % |

Cette courbe signifie qu'un personnage nettement inférieur peut encore réussir exceptionnellement, tandis qu'un personnage nettement supérieur touche beaucoup plus souvent.

## 5. Exemple

### Attaquant

- Épée = 20
- Agilité = 25
- Perception = 20

```text
A = 0.50 × 20 + 0.30 × 25 + 0.20 × 20
A = 10 + 7.5 + 4
A = 21.5
```

### Défenseur

- Esquive = 80
- Agilité = 70
- Perception = 60

```text
E = 0.50 × 80 + 0.35 × 70 + 0.15 × 60
E = 40 + 24.5 + 9
E = 73.5
```

Écart :

```text
Δ = 21.5 − 73.5
Δ = −52
```

La probabilité de toucher devient donc très faible. Le personnage faible n'est cependant pas déclaré incapable d'attaquer.

## 6. Toucher et dégâts sont deux calculs distincts

Le système ne considère pas qu'une faible compétence d'attaque signifie automatiquement « aucun dégât ».

La séquence générale est :

```text
1. Calcul de la capacité offensive.
2. Calcul de la capacité défensive pertinente.
3. Détermination de la probabilité de réussite.
4. Résolution de l'action.
5. Si l'attaque touche : calcul des dégâts.
```

Ainsi, un personnage peu compétent peut rarement toucher un adversaire supérieur, mais lorsqu'il réussit, **l'attaque inflige bien des dégâts** selon les paramètres de dégâts de l'arme et de l'attaquant.

La Force sera notamment prise en compte dans ce calcul de dégâts, avec l'arme et la maîtrise technique, lorsque le système de dégâts sera défini.

## 7. Combat contre un adversaire très supérieur

Un très grand écart entre les capacités ne crée pas de « niveau requis » artificiel.

Il rend simplement le combat direct progressivement plus défavorable.

Lorsque l'adversaire est largement supérieur, le joueur peut chercher une autre solution :

- piège permettant de l'immobiliser ou de le gêner ;
- embuscade ;
- poison ou préparation alchimique ;
- furtivité ;
- exploitation du terrain ou de l'environnement ;
- magie ;
- aide d'alliés ou de PNJ ;
- manipulation sociale ;
- connaissances spécifiques de la cible ou du monde.

Ces méthodes permettent de réduire ou de contourner l'avantage de l'adversaire sans introduire de règle artificielle du type « niveau minimum obligatoire ».

## 8. Extension du modèle

Le même principe d'opposition progressive servira de base aux autres situations de combat :

- attaque → Esquive ;
- attaque → Parade ;
- attaque → Blocage ;
- attaques à distance → capacités défensives pertinentes ;
- autres actions opposées entre personnages.

Les coefficients précis des autres oppositions seront définis séparément afin de ne pas supposer qu'une même caractéristique possède exactement le même poids dans toutes les situations.

## 9. État actuel

La formule **Attaque ↔ Esquive** est définie comme base numérique du système de combat.

Restent à définir :

- formule Attaque ↔ Parade ;
- formule Attaque ↔ Blocage ;
- formule des dégâts ;
- influence précise des armes et armures ;
- interactions avec les capacités spéciales et les techniques débloquées par les compétences ;
- éventuels effets des états physiques.
