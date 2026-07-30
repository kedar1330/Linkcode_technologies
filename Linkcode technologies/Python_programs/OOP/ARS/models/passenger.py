class Passenger:

    def __init__(self, passenger_id, name, age, gender, email, phone, password):

        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone = phone
        self.password = password


    def display(self):

        print("-" * 50)
        print("------------- Passenger Details -------------")
        print("Passenger ID:", self.passenger_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("-" * 50)