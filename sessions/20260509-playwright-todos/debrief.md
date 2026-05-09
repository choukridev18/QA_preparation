# Debrief — Gestionnaire de tâches (Playwright)

## Résultat

5/5 tests passent. Les 7 TODOs du POM sont implémentés. Les 2 tests supplémentaires écrits.

## Ce qui s'est bien passé

- `navigate()`, `add_todo()`, `delete_todo()` implémentés sans aide
- `is_empty()` : bonne intuition d'utiliser `is_visible()` plutôt qu'un `if/else`
- `delete_todo()` avec f-string dynamique : bon réflexe
- Double assertion dans `test_delete_one_of_three_leaves_two` (vérifier les 3 avant, puis les 2 après) — bonne pratique

## Points travaillés

- **`set_filter`** : mapping nécessaire entre les clés internes (`"active"`) et les textes visibles dans le DOM (`"Actives"`) via un dictionnaire `labels`
- **`get_visible_count`** : `locator("#todo-list")` compte le conteneur (1 résultat), pas ses enfants — il faut `locator("#todo-list li")`
- **`mark_done`** : aria-label dynamique avec f-string `f"Marquer {title} comme terminée"` — pas de valeur hardcodée
- **Isolation entre tests** : le serveur Flask garde un état global — un fixture `autouse=True` avec une route `/reset` est nécessaire pour repartir d'une liste vide à chaque test

## Erreurs rencontrées

| Erreur | Cause | Fix |
|--------|-------|-----|
| `test_mark_done` et `test_delete` échouaient | État serveur partagé entre tests | Route `/reset` + fixture `autouse` |
| `fill()` appelé sans argument | Oubli du paramètre `title` | `fill(title)` |
| `get_by_role("button")` pour un lien de filtre | Mauvais rôle HTML | `get_by_role("link")` |
| `locator("#todo-list").count()` retournait 1 | Compte le conteneur, pas les `<li>` | `locator("#todo-list li").count()` |

## Notions clés retenues

- `get_by_label` pour les inputs et boutons avec `aria-label`
- `get_by_role("link")` pour les liens de navigation
- `is_visible()` pour vérifier la présence d'un élément conditionnel
- L'isolation des tests : chaque test doit repartir d'un état propre
- Arrange / Act / Assert : séparer la préparation, l'action, et la vérification
