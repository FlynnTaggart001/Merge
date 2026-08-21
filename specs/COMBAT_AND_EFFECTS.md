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
Defense / Block / Parry / Resistance / Armor
      ↓
FinalDamage or Negation
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

## Parade

Le combat physique doit intégrer un **système de parade actif** distinct du blocage et de l'esquive.

La parade repose sur le timing : le joueur tente de faire entrer son arme ou son équipement défensif dans une fenêtre précise avant l'impact d'une attaque ennemie.

Une parade réussie doit pouvoir :

- annuler ou fortement réduire les dégâts ;
- interrompre, dévier ou déséquilibrer l'attaquant selon l'attaque ;
- ouvrir une fenêtre de riposte ;
- générer une réaction d'impact appropriée ;
- contribuer à l'expérience de combat et, si retenu, à une progression liée à la maîtrise défensive.

Une parade ne doit pas être un simple `Block = true` : elle dépend d'une **fenêtre temporelle**, de l'orientation, de la compatibilité de l'arme/équipement et de l'état des combattants.

### États conceptuels

```text
Normal
   ↓
ParryWindow
   ├── Succès → Parried / RiposteWindow
   └── Échec → attaque résolue normalement
```

### Conditions à prévoir

Le système doit pouvoir prendre en compte :

- timing de l'input ;
- direction/orientation ;
- portée de l'attaque ;
- type d'attaque ;
- arme ou équipement utilisé pour parer ;
- état du joueur ;
- attaques imparables ou non parables ;
- coût éventuel en Endurance ;
- récupération après tentative ;
- différence entre parade parfaite et parade partielle si le game design la conserve.

Les valeurs de fenêtre, coûts, pénalités et effets ne sont pas encore figés et seront équilibrés dans le prototype.

### Parade et progression

Une parade réussie peut produire un événement de gameplay `SuccessfulParry` destiné au `ProgressionSystem`.

La progression exacte associée à cet événement reste à définir : elle ne doit pas automatiquement créer une nouvelle statistique si une maîtrise existante suffit.

### Parade et Réflexe

Le **Réflexe** intervient dans la parade comme une aide passive liée à l'expérience de combat, mais ne remplace pas l'input du joueur.

Le joueur doit toujours déclencher la tentative de parade. Le niveau de Réflexe peut ensuite modifier la **tolérance de la fenêtre de parade** : plus le personnage est expérimenté, plus il peut anticiper légèrement l'impact.

```text
Réflexe faible
→ fenêtre de parade très exigeante

Réflexe moyen
→ fenêtre légèrement plus permissive

Réflexe élevé
→ fenêtre nettement plus permissive
```

Le Réflexe ne doit pas fournir une parade automatique complète. Cela préserve la maîtrise du joueur et différencie clairement :

```text
Esquive automatique
→ automatisme possible selon le Réflexe

Parade réflexe
→ assistance au timing, input toujours requis
```

La tolérance peut également être influencée par la **familiarité de combat** : un personnage très expérimenté contre une famille d'attaques peut mieux anticiper celle-ci qu'une attaque totalement inconnue. Cette familiarité doit rester data-driven et ne doit pas rendre les nouveaux ennemis trivialement prévisibles.

### Saut arrière et parade

Le saut arrière et la parade restent deux réponses défensives différentes. Une tentative de parade ne doit pas déclencher automatiquement un saut arrière. Les deux peuvent cependant être enchaînés selon les fenêtres de récupération et l'Endurance.

## Blocage vs parade vs esquive

```text
Blocage
→ défense plus permissive, généralement réactive et moins exigeante en timing.

Parade
→ défense active fondée sur un timing précis, pouvant créer une ouverture.

Esquive
→ évitement spatial de l'attaque.
```

Ces trois mécaniques doivent partager le pipeline de combat sans être confondues.

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
4. Le système doit être compatible avec furtivité, Backstab, esquive, saut arrière, parade, défense, magie et IA.
5. La parade doit être une mécanique de timing, pas un simple blocage.
6. Une parade réussie doit pouvoir créer une ouverture de riposte.
7. Les attaques non parables doivent être définissables par données.
8. Les valeurs finales sont réservées à l'équilibrage du prototype.
9. Le Réflexe peut assister la parade par la fenêtre de timing, mais ne doit pas la déclencher automatiquement.
