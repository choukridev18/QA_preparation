---
name: qa-bug-hunt
description: Génère une suite de tests intentionnellement cassée sur une app Flask construite par l'agent. L'utilisateur lance le serveur, puis trouve et corrige les bugs dans les tests sans toucher à l'app. ~40 min. Utilise quand l'utilisateur dit /qa-bug-hunt.
---

# QA Bug Hunt

La suite de tests était verte. Elle ne l'est plus. L'agent génère une mini app Flask fonctionnelle **et** une suite de tests avec des bugs intentionnels. L'utilisateur lance le serveur, diagnostique les échecs, et corrige les bugs — uniquement dans `tests/`.

**Pourquoi une app générée ?** L'agent contrôle 100% du HTML et du code Python — il peut planter des bugs précis et réalistes dans les tests, en sachant exactement ce que l'app fait. Aucune surprise liée à un site tiers.

**Stack** : Flask (app) + Python + pytest + pytest-playwright (si scénario E2E)
**Durée** : ~40 min
**Règle absolue** : ne modifier que les fichiers dans `tests/` — jamais `app/` ni `src/`

---

## Workflow

### Étape 0 — Proposer 3 scénarios

Avant de générer quoi que ce soit, propose exactement 3 scénarios distincts et attends le choix de l'utilisateur.

Règles :
- Chaque scénario cible un type de bug différent
- Varier la difficulté : 1 facile, 1 moyen, 1 difficile
- Ne pas reproduire un scénario récent (vérifier `hunts/`)
- Préciser le type de bugs dans la proposition

Format :
```
Voici 3 scénarios de bug hunt — choisis-en un :

**A — [nom] (Facile)**
[2 lignes : contexte + type de bugs]

**B — [nom] (Moyen)**
[2 lignes : contexte + type de bugs]

**C — [nom] (Difficile)**
[2 lignes : contexte + type de bugs]
```

### Étape 1 — Générer le projet

Deux structures possibles selon le scénario :

**Scénario pytest pur (pas de Playwright) :**
```
hunts/YYYYMMDD-hunt-[slug]/
├── BRIEF.md
├── BUGS.md
├── requirements.txt
├── src/
│   └── [module].py         # code Python correct — ne pas toucher
└── tests/
    ├── conftest.py          # peut contenir des bugs de fixture
    └── test_[feature].py    # contient les bugs intentionnels
```

**Scénario Playwright (tests E2E sur une app Flask) :**
```
hunts/YYYYMMDD-hunt-[slug]/
├── BRIEF.md
├── BUGS.md
├── requirements.txt
├── app/
│   ├── server.py            # app Flask correcte — ne pas toucher
│   └── templates/
│       └── *.html           # HTML correct — ne pas toucher
├── conftest.py              # peut contenir des bugs de fixture
├── pages/
│   └── [page].py            # Page Objects corrects — ne pas toucher
└── tests/
    └── test_[feature].py    # contient les bugs intentionnels
```

---

### Règles de conception de l'app Flask (scénarios Playwright)

Identiques au skill `qa-playwright-session` :
- App simple, sans base de données, données en mémoire
- HTML avec attributs sémantiques (`aria-label`, `id`, `role`, `<label for=>`)
- URLs stables et prévisibles
- Endpoint `POST /reset` pour que les fixtures puissent remettre l'état à zéro
- **Noms de variables et fonctions en anglais**, textes affichés en français

**`requirements.txt`** :
```
# scénario pytest pur :
pytest
pytest-mock

# scénario Playwright — ajouter :
flask
playwright
pytest-playwright
```

**`conftest.py`** pour scénarios Playwright :
```python
import pytest
from playwright.sync_api import Page

BASE_URL = "http://localhost:5001"

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1280, "height": 720}}

@pytest.fixture(autouse=True)
def reset_server(page: Page):
    page.request.post(f"{BASE_URL}/reset")
    yield
```

---

### Types de bugs à planter (varier selon le scénario)

**Bugs d'assertion :**
- Float sans `pytest.approx` (`assert result == 0.3`)
- Liste non triée (`assert result == [3, 1, 2]` quand l'ordre est aléatoire)
- Casse incorrecte (`assert text == "bonjour"` au lieu de `"Bonjour"`)
- `.to_have_text("Exact")` au lieu de `.to_contain_text("Partiel")` en Playwright

**Bugs de mock :**
- Chemin de patch incorrect (`mock.patch("module.fn")` au lieu de `mock.patch("src.module.fn")`)
- `return_value` vs `side_effect` inversés
- Mock configuré après l'appel à la fonction testée
- `pytest.raises(ValueError)` quand c'est un `TypeError` qui est levé

**Bugs de fixture :**
- Fixture avec `scope="session"` qui modifie un état mutable
- Fixture qui ne retourne pas l'objet (return manquant → `None`)
- Fixture `autouse=True` qui s'applique aux mauvais tests
- `yield` sans teardown quand le teardown est nécessaire

**Bugs Playwright :**
- Locator trop générique (`page.locator("button")` au lieu de `get_by_role("button", name="...")`)
- `expect(...).to_have_url(...)` vérifié avant que la navigation soit terminée
- `page.fill("#id")` avec le mauvais ID (ID qui n'existe pas dans le HTML généré)
- Assertion sur un élément caché (`display:none`) qui retourne toujours vide

### Règles de conception des bugs

- **1 bug par test au maximum**
- **Les bugs ressemblent à de vraies erreurs de dev** — pas de fautes de frappe évidentes
- **`src/` et `app/` sont 100% corrects** — si les tests étaient bien écrits, tout passerait
- **2-3 tests passent dès le départ** — pour donner un point de repère
- **Les tracebacks sont informatifs** — l'erreur doit pointer vers la cause sans la révéler entièrement
- **Noms de variables et fonctions en anglais** dans tout le code généré

### Format `BRIEF.md`

```markdown
# Bug Hunt — [nom du scénario]

## Contexte

[2-3 phrases : quelle app/module, ce qu'il fait, quand les tests ont commencé à échouer]
**Le code dans `app/` (ou `src/`) est correct et ne doit pas être modifié.**

## Lancer le serveur (scénarios Playwright uniquement)

```bash
cd app && python server.py
# App disponible sur http://localhost:5001
```

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec a 1 bug dans les fichiers de test
3. Corrige les bugs **uniquement dans `tests/`**
4. Lance `pytest tests/ -v` après chaque correction
5. Quand tout est vert, dis "j'ai fini"

## Règles

- Ne touche pas à `app/` ni `src/` — seulement `tests/` et `conftest.py`
- Chaque test qui échoue a exactement 1 bug
- Les tests qui passent sont corrects

## Indices (seulement si bloqué depuis plus de 10 min)

<details>
<summary>Fichiers concernés</summary>
[Liste des fichiers contenant des bugs — sans préciser lesquels]
</details>

<details>
<summary>Catégories de bugs</summary>
[Ex: "deux bugs d'assertion, un bug de mock, un bug de fixture" — sans les localiser]
</details>
```

### Format `BUGS.md`

```markdown
# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini</summary>

## Bug 1 — [fichier], ligne [N]
**Symptôme :** [ce que pytest affiche]
**Cause :** [explication]
**Correction :** [la ligne correcte]

[répéter pour chaque bug]
</details>
```

### Étape 2 — Setup et vérification

Après avoir généré les fichiers :

```bash
cd hunts/YYYYMMDD-hunt-[slug]
uv venv .venv
uv pip install -r requirements.txt
.venv/bin/playwright install chromium  # scénarios Playwright uniquement
```

Vérifier que les tests échouent sur les bons bugs (pas sur des erreurs d'import ou de setup) :
```bash
.venv/bin/pytest tests/ -v
```

Corriger tout problème de setup avant de présenter le brief.

### Étape 3 — Lancement

```
🐛  BUG HUNT — ~40 minutes.

📋  Brief dans BRIEF.md
▶️  Lance le serveur (si Playwright) :
    cd hunts/YYYYMMDD-hunt-[slug]/app && python server.py

▶️  Lance les tests :
    cd hunts/YYYYMMDD-hunt-[slug]
    .venv/bin/pytest tests/ -v

🎯  Objectif : tous les tests passent en modifiant uniquement tests/
⚠️  Ne regarde pas BUGS.md avant d'avoir fini.

Dis-moi quand tu as terminé ou si tu es bloqué depuis plus de 10 min.
```

### Étape 4 — Débrief (quand l'utilisateur dit qu'il a fini)

1. Demander de coller la sortie finale de `pytest tests/ -v`
2. Dire à l'utilisateur d'ouvrir `BUGS.md`
3. Évaluer :
   - Bugs trouvés vs bugs manqués
   - Efficacité du diagnostic : traceback → cause → correction directe ou tâtonnement ?
   - Patterns reconnus rapidement vs lentement

**Format du débrief (dans le chat) :**
```
## Débrief — [nom du scénario]

**Résultat :** [X] bugs trouvés sur [Y]

**Ce que tu maîtrises :**
- [pattern reconnu rapidement]

**Ce qui t'a coûté du temps :**
- [bug difficile + pourquoi]

**Règle à retenir :**
[Une heuristique concrète pour reconnaître ce type de bug plus vite]
```

---

## Banque de scénarios

**pytest pur — Calcul financier**
Module de calcul de remboursements. Bugs : float sans `pytest.approx`, mock mal ciblé, fixture qui retourne `None`.

**pytest pur — Client API mocké**
Wrapper HTTP. Bugs : chemin de patch incorrect, `return_value` vs `side_effect` inversés, `pytest.raises` avec le mauvais type d'exception.

**pytest pur — Gestionnaire d'authentification**
Module login/logout/token. Bugs : fixture `scope="session"` qui pollue les tests, exception avalée dans un `try/except`, mock de `datetime.now` mal scopé.

**Playwright — Interface de gestion de tâches**
App Flask de todos. Bugs : locator trop générique, `.to_have_text()` sur texte partiel, assertion avant navigation terminée, mauvais ID dans `page.fill()`.

**Playwright — Formulaire de login**
App Flask avec login. Bugs : assertion sur message d'erreur caché, `get_by_role` avec mauvais nom, fixture `reset_server` manquante sur un test, URL vérifiée trop tôt.


# QA Bug Hunt

La suite de tests était verte. Elle ne l'est plus. L'utilisateur récupère un projet avec des bugs intentionnels dans les fichiers de test — pas dans le code de production. Il doit diagnostiquer les échecs, identifier les causes, et tout corriger.

**Stack** : Python + pytest (et/ou pytest-playwright selon le scénario)
**Durée** : ~40 min
**Règle** : ne pas modifier les fichiers dans `src/` — seulement les fichiers dans `tests/`

---

## Workflow

### Étape 0 — Proposer 3 scénarios

Avant de générer quoi que ce soit, propose exactement 3 scénarios de bug hunt distincts et attends le choix de l'utilisateur.

Règles pour les 3 propositions :
- Chaque scénario cible un type de bug différent (assertions, mocks, fixtures, locators Playwright, conditions de course…)
- Varier la difficulté : 1 scénario facile, 1 moyen, 1 difficile
- Ne pas reproduire un scénario récent (vérifier le dossier `hunts/` si nécessaire)
- Nommer clairement le type de problème dans la proposition pour que l'utilisateur sache dans quoi il s'engage

Format :
```
Voici 3 scénarios de bug hunt — choisis-en un :

**A — [nom] (Facile)**
[2 lignes : contexte + type de bugs cachés]

**B — [nom] (Moyen)**
[2 lignes : contexte + type de bugs cachés]

**C — [nom] (Difficile)**
[2 lignes : contexte + type de bugs cachés]
```

Attends le choix de l'utilisateur avant de générer quoi que ce soit.

### Étape 1 — Générer le projet

Créer `hunts/YYYYMMDD-hunt-[slug]/` avec la structure suivante :

```
hunts/YYYYMMDD-hunt-[slug]/
├── BRIEF.md
├── BUGS.md            # liste complète des bugs — spoiler caché sous <details>
├── requirements.txt
├── src/
│   └── [module].py    # code de production — CORRECT, ne pas toucher
└── tests/
    ├── conftest.py    # peut contenir des bugs de fixture
    └── test_[feature].py  # contient les bugs intentionnels
```

**`requirements.txt`** :
```
pytest
pytest-mock
```
Ajouter `playwright` et `pytest-playwright` si le scénario inclut du Playwright.

**`src/[module].py`** — code de production, correct et fonctionnel :
- Logique métier réaliste (calculs, transformations de données, appels API simulés…)
- Le code est volontairement bien écrit — les bugs sont tous dans les tests
- Inclure des docstrings claires pour que l'utilisateur comprenne ce que le code est censé faire

**`tests/conftest.py`** — peut contenir des bugs (ou être correct selon le scénario) :
- Si le scénario cible les fixtures : contenir 1-2 bugs de fixture (mauvais scope, mauvais return, setup incomplet)
- Sinon : fixtures correctes qui servent de base aux tests

**`tests/test_[feature].py`** — contient les bugs intentionnels :
- 6-10 tests au total
- 4-6 tests échouent à cause des bugs intentionnels
- 2-3 tests passent (pour que l'utilisateur ne pense pas que tout est cassé)
- Les bugs sont discrets — pas de faute de frappe évidente, des erreurs de logique réalistes

### Types de bugs à utiliser (varier selon le scénario)

**Bugs d'assertion :**
- Comparaison avec `==` sur un float sans tolérance (`assert result == 0.3` au lieu de `pytest.approx`)
- `assert liste == [...]` avec mauvais ordre (ne pas utiliser `sorted`)
- `assert str == "..."` avec casse incorrecte
- Utiliser `.to_have_text()` au lieu de `.to_contain_text()` en Playwright

**Bugs de mock :**
- Patcher le mauvais chemin (`mock.patch("module.Classe")` au lieu de `mock.patch("tests.test_module.Classe")`)
- `return_value` vs `side_effect` inversés
- Mock non réinitialisé entre tests (sans `autospec` ou `reset_mock`)
- Patcher une méthode d'instance au lieu de la méthode de classe

**Bugs de fixture :**
- Fixture avec `scope="session"` qui modifie un état mutable (les tests s'affectent entre eux)
- Fixture qui crée un objet mais ne le retourne pas (retourne `None`)
- Fixture non demandée par les tests qui la nécessitent (fixture présente dans conftest mais non injectée)
- `yield` dans une fixture sans nettoyage après (teardown manquant)

**Bugs de logique de test :**
- Test qui vérifie le mauvais cas (`test_commande_vide` qui teste une commande avec articles)
- `pytest.raises(ValueError)` avec le mauvais type d'exception (`TypeError` levée à la place)
- Test qui passe toujours parce que l'assertion est dans un bloc `try/except` qui avale l'erreur
- Ordre d'arguments inversé dans `assert attendu == obtenu` (confus mais pas faux — à détecter au message d'erreur)

**Bugs Playwright :**
- `page.locator("button")` trop générique (sélectionne le mauvais bouton)
- `page.fill("#id")` sur un champ qui n'existe pas encore (pas d'attente avant)
- `expect(page.locator("...")).to_have_text("Exact")` au lieu de `.to_contain_text("Partiel")`
- `page.click("...")` sur un élément hors viewport (manque `.scroll_into_view_if_needed()`)
- Attente manquante après une navigation (`page.click` puis assertion immédiate sans `wait_for_url` ou `wait_for_load_state`)

### Règles de conception des bugs

- **Jamais plus de 1 bug par test** — sinon c'est décourageant
- **Les bugs doivent ressembler à des vraies erreurs** — pas de typos volontaires évidentes
- **Le code de production (`src/`) doit être 100% correct** — si les tests étaient bien écrits, ils passeraient tous
- **Toujours 2-3 tests qui passent dès le début** — pour ancrer la confiance et donner un point de comparaison
- **Les messages d'erreur de pytest doivent être informatifs** — le bug doit se diagnostiquer à partir du traceback, pas nécessiter de lire le code de prod en entier

### Format `BRIEF.md`

```markdown
# Bug Hunt — [nom du scénario]

## Contexte

Cette suite de tests couvrait le module `[nom]` qui gère [description fonctionnelle].
Suite à un refactor de [date fictive], plusieurs tests ont commencé à échouer.
**Le code de production (`src/`) n'a pas changé et est correct.**

## Ta mission

1. Lance `pytest tests/ -v` pour voir quels tests échouent
2. Lis les tracebacks — chaque échec est un bug dans les fichiers de test
3. Corrige les bugs **uniquement dans `tests/`** — ne touche pas à `src/`
4. Quand tous les tests passent, dis "j'ai fini"

## Règles

- Tu ne modifies PAS les fichiers dans `src/`
- Chaque test qui échoue a exactement 1 bug à corriger
- Les tests qui passent déjà sont corrects — ne les touche pas
- Lance `pytest tests/ -v` après chaque correction pour vérifier

## Indices (seulement si bloqué depuis plus de 10 min sur un bug)

<details>
<summary>Quels fichiers regarder en premier</summary>
[Donner la liste des fichiers qui contiennent des bugs sans révéler le bug lui-même]
</details>

<details>
<summary>Type de bugs présents</summary>
[Donner les catégories de bugs (ex: "un bug de mock, deux bugs d'assertion, un bug de fixture") sans les localiser précisément]
</details>
```

### Format `BUGS.md` (révélé seulement après la session)

```markdown
# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — [fichier], ligne [N]

**Symptôme :** [ce que pytest affiche]
**Cause :** [explication du bug]
**Correction :** [la ligne correcte]

## Bug 2 — [fichier], ligne [N]

**Symptôme :** ...
**Cause :** ...
**Correction :** ...

[répéter pour chaque bug]
</details>
```

### Étape 2 — Lancement

Après avoir généré les fichiers, afficher :

```
🐛  BUG HUNT — ~40 minutes.

📋  Brief dans BRIEF.md
▶️  Lance : pytest tests/ -v
🎯  Objectif : tous les tests passent en ne modifiant que les fichiers dans tests/

⚠️  Ne regarde pas BUGS.md avant d'avoir fini.

Dis-moi quand tu as terminé ou si tu es bloqué sur un bug depuis plus de 10 min.
```

### Étape 3 — Débrief (quand l'utilisateur dit qu'il a fini)

1. Demander à l'utilisateur de coller la sortie finale de `pytest tests/ -v`
2. Révéler le contenu de `BUGS.md` (ou dire à l'utilisateur de l'ouvrir)
3. Comparer : bugs trouvés vs bugs manqués, temps passé par bug
4. Évaluer :
   - **Efficacité du diagnostic** : lecture du traceback → identification de la cause → correction directe, ou tâtonnement ?
   - **Patterns reconnus** : est-ce que l'utilisateur a identifié la catégorie du bug rapidement ?
   - **Corrections propres** : correction minimale ou réécriture inutile du test ?

**Format du débrief (à écrire dans le chat, pas de fichier) :**

```
## Débrief — [nom du scénario]

**Résultat :** [X] bugs trouvés sur [Y]

**Ce que tu maîtrises :**
- [pattern reconnu rapidement]

**Ce qui t'a coûté du temps :**
- [bug difficile + pourquoi]

**Règle à retenir :**
[Une heuristique concrète pour reconnaître ce type de bug plus vite la prochaine fois]
```

---

## Banque de scénarios (inspiration — générer des variantes originales)

**Suite de calcul financier**
Module : calcul de remboursements, commissions, TVA. Bugs : assertions float sans `pytest.approx`, mock du taux de change mal ciblé, fixture de devise qui retourne `None`.

**Pipeline de traitement de données**
Module : lecture CSV, transformation, agrégation. Bugs : assertion sur liste non triée, fixture `tmp_path` mal utilisée, `side_effect` vs `return_value` inversés.

**Client API REST mocké**
Module : wrapper HTTP autour d'une API externe. Bugs : chemin de patch incorrect (`requests.get` vs `module.requests.get`), `status_code` vérifié après le mock mais jamais configuré, `pytest.raises` avec le mauvais type d'exception.

**Gestionnaire d'authentification**
Module : login, logout, token refresh. Bugs : fixture de session avec `scope="session"` qui pollue les tests suivants, assertion sur token expiré qui passe toujours (exception avalée), mock de `datetime.now` mal scopé.

**Suite Playwright — interface de recherche**
App : moteur de recherche interne. Bugs : locator trop générique (`page.locator("input")`), assertion `.to_have_text()` sur texte partiel, clic sur bouton "Rechercher" sans attendre les résultats, filtre testé dans le mauvais ordre.

**Gestionnaire de fichiers et rapports**
Module : génération de rapports PDF/CSV, écriture sur disque. Bugs : fixture `tmp_path` demandée mais pas injectée dans un test, comparaison de chemin avec string au lieu de `Path`, teardown manquant qui laisse un fichier temporaire.
