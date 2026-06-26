# Lance : pytest test_exercise.py -v

import pytest
from exercise import (
    get_database_url,
    get_log_level,
    print_config,
    is_debug_mode,
    build_config,
    ConfigError,
)


# ── get_database_url ──────────────────────────────────────────────────────────

def test_get_database_url_returns_env_value(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgres://localhost/mydb")
    assert get_database_url() == "postgres://localhost/mydb"


def test_get_database_url_raises_if_missing(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with pytest.raises(ConfigError):
        get_database_url()


# ── get_log_level ─────────────────────────────────────────────────────────────

def test_get_log_level_returns_env_value(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL", "WARNING")
    assert get_log_level() == "WARNING"


def test_get_log_level_defaults_to_info(monkeypatch):
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    assert get_log_level() == "INFO"


# ── print_config ──────────────────────────────────────────────────────────────

def test_print_config_outputs_to_stdout(monkeypatch, capsys, with_database_url):
    monkeypatch.setenv("LOG_LEVEL", "WARNING")
    print_config()
    captured = capsys.readouterr()
    assert "[CONFIG] database=postgres://localhost/testdb" in captured.out
    assert "[CONFIG] log_level=WARNING" in captured.out


def test_print_config_default_log_level(monkeypatch, capsys, with_database_url):
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    print_config()
    captured = capsys.readouterr()
    assert "[CONFIG] log_level=INFO" in captured.out


# ── is_debug_mode ─────────────────────────────────────────────────────────────

def test_is_debug_mode_true_when_debug(with_debug_env):
    assert is_debug_mode() is True


def test_is_debug_mode_false_when_info(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL", "INFO")
    assert is_debug_mode() is False


def test_is_debug_mode_false_when_missing(monkeypatch):
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    assert is_debug_mode() is False


# ── build_config ──────────────────────────────────────────────────────────────

def test_build_config_returns_full_dict(with_debug_env):
    config = build_config()
    assert config["database_url"] == "postgres://localhost/testdb"
    assert config["log_level"] == "DEBUG"
    assert config["debug"] is True


def test_build_config_raises_without_database_url(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with pytest.raises(ConfigError):
        build_config()
