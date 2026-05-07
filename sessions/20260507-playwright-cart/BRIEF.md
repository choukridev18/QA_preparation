# Session Playwright — Panier e-commerce

## Contexte

L'app simule un catalogue de 4 produits avec un panier géré en session Flask.
Elle est déjà construite et fonctionnelle. Ton travail : implémenter les Page Objects
(`pages/catalog_page.py` et `pages/cart_page.py`) pour faire passer les 3 tests fournis,
puis écrire au moins 2 tests supplémentaires.

## Lancer le serveur

```bash
cd app && python server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

Un utilisateur parcourt le catalogue, ajoute des articles dans son panier, modifie les
quantités, supprime des articles, et vérifie que le total est calculé correctement.
Le panier est maintenu en session entre les pages.

## Critères d'acceptance

- [ ] Les 3 tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role`, `get_by_text` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] `get_total()` retourne un `float` (ex: `136.5`) — pas une chaîne brute

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais **pas** `tests/`
- Tu peux inspecter `app/templates/` pour comprendre le DOM

## Idées pour les tests supplémentaires

- Ajouter deux articles différents et vérifier que le panier en contient bien 2
- Vérifier que le compteur dans la nav ("Panier (N)") se met à jour après un ajout
- Ajouter un article avec une quantité > 1 depuis le catalogue et vérifier le total
- Vérifier que naviguer vers `/cart` sans rien ajouter affiche le message panier vide
