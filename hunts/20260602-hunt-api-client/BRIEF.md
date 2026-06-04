# Bug Hunt — Client API mocké

## Contexte

Cette suite de tests couvre le module `weather_client` — un wrapper HTTP autour d'une API météo externe.
Suite à un refactor du 30 mai, plusieurs tests ont commencé à échouer.
**Le code de production (`src/`) n'a pas changé et est correct.**

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec est causé par 1 bug dans les fichiers de test
3. Corrige les bugs **uniquement dans `tests/`** — ne touche pas à `src/`
4. Lance `pytest tests/ -v` après chaque correction
5. Quand tous les tests passent, dis "j'ai fini"

## Règles

- Tu ne modifies PAS les fichiers dans `src/`
- Chaque test qui échoue a exactement 1 bug à corriger
- Les tests qui passent déjà sont corrects — ne les touche pas
