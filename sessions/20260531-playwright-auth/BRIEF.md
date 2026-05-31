# Session Playwright — Authentification avec redirection

## Contexte

L'app est un système de connexion simple avec login, dashboard protégé et logout. Elle est déjà construite. Ton travail : implémenter le Page Object `pages/auth_page.py` (6 TODOs) pour faire passer les 3 tests fournis, puis écrire au moins 2 tests supplémentaires.

## Lancer le serveur

```bash
cd app && python3 server.py
# App disponible sur http://localhost:5001
```

## Comptes disponibles

| Email | Mot de passe |
|---|---|
| admin@example.com | password123 |
| user@example.com | secret456 |

## Ce que tu dois tester

Un utilisateur se connecte avec ses identifiants, accède au dashboard, et peut se déconnecter. En cas d'identifiants incorrects ou de champs vides, un message d'erreur s'affiche. L'accès direct au dashboard sans session redirige vers le login.

## Critères d'acceptance

- [ ] Les 3 tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role`)
- [ ] Pas de `time.sleep()` — utilise `expect()`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais **pas** `tests/`
- Tu peux inspecter `app/templates/` pour comprendre le DOM

## Idées pour les tests supplémentaires

- Champs vides → message d'erreur visible
- Email inconnu → message d'erreur visible
- Accès direct à `/dashboard` sans session → redirection vers `/login`
- Après login, le message de bienvenue contient l'email de l'utilisateur
