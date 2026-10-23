# Brief — Tableau de bord des livraisons

## Contexte

Une société de logistique utilise un tableau de bord interne pour suivre ses livraisons.
Chaque livraison a un statut (en cours, livré, retourné) que les opérateurs peuvent modifier.
Le tableau affiche aussi des compteurs globaux et permet de filtrer par statut.

## Lancer le serveur

```bash
cd app
python3 server.py
```

Serveur disponible sur : http://127.0.0.1:5001

## Critères d'acceptation (minimum 5 tests)

1. La page affiche bien 5 livraisons au total.
2. Filtrer par "En cours" affiche uniquement les livraisons en cours.
3. Le compteur "En cours" affiche le bon nombre.
4. Changer le statut d'une livraison met à jour son statut affiché.
5. Après un changement de statut, les compteurs sont mis à jour.
6. (Bonus) Filtrer par "Livrés" puis revenir sur "Tous" réaffiche toutes les livraisons.

## Contraintes

- POM obligatoire : une seule classe pour cette app (une seule page).
- API sync Playwright uniquement.
- Pas de `time.sleep()`.
- Locators sémantiques : `get_by_role`, `get_by_label`, `locator`.
- Assertions avec `expect` pour l'état visible, `assert` pour les valeurs Python.

## Structure à créer

```
pages/
└── dashboard_page.py   ← ta classe POM

tests/
└── test_dashboard.py   ← tes tests
```

Ouvre `app/templates/dashboard.html` pour identifier les locators avant d'écrire le POM.
