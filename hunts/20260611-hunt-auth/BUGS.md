# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — tests/test_auth.py, ligne 22

**Symptôme :** `AssertionError: assert False is True`
**Cause :** `assert result is True` mais `register("alice", ...)` retourne `False` car alice existe déjà.
**Correction :** `assert result is False`

## Bug 2 — tests/test_auth.py, ligne 28

**Symptôme :** `Failed: DID NOT RAISE <class 'ValueError'>`
**Cause :** `login()` retourne `None` en cas de mauvais mot de passe — elle ne lève pas d'exception.
**Correction :** Remplacer `pytest.raises(ValueError)` par `assert auth.login("alice", "mauvaismdp") is None`

## Bug 3 — tests/test_auth.py, ligne 34

**Symptôme :** `AssertionError: assert True is False`
**Cause :** `assert auth.is_authenticated(active_token) is False` — mais le token est valide, donc la valeur est `True`.
**Correction :** `assert auth.is_authenticated(active_token) is True`

## Bug 4 — tests/test_auth.py, ligne 40

**Symptôme :** `AssertionError: assert 'alice' == 'bob'`
**Cause :** Le token appartient à "alice" (créée par la fixture `registered_user`), pas "bob".
**Correction :** `assert result == "alice"`

## Bug 5 — tests/test_auth.py, ligne 46

**Symptôme :** `AssertionError: assert False is True`
**Cause :** `logout()` retourne `False` pour un token inconnu — l'assertion attendait `True`.
**Correction :** `assert result is False`

</details>
