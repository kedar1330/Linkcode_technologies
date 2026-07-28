class user:
    pass

    def __init__(self, user_id, name, age, gender, mobile, username, password):
        pass
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.username = username
        self.password = password

    def display(self):
        print("-" * 50)
        print("--------------- USER DETAILS ----------------")
        print("User ID   :", self.user_id)
        print("Name      :", self.name)
        print("Age       :", self.age)
        print("Gender    :", self.gender)
        print("Mobile No :", self.mobile)
        print("Username  :", self.username)
        print("-" * 50)