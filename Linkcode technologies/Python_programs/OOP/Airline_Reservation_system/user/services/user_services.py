from user.models.user_model import user


class user_services:
    pass

    def __init__(self):
        self.user_list = []

    def register(self):
        user_id = int(input("Enter User ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        mobile = input("Enter Mobile Number: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        u = user(user_id, name, age, gender, mobile, username, password)
        self.user_list.append(u)

        print("Registration Successful")

    def login(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        for u in self.user_list:
            if u.username == username and u.password == password:
                print("Login Successful")
                return True

        print("Invalid Username or Password")
        return False

    def logout(self):
        print("Logged Out Successfully")