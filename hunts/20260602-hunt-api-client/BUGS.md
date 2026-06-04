# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — tests/test_weather_client.py, test_get_forecast_success

**Symptôme :** `ConnectionError` — une vraie requête HTTP est effectuée vers l'API.
**Cause :** `@mock.patch("requests.get")` patche la fonction dans le module `requests`, mais `weather_client` a déjà importé `get` via `from requests import get`. Le patch ne touche pas la référence locale dans `weather_client`.
**Correction :** `@mock.patch("src.weather_client.get")`

---

## Bug 2 — tests/test_weather_client.py, test_get_temperature_city_not_found

**Symptôme :** `FAILED: DID NOT RAISE WeatherAPIError` — c'est `CityNotFoundError` qui est levée à la place.
**Cause :** Pour un code HTTP 404, `get_temperature` lève `CityNotFoundError`, pas `WeatherAPIError`. Le mauvais type d'exception est attendu dans `pytest.raises`.
**Correction :** `with pytest.raises(CityNotFoundError):`

---

## Bug 3 — tests/test_weather_client.py, test_get_temperature_mock_setup

**Symptôme :** `WeatherAPIError: API error: <Mock name='mock().status_code' ...>`
**Cause :** `mock_get.side_effect = mock_response` fait que `mock_get(url)` appelle `mock_response(url)`, ce qui retourne un nouveau Mock enfant — pas `mock_response` lui-même. Le `status_code` du Mock enfant n'est pas 200.
**Correction :** `mock_get.return_value = mock_response`

---

## Bug 4 — tests/test_weather_client.py, test_get_forecast_json_response

**Symptôme :** `TypeError: 'dict' object is not callable`
**Cause :** `mock_get.return_value.json = {"forecast": [...]}` remplace la méthode `json` par un dict. Quand le code appelle `response.json()`, Python essaie d'appeler le dict comme une fonction.
**Correction :** `mock_get.return_value.json.return_value = {"forecast": [10.0, 12.0, 9.0]}`

</details>
