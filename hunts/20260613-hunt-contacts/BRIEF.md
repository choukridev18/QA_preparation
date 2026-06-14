# Bug Hunt — Gestionnaire de contacts

## Contexte

Cette suite de tests couvrait le module `contacts` qui gère un carnet d'adresses : ajout, suppression, recherche par email, et liste triée. Suite à un refactor récent, plusieurs tests ont commencé à échouer.
**Le code de production (`src/`) n'a pas changé et est correct.**

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec a **1 bug** dans les fichiers de test
3. Corrige les bugs **uniquement dans `tests/`** — ne touche pas à `src/`
4. Lance `pytest tests/ -v` après chaque correction
5. Quand tout est vert, dis "j'ai fini"

## Règles

- Tu ne modifies **PAS** les fichiers dans `src/`
- Chaque test qui échoue a exactement 1 bug à corriger
- Les tests qui passent déjà sont corrects — ne les touche pas
