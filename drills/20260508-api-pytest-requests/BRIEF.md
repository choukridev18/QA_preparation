# Drill — Tests API REST (Flask test client)

## Contexte

Tu testes une API de gestion de tâches déjà implémentée dans `server.py`.
Pas besoin de lancer un serveur — le client de test Flask simule les requêtes HTTP directement.

## Endpoints disponibles

| Méthode | Route               | Description              | Status attendu |
|---------|---------------------|--------------------------|----------------|
| GET     | `/tasks`            | Liste toutes les tâches  | 200            |
| POST    | `/tasks`            | Crée une tâche           | 201 / 400      |
| GET     | `/tasks/<id>`       | Récupère une tâche       | 200 / 404      |
| PATCH   | `/tasks/<id>/done`  | Marque comme terminée    | 200 / 404      |
| DELETE  | `/tasks/<id>`       | Supprime une tâche       | 204 / 404      |

## Lancer les tests

```bash
cd drills/20260508-api-pytest-requests
pytest test_api.py -v
```

## Ce que tu dois faire

Implémenter les 8 tests dans `test_api.py`. Chaque test a un TODO avec l'entrée et le résultat attendu.

## Référence du client Flask

```python
response = client.get("/tasks")
response = client.post("/tasks", json={"title": "Faire les courses"})
response = client.patch("/tasks/1/done")
response = client.delete("/tasks/1")

response.status_code      # int : 200, 201, 404…
response.get_json()       # dict : body JSON parsé
```

## Critères d'acceptance

- [ ] Les 8 tests passent
- [ ] Chaque test vérifie **le status code ET le body** quand pertinent
- [ ] Les tests sont indépendants (l'ordre d'exécution ne change pas le résultat)
- [ ] Pas de données hardcodées fragiles — utilise l'`id` retourné par le POST pour les tests suivants
