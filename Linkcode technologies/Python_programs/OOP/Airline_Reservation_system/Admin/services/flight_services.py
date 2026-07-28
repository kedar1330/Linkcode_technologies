from Admin.models.flight import flight
class flight_services:
    pass
    def __init__(self):
        self.flight_list=[]

    def add_flight(self):
        flight_no=int(input("Enter the flight number"))
        source=input("Enter the Source " )
        Destination=input("Enter the destination point")
        price=input("Enter the price")
        Total_seats=int(input("Enter Total_seats"))
        f=flight(flight_no,source,Destination,price,Total_seats)
        self.flight_list.append(f)
        print("Flight added successfully")

    def view_flight(self):
        if len(self.flight_list)==0:
            print("no flights Available")
        else:
            for f in self.flight_list:
                f.display()

    def update_flight(self):
        ch=int(input("Enter your choice(1.Update_flight\n2.Don't update)"))
        if ch==1:
            pass
            flight_no=int(input("Enter the flight_no you want to update details"))
            for f in self.flight_list:
                if f.flight_no==flight_no:
                    pass
                    source=input("Enter new source:")
                    Destination=input("Enter new destination:")
                    price=input("Enter new price")
                    total_seats=int(input("Enter new total seats"))
                    f.source=source
                    f.Destination=Destination
                    f.price=price
                    f.Total_seats=total_seats
                
        else:
            print("Okay!!!!!!")  

    def search_flight(self):
        if len(self.flight_list) == 0:
            print("No Flights Available")
            return

        flight_no = int(input("Enter Flight Number to Search: "))

        for f in self.flight_list:
            if f.flight_no == flight_no:
                print("\nFlight Found Successfully")
                f.display()
                return

        print("Flight Not Found")  

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


                             

    