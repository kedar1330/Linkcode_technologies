from models.dept import dept
from db import conn,cursor
def add_dept():
    pass
    dept_name=input("Enter department name:")
    d=dept(dept_name)
    query="insert into dept(dept_name) values(%s)"
    values=(d.dept_name,)
    cursor.execute(query, values)
    conn.commit()
    print("Department added successfully.")

def update_dept():
    pass
    dept_id=int(input("Enter department id to update:"))
    query="select * from dept where dept_id = %s"
    values=(dept_id,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    if result:
        new_dept_name=input("Enter new department name:")
        update_query="update dept set dept_name=%s where dept_id=%s"
        update_values=(new_dept_name,dept_id)
        cursor.execute(update_query,update_values)
        conn.commit()
        print("Department updated successfully.")
    else:
        print("Department not found.")

def delete_dept():
    pass
    dept_id=int(input("Enter department id to delete:"))
    query="select * from dept where dept_id = %s"
    values=(dept_id,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    if result:
        delete_query="delete from dept where dept_id=%s"
        delete_values=(dept_id,)
        cursor.execute(delete_query,delete_values)
        conn.commit()
        print("Department deleted successfully.")
    else:
        print("Department not found.")

def view_all_depts():
    pass
    query="select * from dept"
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        for row in result:
            print(f"Department ID: {row[0]}, Department Name: {row[1]}")
    else:
        print("No departments found.")  

def student_count_in_dept():
    pass
    dept_id=int(input("Enter department id to view student count:"))
    query="select count(*) from student where dept_id = %s"
    values=(dept_id,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    if result:
        print(f"Number of students in department {dept_id}: {result[0]}")
    else:
        print("Department not found or no students in this department.")

def dept_count():
    pass
    query="select count(*) from dept"
    cursor.execute(query)
    result=cursor.fetchone()
    if result:
        print(f"Total number of departments: {result[0]}")
    else:
        print("No departments found.")  

def search_by_student_name():
    pass
    name=input("Enter student name to search: ")
    query="select s.name, d.dept_name from student s join dept d on s.dept_id = d.dept_id where s.name = %s"
    values=(name,)
    cursor.execute(query,values)
    result=cursor.fetchall()
    if result:
        for row in result:
            print(f"Student: {row[0]}, Department: {row[1]}")
    else:
        print("Student not found.")



