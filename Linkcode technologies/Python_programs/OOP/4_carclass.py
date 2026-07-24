class car:
    brand = "Toyota"

    def __init__(self, uname, umodelno, uprice, uquantity):
        self.name = uname
        self.modelno = umodelno
        self.price = uprice
        self.quantity = uquantity

print(car.brand) 
car1=car("fortuner", 200608, 4000000, 6 )


print(car.brand)
car2=car("camry", 200609, 3000000, 9 )


x=[car1,car2]
for i in x:
    print(i.name,i.modelno,i.price,i.quantity)
    print("========================================")

total_price=0
for i in x:
    total_price+=i.price*i.quantity
print("Total price of all cars is:", total_price)

print("car name whose quantity is less than 10 and greater than 5 is:")
for i in x:
    if i.quantity<10 and i.quantity>5:
        print(i.name,i.quantity)

 


