# Session Playwright — Profil utilisateur avec validation

## Contexte

App interne Flask : un utilisateur peut consulter et modifier son profil (nom complet + email). Les données sont en mémoire (pas de base de données). Tu prends en charge les tests E2E de ce formulaire de mise à jour.

## Lancer le serveur

```bash
cd sessions/20260505-playwright-user-profile/app
python server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

Le formulaire de profil permet de :
- **Mettre à jour** son nom et son email → message de confirmation affiché
- **Soumettre un nom vide** → message d'erreur
- **Soumettre un email invalide** (sans `@` ou sans `.`) → message d'erreur
- **Vérifier** que les nouvelles valeurs sont bien persistées (re-affichées dans les champs après enregistrement)

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté **au moins 2 tests supplémentaires** couvrant des cas non testés (ex. vérification que la nouvelle valeur est pré-remplie après mise à jour, contenu exact du message d'erreur, etc.)
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` pour attendre un état visible
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] Les 7 méthodes du stub sont implémentées

## Lancer les tests

```bash
cd sessions/20260505-playwright-user-profile
.venv/bin/pytest tests/ -v
```

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` librement
- Tu **ne peux pas** modifier `tests/test_profile.py` (les 3 tests fournis)
- Tu peux inspecter `app/templates/profile.html` pour comprendre le DOM
