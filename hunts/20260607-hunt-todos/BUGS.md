# Liste des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini</summary>

## Bug 1 — test_format_title_capitalizes

**Symptôme :** `assert 'Faire la vaisselle' == 'FAIRE la vaisselle'`
**Cause :** La valeur attendue est en majuscules partiellement — `capitalize()` met tout en minuscule sauf la première lettre.
**Correction :** `"FAIRE la vaisselle"` → `"Faire la vaisselle"`

---

## Bug 2 — test_add_todo_raises_on_invalid_priority

**Symptôme :** `ValueError` levée mais `pytest.raises(KeyError)` attendait `KeyError`.
**Cause :** `add_todo` lève `ValueError` pour priorité invalide, pas `KeyError`.
**Correction :** `pytest.raises(KeyError)` → `pytest.raises(ValueError)`

---

## Bug 3 — test_get_pending_returns_only_undone

**Symptôme :** `assert ['Appeler le médecin', 'Faire les courses'] == ['Faire les courses', 'Appeler le médecin']`
**Cause :** `get_pending` trie par id croissant — "Faire les courses" (id=1) vient avant "Appeler le médecin" (id=2).
**Correction :** Inverser l'ordre dans la liste attendue.

---

## Bug 4 — test_add_todo_increments_id

**Symptôme :** `assert 1 == 2` — le premier id est 1, pas 2.
**Cause :** Les ids démarrent à 1, donc `t1["id"]` vaut `1`.
**Correction :** `assert t1["id"] == 2` → `assert t1["id"] == 1`

</details>
