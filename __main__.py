import requests
import json
from datetime import datetime

API_KEY = "967a2db725f9e215ab255cde7b1b3765"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&"

HISTORY_FILE = "history.json"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units" : "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print(f"Error fetching data for {city}: {response.json().get('message')}")
        return None
    return response.json()

def display_weather(data, city):
    if data is None:
        return
    description = data['weather'][0]['description'].capitalize()
    temp = data['main']['temp']
    print(f"Weather in {city}:{description}")
    print(f"Temperature:{temp}°C")

def save_history(city, weather_data):
    try:
        history = []
        #Load existing history

        try:
            with open("history.json", "r") as f:
                history = json.load(f)
        except FileNotFoundError:
            pass #File does not exist

        #Append new search
        history.append({
            "city" : city,
            "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "weather" : weather_data
        })

        #Save back to JSON
        with open("history.json", "w") as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        print(f"Error saving history: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    data = get_weather(city)
    display_weather(data, city)
    save_history(city, data)
    print(data)