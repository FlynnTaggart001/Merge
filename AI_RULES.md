# AI Collaboration Rules - AI_RULES.md

## Rôles et Responsabilités

### ChatGPT
**Rôle**: Lead Developer

**Responsabilités**:
- Architecture générale du projet
- Intégration des systèmes
- Code principal et infrastructure
- Systèmes techniques
- Coordination technique
- Résolution des conflits entre systèmes

---

### Claude
**Rôle**: Gameplay & RPG Designer

**Responsabilités**:
- Compétences et progression
- Combat
- Magie
- Inventaire et équipement
- Factions et réputation
- Quêtes
- Équilibrage des systèmes RPG

---

### Gemini
**Rôle**: World Designer & Content Creator

**Responsabilités**:
- Monde et régions
- Lieux et géographie
- PNJ et caractères
- Dialogues
- Lore et worldbuilding
- Objets et artefacts
- Événements
- Contenu général
- Level design conceptuel

---

### Grok
**Rôle**: QA / Critic

**Responsabilités**:
- Tests et vérification
- Détection de bugs
- Détection d'incohérences
- Recherche d'exploits
- Problèmes de gameplay
- Équilibrage critique
- Vérification des régressions
- Critique constructive des systèmes

---

### GitHub Copilot
**Rôle**: Repository Maintenance & Documentation

**Responsabilités**:
- Organisation du dépôt
- Maintenance de la documentation
- Gestion Git
- Cohérence des fichiers
- Corrections documentaires mineures
- Assistance ponctuelle
- Liaison entre les différentes IA

---

## Autorité Finale

**Le Game Director (utilisateur)** prend les décisions finales sur :
- La vision générale du projet
- Les changements majeurs de direction
- Les conflits non résolus
- Les priorités de développement
- Les décisions arbitrales

Les IA fournissent des recommandations, propositions et expertise, mais l'utilisateur a le dernier mot.

---

## Principes de Collaboration

1. **Communication claire** : Tous les changements importants sont documentés
2. **Respect des domaines** : Chaque IA respecte les responsabilités des autres
3. **Cohérence** : Les systèmes doivent fonctionner ensemble
4. **Documentation** : Les décisions sont justifiées et expliquées
5. **Flexibilité** : La collaboration peut nécessiter des ajustements
6. **Aide mutuelle** : Les IA s'entraident sur les zones de chevauchement

---

## Statut des Propositions

Chaque proposition ou décision doit être clairement étiquetée :

- **À DÉCIDER** : Nécessite une décision du Game Director
- **PROPOSITION À VALIDER** : Idée en attente d'approbation
- **DÉCIDÉ** : Approuvé et validé
- **EN COURS** : Actuellement en développement
- **COMPLÉTÉ** : Terminé et testé

---

## Source de Vérité

En cas de contradiction :

1. Décision explicite du Game Director
2. GAME_BIBLE.md
3. specs/ (fichiers de spécification)
4. docs/ (documentation générale)
5. Propositions individuelles des IA

---

## Règles de Communication

### Dans les Pull Requests
- Description claire du changement
- Justification de la modification
- Lien vers les issues/décisions concernées
- Revue requise avant fusion

### Dans les Commits
- Messages clairs et descriptifs
- Petits commits atomiques
- Référence aux issues quand applicable

### Documentation
- Chaque système doit être documenté
- Les décisions doivent être justifiées
- Les dépendances doivent être clarifiées

---

## Dépendances Entre Systèmes

Antés de commencer le travail sur un système, vérifier les dépendances :

- **Combat** dépend de : Attributs, Compétences, Équipement, IA Ennemis
- **Magie** dépend de : Attributs, Compétences, Ressource Magique
- **Quêtes** dépend de : PNJ, Dialogues, Factions, Réputation
- **Factions** dépend de : Lore, Réputation, PNJ, Monde
- **Inventaire** dépend de : Équipement, Poids, Système de prix

---

**Dernière mise à jour** : 2026-08-19
**Statut** : En vigueur
