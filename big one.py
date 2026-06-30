import mysql.connector as sq
def additems(): 
    conn = sq.connect( host="localhost",user="root",password="aishani@123",database="ShoppingCart")
    cursor = conn.cursor()
    a=input("Enter name of product : ")
    a=a.strip()
    a=a.title()
    ct=0
    cursor.execute("SELECT * FROM shop WHERE ITEM_NAME= %s", (a,))
    for row in cursor.fetchall():
        if row[1]==a.title():
            print("Product Found")
            ct=1
            print("Product: ",row[1],"\nPrice: ",row[2])
            c=input("Do you want to add this product to cart?(y/n) : ")
            cursor.execute("SELECT * FROM cart WHERE ITEM_NAME= %s", (a,))
            row1=cursor.fetchone()
            if row1==None:
                if c.lower()=="y":
                    s=int(input("Enter quantity needed : "))
                    if s!=0:
                        l=s*row[2]
                        row= row+(s,l,)
                        cursor.execute("INSERT INTO cart VALUES (%s,%s,%s,%s,%s)",row)
                        conn.commit()
                        print("Product has been added to cart")
                    elif s==0:
                        print("No products added to cart")
                    else:
                        print("invalid input")
                elif c.lower()=="n":
                    print("No products added to cart")
                else:
                    print("Invalid Input")
            else:
                s=int(input("Enter quantity needed : "))
                cursor.execute("UPDATE Cart SET Qty = Qty+%s WHERE ITEM_NAME=%s",(s,a,))
                conn.commit()
                cursor.execute("UPDATE Cart SET TOTAL=Qty*PRICE WHERE ITEM_NAME=%s",(a,))
                conn.commit()
                print("Product has been added to cart")
    if ct==0:
        print("Product Not Found")
                
    conn.close()
    print("\n")
def viewcart(): 
    conn = sq.connect(host="localhost", user="root", password="aishani@123", database="ShoppingCart")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Cart")
    cart_items = cursor.fetchall()
    
    # Constants for formatting
    total_width = 69
    title = "YOUR SHOPPING CART"
    centered_title = title.center(total_width)  # Centering the title
    
    if len(cart_items) == 0:
        print("\nYour cart is empty!\n")
    else:
        print("\n" + "-" * total_width)
        print(centered_title)  # Centered title
        print("-" * total_width)
        print("{:<10} {:<20} {:<10} {:<10} {:<10}".format("CODE", "PRODUCT", "PRICE", "QTY", "TOTAL PRICE"))
        print("-" * total_width)
        
        grand_total = 0  # Initialize grand total to calculate total cost of all items
        
        for row in cart_items:
            code, product, price, qty, total_price = row
            print("{:<10} {:<20} {:<10} {:<10} {:<10}".format(code, product, f"₹{price:.2f}", qty, f"₹{total_price:.2f}"))
            grand_total += total_price
        
        print("-" * total_width)
    
    conn.close()
def bill():
    conn = sq.connect( host="localhost",user="root",password="aishani@123", database="ShoppingCart")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Cart')
    total=0
    for row in cursor.fetchall():
        total = total + row[4]
    print("-" * 69)
    print(f"Grand Total: ₹{total:.2f}")
    print("-" * 69)
    d=input("\nProceed to payment(y/n) : ")
    if d=="y":
        g=input("Please enter UPI ID : ")
        for i in range(0,3):
            print("...")
        print("Payment Sucessful")
        cursor.execute("TRUNCATE Cart")
        conn.commit()
        conn.close()
    elif d=="n":
        print("Payment Cancelled")
    else:
        print("Invalid Input")
    
def delete(n):
    conn = sq.connect( host="localhost",user="root",password="aishani@123", database="ShoppingCart")
    cursor = conn.cursor()
    f=int(input("Enter quantity to delete : "))
    cursor.execute("SELECT * FROM cart WHERE ITEM_NAME= %s", (n,))
    row1=cursor.fetchone()
    if row1==None:
        print("Item not in cart")
    else:
        if row1[3]>f:
            cursor.execute("UPDATE Cart SET Qty = Qty-%s WHERE ITEM_NAME=%s",(f,n,))
            conn.commit()
            cursor.execute("UPDATE Cart SET TOTAL=Qty*PRICE WHERE ITEM_NAME=%s",(n,))
            conn.commit()
        else:
            cursor.execute("DELETE FROM Cart WHERE ITEM_NAME = %s", (n,))
            conn.commit()
    conn.commit()
    n=n.title()
    print("Quantity updated")
    conn.close
while True: 
    print("""\n                                   MENU:\n
                    1.To add products to shopping cart\n
                    2.To delete products from shopping cart\n
                    3.To view cart\n
                    4.To start billing\n
                    5.Exit\n""")
    ch=int(input("Enter choice : "))
    if ch==1:
        additems()
    elif ch==4:
        bill()
    elif ch==2:
        p=input("Enter name of item to delete from cart : ")
        delete(p)
    elif ch==3:
        viewcart()
    elif ch==5:
        break
    else:
        print("Invalid Input")
