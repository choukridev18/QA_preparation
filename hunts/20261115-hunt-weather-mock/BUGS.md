# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — tests/test_weather_client.py, test_get_forecast_success

**Symptôme :** `ConnectionError` ou appel réseau réel.
**Cause :** `@mock.patch("requests.get")` ne remplace pas `get` **déjà importé** dans `weather_client`.
**Correction :** `@mock.patch("src.weather_client.get")`

---

## Bug 2 — tests/test_weather_client.py, test_get_temperature_city_not_found

**Symptôme :** `DID NOT RAISE WeatherAPIError` (404 lève `CityNotFoundError`).
**Cause :** Mauvais type dans `pytest.raises`.
**Correction :** `with pytest.raises(CityNotFoundError):`

---

## Bug 3 — tests/test_weather_client.py, test_get_temperature_from_mock_response

**Symptôme :** `WeatherAPIError` ou `status_code` incohérent sur un Mock enfant.
**Cause :** `side_effect = mock_response` appelle l'objet au lieu de le retourner.
**Correction :** `mock_get.return_value = mock_response`

---

## Bug 4 — tests/conftest.py, fixture mock_http_200

**Symptôme :** `AttributeError` ou `NoneType` sur la fixture / `json`.
**Cause :** La fixture crée `response` mais **ne le retourne pas** (`return` manquant).
**Correction :** ajouter `return response` à la fin de `mock_http_200`.

</details>