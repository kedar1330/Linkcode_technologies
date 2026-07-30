from utils.flight_menu import flight_menu
from utils.passenger_menu import passenger_menu
from utils.booking_menu import booking_menu


def admin_login():

    admin_id = input("Enter Admin ID: ")
    password = input("Enter Password: ")

    if admin_id == "Kedar" and password == "1234":

        print("Admin Login Successful")
        return True

    else:

        print("Invalid Admin ID or Password")
        return False


def admin_panel(
        flight_service,
        passenger_service,
        booking_service
):

    if not admin_login():
        return

    while True:

        print("\n" + "=" * 60)
        print("                 ADMIN PANEL")
        print("=" * 60)

        print("1. Flight Management")
        print("2. Passenger Management")
        print("3. Booking Management")
        print("4. Logout")

        print("=" * 60)

        choice = int(input("Enter Your Choice: "))

        if choice == 1:

            while True:

                flight_menu()

                ch = int(input("Enter Choice: "))

                if ch == 1:

                    flight_service.add_flight()

                elif ch == 2:

                    flight_service.update_flight()

                elif ch == 3:

                    flight_service.delete_flight()

                elif ch == 4:

                    flight_service.view_flight()

                elif ch == 5:

                    flight_service.search_flight()

                elif ch == 6:

                    break

                else:

                    print("Invalid Choice")

        elif choice == 2:

            while True:

                passenger_menu()

                ch = int(input("Enter Choice: "))

                if ch == 1:

                    passenger_service.register_passenger()

                elif ch == 2:

                    passenger_service.update_passenger()

                elif ch == 3:

                    passenger_service.delete_passenger()

                elif ch == 4:

                    passenger_service.search_passenger()

                elif ch == 5:

                    passenger_service.view_all_passenger()

                elif ch == 6:

                    break

                else:

                    print("Invalid Choice")
        elif choice == 3:

            while True:

                booking_menu()

                ch = int(input("Enter Choice: "))

                if ch == 1:

                    print("Book Ticket option is available only through User Login.")

                elif ch == 2:

                    booking_service.cancel_booking(
                        flight_service
                    )

                elif ch == 3:

                    booking_service.view_booking()

                elif ch == 4:

                    flight_service.available_flights()

                elif ch == 5:

                    break

                else:

                    print("Invalid Choice")

        elif choice == 4:

            print("Admin Logged Out Successfully")
            break

        else:

            print("Invalid Choice")