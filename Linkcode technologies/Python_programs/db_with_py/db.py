import sqlite3
conn=sqlite3.connect("Linkcode.db")
print("db created")
#cursor object--->execute(table creation syntax)
cursor=conn.cursor()
#table create
cursor.execute("""
  create table if not exists student(
  id int primary key,
  name text not null,
  age int
  )

""")
print("table created")
#manual Input
#cursor.execute("""
#  insert into student(id,name,age) values(?,?,?)
#""",(1,"Ram",20))
#conn.commit()
#print("data inserted")


