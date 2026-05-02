# SPOILER — ne lire qu'après avoir terminé

## Bug 1 — Assertion sur liste triée dans le mauvais ordre
**Test :** `test_sort_by_amount_returns_descending`
**Symptôme :** `AssertionError: assert [200.0, 100.0, 50.0] == [50.0, 100.0, 200.0]`
**Cause :** La liste attendue est en ordre croissant, mais `sort_by_amount` retourne en décroissant.
**Correction :**
```python
# avant (BUG)
assert [o.amount for o in result] == [50.0, 100.0, 200.0]
# après
assert [o.amount for o in result] == [200.0, 100.0, 50.0]
```

---

## Bug 2 — Fixture qui retourne None (return manquant)
**Test :** `test_filter_valid_orders_with_fixture`
**Symptôme :** `TypeError: 'NoneType' object is not iterable`
**Cause :** La fixture `sample_orders` dans `conftest.py` construit la liste mais oublie le `return`.
**Correction :**
```python
# conftest.py — ajouter à la fin de la fixture
return orders
```

---

## Bug 3 — Mauvais type d'exception dans pytest.raises
**Test :** `test_compute_discount_invalid_code_raises`
**Symptôme :** `ValueError: Code promo inconnu : INVALIDE` sort du bloc `with`
**Cause :** Le test attend `KeyError` mais la fonction lève `ValueError`.
**Correction :**
```python
# avant (BUG)
with pytest.raises(KeyError):
# après
with pytest.raises(ValueError):
```

---

## Bug 4 — Assertion sur valeur None au lieu de dict vide
**Test :** `test_get_category_totals_empty_list`
**Symptôme :** `AssertionError: assert {} is None`
**Cause :** `get_category_totals([])` retourne un dict vide `{}`, pas `None`.
**Correction :**
```python
# avant (BUG)
assert result is None, "..."
# après
assert result == {}
```

---

## Bug 5 — side_effect au lieu de return_value pour le mock
**Test :** `test_fetch_exchange_rate_mocked`
**Symptôme :** `TypeError: string indices must be integers, not 'str'`
**Cause :** `mock_get.return_value.json.side_effect = {"rate": 1.08}` — quand `side_effect` est un dict (iterable), le mock retourne les clés une par une ; le premier appel retourne la string `"rate"`. Ensuite `"rate"["rate"]` plante.
**Correction :**
```python
# avant (BUG)
mock_get.return_value.json.side_effect = {"rate": 1.08}
# après
mock_get.return_value.json.return_value = {"rate": 1.08}
```
