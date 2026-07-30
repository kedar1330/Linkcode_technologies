class Booking:

    def __init__(self, booking_id, passenger_id, passenger_name,
                 flight_no, source, destination,
                 seats, price, total_price):

        self.booking_id = booking_id
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name

        self.flight_no = flight_no
        self.source = source
        self.destination = destination

        self.seats = seats
        self.price = price
        self.total_price = total_price

        self.status = "Confirmed"


    def display(self):

        print("-" * 60)
        print("--------------- Booking Details ---------------")

        print("Booking ID:", self.booking_id)
        print("Passenger ID:", self.passenger_id)
        print("Passenger Name:", self.passenger_name)

        print("Flight No:", self.flight_no)
        print("Source:", self.source)
        print("Destination:", self.destination)

        print("Seats Booked:", self.seats)
        print("Ticket Price:", self.price)
        print("Total Price:", self.total_price)

        print("Status:", self.status)

        print("-" * 60)