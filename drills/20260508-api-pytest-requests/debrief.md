# Débrief — Tests API REST — 08/05/2026

## Résultat
8/8 tests passent.

## Points forts

- **Pattern Arrange/Act/Assert bien appliqué** : les tests qui nécessitent une ressource
  existante (TODOs 3, 6, 7) créent d'abord la tâche, récupèrent l'id, puis agissent —
  c'est exactement la bonne structure
- **`task_id` dynamique** : tu utilises l'id retourné par le POST au lieu de hardcoder `1` —
  les tests sont indépendants de l'ordre d'exécution
- **Status code + body vérifiés** : la plupart des tests vérifient les deux — bonne rigueur
- **TODO 7** complet : créer → supprimer → GET → 404 — tu as bien couvert les deux assertions

## Points à retravailler

- **Imports inutiles** : `import json` et `from werkzeug.wrappers import response` en tête
  de fichier ne servent à rien — à supprimer. Des imports inutiles polluent le code et
  peuvent masquer des erreurs.

- **`assert data["done"] == False`** : en Python, la convention est `assert data["done"] is False`
  (ou `assert not data["done"]`). `==` fonctionne mais `is` est plus idiomatique pour les booléens.
  Même chose pour `== True` → `is True`.

- **Tests 4 et 8 ne vérifient pas le body** : tu vérifies le status 404 mais pas le message
  d'erreur dans le body. Un test complet vérifie les deux :
  ```python
  assert delete.status_code == 404
  data = delete.get_json()
  assert "error" in data
  ```

## 1 chose à retenir

**Arrange / Act / Assert** — tout test qui agit sur une ressource suit ce schéma :
créer la ressource (Arrange), faire l'action à tester (Act), vérifier le résultat (Assert).
Si tu te retrouves à hardcoder un id, c'est souvent le signe qu'il manque la phase Arrange.
