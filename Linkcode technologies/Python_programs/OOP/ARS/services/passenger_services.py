from models.passenger import Passenger
from utils.id_generator import generate_passenger_id
class Passenger_services:

    def __init__(self):

        self.passenger_list = []
    def register_passenger(self):
        pass
        passenger_id = generate_passenger_id()
        print("Generated Passenger ID:", passenger_id)
        name = input("Enter Passenger Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        password = input("Create Password: ")
        p = Passenger(
            passenger_id,
            name,
            age,
            gender,
            email,
            phone,
            password
        )


        self.passenger_list.append(p)


        print("Passenger Registered Successfully")
        print("Passenger can now login using Passenger ID and Password")

    def update_passenger(self):
        pass
        if len(self.passenger_list) == 0:

            print("No Passenger Available")
            return


        passenger_id = int(input("Enter Passenger ID to Update: "))


        for p in self.passenger_list:

            if p.passenger_id == passenger_id:

                p.name = input("Enter New Name: ")
                p.age = int(input("Enter New Age: "))
                p.gender = input("Enter New Gender: ")
                p.email = input("Enter New Email: ")
                p.phone = input("Enter New Phone: ")


                print("Passenger Updated Successfully")
                return


        print("Passenger Not Found")

    def delete_passenger(self):
        pass
        if len(self.passenger_list) == 0:

            print("No Passenger Available")
            return


        passenger_id = int(input("Enter Passenger ID to Delete: "))


        for p in self.passenger_list:

            if p.passenger_id == passenger_id:

                self.passenger_list.remove(p)

                print("Passenger Deleted Successfully")
                return


        print("Passenger Not Found")
    def search_passenger(self):

        if len(self.passenger_list) == 0:

            print("No Passenger Available")
            return


        passenger_id = int(input("Enter Passenger ID: "))


        for p in self.passenger_list:

            if p.passenger_id == passenger_id:

                print("Passenger Found Successfully")
                p.display()
                return


        print("Passenger Not Found")

    def view_all_passenger(self):

        if len(self.passenger_list) == 0:

            print("No Passenger Available")
            return


        for p in self.passenger_list:

            p.display()
    def login(self):

        if len(self.passenger_list) == 0:

            print("No Registered Users Available")
            return None


        passenger_id = int(input("Enter Passenger ID: "))
        password = input("Enter Password: ")


        for p in self.passenger_list:

            if p.passenger_id == passenger_id and p.password == password:

                print("Login Successful")

                return p


        print("Invalid Passenger ID or Password")

        return None