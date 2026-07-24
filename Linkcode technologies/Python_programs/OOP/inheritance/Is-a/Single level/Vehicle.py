class Vehicle:
    #instance var
    def __init__(self,fuel_type,brand):
        self.fuel_type=fuel_type
        self.brand=brand

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

        