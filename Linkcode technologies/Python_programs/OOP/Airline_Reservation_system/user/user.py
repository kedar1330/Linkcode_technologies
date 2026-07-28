from user.services.user_services import user_services
from user.services.search_services import search_services
from user.services.booking_services import booking_services
from user.services.ticket_services import ticket_services

from user.utils.user_menu import user_menu, dashboard_menu


class user:
    pass

    def __init__(self):
        self.us = user_services()
        self.ss = search_services([])
        self.bs = booking_services()
        self.ts = ticket_services(self.bs)

    def user_panel(self):

        while True:

            user_menu()

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.us.register()
            elif choice == 2:

                if self.us.login():

                    while True:

                        dashboard_menu()

                        ch = int(input("Enter your choice: "))
                        if ch == 1:
                            self.ss.search_flight()
                        elif ch == 2:
                            self.bs.book_ticket()
                        elif ch == 3:
                            self.bs.view_booking()
                        elif ch == 4:
                            self.bs.cancel_booking()
                        elif ch == 5:
                            self.ts.generate_ticket_pdf()
                        elif ch == 6:
                            self.us.logout()
                            break

                        else:
                            print("Invalid Choice")


            elif choice == 3:
                break

            else:
                print("Invalid Choice")