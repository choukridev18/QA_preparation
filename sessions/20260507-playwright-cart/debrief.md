# Débrief — Panier e-commerce — 07/05/2026

## Résultat
5/5 tests passent.

## Points forts

- **Locators sémantiques bien maîtrisés** : `get_by_label(f"Quantité pour {product_name}")`,
  `get_by_role("button", name=f"Mettre à jour {product_name}")` — les `aria-label` dynamiques
  sont utilisés correctement pour cibler le bon élément parmi plusieurs similaires
- **Scoping article correct** : `locator("article").filter(has_text=product_name)` pour
  isoler le bouton "Ajouter au panier" du bon produit — c'est exactement le pattern attendu
- **`fill(str(quantity))`** : réflexe acquis de convertir en string avant de taper dans un input
- **Tests supplémentaires pertinents** : `test_add_two_items_shows_count_of_two` couvre un cas
  réel (multi-articles), `test_continue_shopping_link_returns_to_catalog` couvre la navigation retour

## Points à retravailler

- **POM non respecté dans un test** : `test_continue_shopping_link_returns_to_catalog` appelle
  `page.get_by_role(...)` directement dans le test au lieu de passer par une méthode `CartPage`.
  Le principe du POM : le test ne parle qu'au Page Object, jamais à Playwright directement.
  Il aurait fallu ajouter `go_to_catalog()` dans `CartPage`.

- **Bug silencieux dans `get_total()`** : `text.replace("Total :", "")` laisse un espace
  avant le nombre (`" 179,98 €"`). Ça fonctionne car `float()` tolère les espaces en Python,
  mais c'est un bug masqué. La version correcte : `text.replace("Total : ", "")` (avec l'espace
  après les deux points).

- **`get_cart_count()` utilise un CSS ID** : `locator("#cart-link")` fonctionne mais sort
  du principe des locators sémantiques. Préférer `get_by_role("link", name="Panier", exact=False)`
  pour rester cohérent avec le reste du POM.

## 1 chose à retenir

**Le test ne touche jamais Playwright directement** — toute interaction avec la page passe par
une méthode du Page Object. Si tu te retrouves à écrire `page.get_by_role(...)` dans un test,
c'est le signe qu'il manque une méthode dans le POM.
