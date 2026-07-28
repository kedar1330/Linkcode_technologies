from models.passenger import passenger
class passenger_services:
    pass 
    def __init__(self):
        self.passenger_list = []

    def register_passenger(self):
        passenger_id = int(input("Enter Passenger ID: "))
        name = input("Enter Passenger Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        mobile = input("Enter Mobile Number: ")

        p = passenger(passenger_id, name, age, gender, mobile)
        self.passenger_list.append(p)

        print("Passenger Registered Successfully")

    def view_all(self):
        if len(self.passenger_list) == 0:
            print("No Passenger Records Found")
        else:
            for p in self.passenger_list:
                p.display()

    def update_passenger(self):
        passenger_id = int(input("Enter Passenger ID to Update: "))

        for p in self.passenger_list:
            if p.passenger_id == passenger_id:
                name = input("Enter New Name: ")
                age = int(input("Enter New Age: "))
                gender = input("Enter New Gender: ")
                mobile = input("Enter New Mobile Number: ")

                p.name = name
                p.age = age
                p.gender = gender
                p.mobile = mobile

                print("Passenger Updated Successfully")
                return

        print("Passenger Not Found")

    def delete_passenger(self):
        passenger_id = int(input("Enter Passenger ID to Delete: "))

        for p in self.passenger_list:
            if p.passenger_id == passenger_id:
                self.passenger_list.remove(p)
                print("Passenger Deleted Successfully")
                return

        print("Passenger Not Found")

    def search_passenger(self):
        passenger_id = int(input("Enter Passenger ID to Search: "))

        for p in self.passenger_list:
            if p.passenger_id == passenger_id:
                print("Passenger Found")
                p.display()
                return

        print("Passenger Not Found")