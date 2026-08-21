# Merge — Combat, Damage & Effects Specification

**Statut** : APPROUVÉ — architecture
**Engine** : Unreal Engine 5.8.1

## Responsabilités

Le système de combat doit être indépendant des données spécifiques des armes et des créatures.

```text
AttackDefinition
      ↓
CombatResolver
      ↓
DamageContext
      ↓
Resistance / Armor / Defense
      ↓
FinalDamage
      ↓
EffectSystem + HitReaction
```

## DamageContext

Une résolution de dégâts doit pouvoir connaître :

- source ;
- cible ;
- montant brut ;
- type de dégâts ;
- arme/capacité ;
- position et direction si pertinentes ;
- contexte furtif ;
- multiplicateurs ;
- effets associés.

## Types de dégâts

Le système doit être extensible : les types définitifs ne sont pas encore figés. Les résistances doivent être data-driven.

## Défense

La Défense du personnage progresse par exposition réelle aux dégâts conformément à `PLAYER_PROGRESSION.md`, mais le calcul de dégâts et la progression restent deux responsabilités distinctes.

## Effets

Les armes, sorts, créatures et objets peuvent appliquer des effets génériques :

- dégâts dans le temps ;
- soins ;
- buffs ;
- debuffs ;
- poison ;
- saignement ;
- immobilisation ;
- ralentissement ;
- effets élémentaires ;
- effets personnalisés futurs.

Les effets doivent pouvoir être définis comme données et composés sans modifier le cœur du système.

## Règles

1. Le combat ne doit pas contenir les règles de progression directement.
2. Une arme ne doit pas implémenter elle-même tout le calcul de dégâts.
3. Les résistances et effets doivent rester réutilisables.
4. Le système doit être compatible avec furtivité, Backstab, esquive, défense, magie et IA.
5. Les valeurs finales sont réservées à l'équilibrage du prototype.
