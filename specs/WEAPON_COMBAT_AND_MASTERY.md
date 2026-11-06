# Merge — Physical Weapon Combat & Mastery Specification

**Statut** : APPROUVÉ — conception / architecture
**Moteur** : Unreal Engine 5.8.4
**Langage principal** : C++

## 1. Principe

Toutes les armes physiques non magiques doivent disposer d'un système d'attaque dédié et cohérent avec leur famille d'arme.

La maîtrise des armes est indépendante par **famille d'arme canonique**. Utiliser une famille améliore progressivement la compétence correspondante, sans augmenter artificiellement les autres compétences d'armes.

Les domaines de magie restent séparés de ces maîtrises physiques.

## 2. Catégories de maîtrise canoniques

Les familles de combat physiques utilisent les compétences canoniques définies dans `specs/CANONICAL_SKILLS.md` :

- **Épée**
- **Hache**
- **Masse**
- **Lance**
- **Dague**
- **Arme à deux mains**
- **Arc**
- **Arbalète**
- **Combat à mains nues**

Une arme appartient à une seule famille de maîtrise déterminée par ses données.

**Important :** les anciennes catégories génériques telles que « Une Main », « Deux Mains », « Polearm » ou « RangedPhysical » ne sont pas des compétences canoniques et ne doivent pas être utilisées comme compétences de progression ou de scaling du personnage.

## 3. Progression de maîtrise

La maîtrise progresse principalement par l'utilisation effective de la famille concernée.

Exemple :

```text
Épée utilisée
    ↓
Compétence Épée ↑
```

```text
Dague utilisée
    ↓
Compétence Dague ↑
```

Utiliser une épée ne doit pas faire progresser automatiquement Hache, Masse, Dague ou une autre famille.

Le système doit distinguer une utilisation significative d'un spam artificiel. Les règles générales de contexte et d'anti-farming de `specs/SKILL_PROGRESSION.md` restent prioritaires.

## 4. Système d'attaque par famille / arme

Chaque arme physique doit disposer d'un système d'attaque adapté à son comportement.

Le système doit pouvoir gérer :

- attaques de base ;
- attaques puissantes chargées ;
- attaques spéciales / combos préenregistrés ;
- attaques directionnelles lorsque pertinent ;
- fenêtres de récupération ;
- portée ;
- vitesse ;
- endurance consommée lorsque le design le prévoit ;
- impact ;
- interruptions éventuelles ;
- interactions avec esquive et défense ;
- interactions avec Backstab lorsque l'arme est compatible.

Il ne faut pas coder une seule animation ou un seul combo universel pour toutes les armes.

L'architecture doit permettre à chaque famille et/ou arme de définir ses propres caractéristiques et séquences d'attaque via des données.

## 5. Relation avec l'Endurance

Les actions de combat pertinentes peuvent contribuer à la progression selon les règles générales de progression.

Les attaques doivent pouvoir consommer de l'Endurance lorsque le design final le prévoit. Les attaques de base n'ont pas de coût d'endurance par défaut conformément à `specs/COMBAT_SYSTEM_SPEC.md`.

Les coûts exacts restent des paramètres de balance à définir.

## 6. Relation avec l'Agilité

L'esquive est une mécanique commune du combat physique.

Une esquive validée peut contribuer à la progression de la compétence Esquive selon les règles de `specs/SKILL_PROGRESSION.md`.

Le combat doit permettre des transitions propres entre :

```text
Attaque → récupération → esquive
Esquive → récupération → attaque
Attaque → blocage / réaction
```

Les détails d'animation et de fenêtre d'interruption seront déterminés pendant le prototype.

## 7. Relation avec la défense

Les armes physiques interagissent avec les réponses défensives canoniques **Esquive**, **Parade** et **Blocage**.

Les dégâts subis ne créent pas de progression automatique d'une compétence « Défense » : aucune telle compétence canonique n'existe.

La compétence **Parade** reste une compétence de Défense / mouvement, conformément à `specs/CANONICAL_SKILLS.md`.

## 8. Backstab

Certaines armes physiques peuvent être compatibles avec le Backstab.

La compatibilité doit être définie dans les données de l'arme/famille plutôt que codée comme une règle globale.

Le Backstab reste soumis au système de furtivité, au positionnement et à l'état de la cible.

Un Backstab conforme aux conditions canoniques est un coup critique automatique ; il ne constitue pas une catégorie de dégâts distincte.

## 9. Architecture cible

```text
WeaponSystem
├── WeaponDefinition
│   ├── WeaponFamily
│   ├── AttackSet
│   ├── DamageProfile
│   ├── StaminaCost
│   ├── Reach
│   ├── Speed
│   └── BackstabCompatibility
│
├── WeaponCombat
│   ├── BasicAttack
│   ├── HeavyAttack
│   ├── SpecialAttack
│   ├── Recovery
│   └── HitResolution
│
└── WeaponMastery
    ├── Sword
    ├── Axe
    ├── Mace
    ├── Spear
    ├── Dagger
    ├── TwoHanded
    ├── Bow
    ├── Crossbow
    └── Unarmed
```

Les noms techniques peuvent être ajustés dans le code, mais ils doivent correspondre sans ambiguïté aux neuf compétences canoniques.

## 10. Règles

1. Une arme physique doit avoir un système d'attaque adapté à sa famille.
2. Les maîtrises sont indépendantes par famille d'arme canonique.
3. L'utilisation réelle fait progresser la compétence correspondante.
4. Une maîtrise ne doit pas automatiquement augmenter les autres familles.
5. Les familles d'armes doivent être extensibles par données sans créer de nouvelle compétence non approuvée.
6. Le système doit rester compatible avec Endurance, Agilité, Esquive, Parade, Blocage, furtivité et Backstab.
7. Aucun système de combat complet n'est considéré comme implémenté par cette spécification seule.
8. Les valeurs d'équilibrage et les combos définitifs seront déterminés lors du prototype.
9. `specs/CANONICAL_SKILLS.md` est la source canonique pour les noms et le nombre des compétences d'armes.
