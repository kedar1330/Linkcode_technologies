class flight:
    pass
    def __init__(self,flight_no,source,Destination,price,Total_seats):
        pass
        self.flight_no=flight_no
        self.source=source
        self.Destination=Destination
        self.price=price
        self.Total_seats=Total_seats
    def display(self):
        print("-"*50)
        print("-------------------Flight details--------------------- ")
        print("Flight_no:",self.flight_no)
        print("Source:",self.source)
        print("Destination:",self.Destination)
        print("price:",self.price)
        print("Total seats",self.Total_seats)
        print("-"*50)   

