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
- compétences pertinentes, notamment la cartographie lorsqu'elle sera définie.

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

Le joueur peut convertir ses richesses par :

- changeurs de monnaie ;
- commerce direct ;
- vente d'objets ;
- travail ou récompenses dans la monnaie locale ;
- troc lorsque celui-ci est accepté.

Les taux de change peuvent varier selon les royaumes, les relations politiques, la rareté, les événements et l'état économique local.

La compréhension des prix, contrats et conversations commerciales peut être influencée par la maîtrise linguistique du joueur lorsqu'il ne parle pas la langue locale.

## Mouvement du joueur

Merge est un Action-RPG à la troisième personne. Le joueur dispose de :

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

Toutes les actions physiques significatives possèdent des coûts d'Endurance data-driven. Le saut, la roulade, le bond arrière, le pas de côté, le franchissement et l'escalade ne sont donc pas gratuits.

### Défense et esquive

La défense distingue :

- **Blocage** : réduction/absorption selon équipement et règles défensives.
- **Parade** : timing précis avant impact, avec possibilité d'interruption/déséquilibre et de riposte.
- **Esquive** : déplacement spatial par roulade, bond arrière ou pas de côté.

La roulade possède des **i-frames temporaires**. Le Réflexe augmente leur durée sans rendre toute l'animation invulnérable. Certaines attaques peuvent ignorer les i-frames.

Le Réflexe peut également déclencher une esquive automatique probabiliste, tandis que la parade réflexe ne fait qu'élargir la fenêtre de timing après l'input du joueur.

### Furtivité

L'accroupissement et le déplacement discret influencent la furtivité. La détection est progressive selon posture, vitesse, distance, ligne de vue, luminosité, bruit, terrain, équipement et état de l'ennemi.
La compétence **Discrétion** progresse avec les actions furtives réussies et réduit la visibilité / le bruit du joueur ainsi que la sensibilité à la détection.

États conceptuels :

`Calme → Soupçon → Recherche → Alerte → Combat`

### Backstab

Le Backstab dépend du positionnement, de la furtivité, de l'angle, de la distance et de l'état de l'ennemi. Être simplement derrière une cible ne suffit pas.

## Ciblage

Un bouton dédié permet de sélectionner et parcourir les cibles valides.

La priorité est donnée aux ennemis proches, puis modulée par l'angle, la menace, la visibilité et la validité de la cible. Le joueur peut parcourir le cycle jusqu'à une cible plus éloignée et quitter volontairement le lock-on.

## Combat et armes

Chaque famille d'arme physique possède ses propres attaques et sa propre maîtrise. Le combat central gère dégâts, résistances, armure, effets, blocage, parade, esquive, stagger, interruptions et mort.

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

La progression vient principalement de l'utilisation réelle :

- **Endurance** : effort physique, course, combat, saut, roulade, bond arrière, pas de côté, franchissement, escalade et autres efforts.
- **Agilité** : mobilité, esquives, sauts, franchissements, escalade et réceptions pertinentes.
- **Défense** : dégâts réellement subis dans des situations pertinentes.
- **Réflexe** : expérience de combat et automatismes défensifs.
- **Domptage** : pratique réelle de capture/domestication des montures compatibles.
- **Médecine** : diagnostics, traitements et soins non magiques réellement pertinents.
- **Magie** : maîtrise distincte pour chaque domaine magique.

Les systèmes anti-farming empêchent qu'un spam sans danger fournisse une progression normale.

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

La faim prolongée, la déshydratation et le manque de sommeil peuvent provoquer faiblesse, récupération réduite, Endurance moins efficace, performances dégradées et autres conséquences graduelles.

Le sommeil dépend du contexte : lit, campement, refuge, sécurité, confort, météo et perturbations.

## Médecine et maladies

La **Médecine** est une compétence distincte de la magie de soin.

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

La magie de soin reste une voie séparée et n'augmente pas Médecine.

## Montures

Le joueur possède deux grandes voies d'acquisition :

```text
Éleveur → achat
Nature → domptage
```

Il n'existe pas de système générique de marchand de bêtes.

La compétence **Domptage** est indépendante. Certaines espèces peuvent être déclarées non domptables. Une relation de confiance peut évoluer après acquisition selon le type de monture.

Les montures ont leur propre mouvement, Endurance, comportement, interactions avec terrain/eau/dangers et éventuellement combat monté.

## Système aquatique

Le personnage passe progressivement par :

`Eau peu profonde → Flottaison → Nage → Plongée → Air critique → Noyade`

La réserve d'air est distincte de l'Endurance. La flottabilité dépend du personnage et de son équipement ; une armure lourde peut faire couler le personnage ou rendre la remontée très difficile.

## Dégâts environnementaux

Le jeu gère notamment :

- brûlure ;
- chute ;
- noyade ;
- chaleur extrême ;
- autres dangers environnementaux futurs.

Ces sources utilisent des systèmes de dégâts/effets communs et data-driven.

## Monde vivant et catastrophes

Les populations animales sont simulées comme des populations abstraites hors zone et les espèces se reproduisent, migrent et réagissent aux relations prédateur/proie, ressources et actions du joueur.

Les catastrophes naturelles prévues comprennent :

- tremblements de terre ;
- tornades ;
- feux de forêt ;
- foudre/tonnerre ;
- pluie torrentielle ;
- inondations ;
- glissements de terrain ;
- éruptions volcaniques ;
- coulées de lave.

Un séisme compatible peut augmenter la probabilité de réveil d'un volcan sans rendre l'éruption automatique. La lave peut suivre le relief, remplir certains ravins/dépressions, créer des zones dangereuses et déclencher des feux.

## Structure générale du monde

La direction de world design actuelle prévoit trois grandes régions continues :

1. **Dark Fantasy** : montagnes, falaises, ravins et volcan ; dangers volcaniques et environnement plus hostile.
2. **Light Fantasy** : grande colline verte d'échelle comparable au grand relief montagneux, avec une dépression au sommet remplie d'un grand lac d'altitude. Cette région peut provoquer des ruissellements, torrents, débordements et inondations en aval.
3. **Fantasy classique** : grandes forêts, plaines, collines, rivières, villages, routes et zones de transition.

Les frontières sont progressives. Les espèces, maladies, ressources, catastrophes et phénomènes météo peuvent franchir les transitions lorsque les conditions le permettent.

## Monde persistant

Le monde ne se régénère pas artificiellement. Les morts, destructions, ressources supprimées et modifications durables persistent. La nature peut cependant produire de nouvelles générations, migrations, croissance et évolution écologique.

Une nouvelle partie peut créer un nouveau monde indépendant sans détruire les anciens mondes sauvegardés.

## Règle de simulation
Un Backstab réussi contribue à la progression de la Discrétion.

## Monde vivant

```text
Hors zone joueur
→ probabilité / état régional / agrégat

Entrée zone
→ résolution du temps écoulé
→ matérialisation pertinente

Zone active
→ simulation locale détaillée

Sortie zone
→ agrégation
→ WorldState
```

Cette règle s'applique à l'écologie, aux PNJ éloignés, aux catastrophes, aux maladies, aux besoins physiologiques, aux montures non actives, à l'eau locale et aux autres systèmes qui ne nécessitent pas une simulation pleine précision partout.

## Spécifications de référence

- `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md`
- `specs/GAMEPLAY_SYSTEMS_MASTER_SPEC.md`
- `specs/PLAYER_PROGRESSION.md`
- `specs/COMBAT_AND_EFFECTS.md`
- `specs/AI_PERCEPTION_AND_REACTIVE_WORLD.md`
- `specs/TARGETING_AND_PARTY_SYSTEMS.md`
- `specs/MOUNT_SYSTEM_SPEC.md`
- `specs/FOOD_MEDICINE_AND_NONMAGICAL_HEALING_SPEC.md`
- `specs/AQUATIC_AND_ENVIRONMENTAL_DAMAGE_SPEC.md`
- `specs/NATURAL_DISASTERS_AND_DYNAMIC_ENVIRONMENT_SPEC.md`
- `specs/WORLD_REGIONS_HYDROLOGY_AND_THREATS_SPEC.md`
- `specs/PERFORMANCE_AND_SIMULATION_SPEC.md`
- `specs/SYSTEM_INTEGRATION_MATRIX.md`