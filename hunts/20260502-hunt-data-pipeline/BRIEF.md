# Bug Hunt — Pipeline de traitement de commandes

## Contexte

Cette suite de tests couvrait le module `pipeline` qui filtre, trie et agrège
des commandes e-commerce. Suite à un refactor du 28 avril, plusieurs tests ont
commencé à échouer.
**Le code de production (`src/`) est correct et ne doit pas être modifié.**

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec a 1 bug dans les fichiers de test
3. Corrige les bugs **uniquement dans `tests/`** — ne touche pas à `src/`
4. Lance `pytest tests/ -v` après chaque correction
5. Quand tout est vert, dis "j'ai fini"

## Lancer les tests

```bash
cd hunts/20260502-hunt-data-pipeline
.venv/bin/pytest tests/ -v
```

## Règles

- Tu ne modifies PAS les fichiers dans `src/`
- Chaque test qui échoue a exactement **1 bug** à corriger
- Les 3 tests qui passent déjà sont corrects — ne les touche pas
