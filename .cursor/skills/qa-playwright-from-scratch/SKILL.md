---
name: qa-playwright-from-scratch
description: >-
  Génère une mini app Flask + un brief métier uniquement : aucun Page Object
  pré-rempli, aucun test fourni. L'utilisateur écrit from scratch tous les POM
  et tous les tests Playwright (pytest-playwright). ~60-90 min. À placer de
  temps en temps dans la semaine pour consolider sans stubs. Utilise quand
  l'utilisateur dit /qa-playwright-from-scratch, veut apprendre POM + tests
  seul, ou « from scratch Playwright ».
---

# QA Playwright — Page Objects & tests from scratch

Session **volontairement plus dure** que `/qa-playwright-session` : l’agent ne te donne **ni** méthodes `NotImplementedError` avec indices, **ni** fichier de tests à faire passer. Tu reçois une **app Flask qui marche**, un **`BRIEF.md`** avec critères d’acceptation, et tu **inventes** toi-même les classes Page Object et les tests.

**Objectif pédagogique** : savoir ouvrir le HTML, choisir les locators, structurer un POM, écrire des `test_*` stables — **sans filet**.

**Stack** : Flask + Python + Playwright + pytest-playwright (identique aux autres sessions).

**Durée** : ~60 à 90 minutes (selon le scénario).

---

## Différence avec `/qa-playwright-session`

| | `qa-playwright-session` | `qa-playwright-from-scratch` |
|--|-------------------------|------------------------------|
| Page Objects | Stubs avec TODO + indices | **Tu crées** les fichiers et méthodes |
| Tests | 2–3 tests fournis (échouent au début) | **Aucun** test fourni : tu écris **tous** les tests |
| Brief | Oui | Oui, avec **liste de scénarios à couvrir** (checklist) |
| Débrief | Quand tu dis « j’ai fini » | Idem + `debrief.md` si tu demandes |

---

## Où placer cette session dans la semaine (recommandation)

Le **`PROGRAMME.md`** prévoit déjà **3× Playwright** (mardi, jeudi, dimanche). Ce skill sert à **renforcer** sans doubler la même recette « stubs + tests fournis ».

**Rythme conseillé** :

- **1 fois par semaine**, **entre** deux grosses sessions Playwright du programme — par exemple **mercredi** (jour bug hunt le matin / l’après-midi : tu peux placer ce skill **un autre créneau** le même jour ou **jeudi matin** avant le gros E2E du soir), **ou** le **lundi soir / vendredi** si tu veux varier.
- **Pas obligatoire chaque semaine** : une fois **sur deux** suffit si tu es déjà à l’aise avec `/qa-playwright-session`.
- **Éviter** le même créneau que la chasse aux bugs si tu es fatigué : ce skill demande **concentration** (lecture HTML + design de tests).

En une phrase : **« de temps en temps »** = idéalement **1 créneau dédié 60–90 min**, pas le même jour que les 3 gros jours Playwright si tu veux respirer.

---

## Workflow agent

### Étape 0 — Proposer 3 scénarios (comme `qa-playwright-session`)

Avant toute génération, proposer **exactement 3** scénarios **distincts** (auth, formulaire multi-étapes, liste / filtres, panier simplifié, etc.). Attendre le choix **A**, **B** ou **C**. Ne pas recopier un scénario déjà présent dans `sessions/` récent.

### Étape 1 — Générer le dossier de session

Créer `sessions/YYYYMMDD-pom-from-scratch-[slug]/` avec :

```
sessions/YYYYMMDD-pom-from-scratch-[slug]/
├── BRIEF.md
├── requirements.txt
├── conftest.py
├── app/
│   ├── server.py
│   └── templates/
│       └── *.html
├── pages/
│   └── .gitkeep          # dossier vide — l'utilisateur crée les .py
└── tests/
    └── .gitkeep          # dossier vide — l'utilisateur crée test_*.py
```

**Interdit dans ce skill** (pour respecter « from scratch ») :

- Aucun fichier `pages/*_page.py` avec méthodes pré-écrites ou `NotImplementedError`.
- Aucun `tests/test_*.py` avec corps de tests.
- Optionnel : un **`pages/README.md`** d’**une ligne** du type « Crée ici une classe par page importante » — **sans** donner les noms de méthodes ni les sélecteurs.

**`requirements.txt`** (identique aux autres sessions) :

```
flask
playwright
pytest
pytest-playwright
```

**`conftest.py`** : même base que `qa-playwright-session` (`BASE_URL`, `browser_context_args`, fixture `app_url`).

**App Flask** : mêmes règles de qualité que `qa-playwright-session` (labels, `role="alert"`, URLs stables, pas de DB lourde).

### Étape 2 — Contenu de `BRIEF.md` (obligatoire)

Le brief doit contenir **au minimum** :

1. **Contexte** (2–3 phrases).
2. **Comment lancer le serveur** (`cd app && python server.py`, port **5001** sauf conflit documenté).
3. **Critères d’acceptation** sous forme de **checklist** : par ex. « au moins **N** tests pytest », « couvrir : connexion OK, erreur login, redirection si non connecté… » — **N** adapté au scénario (souvent 4 à 6 tests au total).
4. **Contraintes** : POM obligatoire ; sync Playwright ; pas de `time.sleep()` ; locators sémantiques privilégiés ; **l’utilisateur peut modifier `pages/` et `tests/` librement**.
5. **Indices** : **aucun** bloc du type « TODO + indice locator » dans le code généré ; éventuellement **une** section « Indices » en `<details>` dans le brief, **très parcimonieuse** (max 2 indices vagues), à n’ouvrir qu’après 20 min de blocage.

### Étape 3 — Setup (comme les autres skills)

Depuis le dossier de session :

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/playwright install chromium
```

Vérifier que le serveur démarre. **Ne pas** lancer de tests fournis (il n’y en a pas).

### Étape 4 — Message de passation à l’utilisateur

Indiquer clairement :

- L’app est prête ; **`pages/`** et **`tests/`** sont **vides** — tout est à créer.
- Ouvrir **`app/templates/`** pour comprendre le DOM avant d’écrire le POM.
- Lancer le serveur puis **`pytest tests/ -v`** une fois les fichiers créés.
- Objectif : remplir la checklist du **`BRIEF.md`**.

### Étape 5 — Débrief (quand l’utilisateur dit « j’ai fini »)

Comme `qa-playwright-session` : demander la sortie de `pytest`, évaluer critères / locators / POM / qualité des tests, rédiger **`debrief.md`** dans le dossier de session si l’utilisateur le souhaite.

---

## Banque d’idées de scénarios (inspiration)

Réutiliser la même inspiration que `qa-playwright-session` mais **générer des variantes** (noms d’app, champs, URLs différents) pour éviter la copie de sessions existantes.

---

## Rappel pour l’agent

- **Ne pas** générer de stubs POM ni de tests fournis : c’est le cœur du skill.
- **Ne pas** modifier `PROGRAMME.md` sauf si l’utilisateur demande explicitement d’y ajouter une ligne pour ce skill.
- Si l’utilisateur est **débutant** et bloque 30 min, proposer **un seul** micro-indice (ex. « commence par une classe pour la page d’accueil du formulaire ») — pas la solution complète.
