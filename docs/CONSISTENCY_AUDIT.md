# Audit de cohérence — Merge

**Date :** 2026-10-15  
**Dépôt :** `FlynnTaggart001/Merge`  
**Périmètre :** progression canonique, spécifications de combat/armes, feuille de route et état Unreal  
**Statut :** audit documentaire actualisé ; validation Unreal locale restante

## 1. Règles canoniques confirmées

- 46 compétences canoniques ; `Domptage` est une compétence canonique.
- 6 caractéristiques sur 0–20.
- Création du personnage : choix Homme/Femme ; toutes les caractéristiques démarrent à 6/20 ; 20 points distribuables ; plafond de création à 14/20.
- Les compétences initiales sont calculées automatiquement ; aucun point de compétence n'est distribué manuellement.
- Progression après création par Learning by Doing ; les caractéristiques progressent automatiquement selon les poids, réserves et seuils spécifiés.
- `Réflexe` est un système automatique fondé notamment sur Agilité et Perception, et non une compétence ou une caractéristique.
- `Parade` appartient à Défense / mouvement ; `Filature` et `Domptage` sont canoniques.
- Les classes/voies dérivent du profil et sont révélées lorsque leurs conditions sont remplies.
- L'architecture cible est distincte du scaffold Unreal réellement livré.
- Les statuts `APPROUVÉ`, `SPÉCIFIÉ`, `SCAFFOLD`, `IMPLÉMENTÉ` et `VALIDÉ` ne sont pas interchangeables.

## 2. Références canoniques du combat

- `specs/COMBAT_SYSTEM_SPEC.md` : règles centrales de combat.
- `specs/WEAPONS_AND_EQUIPMENT_SPEC.md` : dégâts des armes, propriétés physiques, armures, durabilité, réparation et critiques.
- `specs/CANONICAL_SKILLS.md` : compétences de maîtrise des neuf familles.
- `specs/SKILL_PROGRESSION.md` : progression des compétences et anti-farming.

Au 2026-10-15, le fichier historique `COMBAT_RESOLUTION.md` n'a pas été retrouvé à la racine ni au chemin `gameplay/COMBAT_RESOLUTION.md` vérifié pendant l'audit. La spécification centrale disponible est `specs/COMBAT_SYSTEM_SPEC.md`. Ne pas recréer de document concurrent : vérifier l'historique Git si le contenu historique doit être récupéré, puis corriger les références obsolètes.

## 3. Paramètres de combat déjà spécifiés

- Une barre d'endurance de 100 points ; régénération de 15 points/seconde après 0,5 seconde sans action consommatrice.
- Coûts actuels : esquive 20 ; parade réussie 10 ; parade parfaite 5 ; blocage 10 par impact intercepté ; attaque puissante 20–40 selon la charge ; attaque spéciale 30 ; sprint 5/seconde.
- Attaque puissante : charge maximale de 3 secondes ; multiplicateur linéaire de 1× à 4×.
- Dégâts physiques : dégâts de base × maîtrise × Force × modificateur d'armure × autres modificateurs.
- Maîtrise d'arme : +0,5 % par point, jusqu'à +50 % à 100.
- Force : +2 % par point, jusqu'à +40 % à 20/20.
- Réductions d'armure fixes : tranchant 35 %/60 %, perforant 30 %/45 %, contondant 25 %/40 % (armure légère/lourde).
- Critique : multiplicateur de 2× ; parade parfaite et backstab peuvent déclencher un critique contextuel garanti selon les conditions décrites.
- Qualité d'arme : influence la résistance à la dégradation, pas les dégâts de base ; une arme standard à 0 % de durabilité est inutilisable et une réparation restaure 100 %.

## 4. Clarification apportée sur le blocage

Le coût de base canonique actuel est de **10 endurance par impact effectivement bloqué**, quelle que soit la durée de garde. Une garde sans impact coûte 0.

La spécification décrit aussi un style lourd davantage orienté vers le blocage et mentionnait un blocage plus coûteux. Ces formulations ne définissaient pas de modificateur chiffré. Le document de combat est clarifié : un surcoût selon le poids de l'armure reste **à décider** ; aucun coefficient supplémentaire ne doit être inventé ou implémenté avant approbation. Le coût de base de 10 reste la valeur utilisable en attendant cette décision.

## 5. Éléments de conception restant à définir

- Formule et poids exacts de la chance de critique (Agilité, Perception et maîtrise pertinente).
- Fenêtres numériques de parade.
- Seuils et résultats exacts du stagger.
- Règles d'interruption et détails des réactions automatiques de Réflexe.
- Dégâts de base de chaque famille d'arme et valeurs détaillées des projectiles.
- Éventuel modificateur du coût de blocage selon l'armure.
- Effets du poids d'armure sur la mobilité/endurance.
- Formule des coûts de réparation selon Forge et taux de dégradation par qualité.
- Détails définitifs des combos spéciaux, de l'IA et du système de magie en combat.

Ces points sont des décisions ouvertes, pas automatiquement des contradictions. Ils ne doivent pas être remplis arbitrairement dans le code.

## 6. Feuille de route et validation Unreal

La feuille de route est datée du 2026-10-15. La Phase 1 reste : **scaffold livré, validation locale requise**. Les systèmes de combat et de progression sont spécifiés mais ne sont pas déclarés implémentés.

Restent à vérifier sur une machine équipée d'Unreal Engine 5.8.1 :
- génération des project files et compilation C++ ;
- création/configuration des Blueprints et de `L_TestArena` ;
- Enhanced Input, déplacement, caméra et saut ;
- tests PIE et profilage CPU/GPU/mémoire ;
- après la fondation, tests unitaires et en jeu des dégâts, armures, parade, blocage, endurance et progression.

## 7. Conclusion

L'audit documentaire confirme les règles canoniques principales et met à jour l'état des paramètres de combat. La contradiction rédactionnelle autour du coût du blocage est explicitée sans inventer de nouvelle valeur. Le statut documentaire ne vaut pas validation technique.

**Dernière mise à jour :** 2026-10-15
