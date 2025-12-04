import requests


API_KEY = "967a2db725f9e215ab255cde7b1b3765"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&"


def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units" : "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print(f"Error fetching data for {city}: {response.json().get('message')}")
        return None
    return response.json()
