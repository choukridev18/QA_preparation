# Liste des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — tests/test_booking.py, `test_get_available_slots_returns_list`

**Symptôme :** `ModuleNotFoundError: No module named 'booking'`

**Cause :** Le chemin de patch est `"booking.requests.get"` — il manque le préfixe `src.`. Python cherche un module `booking` à la racine, qui n'existe pas. Le module s'appelle `src.booking`.

**Correction :** Remplacer `@mock.patch("booking.requests.get")` par `@mock.patch("src.booking.requests.get")`

---

## Bug 2 — tests/test_booking.py, `test_send_confirmation_email_success`

**Symptôme :** `AssertionError: assert False is True`

**Cause :** `mock_post.side_effect = mock_response` fait que l'appel à `mock_post(...)` invoque `mock_response(...)` comme une fonction, retournant un nouveau MagicMock dont `.status_code` n'est pas `200`. Il faut `return_value` pour que le mock retourne directement `mock_response`.

**Correction :** Remplacer `mock_post.side_effect = mock_response` par `mock_post.return_value = mock_response`

---

## Bug 3 — tests/test_booking.py, `test_cancel_nonexistent_booking_raises`

**Symptôme :** `ValueError: Réservation 'BOOKING-9999' introuvable.` non capturée par `pytest.raises(TypeError)`

**Cause :** La docstring de `cancel_booking` indique clairement `Lève ValueError` — le test attend le mauvais type d'exception.

**Correction :** Remplacer `pytest.raises(TypeError)` par `pytest.raises(ValueError)`

---

## Bug 4 — tests/test_booking.py, `test_calculate_price_with_discount`

**Symptôme :** `AssertionError: assert 0.30000000000000004 == 0.3`

**Cause :** `1.0 * (1 - 0.7)` produit `0.30000000000000004` à cause de la représentation binaire des flottants. Une comparaison `==` stricte échoue.

**Correction :** Remplacer `assert result == 0.3` par `assert result == pytest.approx(0.3)`

</details>
