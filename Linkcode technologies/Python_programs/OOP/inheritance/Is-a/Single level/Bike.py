from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, fuel_type, brand, colour,price):
        super().__init__(fuel_type, brand) #calling instance variable of vehicle class using super() method
        self.colour=colour
        self.price=price

    def ride(self):
        print("Bike is riding")

    def custom_start(self):
        super().start() #calling method of vehicle class using super() method
        print("BRUMM BRUMM")

    def average(self,petrol_consumed, total_petrol,distance):
        a=distance/petrol_consumed
        print(f"average of bike is:{a} km/litre")
        remaining_petrol=total_petrol-petrol_consumed
        print(f"remaining petrol is:{remaining_petrol} litres")

B=Bike("petrol","Honda","red",100000)
B.custom_start()
B.ride()
B.stop()
print(B.fuel_type)
print(B.brand)
print(B.colour)
print(B.price)
B.average(10,50,100)


