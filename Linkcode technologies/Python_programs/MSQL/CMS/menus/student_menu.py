from services.student_services import *

def student_menu():
    pass
    choice=int(input("1.view dept\n2.view student details\3n.update details\n4.exit\nEnter your choice:"))
    match choice:
        case 1:
            view_name_with_dept()
        case 2:
            view_student_details()
        case 3:
            update_student_details()
        case 4:
            print("Exiting from student menu.")
        case _:
            print("Invalid choice.")
