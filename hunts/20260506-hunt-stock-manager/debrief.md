# Débrief — Gestionnaire de stocks (Bug Hunt) — 6 mai 2026

## Résultat

**3 / 3** bugs trouvés.

## Ce que tu maîtrises

- **`pytest.raises` avec le bon type** : tu as identifié que `TypeError` vs `ValueError` ne sont pas interchangeables — le traceback te donne le type exact levé, il suffit de le lire.
- **Lecture des listes dans le traceback** : `assert ['Souris', 'Écran'] == ['Écran', 'Souris']` affiche les deux côtés en clair — pas besoin de deviner.

## Ce qui t'a coûté du temps

- **`pytest.approx`** : notion nouvelle, plusieurs tentatives avant de trouver. Normal pour une première rencontre. À retenir pour tous les tests sur des floats calculés.
- **Bug d'ordre de liste** : difficile d'identifier que le bug était dans l'assertion et non dans la fonction. Dans un bug hunt, `src/` est correct par définition — si un test échoue, c'est le test qui ment.

## Règle à retenir

Deux patterns à reconnaître en moins de 10 secondes :
- `AssertionError: assert 0.30000000000000004 == 0.3` → float → corriger avec `pytest.approx(valeur)`
- `ValueError` dans un `pytest.raises(TypeError)` → mauvais type d'exception dans le test → lire le traceback et corriger le type
