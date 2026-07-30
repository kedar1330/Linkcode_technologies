import sqlite3
conn=sqlite3.connect("Grocery.db")
print("db created")
#cursor object--->execute(table creation syntax)
cursor=conn.cursor()
#table create
cursor.execute("""
  create table if not exists grocery(
  id int PRIMARY KEY,
  name text not null,
  brand text not null,
  SP int not null,
  MRP int not null,
  QTY int 
  )

""")
# Create Cart Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cart(
    id INTEGER,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    qty INTEGER NOT NULL,
    total INTEGER NOT NULL
)
""")

# Save changes
conn.commit()

print("Tables created successfully!")


