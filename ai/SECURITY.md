# Merge — Security & Secrets Policy

**Statut : APPROUVÉ**  
**Date : 2026-08-20**

## 1. Objectif

Protéger le dépôt, les clés API, les données locales et le budget du système multi-agents.

## 2. Secrets

- Aucune clé API, aucun token, mot de passe ou certificat privé dans Git.
- Les secrets sont fournis par variables d'environnement ou gestionnaire de secrets.
- `.env` est ignoré par Git ; `.env.example` contient uniquement des noms de variables et des valeurs non sensibles.
- Une clé exposée doit être considérée comme compromise et révoquée immédiatement.
- Les logs ne doivent jamais afficher de secret, même partiellement.

## 3. Principe du moindre privilège

Les agents reçoivent uniquement les permissions nécessaires à leur tâche. Les opérations critiques (architecture majeure, suppression importante, exposition de secrets, merge risqué) nécessitent une validation humaine.

## 4. Validation des entrées/sorties IA

Toute réponse d'un fournisseur externe doit être traitée comme une entrée non fiable :

- taille maximale ;
- type attendu ;
- format attendu ;
- contenu obligatoire ;
- refus des instructions qui tentent de modifier les règles d'orchestration ;
- aucune exécution directe de code généré sans validation.

## 5. Limitation de ressources

Chaque requête est soumise à des limites de tokens, coût, durée, concurrence et nombre de tentatives. Le système doit refuser proprement une requête qui dépasse une limite au lieu de la contourner.

## 6. Rate limiting

Les limites globales préviennent les boucles, erreurs de configuration et surconsommations. Des limites spécifiques par fournisseur et par tâche doivent être ajoutées lors de l'intégration réelle.

## 7. Timeouts et retries

- Timeout par requête obligatoire.
- Nombre de retries limité.
- Backoff exponentiel recommandé.
- Les erreurs non récupérables ne sont pas rejouées indéfiniment.

## 8. Circuit breaker

Après plusieurs échecs consécutifs, le fournisseur est temporairement désactivé. Le système attend le cooldown avant de permettre de nouvelles tentatives.

## 9. Protection contre les coûts

Une requête doit être refusée si son coût estimé dépasse le budget de la tâche, de la session ou de la journée. Le système doit conserver un compteur de consommation local et traçable.

## 10. Audit

Chaque appel réel devra pouvoir être associé à :

- task ID ;
- agent/role ;
- fournisseur ;
- modèle ;
- timestamp ;
- tokens entrée/sortie ;
- coût estimé/réel si disponible ;
- durée ;
- statut ;
- motif d'échec éventuel.

Les secrets et contenus sensibles ne doivent pas être enregistrés dans les logs d'audit.

## 11. Règle d'arrêt

Si une limite de sécurité est atteinte, le système s'arrête proprement, signale la raison et attend une action explicite de l'orchestrateur/Game Director. Il ne doit jamais augmenter automatiquement les limites.

## 12. Pré-API

Ces règles peuvent être implémentées et testées avant toute clé API. Les valeurs de `.env.example` constituent des garde-fous de départ et devront être calibrées après observation réelle.
