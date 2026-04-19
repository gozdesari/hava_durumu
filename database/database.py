import sqlite3

DB_NAME = "weather.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature REAL,
        humidity INTEGER,
        wind_speed REAL,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO weather_data (city, temperature, humidity, wind_speed, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (
        data["city"],
        data["temperature"],
        data["humidity"],
        data["wind_speed"],
        data["timestamp"]
    ))

    conn.commit()
    conn.close()

def get_last_temperatures(limit=5):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT temperature FROM weather_data
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return [row[0] for row in rows]

def create_analysis_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        average_temperature REAL,
        max_temperature REAL,
        warning TEXT,
        analysis_time TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_analysis(avg_temp, max_temp, warning, analysis_time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO weather_analysis (average_temperature, max_temperature, warning, analysis_time)
    VALUES (?, ?, ?, ?)
    """, (avg_temp, max_temp, warning, analysis_time))

    conn.commit()
    conn.close()