# Session Playwright — Tableau de bord avec filtres

## Contexte

Tu es QA sur un outil interne de suivi de tickets support. L'équipe dev a livré un tableau de bord avec filtres par statut, priorité et recherche texte. Ton job : automatiser les scénarios critiques avant la mise en prod.

L'app Flask et le HTML sont déjà en place. Les Page Objects sont des stubs — les tests fournis échouent tant que tu ne les implémentes pas.

## Lancer le serveur

```bash
cd app && python server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

- Affichage initial : tous les tickets visibles sans filtre
- Filtre par statut : seuls les tickets correspondants restent dans le tableau
- Recherche texte : filtrage par mot-clé dans le titre ; cas sans résultat
- Réinitialisation : après filtrage, le lien remet la liste complète
- (Bonus) Combinaison statut + priorité, ou priorité seule — via tes tests supplémentaires

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement (sauf `expect` dans les tests fournis)
- [ ] Tu comprends la différence entre filtrer (soumettre le formulaire) et réinitialiser (lien direct)

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais pas `tests/`
- Tu peux inspecter `app/templates/dashboard.html` pour comprendre le DOM
- Lance `pytest` depuis la racine de la session (`sessions/20260605-playwright-dashboard/`), pas depuis `tests/`

## Données de référence


| ID  | Titre                          | Statut   | Priorité |
| --- | ------------------------------ | -------- | -------- |
| 1   | Bug connexion impossible       | ouvert   | haute    |
| 2   | Export CSV ne fonctionne pas   | ouvert   | basse    |
| 3   | Lenteur page tableau de bord   | en_cours | haute    |
| 4   | Email de confirmation manquant | en_cours | basse    |
| 5   | Erreur 500 sur facturation     | ferme    | haute    |
| 6   | Typo page d'accueil            | ferme    | basse    |


Valeurs des `<select>` : statut `ouvert`, `en_cours`, `ferme` ; priorité `haute`, `basse`.