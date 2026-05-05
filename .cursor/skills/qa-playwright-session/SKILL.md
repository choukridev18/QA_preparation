---
name: qa-playwright-session
description: Génère une session complète de tests E2E avec Playwright Python. L'agent construit lui-même une mini web app (Flask + HTML) et les POM stubs à compléter. L'utilisateur lance le serveur localement puis implémente les Page Objects et écrit ses propres tests. ~1h. Utilise quand l'utilisateur dit /qa-playwright-session.
---

# QA Playwright Session

Session complète de tests E2E sur une application web **construite par l'agent**. L'agent génère une mini app Flask fonctionnelle, les Page Object stubs à implémenter, et les tests fournis qui échouent. L'utilisateur lance le serveur, implémente les POMs, et écrit des tests supplémentaires.

**Pourquoi une app générée et non un site externe ?** L'agent contrôle 100% du HTML — les éléments, les IDs, les rôles ARIA, les URLs. Les locators des stubs POM correspondent exactement à ce qui est dans le DOM. Aucune surprise liée à un site tiers.

**Stack** : Flask (app) + Python + Playwright + pytest-playwright
**Durée** : ~1h
**Tests** : stubs de Page Objects fournis + tests fournis qui échouent + tests à écrire

---

## Workflow

### Étape 0 — Proposer 3 scénarios

Avant de générer quoi que ce soit, propose exactement 3 scénarios distincts et attends le choix de l'utilisateur.

Règles pour les 3 propositions :
- Chaque scénario cible un type de parcours utilisateur différent (authentification, formulaire multi-étapes, tableau de données, panier, recherche/filtres…)
- Chaque scénario doit faire travailler des aspects différents de Playwright (locators sémantiques, navigation, assertions d'état, dialog, messages d'erreur…)
- Ne pas reproduire un scénario récent (vérifier le dossier `sessions/` si nécessaire)

Format :
```
Voici 3 scénarios — choisis-en un :

**A — [nom du scénario]**
[2-3 lignes : contexte de l'app + quel parcours utilisateur tester]

**B — [nom du scénario]**
[2-3 lignes]

**C — [nom du scénario]**
[2-3 lignes]
```

Attends le choix de l'utilisateur avant de générer quoi que ce soit.

### Étape 1 — Générer la structure du projet

Créer `sessions/YYYYMMDD-playwright-[slug]/` avec la structure suivante :

```
sessions/YYYYMMDD-playwright-[slug]/
├── BRIEF.md
├── requirements.txt
├── app/
│   ├── server.py           # serveur Flask — à lancer par l'utilisateur
│   └── templates/
│       └── *.html          # pages HTML de l'app
├── conftest.py
├── pages/
│   └── [page_name].py      # Page Object stubs à implémenter
└── tests/
    └── test_[feature].py   # tests fournis qui échouent
```

**`requirements.txt`** :
```
flask
playwright
pytest
pytest-playwright
```

---

### Règles de conception de l'app Flask

L'app doit être **simple, réaliste et entièrement sous contrôle** :

- Pas de base de données — utiliser des variables Python en mémoire ou des données hardcodées
- Chaque page HTML a des éléments avec des attributs sémantiques explicites :
  - `role=` ou balises sémantiques (`<button>`, `<input>`, `<label>`)
  - `aria-label=` ou `id=` pour les éléments ambigus
  - Messages d'erreur dans des éléments identifiables (`id="error-message"`, `role="alert"`)
- Les URLs sont stables et prévisibles (`/`, `/dashboard`, `/checkout/step1`, etc.)
- L'app doit fonctionner sans JavaScript complexe — HTML + formulaires POST suffisent pour la plupart des scénarios
- Ajouter du JS minimal si nécessaire (ex: show/hide d'un élément) mais jamais de framework

**Structure type de `server.py`** :
```python
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

# données en mémoire — pas de base de données
USERS = {"admin@example.com": "password123"}

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if USERS.get(email) == password:
            session["user"] = email
            return redirect("/dashboard")
        error = "Identifiants incorrects"
    return render_template("login.html", error=error)

# [autres routes selon le scénario]

if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

**Structure type d'un template HTML** :
```html
<!DOCTYPE html>
<html lang="fr">
<head><meta charset="UTF-8"><title>[Titre de la page]</title></head>
<body>
  <main>
    <h1>[Titre visible]</h1>

    {% if error %}
    <p id="error-message" role="alert">{{ error }}</p>
    {% endif %}

    <form method="POST" action="[url]">
      <label for="email">Email</label>
      <input type="email" id="email" name="email" placeholder="Email" required>

      <label for="password">Mot de passe</label>
      <input type="password" id="password" name="password" placeholder="Mot de passe" required>

      <button type="submit">Se connecter</button>
    </form>
  </main>
</body>
</html>
```

Règles HTML :
- Chaque `<input>` a un `<label>` associé avec `for=` — permet `get_by_label()` dans Playwright
- Chaque bouton a un texte clair — permet `get_by_role("button", name="...")`
- Les messages d'état (succès, erreur) ont un `id=` ou `role="alert"` — permet `locator("#id")`
- **Noms de variables et fonctions Python en anglais** — textes affichés dans l'app en français

---

**`conftest.py`** :
```python
import pytest
from playwright.sync_api import Page

BASE_URL = "http://localhost:5001"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture
def app_url() -> str:
    return BASE_URL


# Ajouter les fixtures nécessaires selon le scénario
# ex: logged_in_page, populated_cart, etc.
```

**`pages/[page_name].py`** — Page Object stub :

```python
from playwright.sync_api import Page


class PageName:
    """
    Page Object pour [description].
    URL : http://localhost:5001/[route]
    """

    URL = "http://localhost:5001/[route]"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page
    # ----------------------------------------------------------
    def navigate(self) -> None:
        raise NotImplementedError

    # ----------------------------------------------------------
    # TODO 2 — [action]
    # ----------------------------------------------------------
    # Entrée  : [exemple concret]
    # Attendu : [ce que ça fait]
    # ----------------------------------------------------------
    def method_name(self, value: str) -> None:
        raise NotImplementedError

    # ----------------------------------------------------------
    # TODO N — Lire [état]
    # ----------------------------------------------------------
    # Sortie  : [exemple concret de valeur retournée]
    # ----------------------------------------------------------
    def get_something(self) -> str:
        raise NotImplementedError
```

Règles pour les stubs POM :
- Toutes les méthodes lèvent `NotImplementedError`
- **Noms de méthodes et variables en anglais**

**`tests/test_[feature].py`** — tests fournis :

```python
import pytest
from playwright.sync_api import Page, expect
from pages.page_name import PageName


def test_main_scenario(page: Page):
    """[Description du cas testé]"""
    p = PageName(page)
    p.navigate()
    p.method_name("value")
    expect(page).to_have_url("http://localhost:5001/expected-url")


def test_error_case(page: Page):
    """[Cas d'erreur]"""
    # ...


# 2-3 tests au total
```

Règles pour les tests :
- 2-3 tests couvrant le parcours principal + 1 cas d'erreur
- Tous échouent sur `NotImplementedError` tant que les POM ne sont pas implémentés
- `expect()` de Playwright pour les assertions sur l'état de la page
- Noms de tests en anglais, docstrings en français

---

### Étape 2 — Setup

Après avoir généré tous les fichiers, lancer dans le dossier de la session :

```bash
uv venv .venv
uv pip install -r requirements.txt
.venv/bin/playwright install chromium
```

Puis vérifier que le serveur démarre correctement :
```bash
cd app && python server.py
```

Si une erreur de démarrage se produit, la corriger avant de passer la main.

Vérifier que les tests échouent bien sur `NotImplementedError` (pas d'autre erreur) :
```bash
# Dans un second terminal, depuis le dossier de la session :
.venv/bin/pytest tests/ -v
```

Corriger tout problème de setup avant de présenter le brief.

### Étape 3 — Présenter le brief

```
✅ Setup OK. Tests fournis : tous en échec (NotImplementedError — c'est normal).

📋 Brief dans BRIEF.md

▶️  Lance le serveur :
    cd sessions/YYYYMMDD-playwright-[slug]/app
    python server.py

▶️  Dans un autre terminal, lance les tests :
    cd sessions/YYYYMMDD-playwright-[slug]
    .venv/bin/pytest tests/ -v

📝  Tu dois aussi écrire au moins 2 tests supplémentaires
🔚  Dis-moi quand tu as fini pour le débrief
```

**Format de `BRIEF.md`** :

```markdown
# Session Playwright — [nom du scénario]

## Contexte

[2-3 phrases : quelle app, ce qui est déjà construit, pourquoi ces tests sont nécessaires]

## Lancer le serveur

```bash
cd app && python server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

[Description du parcours utilisateur à couvrir — point de vue métier, pas technique]

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] [critère spécifique au scénario]

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais pas `tests/`
- Tu peux inspecter `app/templates/` pour comprendre le DOM
```

### Étape 4 — Débrief (quand l'utilisateur dit qu'il a fini)

1. Demander de coller la sortie de `pytest tests/ -v`
2. Évaluer :
   - **Critères d'acceptance** : lesquels sont remplis
   - **Locators** : sémantiques (`get_by_label`, `get_by_role`) ou fragiles (CSS, XPath) ?
   - **POM** : méthodes cohérentes, nommage clair, pas de logique de test dans le POM ?
   - **Tests supplémentaires** : vrais cas aux limites ou doublons ?
   - **Attentes Playwright** : `expect()` utilisé correctement ?
3. Écrire le débrief dans `sessions/YYYYMMDD-playwright-[slug]/debrief.md`

**Format `debrief.md`** :
```markdown
# Débrief — [nom du scénario] — [date]

## Résultat
[X]/[Y] tests passent.

## Points forts
- [ce qui est maîtrisé]

## Points à retravailler
- [ce qui mérite attention + explication courte]

## 1 chose à retenir
[Règle concrète ou pattern à garder pour la prochaine session]
```

---

## Banque de scénarios (inspiration — générer des variantes originales)

**Authentification avec redirection**
App Flask avec login/logout. Tester : login valide → dashboard, login invalide → message d'erreur, accès `/dashboard` sans session → redirection `/login`.

**Formulaire multi-étapes**
App Flask avec 3 routes (`/step1`, `/step2`, `/confirm`). Tester : remplissage complet, navigation arrière, validation champ manquant, confirmation finale.

**Gestionnaire de tâches**
App Flask avec liste de todos. Tester : créer une tâche, la marquer comme faite, la supprimer, filtrer par statut.

**Tableau de données avec filtres**
App Flask avec une liste d'items filtrables (statut, catégorie, recherche texte). Tester : filtres individuels, combinaison de filtres, reset des filtres.

**Panier e-commerce simplifié**
App Flask avec catalogue et panier en session. Tester : ajouter un article, modifier la quantité, vider le panier, vérifier le total.

**Formulaire de profil avec validation**
App Flask avec un formulaire de mise à jour de profil. Tester : modification réussie, email invalide → erreur, champ requis vide → erreur, message de succès.
