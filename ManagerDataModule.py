import sqlite3

connection = sqlite3.connect("HotelData.db")

cursor = connection.cursor()

cursor.execute("""
Create Table IF NOT EXISTS persons (

        User_ID  Text,
        Floor_Level Text,
        Room_Description Text,
        Price      Text,
        Date       INTEGER

)
""")

connection. commit()
connection.close()
