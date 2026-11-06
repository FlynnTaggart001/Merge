# Merge — World Regions, Hydrology & Regional Threats Specification

**Statut** : APPROUVÉ — direction de conception / architecture
**Engine** : Unreal Engine 5.8.4

## 1. Principe

La carte de Merge est actuellement pensée comme un grand monde continu organisé autour de trois grandes identités géographiques et visuelles. Ce découpage sert de direction de conception ; les frontières, dimensions exactes et positions définitives seront décidées dans la production de la map.

## 2. Région I — Dark Fantasy

Cette région constitue le secteur le plus dangereux et contient notamment le volcan.

Éléments directeurs :
- relief montagneux ;
- grandes falaises ;
- ravins et vallées ;
- volcan ;
- forêts sombres ;
- zones volcaniques ;
- territoires de créatures dangereuses ;
- zones susceptibles d'être transformées par éruptions, séismes, incendies et glissements.

La présence du volcan doit faire de la géologie une composante importante de l'évolution de la région.

## 3. Région II — Light Fantasy

Cette région doit être dominée par une **grande colline verte**, d'une échelle comparable au grand relief montagneux de la région Dark Fantasy.

Au sommet se trouve une dépression naturelle contenant un grand volume d'eau, avec une silhouette de relief évoquant l'idée d'une colline portant une cuvette/lac d'altitude.

Le lac n'est pas un simple décor : il sert de point majeur du réseau hydrologique.

```text
        Colline
      /─────────\
     /    Lac    \
    /_____________\
          ↓
     Ruissellement
          ↓
      Sources
          ↓
     Rivières aval
```

## 4. Hydrologie et danger

La Light Fantasy ne doit pas être considérée comme une zone sûre.

Le lac et les pentes peuvent générer :
- débordements ;
- ruissellements importants ;
- torrents temporaires ;
- inondations en aval ;
- érosion ;
- boue ;
- glissements de terrain lorsque les conditions sont réunies ;
- rupture ou débordement de certaines zones de retenue si le terrain et les événements le permettent.

Une pluie torrentielle prolongée peut augmenter fortement le volume d'eau et provoquer une chaîne hydrologique :

```text
Pluie intense
  ↓
Lac / sols saturés
  ↓
Débordement ou ruissellement accru
  ↓
Torrents
  ↓
Rivières gonflées
  ↓
Inondations en aval
```

Les conséquences sont régies par le système naturel général et non par un script fixe.

## 5. Région III — Fantasy classique

Cette région joue le rôle de grand espace de transition et d'exploration :
- forêts ;
- plaines ;
- collines ;
- rivières ;
- villages ;
- routes ;
- ruines ;
- zones agricoles ;
- reliefs intermédiaires.

Elle doit pouvoir recevoir des influences des deux autres régions, notamment migrations, catastrophes, commerce, maladies, conflits ou changements écologiques.

## 6. Frontières régionales

Les trois régions ne doivent pas être séparées par des barrières artificiellement nettes.

Le passage doit être progressif :

```text
Dark Fantasy
    ↓
Dark / Transition
    ↓
Fantasy classique
    ↓
Classic / Light Transition
    ↓
Light Fantasy
```

Des espèces, phénomènes météo, maladies et migrations peuvent franchir les zones de transition lorsque les conditions le permettent.

## 7. Réseau hydrologique

Les reliefs doivent déterminer autant que possible le trajet de l'eau :
- sommets ;
- pentes ;
- ravins ;
- bassins ;
- rivières ;
- lacs ;
- zones de débordement.

L'eau doit avoir une relation avec les catastrophes et le monde vivant :

```text
Relief + Pluie + Eau
        ↓
Hydrologie régionale
        ↓
Inondation / érosion / glissement
        ↓
Terrain / routes / habitats modifiés
        ↓
Écologie / PNJ / quêtes
```

## 8. Menaces régionales

Chaque grande région peut avoir un profil de danger différent sans devenir un biôme fermé.

### Dark Fantasy
- activité volcanique ;
- lave ;
- chaleur ;
- incendies ;
- séismes ;
- falaises et chutes ;
- créatures dangereuses.

### Light Fantasy
- météo ;
- inondations ;
- torrents ;
- terrain boueux ;
- glissements liés à l'eau ;
- faune sauvage ;
- maladies hydriques potentielles.

### Fantasy classique
- dangers plus répartis ;
- catastrophes traversantes ;
- faune/prédateurs ;
- risques liés aux routes, villages et activités humaines.

Les listes restent ouvertes et ne constituent pas des exclusions.

## 9. Interaction avec la simulation probabiliste

Hors zone joueur, les régions conservent leurs états abstraits :

```text
RegionalState
├── TerrainState
├── WaterState
├── WeatherState
├── HazardState
├── EcologyState
├── DiseaseRiskState
└── WorldEventHistory
```

Lors de l'entrée du joueur :
- l'état est résolu à partir du temps écoulé et des probabilités ;
- les conséquences sont matérialisées localement ;
- les systèmes de gameplay utilisent l'état régional résultant.

## 10. Persistences importantes

Peuvent devenir persistants :
- terrain érodé ou modifié ;
- ravin partiellement rempli ;
- route détruite ;
- zone inondée affectée ;
- végétation détruite ;
- nouvelles zones de danger ;
- migrations ;
- modifications de ressources ;
- historique des catastrophes.

## 11. Ce qui reste ouvert

Les noms des régions, dimensions exactes, frontières, emplacement précis du lac, réseau définitif des rivières, villages, reliefs et contenu du bestiaire restent des choix de world design. La structure générale en trois grandes régions et le principe d'un lac d'altitude dangereux dans la Light Fantasy sont approuvés comme direction.
