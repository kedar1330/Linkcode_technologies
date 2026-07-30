class Flight:

    def __init__(self, flight_no, source, destination, price, total_seats):

        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.price = price
        self.total_seats = total_seats
        self.available_seats = total_seats


    def display(self):

        print("-" * 50)
        print("---------------- Flight Details ----------------")
        print("Flight No:", self.flight_no)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Price:", self.price)
        print("Total Seats:", self.total_seats)
        print("Available Seats:", self.available_seats)
        print("-" * 50)