# Débrief — Profil utilisateur (Playwright) — 5 mai 2026

## Résultat

**5 / 5** tests passent — les 3 fournis + **2 tests ajoutés** :
- `test_check_new_value_after_update` : vérifie que le champ nom est bien pré-rempli avec la nouvelle valeur après sauvegarde
- `test_check_error_message` : vérifie le texte exact du message d'erreur quand le nom est vide

## Points forts

- **7 méthodes implémentées correctement** : locators sémantiques (`get_by_label`, `get_by_role`) utilisés systématiquement — aucun CSS fragile dans le POM.
- **`input_value()` bien assimilé** : après plusieurs tentatives, la distinction entre `.inner_text()` (texte entre balises HTML) et `.input_value()` (valeur d'un `<input>`) est acquise — c'est une erreur classique que tu ne referas plus.
- **Tests supplémentaires pertinents** : les 2 tests couvrent des cas réellement différents des tests fournis — pas des doublons.
- **Lecture du HTML** : tu as su retrouver les bons labels et IDs dans `profile.html` pour construire les locators (`"Nom complet"`, `"Email"`, `#success-message`, `#error-message`).

## Points à retravailler

- **`get_by_role` nécessite un rôle ARIA valide** : `"input"` et `"nutton"` ne sont pas des rôles — les rôles courants sont `"button"`, `"link"`, `"heading"`, `"textbox"`, `"alert"`. Pour un champ de saisie, préférer `get_by_label` plutôt que `get_by_role("textbox")`.
- **Distinguer lire vs écrire** : `.fill()` écrit, `.input_value()` lit, `.inner_text()` lit le texte HTML — garder ce repère en tête avant d'écrire la ligne.

## Une chose à retenir

Pour tout `<input>` : **`get_by_label("texte du label").input_value()`** pour lire, **`.fill(value)`** pour écrire. La même logique s'applique à tous les champs de formulaire dans Playwright.
