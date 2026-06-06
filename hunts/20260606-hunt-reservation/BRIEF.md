# Bug Hunt — Système de réservation

## Contexte

Ce module gère les réservations de créneaux horaires pour une plateforme interne. Il s'appuie sur une API calendrier externe (mockée dans les tests) pour récupérer les disponibilités et envoyer des confirmations email.

Suite à un refactor du 6 juin 2026, plusieurs tests ont commencé à échouer.
**Le code dans `src/` est correct et ne doit pas être modifié.**

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec a **1 seul bug** dans `tests/`
3. Corrige les bugs **uniquement dans `tests/test_booking.py`**
4. Lance `pytest tests/ -v` après chaque correction
5. Quand tout est vert, dis "j'ai fini"

## Règles

- Ne touche pas à `src/` — seulement `tests/`
- Chaque test qui échoue a exactement 1 bug
- Les 3 tests qui passent sont corrects — ne les touche pas
- Lis bien les docstrings de `src/booking.py` pour comprendre le comportement attendu
