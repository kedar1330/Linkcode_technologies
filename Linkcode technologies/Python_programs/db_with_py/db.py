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
def add_stud():
  id=int(input("Enter your Id:"))
  name=input("Enter your name:")
  age=int(input("Enter your age:"))
  cursor.execute("""
    insert into student(id,name,age) values(?,?,?)
  """,(id,name,age))
  conn.commit()
  print("data inserted by user")

#fetchall()---->entire row--->[]
def view_all():
  cursor.execute("select * from student")
  rows=cursor.fetchall()
  print(rows)
  #print only names
  for i in rows:
      print(i[1])


#fetchone()---->single row--->()
def view_one_stud():
  id=int(input("Enter your Id to fetch data:"))
  cursor.execute("SELECT * FROM student WHERE id=?",(id,))
  row=cursor.fetchone()
  print(row)

def update_stud():
   pass
   cursor.execute("SELECT * from student")
   rows=cursor.fetchall()
   id=int(input("Enter your ID:"))
   for i in rows:
      if id==i[0]:
        name=input("Enter new name:")
        age=int(input("Enter new age:"))
        cursor.execute("UPDATE student set name=?,age=? where id=?",(name,age,id)) 
        conn.commit()
        print("Data updated!")
        return
   print("NO record found")

def delete_record():
   pass
   cursor.execute("SELECT * from student")
   rows=cursor.fetchall()
   id=int(input("Enter your ID to delete:"))
   for i in rows:
      if id==i[0]:
         cursor.execute("delete from student where id=?",(id,)) 
         conn.commit()
         print("Deleted successfully")
         return
   print("NO record found")
         
   
#funtion_call
#add_stud()
#view_all()
#view_one_stud()
#update_stud()
delete_record()


