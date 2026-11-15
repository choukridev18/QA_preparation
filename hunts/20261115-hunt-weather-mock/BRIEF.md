# Bug Hunt — Client météo mocké

## Contexte

Le module `weather_client` appelle une API météo externe via `requests`.
Les tests mockent `get` pour ne jamais toucher le réseau.
Après une fusion du 14 novembre, **4 tests échouent**.
**Le code dans `src/` est correct — ne pas le modifier.**

## Ta mission

1. Depuis la racine du hunt : `pytest tests/ -v`
2. Chaque échec = **1 bug** dans `tests/` (ou `conftest.py`)
3. Corrige **uniquement** ces fichiers
4. Relance après chaque correction
5. Tout vert → dis **« j'ai fini »**

## Règles

- Pas de modification dans `src/`
- Les 3 premiers tests qui passent sont des repères — ne les casse pas
- Ne ouvre pas `BUGS.md` avant la fin