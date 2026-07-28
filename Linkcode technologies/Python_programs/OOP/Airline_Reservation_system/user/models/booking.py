class booking:
    pass

    def __init__(self, booking_id, passenger_name, flight_no, source, destination, seat_no, price):
        self.booking_id = booking_id
        self.passenger_name = passenger_name
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.seat_no = seat_no
        self.price = price

    def display(self):
        print("-" * 50)
        print("Booking ID      :", self.booking_id)
        print("Passenger Name  :", self.passenger_name)
        print("Flight Number   :", self.flight_no)
        print("Source          :", self.source)
        print("Destination     :", self.destination)
        print("Seat Number     :", self.seat_no)
        print("Price           :", self.price)
        print("-" * 50)