from menus.dept_menu import *
from menus.student_menu import *
choice=int(input("WELCOME TO CMS\n1.Admin login\n2.Student login\n3.Exit\nEnter Your choice: "))
match choice:
    case 1:
        username="Kedar"
        password="Kedar1234#"
        if username==input("Enter username:") and password==input("Enter password:"):
            print("Login successful")
            while True:
                choice=int(input("1.Department Management\n2.Student Management\n3.Exit\nEnter your choice:"))
                match choice:
                    case 1:
                        dept_menu()
                    case 2:
                        student_menu()
                    case 3:
                        print("Exiting from admin menu.")
                        break
                    case _:
                        print("Invalid choice.")
    case 2:
        print("Student login")
        cursor.execute("SELECT * from student")
        rows=cursor.fetchall()
        email=input("Enter your email:")
        for i in rows:
              if email==i[2]:
                  print("Login successful")

        student_menu()
    case 3:
        print("Exit")
    case _:
        print("Invalid Choice")
