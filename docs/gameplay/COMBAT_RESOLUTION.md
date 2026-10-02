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
- `Agilité` = caractéristique Agilité, 0–20 ;
- `Perception` = caractéristique Perception, 0–20.

La **Force n'entre pas dans le score de chance de toucher** dans cette première définition. Elle intervient principalement dans le calcul des dégâts après une touche.

La même logique sera adaptée aux autres compétences d'attaque : la compétence spécifique reste le facteur principal, avec les caractéristiques réellement pertinentes pour l'action.

### 2.2 Score d'esquive

```text
E = 0.50 × Esquive + 0.35 × Agilité + 0.15 × Perception
```

- `E` = score défensif utilisé contre l'attaque ;
- `Esquive` = compétence Esquive, 0–100 ;
- `Agilité` = caractéristique Agilité, 0–20 ;
- `Perception` = caractéristique Perception, 0–20.

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

## 8. Attaque contre parade

La **Parade** est une défense active fondée sur le **timing**, conformément au système de combat canonique. Elle ne se résout pas par une probabilité logistique indépendante.

La tentative de parade doit être déclenchée par l'input du joueur et évaluée dans une fenêtre temporelle définie par les données de combat.

### 8.1 Résolution temporelle

```text
Attaque ennemie
      ↓
Fenêtre de parade
      ↓
Input du joueur ?
   ├── Non → attaque résolue normalement
   └── Oui
        ↓
Timing valide ?
   ├── Oui → parade réussie
   └── Non → parade ratée
```

Les valeurs exactes de la fenêtre de parade restent **À DÉFINIR** et seront équilibrées pendant le prototype.

La compétence **Parade**, ainsi que les caractéristiques pertinentes, peuvent influencer les paramètres de résolution prévus par le système, mais aucune formule probabiliste n'est introduite ici tant qu'elle n'est pas définie par le game design canonique.

### 8.2 Résultats canoniques

- **Parade réussie** → aucun dégât subi.
- **Parade parfaite** → aucun dégât + contre-attaque automatique + coup critique.
- **Parade ratée** → le joueur subit un coup critique.
- Les attaques explicitement définies comme non parables restent non parables.

Le système **Réflexe** ne déclenche pas une parade et ne modifie pas sa fenêtre.

### 8.3 Critiques liés à la parade

Une contre-attaque issue d'une parade parfaite constitue un **coup critique automatique**. Elle applique le multiplicateur critique canonique de **2.0×** défini dans `specs/COMBAT_SYSTEM_SPEC.md` et `specs/WEAPONS_AND_EQUIPMENT_SPEC.md`.
## 9. Attaque contre blocage

Le **Blocage** représente une tentative d'arrêter ou d'absorber physiquement une attaque, notamment avec un bouclier, une arme ou un autre moyen défensif approprié.

Contrairement à la Parade, qui repose sur la précision du geste et le timing, le Blocage accorde davantage de poids à la capacité physique à maintenir et absorber le choc. La Force intervient donc directement dans le score de Blocage.

### 9.1 Score de blocage

```text
B = 0.50 × Blocage + 0.30 × Force + 0.20 × Agilité
```

- `B` = score défensif utilisé contre l'attaque ;
- `Blocage` = compétence Blocage, 0–100 ;
- `Force` = caractéristique Force, 0–20 ;
- `Agilité` = caractéristique Agilité, 0–20.

### 9.2 Écart entre attaque et blocage

On définit :

```text
Δ = A − B
```

- `Δ < 0` : le défenseur possède l'avantage et a davantage de chances d'arrêter l'attaque ;
- `Δ = 0` : les capacités sont équilibrées ;
- `Δ > 0` : l'attaquant possède l'avantage et a davantage de chances de traverser le blocage.

### 9.3 Probabilité que l'attaque passe

```text
P_passer = 5 + 90 / (1 + e^(−Δ / 15))
```

La valeur finale est bornée entre **5 % et 95 %**.

La même courbe logistique est utilisée afin de conserver une progression cohérente avec l'Esquive et le Blocage.

### 9.4 Référence de comportement

| Écart `Δ` | Probabilité approximative que l'attaque passe |
|---:|---:|
| -60 | 6,6 % |
| -40 | 11,1 % |
| -20 | 23,3 % |
| -10 | 39,1 % |
| 0 | 50 % |
| +10 | 60,9 % |
| +20 | 76,7 % |
| +40 | 88,9 % |
| +60 | 93,4 % |

### 9.5 Différence avec Parade et Esquive

| Défense | Fonction principale | Facteurs complémentaires |
|---|---|---|
| Esquive | Éviter complètement l'attaque | Agilité + Perception |
| Parade | Dévier/intercepter précisément l'attaque | Agilité + Perception |
| Blocage | Arrêter/absorber physiquement l'attaque | Force + Agilité |

## 10. Combat contre un adversaire très supérieur

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

## 11. Extension du modèle

Le même principe d'opposition progressive servira de base aux autres situations de combat :

- attaque → Esquive ;
- attaque → Parade ;
- attaque → Blocage ;
- attaques à distance → capacités défensives pertinentes ;
- autres actions opposées entre personnages.

Les coefficients précis des autres oppositions seront définis séparément afin de ne pas supposer qu'une même caractéristique possède exactement le même poids dans toutes les situations.

## 12. État actuel

Les trois oppositions suivantes sont maintenant définies comme base numérique du système de combat :

- **Attaque ↔ Esquive** ;
- **Attaque ↔ Parade** ;
- **Attaque ↔ Blocage**.

Restent à définir :

- formule des dégâts ;
- influence précise des armes et armures ;
- interactions avec les capacités spéciales et les techniques débloquées par les compétences ;
- éventuels effets des états physiques.
