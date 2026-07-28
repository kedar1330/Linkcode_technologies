from models.booking import booking
class booking_services:
    pass

    def __init__(self):
        self.booking_list = []

    def book_ticket(self):
        booking_id = int(input("Enter Booking ID: "))
        passenger_id = int(input("Enter Passenger ID: "))
        flight_no = int(input("Enter Flight Number: "))
        seat_no = input("Enter Seat Number: ")

        b = booking(booking_id, passenger_id, flight_no, seat_no)
        self.booking_list.append(b)

        print("Ticket Booked Successfully")

    def cancel_ticket(self):
        booking_id = int(input("Enter Booking ID to Cancel: "))

        for b in self.booking_list:
            if b.booking_id == booking_id:
                self.booking_list.remove(b)
                print("Ticket Cancelled Successfully")
                return

        print("Booking Not Found")

    def view_booking(self):
        if len(self.booking_list) == 0:
            print("No Bookings Available")
        else:
            for b in self.booking_list:
                b.display()

    def seat_availability(self):
        flight_no = int(input("Enter Flight Number: "))

        booked_seats = 0

        for b in self.booking_list:
            if b.flight_no == flight_no:
                booked_seats += 1

        print("Booked Seats:", booked_seats)