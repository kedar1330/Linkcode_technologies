class personal:
    def __init__(self,name,city,age):
        self.name=name
        self.city=city
        self.age=age

    def display_personal_details(self):
        print("=====personal info===========")
        print(f"Name:{self.name}\nCity:{self.city}\nAge:{self.age}")
        
    def show(self):
        print("Hello I am from personal details class")