
import mysql.connector

search_term = input("Item name: ")
print(f"item is: {search_term}")


conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dubclub2464!",
    database = "osrs_ge"
)

cursor = conn.cursor()

def get_item_price(item_name):
    cursor.execute("""
                    select item_name,
                            high_price,
                            low_price
                    from items
                    where item_name = %s
                    """, (item_name,))
    return cursor.fetchone()

item=get_item_price(search_term)

print(item)








