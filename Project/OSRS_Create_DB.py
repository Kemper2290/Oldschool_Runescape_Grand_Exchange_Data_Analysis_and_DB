
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dubclub2464!"
)

cursor = conn.cursor()

#create database if not exist
cursor.execute(
    """
    Create Database if not exists osrs_ge
    """
)

cursor.execute("use osrs_ge")

# create table
cursor.execute("""
Create table if not exists items
(
    item_id    int primary key,
    item_name  VARCHAR(255),
    high_price int,
    low_price  INT
)
""")

conn.commit()
conn.close()

print("Database Created")








