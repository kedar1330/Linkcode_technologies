from services.dept_services import *
from services.student_services import *
from models.dept import *
def dept_menu():
    while True:
      choice=int(input("1.ADD\n2.UPADTE\n3.READ\n4.DELETE\n5.Student according to department\n6.department count\n7.Search by student name\nEnter your choice:"))
      match choice:
          case 1:
              add_dept()
          case 2:
              update_dept()
          case 3:
              view_all_depts()
          case 4:
              delete_dept()
          case 5:
              student_count_in_dept()
          case 6:
              dept_count()
          case 7:
              search_by_student_name()
          case 8:
              print("Exit")
          case _:
              print("Invalid choice")
              
              