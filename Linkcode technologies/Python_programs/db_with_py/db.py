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

#user input
id=int(input("Enter your Id:"))
name=input("Enter your name:")
age=int(input("Enter your age:"))
cursor.execute("""
  insert into student(id,name,age) values(?,?,?)
""",(id,name,age))
conn.commit()
print("data inserted by user")