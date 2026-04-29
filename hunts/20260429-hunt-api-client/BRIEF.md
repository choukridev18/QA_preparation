# Bug Hunt — Client API météo

## Contexte

Cette suite de tests couvrait le module `WeatherClient` — un wrapper autour d'une
API météo externe qui expose trois méthodes : `get_temperature`, `get_forecast` et
`get_alerts`. Suite à un refactor du 14 avril, plusieurs tests ont commencé à
échouer sans raison apparente.

**Le code de production (`src/`) n'a pas changé et est correct. Ne le touche pas.**

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec contient 1 bug dans les fichiers de test
3. Corrige les bugs **uniquement dans `tests/`** — ne touche pas à `src/`
4. Lance `pytest tests/ -v` après chaque correction pour vérifier
5. Quand tous les tests passent, dis "j'ai fini"

## Lancer les tests

```bash
cd hunts/20260429-hunt-api-client
.venv/bin/pytest tests/ -v
```

## Règles

- Tu ne modifies PAS les fichiers dans `src/`
- Chaque test qui échoue a exactement **1 bug** à corriger
- Les 3 tests qui passent déjà sont corrects — ne les touche pas
- Lance `pytest tests/ -v` après chaque correction

## Indices (seulement si bloqué depuis plus de 10 min sur un bug)

<details>
<summary>Quels fichiers regarder en premier</summary>

Tous les bugs sont dans `tests/test_weather_client.py`. Le fichier `tests/conftest.py` est correct.

</details>

<details>
<summary>Type de bugs présents</summary>

Deux bugs d'assertion, un bug de type d'exception attendu, un bug de mock mal configuré (timing), un bug de mock avec mauvais type d'objet.

</details>
