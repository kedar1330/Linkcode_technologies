from admin import admin_panel
from users import user_panel

from services.flight_services import Flight_services
from services.passenger_services import Passenger_services
from services.booking_services import Booking_services
from services.payment_services import Payment_services
from services.ticket_services import Ticket_services

flight_service = Flight_services()
passenger_service = Passenger_services()
booking_service = Booking_services()
payment_service = Payment_services()
ticket_service = Ticket_services()


def main():
    while True:

        print("\n" + "=" * 60)
        print("          AIRLINE RESERVATION SYSTEM")
        print("=" * 60)

        print("1. Admin Panel")
        print("2. User Panel")
        print("3. Exit")

        print("=" * 60)

        try:

            choice = int(input("Enter Your Choice: "))

        except ValueError:

            print("Please Enter a Valid Number")
            continue


        if choice == 1:

            admin_panel(
                flight_service,
                passenger_service,
                booking_service
            )
        elif choice == 2:

            user_panel(
                passenger_service,
                flight_service,
                booking_service,
                payment_service,
                ticket_service
            )
        elif choice == 3:

            print("Thank You For Using Airline Reservation System")
            break
        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()