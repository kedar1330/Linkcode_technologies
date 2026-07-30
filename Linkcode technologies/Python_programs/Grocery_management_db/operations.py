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

add_prod()

def view_all():
    pass
    cursor.execute("select * from grocery")
    rows=cursor.fetchall()
    print(f"\n{rows}")


view_all()
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
            if name == i[1]:
                cursor.execute("SELECT * FROM grocery where name=?",(name,))
                row = cursor.fetchone()
                print("Product found:")
                print(row)
                return

        print("Product not found")

    else:
        print("Invalid choice")

search()