# Session Playwright — Réservation de salle (3 étapes)

## Contexte

Tu travailles sur un mini outil interne de **réservation de salles de réunion**.
L’application Flask est déjà en place : formulaire en trois étapes (session serveur),
récapitulatif puis confirmation avec **référence unique** `BK-XXXXXX`.
Ton rôle : implémenter les Page Objects, faire passer les tests fournis, puis ajouter
au moins deux tests personnels.

## Lancer le serveur

```bash
cd sessions/20260503-playwright-room-booking/app
python server.py
```

L’app écoute sur **http://localhost:5001** (racine `/` redirige vers l’étape 1).

## Ce que tu dois tester

- Parcours nominal : date + salle → créneau + participants → récap → confirmation ;
  la page finale affiche une référence qui commence par `BK-`.
- Accès direct à `/booking/step2` ou `/booking/step3` **sans avoir rempli les étapes**
  : redirection vers l’étape 1.

## Ta mission

1. Implémente tous les `TODO` dans `pages/booking_step1_page.py`, `booking_step2_page.py`,
   `booking_step3_page.py`, `booking_success_page.py`.
2. Lance `pytest tests/ -v` depuis le dossier de la session — les **3** tests fournis doivent passer.
3. Ajoute **au moins 2 tests supplémentaires** dans `tests/test_room_booking.py` (cas aux limites,
   message d’erreur étape 1, lien « Nouvelle réservation », etc.).
4. Dis « j’ai fini » pour le débrief.

## Critères d’acceptation

- [ ] Les 3 tests fournis passent
- [ ] Au moins 2 tests supplémentaires couvrant des cas non couverts
- [ ] Locators sémantiques (`get_by_label`, `get_by_role`, `select_option` avec `label=`)
- [ ] Pas de `time.sleep()` — privilégier `expect()` pour l’état de la page
- [ ] Le POM encapsule les interactions — pas de `page.click` / `page.fill` dans les tests
- [ ] Le récap étape 3 correspond bien aux choix faits aux étapes 1 et 2

## Lancer les tests

```bash
cd sessions/20260503-playwright-room-booking
.venv/bin/pytest tests/ -v
```

## Indices (seulement si bloqué depuis plus de 15 min)

<details>
<summary>Indice 1 — liste déroulante</summary>

Pour une `<select>` avec libellés visibles en français, utilise
`locator.select_option(label="…")` ou `get_by_label("…").select_option(label="…")`
avec le **texte exact** de l’option dans le HTML.
</details>

<details>
<summary>Indice 2 — ordre des étapes</summary>

Les routes `/booking/step2` et `/booking/step3` vérifient la session Flask : sans données
préalables, la redirection attendue est vers `/booking/step1` (voir les tests fournis).
</details>

<details>
<summary>Indice 3 — idées pour tes 2+ tests</summary>

Erreur serveur étape 1 si champs manquants (ex. soumission incomplète si tu simules le cas),
vérification du créneau ou du nombre de participants au récap, navigation « Nouvelle réservation »
qui ramène à l’étape 1 avec état cohérent.
</details>

## Contraintes

- Playwright Python — API **sync** uniquement
- Page Object Model obligatoire
- Tu modifies `pages/` librement ; pour `tests/test_room_booking.py`, ajoute uniquement tes **nouveaux** tests à la fin du fichier (ne pas casser les tests fournis)
- Tu peux ouvrir `app/templates/` pour t’aligner sur les libellés et `id` du DOM
