
import mysql.connector
import requests
from datetime import datetime,timezone
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("DB_HOST"))
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")

)

cursor = conn.cursor()

cursor.execute(
    """
    Create Table if not exists Player_count
    (
        timestamp DATETIME,
        player_count int,
        
        primary key (timestamp)
    )
    """
)

conn.commit()

#website is exclusively the osrs player count
url = "https://www.osrsplayercount.com/api/history"

params = {
    "start": "2025-06-29T00:00:00Z",
    "end": "2026-06-28T00:00:00Z",
    "unit": "hour",
    "agg": "max"
}

response = requests.get(url,params=params)
history = response.json()
print(history[0])
print(history[-1])


for point in history:

    ts = datetime.strptime(
        point["timestamp"],
        "%Y-%m-%dT%H:%M:%SZ"
    )

    cursor.execute(
        """
        INSERT INTO Player_count(
            timestamp,
            player_count
        )
        VALUES (%s,%s)
        ON DUPLICATE KEY UPDATE
            player_count = VALUES(player_count)
        """,
        (
            ts,
            point["count"]
        )
    )

conn.commit()

cursor.close()
conn.close()

print("Finished!")


























