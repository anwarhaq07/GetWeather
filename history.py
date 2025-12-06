import json
from datetime import datetime

from databse import insert_history

HISTORY_FILE = "history.json"

def save_history(city, weather_data):
   entry = {
       "city" : city,
       "timestamp" : datetime.now().isoformat(),
       "weather" : weather_data
   }
   print("Saving History in DB.....")
   time = entry["timestamp"]
   insert_history(city, time, weather_data)
   try:
        #Load existing history
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
   except:
        history = []

   #Append new search
   history.append(entry)

   #Save back to JSON
   with open(HISTORY_FILE, "w") as f:
       json.dump(history, f, indent=2)

def show_history():

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except:
        print("No history available")
        return

    print("\n=========== Search History ============")
    for entry in history:
        print(f"{entry['timestamp']} → {entry['city'].capitalize()}")
    print()
