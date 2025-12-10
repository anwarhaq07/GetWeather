import sqlite3
import json
from datetime import datetime
from databse import insert_history

HISTORY_FILE = "history.json"
DB_FILE = "weather.db"

def format_timestamp(ts):
    dt = datetime.fromisoformat(ts)
    return dt.strftime("%b %d, %Y %I:%M %p")

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

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("SELECT id, city, timestamp, temperature, description FROM history")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No history found.")
        return

    print("n --------Weather Search History--------")
    for row in rows:
        _id, city, ts,temp, desc = row
        formatted_ts = format_timestamp(ts)

        print(f"\n{_id}, {city.title()} ({desc.title()})")
        print(f"   Temp:{temp}°C")
        print(f"   Time: {formatted_ts}")

    # try:
    #     with open(HISTORY_FILE, "r") as f:
    #         history = json.load(f)
    # except:
    #     print("No history available")
    #     return
    #
    # print("\n=========== Search History ============")
    # for entry in history:
    #     print(f"{entry['timestamp']} → {entry['city'].capitalize()}")
    # print()
