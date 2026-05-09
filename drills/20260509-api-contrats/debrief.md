# Debrief — Drill API contrats (20260509)

## Résultat

12/12 tests passent.

## Ce qui s'est bien passé

- Structure générale des tests acquise : `response = client.verb("/url")` → `assert status_code` → `data = get_json()` → `assert`
- `pytest.mark.parametrize` compris et appliqué sur les TODO 5 et 6
- Bon réflexe d'aller lire `server.py` pour trouver les URLs et les champs attendus
- `len(data["orders"])` vs `len(data)` — distinction comprise entre le dict wrapper et la liste

## Points à retenir

- **`response.get_json()`** et non `response.json()` ni `client.get_json()` — c'est une méthode de l'objet réponse Flask
- **URL ≠ clé JSON** : l'URL `/orders` et la clé `"orders"` dans le body sont deux choses distinctes — le nom de la clé est défini dans `jsonify({"orders": ...})` dans le serveur
- **`parametrize` avec scalaires vs dicts** : quand on varie un seul champ, la liste contient des valeurs directes (`[0, -1, "deux"]`) ; quand on varie tout le payload, elle contient des dicts (`[{}, {"product_id": 1}, ...]`)
- **Codes HTTP à connaître** : 200 (OK), 201 (créé), 400 (champs manquants), 404 (introuvable), 409 (conflit/stock), 422 (valeur invalide)

## Erreurs récurrentes

| Erreur | Fix |
|--------|-----|
| `client.get_json()` | `response.get_json()` |
| `assert response == 200` | `assert response.status_code == 200` |
| `len(data)` au lieu de `len(data["orders"])` | Toujours accéder à la clé de la liste |
| Payload avec `"stock"` au lieu de `"quantity"` | Lire `server.py` pour voir ce que l'API attend |
| Import automatique `from werkzeug...` | Supprimer les imports inutiles ajoutés par l'IDE |
