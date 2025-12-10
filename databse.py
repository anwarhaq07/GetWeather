import sqlite3
import os

DB_NAME = "weather.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    print("DB absolute path:", os.path.abspath(DB_NAME))
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            temperature REAL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_history(city, timestamp, weather):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history(city, timestamp, temperature, description)
        VALUES (?,?,?,?)
        """, (
            city,
            timestamp,
            weather["main"]["temp"],
            weather["weather"][0]["description"]
    ))
    conn.commit()
    conn.close()

#Clean history, entries must be restricted to maximum of 5
def clean_history(max_entries = 5):
    conn = get_connection()
    cursor = conn.cursor()

    #Count total entries
    cursor.execute("SELECT count(*) FROM history")
    total = cursor.fetchall()[0]

    if total <= max_entries:
        conn.close()
        return

    #Delete oldest entries
    cursor.execute(f"""DELETE FROM history
        WHERE id IN(
            SELECT id FROM history
            ORDER BY timestamp ASC
            LIMIT {total - max_entries}
        )
    """)
    conn.commit()
    conn.close()