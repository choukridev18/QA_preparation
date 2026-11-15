# Bug Hunt — To-do (interface web)

## Contexte

Application interne **Mes tâches** : ajouter une tâche, la voir dans la liste, la marquer comme faite, compteur « à faire ».
Après une mise à jour de la suite E2E, **plusieurs tests échouent**.
**Le code dans `app/`, les templates et `pages/todos_page.py` est correct — ne pas les modifier.**

## Lancer le serveur

```bash
cd app
python3 server.py
```

App : http://127.0.0.1:5001

## Ta mission

1. Lance `pytest tests/ -v` (depuis la racine du hunt)
2. Lis les tracebacks — **1 bug par test** qui échoue, dans `tests/` ou `conftest.py`
3. Corrige **uniquement** les fichiers de test (et `conftest.py` si besoin)
4. Relance après chaque correction
5. Quand tout est vert, dis **« j'ai fini »**

## Règles

- Ne touche pas à `app/`, `templates/`, ni `pages/`
- Les tests qui passent au départ sont corrects — ne les casse pas
- Ne regarde pas `BUGS.md` avant la fin