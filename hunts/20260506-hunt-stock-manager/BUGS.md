# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — tests/test_stock.py, ligne 36

**Symptôme :** `AssertionError: assert 0.30000000000000004 == 0.3`
**Cause :** Comparaison d'un résultat `float` avec `==`. Les opérations sur les flottants accumulent des erreurs de précision — `0.1 + 0.2` ne vaut pas exactement `0.3` en binaire.
**Correction :** `assert calculate_stock_value(products) == pytest.approx(0.3)`

## Bug 2 — tests/test_stock.py, ligne 42

**Symptôme :** `AssertionError: assert ['Souris', 'Écran'] == ['Écran', 'Souris']`
**Cause :** L'assertion suppose que les produits sont retournés dans un ordre différent de celui de la liste d'entrée. `get_low_stock_products` préserve l'ordre d'entrée — Souris apparaît avant Écran dans `sample_products`.
**Correction :** `assert [p.name for p in low] == ["Souris", "Écran"]`

## Bug 3 — tests/test_stock.py, ligne 48

**Symptôme :** `ValueError: Remise invalide : -5. Doit être entre 0 et 100.`
**Cause :** Le test attend `TypeError` mais `apply_discount` lève `ValueError` pour une remise hors plage. Le mauvais type d'exception est spécifié dans `pytest.raises`.
**Correction :** `with pytest.raises(ValueError):`

</details>
