import pytest
from src.contacts import (
    add_contact,
    remove_contact,
    find_by_email,
    list_contacts,
    count,
    ContactError,
)


# ✅ PASSE
def test_add_contact_returns_contact():
    """Ajouter un contact retourne un dict avec les bonnes clés."""
    c = add_contact("Alice Dupont", "alice@example.com")
    assert c["name"] == "Alice Dupont"
    assert c["email"] == "alice@example.com"


# ✅ PASSE
def test_count_increments_after_add():
    """Le compteur augmente après chaque ajout."""
    add_contact("Alice Dupont", "alice@example.com")
    add_contact("Marc Bernard", "marc@example.com")
    assert count() == 2


# ✅ PASSE
def test_find_by_email_returns_none_if_not_found():
    """find_by_email retourne None si l'email n'existe pas."""
    result = find_by_email("inconnu@example.com")
    assert result is None


# 🐛 BUG 1
def test_add_contact_raises_on_empty_name():
    """Ajouter un contact sans nom lève une exception."""
    with pytest.raises(ValueError):
        add_contact("", "test@example.com")


# 🐛 BUG 2
def test_remove_contact_returns_true():
    """Supprimer un contact existant retourne True."""
    c = add_contact("Alice Dupont", "alice@example.com")
    result = remove_contact(c["id"])
    assert result is True


# 🐛 BUG 3
def test_remove_nonexistent_contact_raises(populated):
    """Supprimer un contact inexistant lève ContactError."""
    with pytest.raises(ContactError):
        remove_contact(999)


# 🐛 BUG 4
def test_list_contacts_sorted_alphabetically(populated):
    """list_contacts retourne les contacts triés par nom."""
    result = list_contacts()
    names = [c["name"] for c in result]
    assert names == ["Alice Dupont", "Marc Bernard", "Zineb Amrani"]


# 🐛 BUG 5
def test_find_by_email_case_insensitive():
    """find_by_email est insensible à la casse."""
    add_contact("Alice Dupont", "alice@example.com")
    result = find_by_email("ALICE@EXAMPLE.COM")
    assert result is not None
