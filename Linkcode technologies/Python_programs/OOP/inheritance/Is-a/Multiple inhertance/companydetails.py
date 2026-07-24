class company:
    def __init__(self,dept,role):
        self.dept=dept
        self.role=role

    def display_company(self):
        print("=====company info===========")
        print(f"Department:{self.dept}\nRole:{self.role}")

    def show(self):
        print("Hello I am from company details class")