class search_services:
    pass

    def __init__(self, flight_list):
        self.flight_list = flight_list

    def search_flight(self):

        if len(self.flight_list) == 0:
            print("No Flights Available")
            return

        flight_no = int(input("Enter Flight Number: "))

        for f in self.flight_list:
            if f.flight_no == flight_no:
                print("Flight Found")
                f.display()
                return

        print("Flight Not Found")

    def view_all_flights(self):

        if len(self.flight_list) == 0:
            print("No Flights Available")
        else:
            for f in self.flight_list:
                f.display()