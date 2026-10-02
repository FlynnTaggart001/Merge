# Merge — Physical Weapon Combat & Mastery Specification

**Statut** : APPROUVÉ — conception / architecture
**Moteur** : Unreal Engine 5.8.1
**Langage principal** : C++

## 1. Principe

Toutes les armes physiques non magiques doivent disposer d'un système d'attaque dédié et cohérent avec leur famille d'arme.

La maîtrise des armes est indépendante par catégorie, dans l'esprit de Skyrim : utiliser une famille d'arme améliore progressivement la maîtrise de cette famille, sans augmenter artificiellement toutes les autres maîtrises.

Les domaines de magie restent séparés de ces maîtrises physiques.

## 2. Catégories de maîtrise

Les catégories doivent être définies comme des données extensibles et non comme une liste rigide dans le code central.

Catégories prévues conceptuellement :

- Armes à une main
- Armes à deux mains
- Armes d'hast / armes longues
- Armes à distance physiques
- autres familles physiques à définir selon le game design

La distinction exacte des familles sera validée pendant la conception du bestiaire, des armes et du combat.

Une arme appartient à une famille de maîtrise déterminée par ses données.

## 3. Progression de maîtrise

La maîtrise progresse principalement par l'utilisation effective de la famille concernée.

Exemple :

```text
Épée à une main utilisée
        ↓
Maîtrise Une Main ↑
```

```text
Épée à deux mains utilisée
        ↓
Maîtrise Deux Mains ↑
```

Utiliser une épée à une main ne doit pas faire progresser automatiquement la maîtrise des armes à deux mains.

Le système doit pouvoir distinguer une utilisation significative d'un spam artificiel.

Prévoir des règles d'anti-farming comparables aux autres systèmes de progression : contexte, fréquence, intensité, répétition et pertinence de l'action.

## 4. Système d'attaque par famille / arme

Chaque arme physique doit disposer d'un système d'attaque adapté à son comportement.

Le système doit pouvoir gérer :

- attaques légères ;
- attaques lourdes ;
- attaques enchaînées / combos ;
- attaques directionnelles lorsque pertinent ;
- fenêtres de récupération ;
- portée ;
- vitesse ;
- stamina/endurance consommée ;
- impact ;
- interruptions éventuelles ;
- interactions avec esquive et défense ;
- interactions avec Backstab lorsque l'arme est compatible.

Il ne faut pas coder une seule animation ou un seul combo universel pour toutes les armes.

L'architecture doit permettre à chaque famille et/ou arme de définir ses propres caractéristiques et séquences d'attaque via des données.

## 5. Relation avec l'Endurance

Les attaques physiques peuvent contribuer à la progression de l'Endurance selon les règles générales de progression.

Les attaques doivent également pouvoir consommer de l'Endurance si le design final le confirme.

Les coûts exacts ne sont pas encore définitifs.

## 6. Relation avec l'Agilité

L'esquive est une mécanique commune du combat physique.

Une esquive réussie peut contribuer à la progression de l'Agilité selon le système déjà défini.

Le combat doit permettre des transitions propres entre :

```text
Attaque → récupération → esquive
Esquive → récupération → attaque
Attaque → blocage / réaction
``` 

Les détails seront déterminés pendant le prototype.

## 7. Relation avec la défense

Les armes physiques interagissent avec les réponses défensives canoniques **Esquive**, **Parade** et **Blocage**.

Les dégâts subis ne créent pas de progression automatique d'une compétence « Défense » : aucune telle compétence canonique n'est ajoutée par ce système.

## 8. Backstab

Certaines armes physiques peuvent être compatibles avec le Backstab.

La compatibilité doit être définie dans les données de l'arme/famille plutôt que codée comme une règle globale.

Le Backstab reste soumis au système de furtivité, au positionnement et à l'état de la cible.

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
│   ├── LightAttack
│   ├── HeavyAttack
│   ├── Combo
│   ├── Recovery
│   └── HitResolution
│
└── WeaponMastery
    ├── OneHanded
    ├── TwoHanded
    ├── Polearm
    ├── RangedPhysical
    └── FutureFamilies[*]
```

Les noms de catégories ci-dessus sont des exemples de conception et peuvent être ajustés sans casser le système central.

## 10. Règles

1. Une arme physique doit avoir un système d'attaque adapté à sa famille.
2. Les maîtrises sont indépendantes par famille d'arme.
3. L'utilisation réelle fait progresser la maîtrise correspondante.
4. Une maîtrise ne doit pas automatiquement augmenter les autres familles.
5. Les familles d'armes doivent être extensibles par données.
6. Le système doit rester compatible avec Endurance, Agilité, Esquive, Parade, Blocage, furtivité et Backstab.
7. Aucun système de combat complet n'est considéré comme implémenté par cette spécification seule.
8. Les valeurs d'équilibrage et les combos définitifs seront déterminés lors du prototype.
