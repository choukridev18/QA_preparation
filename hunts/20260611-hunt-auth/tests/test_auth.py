import pytest
from src import auth


# ✅ PASSE — test correct
def test_register_new_user_returns_true(registered_user):
    """Enregistrer un nouvel utilisateur retourne True."""
    result = auth.register("bob", "pass456")
    assert result is True


# ✅ PASSE — test correct
def test_login_valid_credentials_returns_token(registered_user):
    """Un login valide retourne un token non vide."""
    token = auth.login("alice", "secret123")
    assert token is not None
    assert len(token) > 0


# ✅ PASSE — test correct
def test_logout_invalidates_token(active_token):
    """Après logout, le token n'est plus valide."""
    result = auth.logout(active_token)
    assert result is True
    assert auth.is_authenticated(active_token) is False


# 🐛 BUG 1
def test_register_existing_user_returns_false(registered_user):
    """Enregistrer un utilisateur déjà existant retourne False."""
    result = auth.register("alice", "autremdp")
    assert result is False  # BUG : alice existe déjà, register() retourne False


# 🐛 BUG 2
def test_login_wrong_password_returns_none(registered_user):
    """Un login avec mauvais mot de passe retourne None."""
    # BUG : login() retourne None, ne lève pas d'exception
    assert auth.login("alice", "mauvaismdp") is None


# 🐛 BUG 3
def test_is_authenticated_with_valid_token(active_token):
    """Un token valide est authentifié."""
    assert (
        auth.is_authenticated(active_token) is True
    )  # BUG : le token est valide, devrait être True


# 🐛 BUG 4
def test_get_username_returns_correct_user(active_token):
    """get_username retourne le bon nom d'utilisateur."""
    result = auth.get_username(active_token)
    assert result == "alice"  # BUG : le token appartient à "alice", pas "bob"


# 🐛 BUG 5 — subtil
def test_logout_unknown_token_returns_false():
    """Logout avec un token inexistant retourne False."""
    result = auth.logout("token-qui-nexiste-pas")
    assert result is False  # BUG : logout retourne False pour un token inconnu
