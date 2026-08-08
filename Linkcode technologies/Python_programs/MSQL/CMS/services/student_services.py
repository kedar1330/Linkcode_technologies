from models.student import student
from db import conn,cursor
def add_student():
    pass
    name=input("Enter student name:")
    age=int(input("Enter student age:"))
    email=input("Enter student email:")
    dept_id=int(input("Enter department id:"))
    s=student(name,age,email,dept_id)
    query="insert into student(name,age,email,dept_id) values(%s,%s,%s,%s)"
    values=(s.name,s.age,s.email,s.dept_id)
    cursor.execute(query,values)
    conn.commit()
    print("Student added successfully.")
def view_name_with_dept():
    pass
    name=input("Enter student name:")
    query="select s.name, d.dept_name from student s join dept d on s.dept_id = d.dept_id where s.name = %s"
    values=(name,)
    cursor.execute(query,values)
    result=cursor.fetchall()
    if result:
        for row in result:
            print(f"Student: {row[0]}, Department: {row[1]}")
    else:
        print("Student not found.")

def view_student_details():
    pass
    email=input("Enter student email:")
    query="select * from student where email = %s"
    values=(email,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    if result:
        print(f"ID: {result[0]}, Name: {result[1]}, Age: {result[2]}, Email: {result[3]}, Department ID: {result[4]}")
    else:
        print("Student not found.")

def update_student_details():
    pass
    email=input("Enter student email to update details:")
    query="select * from student where email = %s"
    values=(email,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    if result:
        new_name=input("Enter new name:")
        new_age=int(input("Enter new age:"))
        new_dept_id=int(input("Enter new department id:"))
        update_query="update student set name=%s, age=%s, dept_id=%s where email=%s"
        update_values=(new_name,new_age,new_dept_id,email)
        cursor.execute(update_query,update_values)
        conn.commit()
        print("Student details updated successfully.")
    else:
        print("Student not found.")