# Session Playwright — Formulaire de profil avec validation

## Contexte

Une petite app Flask permet à un utilisateur de consulter et modifier son profil (nom, email, bio). Le formulaire d'édition valide les champs côté serveur : nom requis, email requis et au bon format. Les Page Objects sont fournis sous forme de stubs — toutes les méthodes lèvent `NotImplementedError`. Tu dois les implémenter, puis t'assurer que les 5 tests fournis passent.

## Lancer le serveur

```bash
cd app && python3 server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

Un utilisateur peut :
1. Consulter son profil (nom, email, bio affichés)
2. Cliquer sur "Modifier le profil" pour accéder au formulaire
3. Modifier ses informations et les enregistrer → message de succès + données mises à jour
4. Soumettre le formulaire avec un nom vide → message d'erreur sous le champ nom
5. Soumettre le formulaire avec un email invalide → message d'erreur sous le champ email

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] Les méthodes `get_*` et `has_*` lisent l'état de la page, pas les méthodes `fill_*`

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais **pas** `tests/`
- Tu peux inspecter `app/templates/` pour comprendre le DOM
- Deux Page Objects à implémenter : `ProfilePage` et `EditProfilePage`

## Indices HTML utiles

| Élément                  | Sélecteur à utiliser                              |
|--------------------------|---------------------------------------------------|
| Nom affiché (profil)     | `#profile-name`                                   |
| Email affiché (profil)   | `#profile-email`                                  |
| Message de succès        | `#success-message`                                |
| Lien "Modifier"          | `get_by_role("link", name="Modifier le profil")`  |
| Champ Nom (formulaire)   | `get_by_label("Nom")`                             |
| Champ Email (formulaire) | `get_by_label("Email")`                           |
| Champ Bio (formulaire)   | `get_by_label("Bio")`                             |
| Bouton soumettre         | `get_by_role("button", name="Enregistrer")`       |
| Erreur nom               | `#error-name`                                     |
| Erreur email             | `#error-email`                                    |
