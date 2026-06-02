# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — tests/test_pricing.py, test_apply_discount_one_third

**Symptôme :** `AssertionError: assert 19.999999999999996 == 20.0`
**Cause :** `1/3` est un float irrationnel — le résultat n'est jamais exactement `20.0` en virgule flottante.
**Correction :** `assert result == pytest.approx(20.0)`

---

## Bug 2 — tests/test_pricing.py, test_validate_discount_above_one

**Symptôme :** `Failed: DID NOT RAISE <class 'TypeError'>` (ou `FAILED` avec mention de TypeError)
**Cause :** `validate_discount` lève une `ValueError`, pas une `TypeError`. Le type d'exception dans `pytest.raises` est incorrect.
**Correction :** `with pytest.raises(ValueError):`

---

## Bug 3 — tests/test_pricing.py, test_get_cheapest_three

**Symptôme :** `AssertionError: assert [1.0, 3.0, 8.5] == [15.0, 3.0, 8.5]`
**Cause :** La liste attendue n'est ni triée ni correcte. `get_cheapest_items` retourne les éléments triés en ordre croissant.
**Correction :** `assert result == [1.0, 3.0, 8.5]`

---

## Bug 4 — tests/test_pricing.py, test_final_price_no_discount

**Symptôme :** `AssertionError: assert 80.0 == 120.0 ± 1.2e-04`
**Cause :** Les arguments `discount_rate` et `tva_rate` sont inversés. `final_price(base_price, 0.20, 0)` applique 20% de remise et 0% de TVA au lieu de l'inverse.
**Correction :** `result = final_price(base_price, 0, 0.20)`

</details>
