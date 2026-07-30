from models.flight import Flight
class Flight_services:
    pass
    def __init__(self):

        self.flight_list = []
    # admin
    def add_flight(self):
        pass
        flight_no = int(input("Enter Flight Number: "))
        source = input("Enter Source: ")
        destination = input("Enter Destination: ")
        price = int(input("Enter Ticket Price: "))
        total_seats = int(input("Enter Total Seats: "))


        f = Flight(
            flight_no,
            source,
            destination,
            price,
            total_seats
        )


        self.flight_list.append(f)

        print("Flight Added Successfully")



    # admin
    def view_flight(self):
        pass
        if len(self.flight_list) == 0:

            print("No Flights Available")
            return
        for f in self.flight_list:

            f.display()
# ADMIN 
    def update_flight(self):

        if len(self.flight_list) == 0:

            print("No Flights Available")
            return


        flight_no = int(input("Enter Flight Number to Update: "))


        for f in self.flight_list:

            if f.flight_no == flight_no:

                source = input("Enter New Source: ")
                destination = input("Enter New Destination: ")
                price = int(input("Enter New Price: "))
                total_seats = int(input("Enter New Total Seats: "))


                f.source = source
                f.destination = destination
                f.price = price
                f.total_seats = total_seats


                if f.available_seats > total_seats:

                    f.available_seats = total_seats


                print("Flight Updated Successfully")
                return


        print("Flight Not Found")



    # admin

    def delete_flight(self):

        if len(self.flight_list) == 0:

            print("No Flights Available")
            return


        flight_no = int(input("Enter Flight Number to Delete: "))


        for f in self.flight_list:

            if f.flight_no == flight_no:

                self.flight_list.remove(f)

                print("Flight Deleted Successfully")
                return


        print("Flight Not Found")
    # admin ani user donhi sathi
    def search_flight(self):

        if len(self.flight_list) == 0:

            print("No Flights Available")
            return


        flight_no = int(input("Enter Flight Number: "))


        for f in self.flight_list:

            if f.flight_no == flight_no:

                print("Flight Found Successfully")
                f.display()
                return


        print("Flight Not Found")



    # User

    def available_flights(self):

        if len(self.flight_list) == 0:

            print("No Flights Available")
            return


        print("\nAvailable Flights")


        for f in self.flight_list:

            if f.available_seats > 0:

                f.display()



    # user

    def search_by_route(self):

        if len(self.flight_list) == 0:

            print("No Flights Available")
            return


        source = input("Enter Source: ")
        destination = input("Enter Destination: ")


        found = False


        for f in self.flight_list:

            if f.source == source and f.destination == destination:

                f.display()
                found = True



        if found == False:

            print("No Flight Found")

    def update_seats_after_booking(self, flight_no, seats):

        for f in self.flight_list:

            if f.flight_no == flight_no:

                if f.available_seats >= seats:

                    f.available_seats -= seats
                    return True


                else:

                    return False


        return False
    def update_seats_after_cancel(self, flight_no, seats):

        for f in self.flight_list:

            if f.flight_no == flight_no:

                f.available_seats += seats

                return True


        return False

    def get_flight(self, flight_no):
        for f in self.flight_list:

            if f.flight_no == flight_no:

                return f
        return None