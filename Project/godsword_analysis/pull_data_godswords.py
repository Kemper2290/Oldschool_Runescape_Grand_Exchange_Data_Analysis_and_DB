
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
    Create Table if not exists godswords_30day
    (
        item_id int,
        item_name varchar(255),
        timestamp DATETIME,
        avg_buy_price int,
        avg_sell_price int,
        buy_volume BIGINT,
        sell_volume BIGINT,
        
        primary key (item_id,timestamp)
    )
    """

)

conn.commit()

cursor.execute(
    """
    with cte as (
        select *
        from items
        where item_name like "%godsword" or item_name like "%hilt" or item_name = "Godsword blade"
    )
    select item_id,item_name
    from cte
    where item_name regexp 'Saradomin|Zamorak|Bandos|Armadyl' or item_name like "%Godsword Blade%"

    """
)

godsword_result = cursor.fetchall() #returns a list of tuples as type list

print("list of godsword_result")
for row in godsword_result:
    print(row)

print(godsword_result)

items = {}
for item_id,item_name in godsword_result:
    items[item_id] = item_name

print("dictionary of godsword_result")
print(items)
print("\n")

# ------------------
# API header (which is required)
# ------------------
headers = {"User_Agent": "OSRS-Price-Tracker"}



# ----------------
# Loop over Items
# ----------------

for item_id,item_name in items.items():
    print(f"fetching {item_name} ({item_id})")

    # -------------
    # Build api Url
    # -------------

    url = ( "https://prices.runescape.wiki/api/v1/osrs/timeseries")

    params = {"timestep": "6h",
              "id" : item_id}


    # ------------------
    # Request data
    # ------------------

    response = requests.get(url,headers = headers, params = params)
    data = response.json()["data"]

    # ----------------------
    # insert each time point
    # ----------------------

    for point in data:

        ts = datetime.fromtimestamp(point["timestamp"], tz=timezone.utc)

        avg_buy_price = point["avgHighPrice"]
        avg_sell_price = point["avgLowPrice"]
        buy_volume = point["highPriceVolume"]
        sell_volume = point["lowPriceVolume"]

        cursor.execute(
            """
            INSERT INTO Venezuela_bots
            (
                item_id,
                item_name,
                timestamp,
                avg_buy_price,
                avg_sell_price,
                buy_volume,
                sell_volume
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE
                                 avg_buy_price = VALUES(avg_buy_price),
                                 avg_sell_price = VALUES(avg_sell_price),
                                 buy_volume = VALUES(buy_volume),
                                 sell_volume = VALUES(sell_volume)
            """,
            (
                item_id,
                item_name,
                ts,
                avg_buy_price,
                avg_sell_price,
                buy_volume,
                sell_volume
            )
        )


    conn.commit()
    print(f"Done {item_name}")




cursor.close
conn.close()

print("Success")




















