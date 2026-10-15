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

Le document `docs/gameplay/COMBAT_RESOLUTION.md` existe bien. Il contient un ancien modèle probabiliste d'opposition attaque/esquive/blocage, des fenêtres de parade encore marquées « à définir » et autorise des attaques non parables par données. Ces points ne sont pas alignés sur toutes les règles canoniques actuelles de `specs/COMBAT_SYSTEM_SPEC.md` (combat temps réel, fenêtres de parade définies, toutes les attaques parables par défaut). Le fichier est conservé ; il doit être réconcilié ou explicitement maintenu comme historique avant implémentation. Ne pas créer de nouveau document concurrent.

## 3. Paramètres de combat déjà spécifiés

- Une barre d'endurance de 100 points ; régénération de 15 points/seconde après 0,5 seconde sans action consommatrice.
- Coûts actuels : esquive 20 ; parade réussie 10 ; parade parfaite 5 ; blocage 10 par impact intercepté ; attaque puissante 20–40 selon la charge ; attaque spéciale 30 ; sprint 5/seconde.
- Attaque puissante : charge maximale de 3 secondes ; multiplicateur linéaire de 1× à 4×.
- Dégâts physiques : dégâts de base × maîtrise × Force × modificateur d'armure × autres modificateurs.
- Maîtrise d'arme : +0,5 % par point, jusqu'à +50 % à 100.
- Force : +2 % par point, jusqu'à +40 % à 20/20.
- Réductions d'armure fixes : tranchant 35 %/60 %, perforant 30 %/45 %, contondant 25 %/40 % (armure légère/lourde).
- Critique : multiplicateur de 2× ; parade parfaite et backstab peuvent déclencher un critique contextuel garanti selon les conditions décrites.
- Fenêtre de parade ordinaire : 350 ms de référence au total (dont 200 ms parfaite), avec plafonds respectifs de 400 ms et 250 ms ; attaques lourdes : 250 ms au total et 100 ms parfaite de référence, plafonds de 275 ms et 125 ms.
- Résistance au stagger : `10 + (0,5 × poids_kg) + (0,2 × taille_cm) + bonus_armure` ; bonus 0 sans armure, 15 légère, 35 lourde. Stagger uniquement si les dégâts finaux dépassent strictement le seuil ; durée 2,9 s.
- Dégâts de base : dague 20, épée 25, hache 28, lance 26, masse 32, arme à deux mains 35, arc 22, arbalète 30 ; mains nues à définir.
- Qualité d'arme : influence la résistance à la dégradation, pas les dégâts de base ; une arme standard à 0 % de durabilité est inutilisable et une réparation restaure 100 %.

## 4. Clarification apportée sur le blocage

Le coût de base canonique actuel est de **10 endurance par impact effectivement bloqué**, quelle que soit la durée de garde. Une garde sans impact coûte 0.

L'armure lourde réduit la vitesse de déplacement/course et augmente le coût d'endurance des actions physiques qui consomment de l'endurance. Ce principe est approuvé ; le coefficient exact, y compris le surcoût applicable au blocage, reste à définir. Aucun multiplicateur numérique ne doit être inventé avant validation. Le coût de base du blocage reste de 10 endurance par impact.

## 5. Éléments de conception restant à définir

- Formule exacte de la chance de critique (Agilité, Perception et maîtrise pertinente).
- Calibrage en jeu des dégâts de base et des seuils de stagger déjà spécifiés.
- Dégâts à mains nues, trajectoires/vitesses des projectiles et valeurs détaillées des attaques à distance.
- Coefficients exacts des pénalités de mobilité et du surcoût d'endurance de l'armure lourde.
- Formule des coûts de réparation selon Forge et taux de dégradation par qualité.
- Priorités de résolution des événements simultanés, détails des réactions automatiques de Réflexe, combos spéciaux, IA et magie en combat.

Les fenêtres de parade, la formule de résistance au stagger et les dégâts de base des familles d'armes (hors mains nues) sont maintenant spécifiés. Leur calibration en jeu reste distincte de la décision de conception. Les paramètres encore ouverts ne doivent pas être remplis arbitrairement dans le code.

## 6. Feuille de route et validation Unreal

La feuille de route est datée du 2026-10-15. La Phase 1 reste : **scaffold livré, validation locale requise**. Les systèmes de combat et de progression sont spécifiés mais ne sont pas déclarés implémentés.

Restent à vérifier sur une machine équipée d'Unreal Engine 5.8.1 :
- génération des project files et compilation C++ ;
- création/configuration des Blueprints et de `L_TestArena` ;
- Enhanced Input, déplacement, caméra et saut ;
- tests PIE et profilage CPU/GPU/mémoire ;
- après la fondation, tests unitaires et en jeu des dégâts, armures, parade, blocage, endurance et progression.

## 7. Conclusion

L'audit documentaire confirme les règles canoniques principales et met à jour l'état des paramètres de combat. Les contradictions les plus importantes identifiées entre la spécification canonique et l'ancien document `docs/gameplay/COMBAT_RESOLUTION.md` sont consignées ; les paramètres canoniques déjà décidés ont été synchronisés dans la roadmap et les résumés concernés. Le document historique reste à réconcilier. Le statut documentaire ne vaut pas validation technique.

**Dernière mise à jour :** 2026-10-15
