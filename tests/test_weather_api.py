from weather_api import get_weather

def test_weather_invalid_city(monkeypatch):
    class MockResponse:
        status_code = 404
        def json(self):
            return {"message": "city not found"}

    def test_weather_invalid_city(monkeypatch):
        def mock_get(*args, **kwargs):
            return MockResponse()

        monkeypatch.setattr("requests.get", mock_get)

        result = get_weather("invalidcity")
        assert result is None