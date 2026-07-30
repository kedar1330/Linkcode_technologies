def user_panel(
        passenger_service,
        flight_service,
        booking_service,
        payment_service,
        ticket_service
):

    while True:

        print("\n" + "=" * 60)
        print("                 USER PANEL")
        print("=" * 60)

        print("1. Register")
        print("2. Login")
        print("3. Exit")

        print("=" * 60)

        choice = int(input("Enter Your Choice: "))


        if choice == 1:
            print("\n" + "=" * 60)
            print("         PASSENGER REGISTRATION")
            print("=" * 60)

            passenger_service.register_passenger()

            print("\nRegistration Successful!")
            print("You can now login using your Passenger ID and Password.")


        elif choice == 2:

            passenger = passenger_service.login()

            if passenger is None:
                continue

            while True:

                print("\n" + "=" * 60)
                print("               USER OPERATIONS")
                print("=" * 60)

                print("1. Available Flights")
                print("2. Search Flights")
                print("3. Book Flight")
                print("4. Payment")
                print("5. Cancel Booking")
                print("6. Generate Ticket")
                print("7. Logout")

                print("=" * 60)

                ch = int(input("Enter Your Choice: "))

                if ch == 1:

                    flight_service.available_flights()


                elif ch == 2:

                    print("\n1. Search by Flight ID")
                    print("2. Search by Source and Destination")

                    search_choice = int(input("Enter Choice: "))

                    if search_choice == 1:

                        flight_service.search_flight()

                    elif search_choice == 2:

                        flight_service.search_by_route()

                    else:

                        print("Invalid Choice")
                elif ch == 3:

                    booking = booking_service.book_flight(
                        flight_service,
                        passenger
                    )

                    if booking is None:
                        continue

                    while True:

                        print("\n1. Continue To Payment")
                        print("2. Book More Flights")

                        option = int(input("Enter Choice: "))

                        if option == 1:

                            payment_success = payment_service.make_payment(
                                booking
                            )

                            if payment_success:

                                print("Payment Completed Successfully.")
                                print("You can now generate your ticket from the User Menu.")

                            break

                        elif option == 2:

                            print("\nSearch Flights Again")

                            print("1. Search by Flight ID")
                            print("2. Search by Source and Destination")

                            search = int(input("Enter Choice: "))

                            if search == 1:

                                flight_service.search_flight()

                            elif search == 2:

                                flight_service.search_by_route()

                            booking = booking_service.book_flight(
                                flight_service,
                                passenger
                            )

                            if booking is None:
                                break

                        else:

                            print("Invalid Choice")


                elif ch == 4:

                    booking_id = int(input("Enter Booking ID: "))

                    booking = booking_service.get_booking(
                        booking_id
                    )

                    if booking is None:

                        print("Booking Not Found")

                    else:

                        payment_service.make_payment(
                            booking
                        )


                elif ch == 5:

                    booking_service.cancel_booking(
                        flight_service
                    )


                elif ch == 6:

                    booking_id = int(input("Enter Booking ID: "))

                    booking = booking_service.get_booking(
                        booking_id
                    )

                    if booking is None:

                        print("Booking Not Found")

                    elif len(payment_service.payment_list) == 0:

                        print("Payment Not Completed")

                    else:

                        payment = None

                        for p in payment_service.payment_list:

                            if p.booking_id == booking.booking_id:

                                payment = p
                                break

                        if payment is None:

                            print("Payment Not Found")

                        else:

                            ticket_service.generate_ticket(
                                booking,
                                payment
                            )

                # ---------------- Logout ---------------- #

                elif ch == 7:

                    print("User Logged Out Successfully")
                    break

                else:

                    print("Invalid Choice")


        elif choice == 3:

            return

        else:

            print("Invalid Choice")