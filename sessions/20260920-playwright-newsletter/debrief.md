# Débrief — Préférences newsletter — 2026-09-20

## Résultat
5/5 tests passent (3 fournis + 2 supplémentaires).

## Points forts
- POM clair : `get_by_label` / `get_by_role` pour les actions (email, catégories, fréquence, submit, lien résumé)
- Distinction checkbox vs radio bien comprise
- Correction de `get_saved_email` vers `#saved-email` (texte ciblé, pas tout le bloc)
- 2 vrais cas ajoutés : fréquence manquante + parcours `/summary` avec données cohérentes
- Pas de `time.sleep()` — usage de `expect()`

## Points à retravailler
- Les tests utilisent encore `page.locator("#...")` directement : l’idéal est de tout passer par le POM (ex. `get_summary_email()`), comme pour `get_saved_email`
- `test_error_when_frequency_is_not_checked` pourrait aussi vérifier `role="alert"` visible, comme les autres tests d’erreur — plus robuste
- Piège appris : validation HTML5 (bulle navigateur) ≠ message Flask (`#error-message`) — à retenir pour les champs `type="email"`

## 1 chose à retenir
Pour un formulaire : commence toujours par te demander si l’erreur vient du **navigateur** ou du **serveur**, avant d’écrire l’assertion.
