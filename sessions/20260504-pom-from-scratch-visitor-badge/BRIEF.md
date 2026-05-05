# Session from scratch — Badge visiteur (3 étapes)

## Contexte

Tu es sur une mini-app interne : **demande de badge visiteur** en trois étapes (session Flask en mémoire), puis une page de succès avec un **numéro de dossier** au format `BADGE-XXXXX`.

L’agent a fourni **l’application** et ce brief. **Aucun** Page Object et **aucun** test ne sont fournis : tu les **crées toi-même** dans `pages/` et `tests/`.

## Lancer le serveur

```bash
cd sessions/20260504-pom-from-scratch-visitor-badge/app
python3 server.py
```

App sur **http://localhost:5001** (arrête tout autre serveur qui utiliserait déjà le port 5001).

## Ce que tu dois produire

1. **Page Objects** (sync Playwright) : autant de fichiers / classes que tu juges nécessaires pour couvrir les écrans `/visitor/step1`, `/visitor/step2`, `/visitor/step3`, `/visitor/success`.
2. **Tests Playwright** : fichier(s) sous `tests/` avec des fonctions `test_*` qui utilisent la fixture `page` et les assertions `expect` de l’API Playwright.
3. **Règles** : POM obligatoire (pas de `page.fill` / `page.click` directement dans les tests sauf exception minime documentée) ; privilégier `get_by_label`, `get_by_role` ; pas de `time.sleep()` ; utiliser `expect()` pour les assertions sur l’URL ou l’état visible.

## Critères d’acceptation (checklist)

- [ ] Au moins **5** tests pytest qui passent avec le serveur lancé.
- [ ] **Parcours nominal** : étape 1 → 2 → 3 → succès, et le numéro affiché commence par **`BADGE-`**.
- [ ] **Garde-fou** : accès direct à `/visitor/step2` sans session → redirection vers **étape 1**.
- [ ] **Garde-fou** : accès direct à `/visitor/step3` sans données complètes → redirection vers **étape 1** ou **étape 2** (comportement réel du `server.py`).
- [ ] **Garde-fou** : accès direct à `/visitor/success` sans dossier en session → redirection vers **étape 1**.
- [ ] Au moins **un** test qui vérifie une cohérence du **récapitulatif** étape 3 (nom, email, entreprise, date ou motif) avec les valeurs saisies aux étapes précédentes.

## Setup (une fois)

```bash
cd sessions/20260504-pom-from-scratch-visitor-badge
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/playwright install chromium
```

Lancer les tests :

```bash
.venv/bin/pytest tests/ -v
```

*(Au début : « no tests collected » est normal tant que tu n’as pas créé de fichiers `test_*.py`.)*

## Fin de session

Quand la checklist est verte, dis **« j’ai fini »** dans le chat pour un débrief (optionnel : fichier `debrief.md`).
