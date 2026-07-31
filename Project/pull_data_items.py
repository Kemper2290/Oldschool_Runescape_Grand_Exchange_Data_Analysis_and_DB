
import mysql.connector
import requests

headers = {
    "User-Agent": "OSRS-Price-Tracker/1.0"
}

#returns item list
mapping = requests.get(
    "https://prices.runescape.wiki/api/v1/osrs/mapping",
    headers=headers
).json()

#returns current GE prices
prices = requests.get(
    "https://prices.runescape.wiki/api/v1/osrs/latest",
    headers=headers
).json()["data"] # data is the only key



conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dubclub2464!",
    database = "osrs_ge"
)

cursor = conn.cursor()

for item in mapping:
    item_id = item["id"]
    item_name = item["name"]

    if str(item_id) in prices:
        high_price = prices[str(item_id)]["high"]
        low_price = prices[str(item_id)]["low"]

        cursor.execute("""
        insert into items
            (item_id,item_name,high_price,low_price)
            values (%s,%s,%s,%s) 
            on duplicate key update
                item_name  = %s,
                high_price = %s,
                low_price  = %s
        """,
        (
            item_id,
            item_name,
            high_price,
            low_price,
            item_name,
            high_price,
            low_price
        ))


conn.commit()
conn.close()

print("Prices imported")




