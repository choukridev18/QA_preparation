# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini</summary>

## Bug 1 — `tests/test_coupons.py`, `test_percent_fractional_result`
**Symptôme :** `AssertionError: assert 17.99 == 17.991`
**Cause :** comparaison float trop stricte / mauvaise valeur attendue. `round(19.99 * 0.9, 2) == 17.99`
**Correction :** `assert result == 17.99` ou `assert result == pytest.approx(17.99)`

## Bug 2 — `tests/conftest.py`, fixture `welcome10`
**Symptôme :** `TypeError` / coupon `None` dans `test_welcome10_applies`
**Cause :** la fixture crée le `Coupon` mais **ne le retourne pas**
**Correction :** ajouter `return Coupon(...)`

## Bug 3 — `tests/test_coupons.py`, `test_negative_price_raises`
**Symptôme :** `Failed: DID NOT RAISE TypeError` (ou ValueError non capturée)
**Cause :** le code lève `ValueError`, le test attend `TypeError`
**Correction :** `pytest.raises(ValueError)`

## Bug 4 — `tests/test_coupons.py`, `test_remote_percent_uses_api_rate`
**Symptôme :** `RuntimeError: network call not available...`
**Cause :** mauvais chemin de patch (`"fetch_rate_from_api"` au lieu de `"src.coupons.fetch_rate_from_api"`)
**Correction :** `patch("src.coupons.fetch_rate_from_api", return_value=20)`

## Bug 5 — `tests/test_coupons.py`, `test_remote_percent_retries_on_failure`
**Symptôme :** `TypeError` (liste / float) puis, après `side_effect`, `RuntimeError: timeout`
**Cause :** 1) `return_value` au lieu de `side_effect` 2) le code prod n’a pas de retry : il faut 2 appels dans le test
**Correction :**
```python
with patch("src.coupons.fetch_rate_from_api", side_effect=[RuntimeError("timeout"), 10]):
    with pytest.raises(RuntimeError):
        apply_remote_percent(100, "RETRY10")
    assert apply_remote_percent(100, "RETRY10") == 90.0
```

</details>
