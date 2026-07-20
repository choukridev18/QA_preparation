# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini</summary>

## Bug 1 — tests/test_notifications.py, ligne 28

**Symptôme :** `assert 0.27999999999999997 == 0.28`
**Cause :** Les floats ne peuvent pas être comparés avec `==` à cause des erreurs de précision binaire. `0.7 * 0.4` ne vaut pas exactement `0.28` en mémoire.
**Correction :** `assert result == pytest.approx(0.28)`

---

## Bug 2 — tests/test_notifications.py, ligne 31

**Symptôme :** `ModuleNotFoundError: No module named 'notifications'`
**Cause :** Le chemin de patch `"notifications.requests.post"` est incorrect. Le module se trouve dans `src/notifications.py`, donc le chemin correct est `"src.notifications.requests.post"`.
**Correction :** `@mock.patch("src.notifications.requests.post")`

---

## Bug 3 — tests/test_notifications.py, ligne 38

**Symptôme :** `Failed: DID NOT RAISE` ou `assert TypeError == ValueError`
**Cause :** La fonction `create_notification` lève une `ValueError` quand `user_id` est vide, pas une `TypeError`. Le test attend le mauvais type d'exception.
**Correction :** `with pytest.raises(ValueError):`

---

## Bug 4 — tests/conftest.py, ligne 7

**Symptôme :** `TypeError: 'NoneType' object is not subscriptable`
**Cause :** La fixture `sample_notification` crée la notification mais oublie de la retourner. Sans `return`, Python retourne `None` implicitement.
**Correction :** Ajouter `return notif` à la fin de la fixture.

</details>
