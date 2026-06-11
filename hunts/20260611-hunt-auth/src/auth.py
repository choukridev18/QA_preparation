"""
Module d'authentification simple.
Gère la création d'utilisateurs, le login, et les tokens de session.
"""

import hashlib
import secrets

USERS: dict[str, str] = {}
TOKENS: dict[str, str] = {}


def hash_password(password: str) -> str:
    """Retourne le hash SHA-256 du mot de passe."""
    return hashlib.sha256(password.encode()).hexdigest()


def register(username: str, password: str) -> bool:
    """
    Enregistre un nouvel utilisateur.
    Retourne True si l'enregistrement réussit, False si l'utilisateur existe déjà.
    """
    if username in USERS:
        return False
    USERS[username] = hash_password(password)
    return True


def login(username: str, password: str) -> str | None:
    """
    Authentifie un utilisateur.
    Retourne un token de session (str) si les credentials sont corrects, None sinon.
    """
    if USERS.get(username) != hash_password(password):
        return None
    token = secrets.token_hex(16)
    TOKENS[token] = username
    return token


def logout(token: str) -> bool:
    """
    Invalide un token de session.
    Retourne True si le token existait, False sinon.
    """
    if token not in TOKENS:
        return False
    del TOKENS[token]
    return True


def is_authenticated(token: str) -> bool:
    """Retourne True si le token est valide (utilisateur connecté)."""
    return token in TOKENS


def get_username(token: str) -> str | None:
    """
    Retourne le nom d'utilisateur associé au token.
    Retourne None si le token est invalide.
    """
    return TOKENS.get(token)


def reset() -> None:
    """Remet l'état du module à zéro (pour les tests)."""
    USERS.clear()
    TOKENS.clear()
