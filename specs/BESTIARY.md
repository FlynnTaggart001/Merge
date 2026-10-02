# Merge — Weapons and Equipment Specification

**Status:** SPÉCIFIÉ — système de conception actuel  
**Engine:** Unreal Engine 5.8.1

---

## 1. Objectif

Ce document complète `specs/COMBAT_SYSTEM_SPEC.md` pour les règles d'armes, d'équipement et de réparation.

Il ne doit pas remplacer le document canonique du combat. Il sert à clarifier les règles déjà décidées et à marquer explicitement les points encore à définir.

---

## 2. Règles déjà décidées

### 2.1 Dégâts

Les dégâts utilisent :
- la base de l'arme ;
- la maîtrise réelle de l'arme ;
- le bonus de Force.

Ces contributions sont déjà décidées comme principes canoniques.

Le coefficient exact de la Force, la contribution exacte de la maîtrise de l'arme et la formule complète des dégâts restent **À DÉFINIR**.

Les familles d'armes ont une base de dégâts fixe :
- les armes d'une même catégorie partagent une base fixe ;
- une exception doit être explicitement décrite pour ne pas être interprétée comme une règle canonique.

### 2.2 Propriétés physiques

Les propriétés physiques existantes sont :
- **tranchant** ;
- **perforant** ;
- **contondant**.

Elles sont des propriétés des armes et des attaques, et non trois catégories de dégâts indépendantes.

### 2.3 Poids et vitesse d'attaque

Le poids et la vitesse d'attaque sont des valeurs fixes.

- Poids : fixe
- Vitesse d'attaque : fixe
- Aucune randomisation inutile ne doit être introduite sur ces paramètres.

### 2.4 Durabilité

Une arme possède une durabilité.

- à **0 %**, elle est **cassée et inutilisable** ;
- certaines armes exceptionnelles peuvent éventuellement ne pas utiliser de barre d'usure si cela est explicitement déclaré dans leur définition.

### 2.5 Réparation

Une réparation remet toujours l'arme à **100 %**.

Le coût de réparation dépend de la compétence **Forge** :
- plus la Forge est élevée, moins la réparation coûte de ressources ;
- une faible Forge rend la réparation plus coûteuse.

Le coût exact reste **À DÉFINIR**.

### 2.6 Qualité

La qualité :
- ne sert pas directement à augmenter les dégâts ;
- est liée à la résistance à la dégradation.

Le détail exact de cette relation reste **À DÉFINIR**.

### 2.7 Aléatoire

L'aléatoire doit rester limité aux éléments qui ont réellement une utilité de gameplay.

Les armes et leurs valeurs de base doivent rester fixes, sauf exceptions explicitement décidées.

---

## 3. Critiques

Le multiplicateur de critique est **x2**.

Les critiques sont influencées par :
- **Agilité** ;
- **Perception** ;
- **maîtrise de l'arme** ;
- **contexte**.

Le backstab reste un coup critique.

Les critiques contextuelles comme la parade parfaite restent distinctes d'un simple jet aléatoire.

Réflexe n'est ni une compétence ni une caractéristique : c'est un système automatique.

---

## 4. Armes et données

Les données d'arme sont data-driven. Les catégories et propriétés doivent être conservées dans les tables de données, sans recourir à un système aléatoire inutile.

Les données de base comprennent :
- nom ;
- famille ;
- base de dégâts ;
- propriétés physiques ;
- poids ;
- vitesse d'attaque ;
- durabilité ;
- qualité ;
- icône ;
- description.

Les détails numériques exacts restent **À DÉFINIR**.

---

## 5. Points encore à définir

- coefficients exacts de Force ;
- contribution exacte de la maîtrise de l'arme ;
- formule complète des dégâts ;
- seuils précis de qualité ;
- coût exact de réparation selon Forge ;
- bonus de Force exact ;
- formule de calcul de critique détaillée ;
- participation exacte de la maîtrise de l'arme ;
- valeurs de résistance à la dégradation selon qualité ;
- éventuels effets d'enchantement ou objets magiques.

---

## 6. Statut

- **Dégâts :** SPÉCIFIÉ dans les grands principes
- **Valeurs exactes :** À DÉFINIR
- **Réparation :** SPÉCIFIÉ dans les principes
- **Durabilité :** SPÉCIFIÉ dans les principes
- **Qualité :** SPÉCIFIÉ dans les grandes lignes
- **Aléatoire :** SPÉCIFIÉ dans les principes
- **Combat :** documenté dans `specs/COMBAT_SYSTEM_SPEC.md`

---

**Dernière mise à jour** : 2026-10-02  
**Statut** : SPÉCIFIÉ — préproduction  
**Note** : ce document complète la spécification de combat sans créer de doublon de système.

