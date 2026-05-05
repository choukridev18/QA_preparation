---
name: qa-playwright-from-scratch
description: >-
  Génère une mini app Flask + un brief : aucun Page Object ni aucun test fourni.
  L'utilisateur écrit from scratch le POM et les tests E2E Playwright (~60–90 min).
  Session optionnelle pour consolider sans stubs. Utilise quand l'utilisateur dit
  /qa-playwright-from-scratch, « Playwright from scratch », ou veut du POM + tests
  sans fichier de départ.
---

# QA Playwright — From scratch

Session **plus exigeante** que `/qa-playwright-session` : l'agent livre une **app Flask fonctionnelle** et un **`BRIEF.md`** avec critères d'acceptation. **Aucun** stub de Page Object, **aucun** fichier de tests — tu structures le POM et les `test_*` **à partir du HTML et des routes**.

**Pourquoi ?** Mesurer la capacité à lire le DOM, choisir des locators stables, découper des pages en objets et écrire des parcours E2E **sans filet**.

**Stack** : Flask (app) + Python + Playwright (API sync) + pytest — **même `requirements.txt` et même `conftest.py` de base que** `qa-playwright-session` (reprendre le modèle de ce skill pour les dépendances et la fixture `page`).

**Durée** : ~60 à 90 minutes.

**Livrables côté utilisateur** : tout le code sous `pages/` et `tests/`.

---

## Workflow

### Étape 0 — Proposer 3 scénarios

Avant toute génération, propose **exactement 3** scénarios **distincts** (auth, formulaire multi-étapes, liste / filtres, panier minimal, etc.) et attends le choix **A**, **B** ou **C**.

Règles :
- Chaque scénario cible un parcours et des techniques Playwright **différents** des deux autres.
- Ne pas recopier un scénario déjà présent dans `sessions/` récent.

Format (identique en esprit à `qa-playwright-session`) :

```
Voici 3 scénarios — choisis-en un :

**A — [titre]**
[2–3 lignes]

**B — [titre]**
[2–3 lignes]

**C — [titre]**
[2–3 lignes]
```

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
│   └── .gitkeep          # vide — l'utilisateur ajoute les .py
└── tests/
    └── .gitkeep          # vide — l'utilisateur ajoute test_*.py
```

**Interdit pour respecter « from scratch »** :
- Aucun `pages/*_page.py` pré-rempli (pas de `NotImplementedError`, pas de squelette de méthodes).
- Aucun `tests/test_*.py` avec corps de test.
- Optionnel : `pages/README.md` sur **une ligne** du type « Une classe par écran principal » — **sans** noms de méthodes ni sélecteurs.

**`requirements.txt` et `conftest.py`** : calquer sur **`qa-playwright-session`** (URL de base, navigateur, fixture `page`).

**App Flask** : mêmes règles de qualité que **`qa-playwright-session`** (labels associés aux champs, messages d'erreur identifiables, URLs stables, pas de base lourde).

### Étape 2 — Contenu de `BRIEF.md` (obligatoire)

1. **Contexte** (2–3 phrases).
2. **Lancer le serveur** : `cd app` puis `python server.py`, port **5001** (ou autre si conflit, à documenter).
3. **Checklist** de critères d'acceptation : nombre minimal de tests, parcours nominal, garde-fous (redirections sans session, etc.).
4. **Contraintes** : POM obligatoire ; API **sync** Playwright ; pas de `time.sleep()` ; locators sémantiques (`get_by_role`, `get_by_label`, etc.) ; assertions avec `expect` pour l'état visible ou l'URL.
5. **Indices** : aucun indice dans le code généré, aucune section « Indices » dans le brief.

### Étape 3 — Setup

Depuis le dossier de session : créer le venv, installer les dépendances, installer le navigateur (même commandes que dans **`qa-playwright-session`**). Vérifier que le serveur démarre. **Ne pas** exécuter de suite de tests fournie (il n'y en a pas).

### Étape 4 — Message de passation

Indiquer clairement :
- l'app et le brief sont prêts ;
- `pages/` et `tests/` sont **vides** — tout est à créer ;
- ouvrir `app/templates/` avant d'écrire le POM ;
- lancer le serveur, puis `pytest tests/ -v` une fois les fichiers ajoutés.

### Étape 5 — Débrief

Quand l'utilisateur dit **« j'ai fini »** : demander la sortie de `pytest`, commenter POM, locators, stabilité des tests et respect du brief ; rédiger `debrief.md` dans le dossier de session si demandé.

---

## Banque d'idées

Réutiliser la même veine que **`qa-playwright-session`** mais avec des **variantes** (noms, champs, chemins d'URL) pour ne pas dupliquer une session existante.

---

## Rappel pour l'agent

- Ne pas générer de POM ni de tests fournis : c'est le cœur du skill.
- Ne pas donner d'indices, même si l'utilisateur est bloqué — poser des questions pour le guider.
