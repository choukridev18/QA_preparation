# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — tests/test_contacts.py, test_remove_contact_returns_true

**Symptôme :** `AssertionError: assert True is False`
**Cause :** `remove_contact` retourne `True` quand le contact est supprimé, mais le test assert `result is False`.
**Correction :** `assert result is True`

## Bug 2 — tests/test_contacts.py, test_remove_nonexistent_contact_raises

**Symptôme :** `Failed: DID NOT RAISE <class 'TypeError'>`
**Cause :** `remove_contact` lève `ContactError`, pas `TypeError`.
**Correction :** `with pytest.raises(ContactError):`

## Bug 3 — tests/test_contacts.py, test_list_contacts_sorted_alphabetically

**Symptôme :** `AssertionError: assert ['Alice Dupont', 'Marc Bernard', 'Zineb Amrani'] != ['Zineb Amrani', 'Alice Dupont', 'Marc Bernard']`
**Cause :** `list_contacts` trie par ordre alphabétique — l'ordre attendu dans le test était incorrect.
**Correction :** `assert names == ["Alice Dupont", "Marc Bernard", "Zineb Amrani"]`

## Bug 4 — tests/test_contacts.py, test_find_by_email_case_insensitive

**Symptôme :** `AssertionError: assert {'name': 'Alice Dupont', ...} is None`
**Cause :** `find_by_email` est insensible à la casse et trouve bien le contact — le test assert `result is None` au lieu de vérifier que le contact est trouvé.
**Correction :** `assert result is not None`

</details>
