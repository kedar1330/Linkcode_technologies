from Admin.admin import admin
from user.user import user

while True:

    print("\n========== AIRLINE RESERVATION SYSTEM ==========")
    print("1. Admin Panel")
    print("2. User Panel")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = admin()
        a.admin_panel()

    elif choice == 2:
        u = user()
        u.user_panel()

    elif choice == 3:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")