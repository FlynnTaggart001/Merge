# Merge — Factions, Quests & World Events Specification

**Statut** : APPROUVÉ — architecture
**Engine** : Unreal Engine 5.8.4

## Factions

Les factions sont data-driven et peuvent avoir :

- réputation du joueur ;
- relations inter-factions ;
- territoire ;
- membres et dirigeants ;
- états d'alliance ou d'hostilité ;
- conséquences liées aux morts et destructions.

Une faction peut être durablement affaiblie ou disparaître si le game design le permet.

## Quêtes réactives

Les quêtes doivent consulter le WorldState et pouvoir gérer :

- PNJ mort ;
- faction détruite ;
- créature disparue ou extinction locale ;
- lieu détruit ;
- objet consommé/détruit ;
- événement déjà survenu.

Une quête peut donc changer d'état plutôt que supposer un monde statique.

## Dialogues

Les dialogues pourront utiliser des conditions data-driven liées au joueur, aux factions, aux quêtes et aux événements du monde.

## World Events

Un système central diffuse des événements tels que :

```text
CreatureKilled
FactionLeaderKilled
FactionDestroyed
LocationDestroyed
PopulationCollapse
Migration
QuestCompleted
WorldDiscovery
```

Les événements importants peuvent alimenter un historique persistant du monde.

## Temps et météo

Le WorldState doit réserver une place au temps mondial et aux conditions environnementales. Les effets précis de la météo, des saisons et de l'heure restent à équilibrer et ne sont pas figés ici.
