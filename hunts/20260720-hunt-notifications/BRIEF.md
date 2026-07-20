# Bug Hunt — Système de notifications

## Contexte

Cette suite de tests couvrait le module `notifications` qui gère le calcul de priorités d'alertes, l'envoi de messages et la création de notifications utilisateur. Suite à un refactor du 18 juillet, plusieurs tests ont commencé à échouer.
**Le code de production (`src/`) n'a pas changé et est correct.**

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec a exactement 1 bug dans les fichiers de test
3. Corrige les bugs **uniquement dans `tests/`** — ne touche pas à `src/`
4. Lance `pytest tests/ -v` après chaque correction pour vérifier
5. Quand tous les tests passent, dis "j'ai fini"

## Règles

- Tu ne modifies PAS les fichiers dans `src/`
- Chaque test qui échoue a exactement 1 bug à corriger
- Les tests qui passent déjà sont corrects — ne les touche pas
