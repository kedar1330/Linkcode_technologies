from A import engine
class car:
    def __init__(self,uip):
        self.age=90
        #object of engine class is created inside car class
        self.e=engine(uip)
    def car_details(self):
        self.e.show_details() #calling method of engine class using object of engine class
        return f"car details are:{self.name}"

obj=car(200)
print(obj.age, obj.e.name, obj.e.horsepower)

#method calling
#obj.e.show_details()
print(obj.car_details())


