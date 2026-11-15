# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini</summary>

## Bug 1 — `test_pending_count_after_one_task`

**Symptôme :** `assert 'À faire : 1' == '1'`
**Cause :** Le compteur affiche le préfixe complet `À faire : N`.
**Correction :** `== "À faire : 1"` (ou `assert "1" in tasks.get_pending_count_text()`).

---

## Bug 2 — `test_add_task_via_css_id`

**Symptôme :** Timeout sur `page.fill("#new_task", ...)` — élément introuvable.
**Cause :** L’id HTML est `new-task` (tiret), pas `new_task`.
**Correction :** `#new-task` ou `get_by_label("Nouvelle tâche")`.

---

## Bug 3 — `test_mark_task_done_updates_count`

**Symptôme :** Le compteur reste à 1 au lieu de 0.
**Cause :** `page.locator("button").first` clique sur **Ajouter**, pas sur **Marquer comme fait** (premier bouton du DOM).
**Correction :** `get_by_role("button", name="Marquer comme fait").click()` ou `tasks.mark_done("Ranger le bureau")`.

---

## Bug 4 — `test_task_line_shows_title_only`

**Symptôme :** `to_have_text` échoue — la ligne contient aussi le bouton.
**Cause :** `to_have_text` exige le texte **exact** de tout le `<li>`.
**Correction :** `expect(line.locator(".task-title")).to_have_text("Acheter du lait")` ou `to_contain_text("Acheter du lait")`.

</details>