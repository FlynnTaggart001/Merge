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

Les catégories principales canoniques sont **Physique** et **Magique**. Pour les dégâts physiques, tranchant, perforant et contondant sont des propriétés de dégâts qui déterminent notamment la réduction d'armure. Les résistances détaillées doivent rester data-driven ; voir `specs/COMBAT_SYSTEM_SPEC.md`.

## Défense

Le terme **Défense** désigne ici l'ensemble des réponses défensives du combat. Il ne s'agit pas d'une compétence canonique supplémentaire et il n'existe aucune progression automatique par exposition aux dégâts.

## Parade

Le combat physique doit intégrer un **système de parade actif** distinct du blocage et de l'esquive.

La parade repose sur le timing : le joueur tente de faire entrer son arme ou son équipement défensif dans une fenêtre précise avant l'impact d'une attaque ennemie.

Une parade réussie doit pouvoir :

- annuler les dégâts ;
- interrompre, dévier ou déséquilibrer l'attaquant selon l'attaque ;
- ouvrir une fenêtre de riposte ;
- générer une réaction d'impact appropriée ;
- générer l'événement de gameplay approprié pour le système de progression, si une compétence canonique concernée est validée.

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
- exceptions spéciales de défense explicitement définies ; aucune attaque n'est imparable par défaut, conformément à `specs/COMBAT_SYSTEM_SPEC.md` ;
- coût éventuel en Endurance ;
- récupération après tentative ;
- distinction entre parade parfaite et parade réussie non parfaite.

Les fenêtres de parade et les coûts d'endurance canoniques sont définis dans `specs/COMBAT_SYSTEM_SPEC.md`. Les valeurs non spécifiées dans ce document d'architecture doivent être lues dans les spécifications canoniques, et non réinventées ici ; le calibrage en jeu reste à effectuer.

### Parade et progression

Une parade réussie peut produire un événement de gameplay `SuccessfulParry` destiné au `ProgressionSystem`.

La progression exacte associée à cet événement reste à définir : elle ne doit pas automatiquement créer une nouvelle statistique si une maîtrise existante suffit.

### Parade et Réflexe

Le **Réflexe** n'est ni une compétence ni une caractéristique. C'est un système automatique distinct qui peut éviter une attaque surprise avant qu'elle ne touche le joueur.

Son efficacité dépend notamment de l'**Agilité** et de la **Perception** du joueur et est modifiée par la **Discrétion** de l'adversaire. Le Réflexe ne progresse pas indépendamment, ne dépend pas de l'expérience de combat et ne modifie pas la fenêtre de parade.

La parade reste une action volontaire du joueur, résolue par son input et le timing de la compétence **Parade**.

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
7. Aucune attaque n'est imparable par défaut ; les attaques lourdes ou spéciales peuvent définir des fenêtres de parade plus courtes dans les données, conformément à `specs/COMBAT_SYSTEM_SPEC.md`.
8. Les valeurs finales sont réservées à l'équilibrage du prototype.
9. Le Réflexe est un système automatique distinct de la parade : il ne déclenche pas la parade et ne modifie pas sa fenêtre.
