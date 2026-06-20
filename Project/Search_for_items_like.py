
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

cursor.execute("""
               SELECT item_name,
                      high_price,
                      low_price
               FROM items
               WHERE item_name LIKE %s
               LIMIT 20
               """, (f"%{search_term}%",))

results= cursor.fetchall()  # returns as list
print(type(results))

for row in results:
    print(row)

conn.close()


