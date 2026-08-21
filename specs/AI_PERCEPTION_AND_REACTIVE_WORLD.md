# Merge — AI Perception & Reactive World Specification

**Statut** : APPROUVÉ — architecture
**Engine** : Unreal Engine 5.8.1

## Perception commune

Les IA doivent utiliser une couche de perception commune et extensible :

- vision ;
- audition ;
- visibilité/luminosité ;
- bruit ;
- awareness ;
- sens futurs selon les espèces.

La furtivité du joueur doit fournir des signaux à cette couche plutôt que contourner l'IA.

## Détection

Le comportement de détection doit être progressif et conserver un état de conscience cohérent :

```text
Calme → Soupçon → Recherche → Alerte → Combat
```

Les ennemis doivent pouvoir réagir à une dernière position connue, au bruit et aux événements du monde.

## IA du bestiaire

Le comportement individuel peut exploiter :

- besoins ;
- territoire ;
- prédation ;
- fuite ;
- chasse ;
- reproduction ;
- migration ;
- danger perçu.

La simulation de population et l'IA d'un individu sont deux niveaux distincts.

## Quêtes et monde réactif

Les systèmes narratifs doivent pouvoir consommer les événements persistants du monde. Un PNJ mort ou une faction disparue doit pouvoir modifier les conditions d'une quête ou d'un dialogue.

## Temps et environnement

La perception peut être influencée par l'heure, la météo, la luminosité et le bruit ambiant lorsque ces systèmes sont activés.

## Implémentation

Le choix précis entre Behavior Tree, StateTree, EQS et autres outils Unreal sera validé par prototype et profilage. L'architecture ne doit pas rendre le reste du jeu dépendant d'un seul modèle d'IA.
