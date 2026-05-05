# Session Playwright — Authentification

## Contexte

Tu travailles sur une app interne avec un système de connexion basique.
L'app Flask est déjà construite : elle gère le login, la session utilisateur,
et redirige vers le dashboard après connexion. Ton rôle : implémenter les
Page Objects et faire passer les tests fournis, puis écrire 2 tests supplémentaires.

## Lancer le serveur

```bash
cd sessions/20260430-playwright-auth/app
python3 server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

Le parcours d'authentification complet :
- Un utilisateur qui se connecte avec de bons identifiants arrive sur le dashboard
- Un utilisateur qui entre un mauvais mot de passe reste sur le login avec un message d'erreur
- Un utilisateur non connecté qui tente d'accéder directement au dashboard est renvoyé au login

**Identifiants valides :** `alice@example.com` / `password123`

## Ta mission

1. Implémente les méthodes dans `pages/login_page.py` (3 TODO)
2. Implémente les méthodes dans `pages/dashboard_page.py` (4 TODO)
3. Lance `pytest tests/ -v` — les 3 tests fournis doivent passer
4. Écris **au moins 2 tests supplémentaires** dans `tests/test_auth.py`
5. Dis "j'ai fini" pour le débrief

## Critères d'acceptance

- [ ] Les 3 tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS comme `#id` dans les tests)
- [ ] Pas de `time.sleep()` — utilise `expect()` pour les assertions sur l'état de la page
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas `page.fill()` ou `page.click()` directement

## Lancer les tests

```bash
cd sessions/20260430-playwright-auth
.venv/bin/pytest tests/ -v
```

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire — les tests passent par les méthodes du POM
- Tu peux modifier `pages/` mais pas `tests/test_auth.py` (sauf pour ajouter tes tests supplémentaires à la fin)
- Tu peux inspecter `app/templates/` pour comprendre le DOM
