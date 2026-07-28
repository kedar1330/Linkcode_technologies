class booking:
    pass

    def __init__(self, booking_id, passenger_id, flight_no, seat_no):
        pass
        self.booking_id = booking_id
        self.passenger_id = passenger_id
        self.flight_no = flight_no
        self.seat_no = seat_no

    def display(self):
        print("-" * 50)
        print("---------------- Booking Details ----------------")
        print("Booking ID  :", self.booking_id)
        print("Passenger ID:", self.passenger_id)
        print("Flight No   :", self.flight_no)
        print("Seat No     :", self.seat_no)
        print("-" * 50)