# Bug Hunt — Calculateur de livraison

## Contexte

Cette suite de tests couvrait le module `delivery` qui calcule les frais de livraison selon le poids et la zone géographique.
Suite à un refactor de juin 2026, plusieurs tests ont commencé à échouer.
**Le code de production (`src/`) n'a pas changé et est correct.**

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec est un bug dans les fichiers de test
3. Corrige les bugs **uniquement dans `tests/`** — ne touche pas à `src/`
4. Quand tous les tests passent, dis "j'ai fini"

## Règles

- Tu ne modifies PAS les fichiers dans `src/`
- Chaque test qui échoue a exactement 1 bug à corriger
- Les tests qui passent déjà sont corrects — ne les touche pas
- Lance `pytest tests/ -v` après chaque correction pour vérifier
