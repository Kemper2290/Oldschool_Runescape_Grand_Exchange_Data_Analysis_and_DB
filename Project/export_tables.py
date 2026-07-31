import pandas as pd
import mysql.connector
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

df = pd.read_sql("SELECT * FROM player_count", conn)

df.to_csv("player_count.csv", index=False)

conn.close()