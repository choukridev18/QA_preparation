# Débrief — Formulaire de réservation multi-étapes — 28 mai 2026

## Résultat

9/9 tests passent. 9 TODOs du POM implémentés. 6 tests supplémentaires écrits.

## Points forts

- `fill_step1` / `fill_step2` : bonne utilisation de `get_by_label` avec les paramètres dynamiques
- `get_error_message` : bonne logique `is_visible()` avant `inner_text()`
- Tests de redirection (`/step2` et `/done` sans session) : bonne compréhension du flux
- `select_option(str(guests))` : conversion int → str trouvée rapidement
- Bonne progression sur l'assertion `== "texte exact"` vs `!= ""`

## Points à retravailler

- **`()` oublié** sur les méthodes — `inner_text` au lieu de `inner_text()`, `get_error_message` au lieu de `get_error_message()`. Réflexe à ancrer : une méthode s'appelle toujours avec `()`.
- **Ordre des paramètres** — `app_url: str, page: Page` au lieu de `page: Page, app_url: str`. Toujours `page` en premier dans les tests Playwright.
- **`booking.page.locator(...)` dans les tests** — préférer ajouter une méthode dans le POM (`get_summary_date`, `get_summary_guests`) et l'appeler depuis le test. Les tests ne doivent pas toucher Playwright directement.
- **Typos sur les ids HTML** — `#summary-gests` au lieu de `#summary-guests`. Réflexe : copier l'id depuis le HTML, ne pas le taper de mémoire.

## 1 chose à retenir

Quand tu lis une valeur depuis la page, ajoute une méthode dans le POM (`get_summary_X`) plutôt que d'appeler `booking.page.locator(...)` depuis le test. Le test reste lisible, le POM reste la seule couche qui touche Playwright.
