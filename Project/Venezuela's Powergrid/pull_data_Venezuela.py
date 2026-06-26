
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
    Create Table if not exists Venezuela_bots
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
    select item_id,item_name
    from items
    where item_name in ('Saradomin Brew(4)','Super restore(4)', 'Super Combat Potion(4)',
                        'ranging potion(4)','Prayer Potion(4)','Shark','Lobster',
                        'AnglerFish','Blood rune','Soul rune','Cosmic rune',
                        "Zulrah's scales")"""
)

result = cursor.fetchall() #returns a list of tuples as type list

print("list of result")
for row in result:
    print(row)

print(result)

items = {}
for item_id,item_name in result:
    items[item_id] = item_name

print("dictionary of result")
print(items)
print("\n")

# ------------------
# API header (which is required)
# ------------------
headers = {"User-Agent": "OSRS-Price-Tracker"}



# ----------------
# Loop over Items
# ----------------

for item_id,item_name in items.items():
    print(f"fetching {item_name} ({item_id})")

    # -------------
    # Build api Url
    # -------------

    url = ( "https://prices.runescape.wiki/api/v1/osrs/timeseries")

    params = {"timestep": "24h",
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

cursor.execute("""
    alter table venezuela_bots
    modify column timestamp DATE
""")
conn.commit()


cursor.close
conn.close()

print("Success")




















