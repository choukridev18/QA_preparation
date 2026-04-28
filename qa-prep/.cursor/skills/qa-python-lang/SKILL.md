---
name: qa-python-lang
description: Génère un exercice de Python pur pour renforcer les fondamentaux du langage — sans pytest, sans framework de test. Fonctions à implémenter, validées par des assertions simples. 45-60 minutes. Utilise quand l'utilisateur dit /qa-python-lang, veut travailler son Python pur, les compréhensions, les dataclasses, le tri, les classes, etc.
---

# QA Python Lang

Session de **Python pur** — aucun lien avec pytest ou le testing. L'objectif est de renforcer les réflexes du langage lui-même : manipuler des données, structurer du code, utiliser les bons outils Python. Toujours dans un contexte SaaS réaliste pour garder le lien avec le métier.

**Pas de pytest.** Les vérifications sont faites avec des `assert` simples lancés directement avec `python exercise.py`.

**Durée : 45-60 minutes.** C'est la seule session Python pur de la semaine — elle doit être dense. Générer un exercice avec **5 à 7 fonctions** à implémenter, couvrant plusieurs notions imbriquées.

---

## Workflow

### Étape 0 — Proposer 3 thèmes

Avant de générer quoi que ce soit, propose exactement 3 thèmes différents et attends le choix de l'utilisateur.

Règles pour les 3 propositions :
- Chaque thème combine **5-6 notions** Python qui s'articulent naturellement et permettent de tenir 45-60 min
- Varie les thèmes — ne répète pas les mêmes notions
- Ne reproduis pas un thème déjà traité dans un drill récent (vérifie le dossier `drills/` si nécessaire)
- Au moins un thème doit couvrir quelque chose souvent mal maîtrisé par les débutants Python

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

Créer le dossier `drills/YYYYMMDD-lang-[slug-notion]/` avec :

```
drills/YYYYMMDD-lang-[slug-notion]/
├── exercise.py    # fonctions à implémenter uniquement — pas de vérifications ici
└── verify.py      # assertions de vérification — à lancer avec python verify.py
```

Pas de `conftest.py`, pas de `test_exercise.py`, pas de `solution.py`.

**Structure de `exercise.py` :**

```python
# ============================================================
# DRILL PYTHON — [notion 1] · [notion 2] · [notion 3]
# ============================================================
# Contexte :
#   [2-3 phrases de contexte métier réaliste]
#
# Objectif :
#   Implémenter les fonctions ci-dessous.
#   Lance : python drills/YYYYMMDD-lang-[slug]/verify.py
#   Si aucune AssertionError → tout est bon.
# ============================================================

from dataclasses import dataclass
from typing import ...

# [définitions de types / dataclasses utilisées dans l'exercice]


# ------------------------------------------------------------
# TODO 1 — [nom de la notion]
# ------------------------------------------------------------
# Entrée  : [exemple concret d'input]
# Sortie  : [exemple concret d'output attendu]
#
# Indice : [suggère le bon outil Python, jamais la solution]
# ------------------------------------------------------------
def nom_fonction(...) -> ...:
    raise NotImplementedError


# [répéter pour chaque TODO]
```

**Structure de `verify.py` :**

```python
# Lance : python drills/YYYYMMDD-lang-[slug]/verify.py

from exercise import nom_fonction_1, nom_fonction_2, ...


# --- [description du groupe de vérifications] ---

assert nom_fonction_1(...) == ..., "[message d'erreur explicite en français]"
assert nom_fonction_1(...) == ..., "[cas limite — message explicite]"

assert nom_fonction_2(...) == ..., "[message d'erreur explicite en français]"
assert nom_fonction_2(...) == ..., "[cas limite — message explicite]"

# [répéter pour chaque fonction]

print("✅ Tous les tests passent.")
```

### Pool de notions disponibles

**Règle absolue** : noms de variables, fonctions et classes **toujours en anglais**. Seuls les commentaires `# TODO`, messages d'assertion, et contexte métier sont en français.

Manipulation de données :
- List comprehensions (`[x for x in ... if ...]`)
- Dict comprehensions (`{k: v for k, v in ...}`)
- Set comprehensions
- `sorted()` avec `key=` et `reverse=`
- `filter()`, `map()`
- `zip()`, `enumerate()`
- `any()`, `all()`
- `min()`, `max()` avec `key=`

Structures de données :
- `@dataclass` (champs, valeurs par défaut, `field()`)
- `dict` (`.get()`, `.items()`, `.setdefault()`, `defaultdict`)
- `list` (slicing, `append`, `extend`, `pop`)
- `set` (union, intersection, différence)
- Tuples nommés (`namedtuple`, ou `@dataclass` frozen)

Classes et OOP :
- `__init__`, `__str__`, `__repr__`
- `@property` et setter
- Héritage simple
- Méthodes de classe (`@classmethod`) et statiques (`@staticmethod`)

Chaînes et formatage :
- f-strings et formatage de nombres
- `str.split()`, `str.join()`, `str.strip()`, `str.replace()`
- `str.startswith()`, `str.endswith()`

Gestion des erreurs :
- `try / except / finally`
- Exceptions personnalisées (`class MonErreur(Exception)`)
- `raise` avec message

Fichiers et données :
- `open()` / `with open()`
- `json.load()` / `json.dumps()`
- `pathlib.Path`

Fonctions avancées :
- Arguments par défaut, `*args`, `**kwargs`
- Fonctions imbriquées, closures
- Générateurs (`yield`)
- Décorateurs simples

### Étape 2 — Lancer

Après avoir généré les fichiers, afficher :

```
⏱️  DRILL PYTHON — 45-60 minutes.

🎯  Notions : [liste]
▶️  Lance : python drills/YYYYMMDD-lang-[slug]/verify.py
✅  Objectif : "✅ Tous les tests passent." s'affiche sans erreur

Dis-moi quand tu as fini.
```

### Étape 3 — Review (quand l'utilisateur a fini)

Quand l'utilisateur dit qu'il a fini :

Donner un feedback court (5-10 lignes max) :
- Quelles notions sont maintenant solides
- Laquelle mérite encore de l'attention
- 1 chose concrète à retenir

Pas de débrief complet — c'est un drill langage, pas une session complète.
