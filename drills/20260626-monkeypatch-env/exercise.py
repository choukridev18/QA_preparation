# ============================================================
# DRILL — monkeypatch · variables d'environnement · capsys · fixtures yield
# ============================================================
# Contexte :
#   Tu travailles sur un module de configuration d'une app SaaS.
#   Ce module lit des variables d'environnement pour configurer
#   la connexion à la base de données et le niveau de log.
#   Il expose aussi une fonction qui affiche la config en stdout.
#
# Objectif :
#   Implémenter les fonctions ci-dessous pour que tous les tests passent.
#   Lance : pytest test_exercise.py -v
# ============================================================

import os


class ConfigError(ValueError):
    """Levée quand une variable d'environnement obligatoire est manquante."""

    pass


# ------------------------------------------------------------
# TODO 1 — Lire la variable d'environnement DATABASE_URL
# ------------------------------------------------------------
# Entrée  : os.environ contient DATABASE_URL="postgres://localhost/db"
# Sortie  : "postgres://localhost/db"
# Lève ConfigError si DATABASE_URL n'est pas définie.
# ------------------------------------------------------------
def get_database_url() -> str:
    url = os.environ.get("DATABASE_URL")
    if url is None:
        raise ConfigError("DATABASE_URL n'est pas definie")
    return url


# ------------------------------------------------------------
# TODO 2 — Lire le niveau de log
# ------------------------------------------------------------
# Entrée  : os.environ contient LOG_LEVEL="DEBUG"
# Sortie  : "DEBUG"
# Entrée  : LOG_LEVEL absent
# Sortie  : "INFO"  (valeur par défaut)
# ------------------------------------------------------------
def get_log_level() -> str:
    return os.environ.get("LOG_LEVEL", "INFO")


# ------------------------------------------------------------
# TODO 3 — Afficher la configuration en stdout
# ------------------------------------------------------------
# Entrée  : DATABASE_URL="postgres://localhost/db", LOG_LEVEL="WARNING"
# Affiche exactement :
#   [CONFIG] database=postgres://localhost/db
#   [CONFIG] log_level=WARNING
# Ne retourne rien (None).
# ------------------------------------------------------------
def print_config() -> None:
    print(f"[CONFIG] database={get_database_url()}")
    print(f"[CONFIG] log_level={get_log_level()}")


# ------------------------------------------------------------
# TODO 4 — Vérifier si le mode debug est actif
# ------------------------------------------------------------
# Entrée  : LOG_LEVEL="DEBUG"
# Sortie  : True
# Entrée  : LOG_LEVEL="INFO" ou absente
# Sortie  : False
# ------------------------------------------------------------
def is_debug_mode() -> bool:
    return os.environ.get("LOG_LEVEL", "INFO") == "DEBUG"


# ------------------------------------------------------------
# TODO 5 — Construire le dictionnaire de configuration complet
# ------------------------------------------------------------
# Sortie  : {"database_url": "...", "log_level": "...", "debug": True/False}
# Lève ConfigError si DATABASE_URL est absente.
# ------------------------------------------------------------
def build_config() -> dict:
    return {
        "database_url": get_database_url(),
        "log_level": get_log_level(),
        "debug": is_debug_mode(),
    }
