class ticket:
    pass

    def __init__(self, ticket_id, passenger_name, flight_no, source, destination, seat_no, price):
        pass
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.seat_no = seat_no
        self.price = price

    def display(self):
        print("-" * 50)
        print("--------------- TICKET DETAILS ----------------")
        print("Ticket ID      :", self.ticket_id)
        print("Passenger Name :", self.passenger_name)
        print("Flight Number  :", self.flight_no)
        print("Source         :", self.source)
        print("Destination    :", self.destination)
        print("Seat Number    :", self.seat_no)
        print("Ticket Price   :", self.price)
        print("-" * 50)