# Brief — Mini panier

## Contexte

Boutique interne avec un **catalogue** (3 articles) et un **panier**.
Depuis le catalogue, on ajoute un article ; on ouvre le panier pour voir les lignes et le **total**.
Pas de paiement ni de connexion.

## Lancer le serveur

```bash
cd app
python3 server.py
```

Serveur : http://127.0.0.1:5001

## Critères d'acceptation (minimum 4 tests)

1. Le catalogue affiche les 3 produits.
2. Après ajout d'un produit, le compteur panier (badge) affiche 1.
3. La page panier liste le produit ajouté avec son nom.
4. Le total affiché correspond au prix du produit (une unité).
5. (Bonus) Deux produits différents ajoutés → total = somme des deux prix.

## Contraintes

- POM obligatoire : **une classe par écran principal** (catalogue + panier).
- API sync Playwright uniquement.
- Pas de `time.sleep()`.
- Locators sémantiques : `get_by_role`, `get_by_label`, `locator`.
- Assertions : `expect` pour l'état visible / URL ; `assert` pour textes, comptes et montants.

## Structure à créer

```
pages/
└── (tes classes POM)

tests/
└── (tes test_*.py)

conftest.py
└── reset + fixtures catalogue / panier si tu en as besoin
```

Ouvre `app/templates/` avant d'écrire le POM.
