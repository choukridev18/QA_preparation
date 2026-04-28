---
name: qa-python-drill
description: Génère un exercice Python/pytest ciblé sur des notions que l'utilisateur veut renforcer. Session de 45-60 minutes. Utilise quand l'utilisateur dit /qa-python-drill, veut s'entraîner sur pytest, les fixtures, les mocks, ou tout autre notion Python liée au testing.
---

# QA Python Drill

Session Python/pytest pour renforcer des notions essentielles au QA Automation. Toujours dans un contexte SaaS réaliste (app de gestion, e-commerce, réservation…).

**Durée : 45-60 minutes.** C'est la seule session pytest de la semaine — elle doit être dense. Générer un exercice avec **5 à 7 fonctions** à implémenter et **8 à 12 tests** qui les couvrent, en combinant plusieurs notions pytest imbriquées.

## Workflow

### Étape 0 — Proposer 3 thèmes

Avant de générer quoi que ce soit, propose exactement 3 thèmes différents et attends que l'utilisateur en choisisse un.

Règles pour les 3 propositions :
- Chaque thème combine **5-6 notions** qui s'articulent naturellement et permettent de tenir 45-60 min
- Varie les thèmes — ne répète pas les mêmes notions
- Ne reproduis pas un thème déjà traité dans un drill récent (vérifie le dossier `drills/` si nécessaire)
- Au moins un thème doit couvrir quelque chose souvent mal maîtrisé par les débutants en testing

Format :
```
Voici 3 thèmes de drill — choisis-en un (ou donne-moi tes propres notions) :

**A — [nom du thème]**
Notions : [liste]
[1 phrase décrivant l'angle de l'exercice]

**B — [nom du thème]**
Notions : [liste]
[1 phrase décrivant l'angle de l'exercice]

**C — [nom du thème]**
Notions : [liste]
[1 phrase décrivant l'angle de l'exercice]
```

Attends le choix de l'utilisateur avant de générer quoi que ce soit.

### Étape 1 — Générer les fichiers

Crée le dossier `drills/YYYYMMDD-[slug-notion]/` avec :

```
drills/YYYYMMDD-[slug-notion]/
├── exercise.py        # fonctions à implémenter
├── test_exercise.py   # tests pytest qui doivent passer quand l'exercice est complet
└── conftest.py        # fixtures si le thème en a besoin (sinon laisser vide)
```

**Principes de conception :**

- Contexte SaaS réaliste (ex : système de gestion de commandes, app de réservation, tableau de bord analytics)
- Toutes les notions du thème apparaissent dans UN SEUL exercice — pas une notion par fonction
- Les notions simples apparaissent en premier, les plus complexes s'appuient dessus
- Instructions sous forme de `# TODO:` directement dans le code — pas de fichier brief séparé
- 15-25 minutes max — c'est un drill, pas une session complète
- Les tests sont déjà écrits et **échouent** jusqu'à ce que l'exercice soit terminé

**Structure de `exercise.py` :**

```python
# ============================================================
# DRILL — [notion 1] · [notion 2] · [notion 3]
# ============================================================
# Contexte :
#   [2-3 phrases de contexte métier réaliste]
#
# Objectif :
#   Implémenter les fonctions ci-dessous pour que tous les tests passent.
#   Lance : pytest test_exercise.py -v
# ============================================================

from dataclasses import dataclass
from typing import ...

# [définitions de types / dataclasses utilisées dans l'exercice]


# ------------------------------------------------------------
# TODO 1 — [nom de la notion]
# ------------------------------------------------------------
# Entrée  : [exemple concret]
# Sortie  : [exemple concret du résultat attendu]
#
# Indice : [suggère le bon outil ou concept, jamais la solution]
# ------------------------------------------------------------
def nom_fonction(...) -> ...:
    raise NotImplementedError


# [répéter pour chaque TODO]
```

**Règles pour les blocs TODO :**
- Toujours montrer un exemple Entrée/Sortie concret — pas de description abstraite
- L'indice suggère le bon outil (`pytest.mark.parametrize`, `unittest.mock.patch`, etc.) sans donner l'implémentation
- Ne jamais donner d'instructions étape par étape — c'est donner la réponse
- Chaque fonction commence par `raise NotImplementedError` — pas de logique partielle
- **Noms de variables, fonctions et classes en anglais** — seuls les commentaires, messages d'assertion et instructions `# TODO` sont en français

**Structure de `test_exercise.py` :**

```python
# Lance : pytest test_exercise.py -v

import pytest
from exercise import nom_fonction_1, nom_fonction_2


def test_nom_cas_1():
    # [test avec assert clair et message d'erreur utile]
    assert nom_fonction_1(...) == ..., "Message d'erreur explicite"


@pytest.mark.parametrize("entree,attendu", [
    (..., ...),
    (..., ...),
    (..., ...),
])
def test_nom_cas_parametrise(entree, attendu):
    assert nom_fonction_2(entree) == attendu


# [autres tests selon les notions du thème]
```

**Règles pour les tests :**
- Utiliser `pytest` natif uniquement — pas de custom runner, pas de `unittest.TestCase`
- Chaque test a un nom explicite qui décrit le cas (`test_commande_vide_retourne_zero`)
- Si le thème inclut les fixtures : les définir dans `conftest.py` et les injecter dans les tests
- Si le thème inclut les mocks : utiliser `unittest.mock.patch` ou `pytest-mock` (`mocker`)
- Messages d'assertion en français

**Structure de `conftest.py` :**

Si le thème inclut les fixtures :
```python
import pytest
from exercise import ...


@pytest.fixture
def nom_fixture():
    # [setup réaliste — ex: une commande avec des articles, un utilisateur connecté]
    return ...
```

Si le thème n'inclut pas les fixtures : laisser le fichier vide avec juste un commentaire `# conftest vide`.

### Pool de notions disponibles

Notions pytest :
- `pytest.fixture` (scope function, module, session)
- `pytest.mark.parametrize`
- `pytest.raises` (vérifier qu'une exception est levée)
- `conftest.py` (fixtures partagées entre fichiers)
- `tmp_path` (fixture built-in pour fichiers temporaires)
- `capsys` (capture stdout/stderr)
- `monkeypatch` (patcher des variables d'env, des fonctions)

Notions Python pour le testing :
- `unittest.mock.patch` / `pytest-mock` (`mocker.patch`)
- `MagicMock`, `Mock`, `side_effect`, `return_value`
- `dataclass` et `@dataclass`
- List/dict comprehensions dans un contexte de données de test
- `pathlib.Path` pour lire des fichiers de fixtures
- `json.load` / `csv.reader` pour données de test
- Type hints (`list[str]`, `dict[str, int]`, `Optional`)
- Exceptions personnalisées et `pytest.raises`
- `requests` + mock HTTP (`responses`, `pytest-httpx`)

### Étape 2 — Lancer

Après avoir généré les fichiers, afficher :

```
⏱️  DRILL PYTEST — 45-60 minutes.

🎯  Notions : [liste]
▶️  Lance : pytest drills/YYYYMMDD-[slug]/test_exercise.py -v
✅  Objectif : tous les tests passent

Dis-moi quand tu as fini ou si tu es bloqué.
```

### Étape 3 — Review (quand l'utilisateur a fini)

Quand l'utilisateur dit qu'il a fini ou que tous les tests passent :

Donner un feedback court (5-10 lignes max) :
- Quelles notions sont maintenant solides
- Laquelle mérite encore de l'attention
- 1 chose concrète à retenir pour les prochaines sessions Playwright

Pas de débrief complet — c'est un drill, pas une session complète.
