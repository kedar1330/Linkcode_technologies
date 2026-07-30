import sqlite3
conn=sqlite3.connect("Grocery.db")
print("db created")
#cursor object--->execute(table creation syntax)
cursor=conn.cursor()
#table create
cursor.execute("""
  create table if not exists grocery(
  id int primary key,
  name text not null,
  brand text not null,
  SP int not null,
  MRP int not null,
  QTY int 
  )

""")
print("table created")



