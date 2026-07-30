#switch case
from CRUD import *

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View One Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            add_stud()

        case 2:
            view_all()

        case 3:
            view_one_stud()

        case 4:
            update_stud()

        case 5:
            delete_record()

        case 6:
            print("Thank you for using the Student Management System!")
            break

        case _:
            print("Invalid choice! Please enter a number between 1 and 6.")