"""
Module de gestion de contacts.
Permet d'ajouter, supprimer, rechercher et lister des contacts.
"""

CONTACTS: list[dict] = []
_next_id: int = 1


class ContactError(ValueError):
    """Levée quand une opération sur un contact est invalide."""
    pass


def reset() -> None:
    """Remet le carnet de contacts à zéro (pour les tests)."""
    global CONTACTS, _next_id
    CONTACTS.clear()
    _next_id = 1


def add_contact(name: str, email: str, phone: str = "") -> dict:
    """
    Ajoute un contact et retourne le contact créé (avec son id).
    Lève ContactError si le nom ou l'email est vide.
    """
    global _next_id
    if not name or not name.strip():
        raise ContactError("Le nom est requis.")
    if not email or not email.strip():
        raise ContactError("L'email est requis.")
    contact = {"id": _next_id, "name": name.strip(), "email": email.strip(), "phone": phone.strip()}
    CONTACTS.append(contact)
    _next_id += 1
    return contact


def remove_contact(contact_id: int) -> bool:
    """
    Supprime un contact par son id.
    Retourne True si supprimé, lève ContactError si introuvable.
    """
    for i, c in enumerate(CONTACTS):
        if c["id"] == contact_id:
            CONTACTS.pop(i)
            return True
    raise ContactError(f"Contact {contact_id} introuvable.")


def find_by_email(email: str) -> dict | None:
    """
    Recherche un contact par email (insensible à la casse).
    Retourne le contact ou None s'il n'existe pas.
    """
    for c in CONTACTS:
        if c["email"].lower() == email.lower():
            return c
    return None


def list_contacts() -> list[dict]:
    """Retourne la liste des contacts triés par nom (ordre alphabétique)."""
    return sorted(CONTACTS, key=lambda c: c["name"].lower())


def count() -> int:
    """Retourne le nombre de contacts."""
    return len(CONTACTS)
