# Gameplay — Merge

Cette documentation synthétise les mécaniques actuellement approuvées. Les règles spécialisées se trouvent dans les specs référencées à la fin.

## Navigation diégétique et cartes

Merge n'utilise pas de système de navigation avec marqueurs de quête permanents ou GPS indiquant automatiquement la destination.

La découverte et l'orientation reposent sur :

- cartes physiques achetées auprès de marchands ;
- cartes trouvées, volées, obtenues en récompense ou récupérées sur des PNJ ;
- panneaux, enseignes et indications dans le monde ;
- descriptions et directions données oralement par les PNJ ;
- points de repère visibles et connaissance progressive du monde ;
- exploration et mémoire du joueur ;
- compétences pertinentes lorsqu'elles sont définies dans le système canonique.

Les quêtes doivent fournir des indications diégétiques suffisantes pour permettre au joueur de progresser sans coordonnées ou marqueur obligatoire. Une quête peut être résolue uniquement par l'observation du monde, les conversations et la connaissance géographique acquise.

## Économie et monnaies par peuple

Chaque peuple possède sa propre monnaie. La monnaie n'est donc pas universelle dans Merge.

Monnaies actuellement prévues, noms définitifs à confirmer :

| Peuple | Monnaie provisoire |
|---|---|
| Humains | Couronne |
| Squelettes / Nécromentiens | Osselet |
| Êtres de magie | Éclat |
| Gork | Dent |

Les monnaies possèdent des valeurs et une acceptation propres à chaque économie. Un marchand peut refuser une monnaie étrangère.

Le joueur peut convertir ses richesses par change, commerce direct, vente d'objets, travail, récompenses ou troc lorsque celui-ci est accepté.

La compréhension des prix, contrats et conversations commerciales peut être influencée par la maîtrise linguistique du joueur lorsqu'il ne parle pas la langue locale.

## Mouvement du joueur

Merge est un Action-RPG à la troisième personne. Le joueur dispose notamment de :

- déplacement direct ;
- marche et course/sprint ;
- saut ;
- accroupissement ;
- roulade/esquive ;
- bond en arrière ;
- pas de côté ;
- franchissement contextuel d'obstacles ;
- escalade contextuelle ;
- réception contrôlée après une chute ;
- nage / plongée lorsque le contexte aquatique le permet ;
- montée et déplacement à dos de monture.

Les coûts éventuels en endurance sont des **ressources de gameplay** et ne constituent pas une caractéristique ou une compétence canonique. Leur équilibrage est data-driven.

### Défense et esquive

La défense distingue :

- **Blocage** : réduction/absorption selon équipement et règles défensives.
- **Parade** : timing précis avant impact, avec possibilité d'interruption/déséquilibre et de riposte.
- **Esquive** : déplacement spatial par roulade, bond arrière ou pas de côté.

**Parade est une compétence canonique de Défense / mouvement**, et non une compétence de Combat.

La roulade possède des **i-frames temporaires**. Les règles exactes de leurs effets sont data-driven et doivent rester compatibles avec la compétence Esquive et les caractéristiques canoniques.

### Furtivité

L'accroupissement et le déplacement discret influencent la furtivité. La détection est progressive selon posture, vitesse, distance, ligne de vue, luminosité, bruit, terrain, équipement et état de l'ennemi.

La compétence **Discrétion** progresse avec les actions furtives pertinentes et validées.

États conceptuels :

`Calme → Soupçon → Recherche → Alerte → Combat`

### Backstab

Le Backstab dépend du positionnement, de la furtivité, de l'angle, de la distance et de l'état de l'ennemi. Être simplement derrière une cible ne suffit pas.

## Ciblage

Un bouton dédié permet de sélectionner et parcourir les cibles valides.

La priorité est donnée aux ennemis proches, puis modulée par l'angle, la menace, la visibilité et la validité de la cible. Le joueur peut parcourir le cycle jusqu'à une cible plus éloignée et quitter volontairement le lock-on.

## Combat et armes

Chaque famille d'arme physique possède ses propres attaques et sa propre maîtrise. Le combat central gère dégâts, résistances, armure, effets, blocage, parade, esquive, stagger, interruptions et mort.

Les maîtrises d'armes sont les compétences canoniques correspondantes de `specs/CANONICAL_SKILLS.md`.

## Groupe et magie collective

Le joueur peut constituer un groupe avec des PNJ compatibles. Les membres gardent leur propre IA et personnalité.

Certaines magies peuvent nécessiter plusieurs participants. Les rituels collectifs prennent en compte :

- domaines et compatibilités magiques ;
- maîtrise individuelle ;
- mana ;
- positionnement ;
- synchronisation ;
- durée d'incantation ;
- interruption ;
- état des participants.

Un rituel peut être interrompu par dégâts, stagger, éloignement, incapacité, manque de mana ou conditions propres au sort.

## Progression organique

La progression utilise le système canonique **learning by doing**.

- Les **45 compétences** progressent par utilisation pertinente et validée.
- Les **6 caractéristiques** progressent automatiquement à partir de la progression des compétences qui leur sont liées.
- Le joueur ne distribue plus manuellement de points de compétence ou de caractéristique après la création.
- Les actions répétitives effectuées uniquement pour farmer sont limitées ou rejetées par les règles anti-abus.
- Les formules et seuils sont définis dans les specs de progression.

Les six caractéristiques canoniques sont : **Force, Agilité, Perception, Intelligence, Volonté et Charisme**.

La liste des 45 compétences et leurs relations avec les caractéristiques sont définies exclusivement dans `specs/CANONICAL_SKILLS.md`.

### Magie

Les sept compétences de Magie reposent sur :

**Volonté + Intelligence**

**Volonté est la caractéristique principale** : elle représente la force mentale nécessaire pour imposer, maintenir et contrôler la magie.

**Intelligence est secondaire** : elle représente notamment la compréhension et l'apprentissage des principes magiques.

Aucune caractéristique ou compétence magique générique supplémentaire ne doit être ajoutée sans mise à jour du système canonique.

## Survie : faim, hydratation et sommeil

Le personnage possède des besoins physiologiques progressifs :

```text
Besoins satisfaits
      ↓
État normal
      ↓
Besoin faible
      ↓
Altération physiologique
      ↓
État sévère
      ↓
État critique
```

La faim prolongée, la déshydratation et le manque de sommeil peuvent provoquer faiblesse, récupération réduite, performances dégradées et autres conséquences graduelles.

Le sommeil dépend du contexte : lit, campement, refuge, sécurité, confort, météo et perturbations.

## Médecine et maladies

La **Médecine** est une compétence canonique et reste distincte de la magie de soin.

Le monde possède des **maladies régionales** dont le risque dépend notamment du climat, de l'humidité, de la qualité de l'eau, de la faune, des vecteurs, de l'hygiène, de la densité de population et des catastrophes récentes.

### Diagnostic diégétique

Le jeu **ne révèle pas automatiquement le nom d'une maladie au joueur**.

```text
Symptômes observables
       ↓
  ┌────┴────┐
  ↓         ↓
Médecine   Médecin PNJ
  ↓         ↓
Autodiagnostic / diagnostic professionnel
        ↓
Traitement adapté
```

Une Médecine faible peut laisser plusieurs hypothèses ouvertes. Une Médecine élevée permet d'identifier plus précisément certaines maladies. Un médecin peut fournir un diagnostic selon sa propre expertise.

## Nourriture, eau et soins

La nourriture et l'eau utilisent l'inventaire. Elles peuvent réduire la faim, restaurer progressivement la condition et produire des effets nutritionnels.

Les soins non magiques comprennent notamment bandages, pansements, préparations, plantes médicinales, antidotes et stabilisation.

La magie de soin reste une voie séparée et n'augmente pas automatiquement la compétence Médecine.

## Montures

Le joueur possède deux grandes voies d'acquisition :

```text
Éleveur → achat
Nature → acquisition selon les règles propres à l'espèce
```

Il n'existe pas de compétence **Domptage** dans les 45 compétences canoniques actuelles.

Certaines espèces peuvent être déclarées non acquérables par le joueur. Une relation de confiance peut évoluer après acquisition selon le type de monture.

Les montures ont leur propre mouvement, ressources, comportement, interactions avec terrain/eau/dangers et éventuellement combat monté.

## Références canoniques

Pour toute règle de progression ou de caractéristique :

1. `specs/CANONICAL_SKILLS.md`
2. `specs/SKILL_PROGRESSION.md`
3. `specs/CHARACTERISTIC_PROGRESSION.md`
4. `specs/PLAYER_PROGRESSION.md`

Les anciennes notions **Endurance**, **Défense**, **Réflexe** et **Domptage** ne doivent pas être utilisées comme caractéristiques ou compétences de progression tant qu'elles ne font pas partie du système canonique.
