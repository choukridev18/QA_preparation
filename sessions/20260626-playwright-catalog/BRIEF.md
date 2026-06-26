# Session Playwright — Catalogue produits avec recherche

## Contexte

Une app Flask de catalogue produits est déjà construite. Elle affiche 6 produits filtrables par nom et catégorie. Ton rôle : implémenter les Page Objects et faire passer les tests E2E.

## Lancer le serveur

```bash
cd sessions/20260626-playwright-catalog/app
python3 server.py
# App disponible sur http://localhost:5001
```

## Lancer les tests

```bash
cd sessions/20260626-playwright-catalog
.venv/bin/pytest tests/ -v
```

## Ce que tu dois tester

- Affichage des 6 produits par défaut
- Recherche par mot-clé → filtre les résultats
- Filtre par catégorie → affiche les produits de cette catégorie
- Recherche sans résultat → message "Aucun produit"
- Réinitialiser → retour à la liste complète

## Critères d'acceptance

- [x] Les 5 tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires
- [x] Locators sémantiques (`get_by_label`, `get_by_role`, `locator`)
- [ ] Pas de `time.sleep()`
- [ ] Le POM encapsule toute l'interaction

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Inspecte `app/templates/catalog.html` pour les sélecteurs
- Tu peux modifier `pages/` mais pas `tests/`

