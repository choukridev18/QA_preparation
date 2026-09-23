# Bug Hunt — Moteur de coupons

## Contexte

Cette suite de tests couvre le module `src/coupons.py` qui applique des codes promo
(pourcentage, montant fixe, taux distant via API).
Suite à un refactor des tests, plusieurs cas ont commencé à échouer.
**Le code de production (`src/`) n'a pas changé et est correct.**

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec a 1 bug dans les fichiers de test
3. Corrige les bugs **uniquement dans `tests/`** (y compris `conftest.py`)
4. Lance `pytest tests/ -v` après chaque correction
5. Quand tout est vert, dis "j'ai fini"

## Règles

- Tu ne modifies PAS les fichiers dans `src/`
- Chaque test qui échoue a exactement 1 bug
- Les tests qui passent déjà sont corrects — ne les touche pas

## Lancer

```bash
cd hunts/20260923-hunt-coupons
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pytest tests/ -v
```
