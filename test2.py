import mysql.connector as sq
conn = sq.connect( host="localhost",user="root",password="aishani@123",database="ShoppingCart")
cursor=conn.cursor()
cursor.execute("""Create table if not exists Cart(
ITEM_CODE INT,
ITEM_NAME VARCHAR(100),
PRICE INT,
QTY INT,
TOTAL INT
)""")
conn.commit()
conn.close()
