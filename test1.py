import mysql.connector as sq
conn = sq.connect( host="localhost",user="root",password="aishani@123",database="ShoppingCart")
cursor=conn.cursor()
cursor.execute("""Create table if not exists Shop(
ITEM_CODE INT,
ITEM_NAME VARCHAR(100),
PRICE INT
)""")
passenger= [
    (981,"Water",20),
    (841,"Chips",25),
    (972,"Pads",50),
    (999,"Soda",30),
    (567,"Pen",5),
    (678,"Tissue",30),
    (988,"Chocolate",20),
    (698,"Icecream",40),
    (368,"Pencil",10),
    (348,"Pouch",35),
    (548,"Marker",50),
    (511,"Eraser",10),
    (512,"Bag",100),
    (513,"Deodorant",200),
    (514,"Bodywash",300),
    (515,"Sunscreen",350),
    (516,"Gun",10000),
    (400,"Water Baloons",40),
    (401,"Monopoly",900),
    (402,"Scotland Yard",550),
    (403,"Nail Polish",250),
    (404,"Condoms",90),
    (405,"Ibuprofen",30),
    (406,"Dolo",30),
    (407,"Vicks Vaporub",30)
    ]
cursor.executemany("Insert into Shop values(%s,%s,%s)",(passenger))
conn.commit()
conn.close()
