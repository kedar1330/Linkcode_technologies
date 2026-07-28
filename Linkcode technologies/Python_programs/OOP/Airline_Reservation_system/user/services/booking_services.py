from user.models.booking import booking


class booking_services:

    def __init__(self):
        self.booking_list = []

    def book_ticket(self):

        booking_id = int(input("Enter Booking ID: "))
        passenger_name = input("Enter Passenger Name: ")
        flight_no = int(input("Enter Flight Number: "))
        source = input("Enter Source: ")
        destination = input("Enter Destination: ")
        seat_no = input("Enter Seat Number: ")
        price = float(input("Enter Ticket Price: "))

        b = booking(
            booking_id,
            passenger_name,
            flight_no,
            source,
            destination,
            seat_no,
            price
        )

        self.booking_list.append(b)

        print("Ticket Booked Successfully")

    def view_booking(self):

        if len(self.booking_list) == 0:
            print("No Bookings Found")

        else:
            for b in self.booking_list:
                b.display()

    def cancel_booking(self):

        booking_id = int(input("Enter Booking ID: "))

        for b in self.booking_list:

            if b.booking_id == booking_id:
                self.booking_list.remove(b)
                print("Booking Cancelled Successfully")
                return

        print("Booking Not Found")