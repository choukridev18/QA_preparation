# Solutions — Bug Hunt : Calculateur de livraison

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini</summary>

## Bug 1 — test_delivery.py, test_calculate_shipping_international

**Symptôme :** `assert 37.5 == 36.0`
**Cause :** La valeur attendue oublie le `BASE_FEE` (1.50). `1.50 + 3.0 × 12.00 = 37.50`, pas `36.0`.
**Correction :**
```python
assert result == 37.5
```

## Bug 2 — test_delivery.py, test_apply_multi_discount_two_items

**Symptôme :** `assert 9.0 == 8.0`
**Cause :** La remise à 2 articles est de -10% (×0.90), pas -20%. `10.0 × 0.90 = 9.0`.
**Correction :**
```python
assert result == 9.0
```

## Bug 3 — test_delivery.py, test_apply_multi_discount_five_items

**Symptôme :** `assert 40.0 == 38.0`
**Cause :** La remise à 5 articles est de -20% (×0.80). `50.0 × 0.80 = 40.0`, pas `38.0`.
**Correction :**
```python
assert result == 40.0
```

## Bug 4 — test_delivery.py, test_delivery_error_on_zero_weight

**Symptôme :** `DeliveryError` levée mais `pytest.raises(TypeError)` ne la capture pas.
**Cause :** `DeliveryError` hérite de `ValueError`, pas de `TypeError`.
**Correction :**
```python
with pytest.raises(DeliveryError):
```

## Bug 5 — test_delivery.py, test_is_free_shipping_heavy_national

**Symptôme :** `assert False is True`
**Cause :** 10 kg en zone nationale = `1.50 + 10×5.00 = 51.50`, avec remise -20% = `41.20` — bien au-dessus de 5€. La livraison n'est pas gratuite.
**Correction :**
```python
assert result is False
```

## Bug 6 — test_delivery.py, test_cheapest_zone_for_light_package

**Symptôme :** `assert 'local' == 'international'`
**Cause :** La zone la moins chère est toujours `"local"` (taux le plus bas). L'assertion attendait `"international"` à tort.
**Correction :**
```python
assert result == "local"
```

</details>
