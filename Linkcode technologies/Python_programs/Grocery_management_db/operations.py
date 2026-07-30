from db import conn,cursor
def add_prod():
    pass
    cnt=int(input("Enter how much products you want to add:"))
    for i in range(cnt):
        id=int(input(f"Enter {i+1} id: "))
        name=input(f"Enter Product {i+1} name:")
        brand=input("Enter brand name:")
        SP=int(input("Enter Selling price:"))
        MRP=int(input("Enter MRP:"))
        QTY=int(input(f"Enter quantity of {i+1} product"))
        cursor.execute("""
            insert into grocery(id,name,brand,SP,MRP,QTY) values(?,?,?,?,?,?)
          """,(id,name,brand,SP,MRP,QTY))
        conn.commit()
        print("data inserted by user")


def view_all():
    pass
    cursor.execute("select * from grocery")
    rows=cursor.fetchall()
    print(f"\n{rows}")



def search():
    cursor.execute("SELECT * FROM grocery")
    rows = cursor.fetchall()
    ch = int(input("Enter how you want to search product (1.ID, 2.Name): "))
    if ch == 1:
        id = int(input("Enter ID you want to search:"))
        for i in rows:
            if id == i[0]:
                cursor.execute("SELECT * FROM grocery where id=?",(id,))
                row = cursor.fetchone()
                print("Product found:")
                print(row)
                return
        print("Product not found")

    elif ch == 2:
        name = input("Enter the product name: ")
        for i in rows:
            if name.lower() == i[1].lower():
                cursor.execute("SELECT * FROM grocery where name=?",(name,))
                row = cursor.fetchone()
                print("Product found:")
                print(row)
                return

        print("Product not found")

    else:
        print("Invalid choice")



def update():
    pass
    cursor.execute("SELECT * FROM grocery")
    rows = cursor.fetchall()
    ip=int(input("Enter the id you want to update:"))
    for i in rows:
        if ip==i[0]:
            ch=int(input("Enter what you want to update\n1.name\n2.brand\n3.SP\n4.MRP\n5.QTY)"))
            if ch==1:
                name=input("Enter new name:")
                cursor.execute("Update grocery set name=? where id=?",(name,ip))
                conn.commit()
                print("name updated successfully!")
            elif ch==2:
                pass
                brand=input("Enter new brand_name:")
                cursor.execute("Update grocery set brand=? where id=?",(brand,ip))
                conn.commit()
                print("brand name updated successfully!")
            elif ch==3:
                pass
                SP=int(input("Enter new Selling price:"))
                cursor.execute("Update grocery set SP=? where id=?",(SP,ip))
                conn.commit()
                print("Selling price updated successfully!")
            elif ch==4:
                pass
                MRP=int(input("Enter new MRP:"))
                cursor.execute("Update grocery set MRP=? where id=?",(MRP,ip))
                conn.commit()
                print("MRP updated successfully!")
            elif ch==5:
                pass
                QTY=int(input("Enter new QTY:"))
                cursor.execute("Update grocery set QTY=? where id=?",(QTY,ip))
                conn.commit()
                print("QTY updated successfully!")
            else:
                print("Invalid choice!")
            return
    print("Product not found")



def delete_record():
    pass
    ch=int(input("Enter choice(1.Delete all records\n2.Delete one record):"))
    if ch == 1:
        confirm = input("Are you sure you want to delete all records? (yes/no): ")

        if confirm.lower() == "yes":
            cursor.execute("DELETE FROM grocery")
            conn.commit()
            print("All records deleted successfully!")
        else:
            print("Operation cancelled!")

    elif ch == 2:
        cursor.execute("SELECT * FROM grocery")
        rows = cursor.fetchall()

        ip = int(input("Enter the Product ID to delete: "))

        for i in rows:
            if ip == i[0]:
                cursor.execute("DELETE FROM grocery WHERE id=?", (ip,))
                conn.commit()
                print("Product deleted successfully!")
                return

        print("Product not found!")

    else:
        print("Invalid choice!")



def add_to_cart():
    grand_total = 0

    while True:

        cursor.execute("SELECT * FROM grocery")
        rows = cursor.fetchall()

        ip = int(input("Enter Product ID: "))

        found = False

        for i in rows:
            if ip == i[0]:
                found = True

                print("\nProduct Found")
                print("Name :", i[1])
                print("Brand :", i[2])
                print("Selling Price :", i[3])
                print("Available Quantity :", i[5])

                qty = int(input("Enter quantity: "))

                if qty <= i[5]:

                    total = qty * i[3]
                    grand_total += total

                    new_qty = i[5] - qty

                    
                    cursor.execute("""
                    INSERT INTO cart(id, name, price, qty, total)
                    VALUES(?,?,?,?,?)
                    """, (i[0], i[1], i[3], qty, total))

                    cursor.execute("""
                    UPDATE grocery
                    SET QTY=?
                    WHERE id=?
                    """, (new_qty, ip))

                    conn.commit()

                    print("Product added to cart successfully!")
                    print("Product Total =", total)

                else:
                    print("Insufficient Stock!")

                break

        if not found:
            print("Product not found!")

        ch = input("\nDo you want to add more products? (yes/no): ")

        if ch.lower() != "yes":
            break

    print("\nFINAL BILL")

    cursor.execute("SELECT * FROM cart")
    rows = cursor.fetchall()
    
    print("ID\tName\tPrice\tQty\tTotal")
    
    for i in rows:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")
    
    gst = grand_total * 0.05
    final_amount = grand_total + gst
    
    print("--------------------------------------------")
    print(f"Grand Total : ₹{grand_total:.2f}")
    print(f"GST (5%)    : ₹{gst:.2f}")
    print(f"Net Amount  : ₹{final_amount:.2f}")
    print("============================================")