from personaldetails import personal
from companydetails import company

class employee(personal,company):
    def __init__(self,name,city,age,dept,role,salary):
        #classname.__init__(self,parameters)
        personal.__init__(self,name,city,age)
        company.__init__(self,dept,role)
        self.salary=salary

    def display(self):
        print("=====employee info===========")
        print()
        self.display_personal_details()
        print()
        self.display_company()
        print()
        print(f"Salary:{self.salary}")

obj=employee("Alice", "New York", 30, "Engineering", "Software Engineer", 75000)
obj.display_personal_details()
obj.display()
obj.show() 
#if same method name is present in 2 classes then call using classname.methodname(obj of class pass)
personal.show(obj) #calling personal class show method
company.show(obj) #calling company class show method