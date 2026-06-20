
import mysql.connector
import requests
from datetime import datetime,timezone

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "Dubclub2464!",
    database = "osrs_ge"
)

cursor = conn.cursor()

cursor.execute(
    """
    Create Table if not exists godswords_30day
    (
        item_id int,
        item_name varchar(255),
        timestamp DATETIME,
        avg_high_price int,
        avg_low_price int,
        high_volume BIGINT,
        low_volume BIGINT,
        
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

        ts = datetime.fromtimestamp(point["timestamp"],tz=timezone.utc)

        cursor.execute(
            """
            INSERT INTO godswords_30day
            (
                item_id,
                item_name,
                timestamp,
                avg_high_price,
                avg_low_price,
                high_volume,
                low_volume
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE
                avg_high_price = VALUES(avg_high_price),
                avg_low_price = VALUES(avg_low_price),
                high_volume = VALUES(high_volume),
                low_volume = VALUES(low_volume)
            """,
            (
                item_id,
                item_name,
                ts,
                point["avgHighPrice"],
                point["avgLowPrice"],
                point["highPriceVolume"],
                point["lowPriceVolume"]
            )
        )
    conn.commit()
    print(f"Done {item_name}")




cursor.close
conn.close()

print("Success")




















