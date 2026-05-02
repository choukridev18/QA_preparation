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

## Indices (seulement si bloqué depuis plus de 10 min)

<details>
<summary>Quels fichiers regarder</summary>

Les bugs sont dans `tests/test_pipeline.py` et `tests/conftest.py`.
</details>

<details>
<summary>Type de bugs présents</summary>

Deux bugs d'assertion, un bug de type d'exception attendu, un bug de fixture, un bug de mock.
</details>
