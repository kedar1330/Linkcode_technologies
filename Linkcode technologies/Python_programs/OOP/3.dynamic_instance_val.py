class mobile:
    def __init__(self, uname, ubrand, uprice, ucolor):
        self.brand = ubrand
        self.price = uprice
        self.name = uname
        self.color = ucolor
#obj creation
obj=mobile("Iphone", "Apple", 100000, "Black")
print(obj.name, obj.color, obj.price)

obj1=mobile("iphone15","iphone","150000","Pink")
print(obj1.name, obj1.brand, obj1.price, obj1.color)

#storing object inside loop
x=[obj,obj1]
for i in x:
    print(i.name, i.color, i.price)




