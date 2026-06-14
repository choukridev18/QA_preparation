# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — tests/test_invoice.py, ligne 26

**Symptôme :** `AssertionError: assert 69.92999999999999 == 69.93`
**Cause :** Comparaison de float sans tolérance — `99.9 * 0.7` produit une valeur avec erreur de précision flottante.
**Correction :** `assert result == pytest.approx(69.93)`

## Bug 2 — tests/test_invoice.py, ligne 32

**Symptôme :** `AssertionError: assert 130.0 == 100.0`
**Cause :** Le subtotal de `2×50 + 1×30` est `130.0`, pas `100.0`.
**Correction :** `assert result["subtotal"] == 130.0`

## Bug 3 — tests/test_invoice.py, ligne 38

**Symptôme :** `Failed: DID NOT RAISE <class 'TypeError'>`
**Cause :** `apply_discount` lève `InvoiceError`, pas `TypeError`.
**Correction :** `with pytest.raises(InvoiceError):`

## Bug 4 — tests/test_invoice.py, ligne 44

**Symptôme :** `AssertionError: assert 117.0 == 140.4` (environ)
**Cause :** Le test vérifie `total_ht` (117.0) mais compare à 140.4 qui est la valeur de `total_ttc`.
**Correction :** `assert pytest.approx(result["total_ttc"]) == 140.4`

## Bug 5 — tests/test_invoice.py, ligne 50

**Symptôme :** `AssertionError: assert 26.0 == 20.0`
**Cause :** La remise de 20% sur 130.0 est `26.0`, pas `20.0`.
**Correction :** `assert result["discount"] == pytest.approx(26.0)`

</details>
