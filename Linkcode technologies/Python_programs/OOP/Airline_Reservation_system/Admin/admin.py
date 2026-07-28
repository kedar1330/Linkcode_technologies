from services.flight_services import flight_services
from services.passenger_services import passenger_services
from services.booking_services import booking_services

from utils.flight_menu import flight_menu
from utils.passenger_menu import passenger_menu
from utils.booking_menu import booking_menu


class admin:
    pass

    def __init__(self):
        self.fs = flight_services()
        self.ps = passenger_services()
        self.bs = booking_services()

    def admin_panel(self):

        while True:

            print("\n" + "=" * 55)
            print("                 ADMIN PANEL")
            print("=" * 55)
            print("1. Flight Management")
            print("2. Passenger Management")
            print("3. Booking Management")
            print("4. Reports")
            print("5. Logout")
            print("=" * 55)

            choice = int(input("Enter your choice: "))


            if choice == 1:

                while True:

                    flight_menu()

                    ch = int(input("Enter your choice: "))

                    if ch == 1:
                        self.fs.add_flight()

                    elif ch == 2:
                        self.fs.update_flight()

                    elif ch == 3:
                        self.fs.delete_flight()

                    elif ch == 4:
                        self.fs.view_flight()

                    elif ch == 5:
                        self.fs.search_flight()

                    elif ch == 6:
                        break

                    else:
                        print("Invalid Choice")


            elif choice == 2:

                while True:

                    passenger_menu()

                    ch = int(input("Enter your choice: "))

                    if ch == 1:
                        self.ps.register_passenger()

                    elif ch == 2:
                        self.ps.update_passenger()

                    elif ch == 3:
                        self.ps.delete_passenger()

                    elif ch == 4:
                        self.ps.search_passenger()

                    elif ch == 5:
                        self.ps.view_all()

                    elif ch == 6:
                        break

                    else:
                        print("Invalid Choice")


            elif choice == 3:

                while True:

                    booking_menu()

                    ch = int(input("Enter your choice: "))

                    if ch == 1:
                        self.bs.book_ticket()

                    elif ch == 2:
                        self.bs.cancel_ticket()

                    elif ch == 3:
                        self.bs.view_booking()

                    elif ch == 4:
                        self.bs.seat_availability()

                    elif ch == 5:
                        break

                    else:
                        print("Invalid Choice")


            elif choice == 4:
                pass


            elif choice == 5:
                print("Logging Out...")
                break

            else:
                print("Invalid Choice")