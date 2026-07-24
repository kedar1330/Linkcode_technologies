class SBI:
    bank_name="SBI"
    IFSC_code="SBI00007"
    def __init__(self,name,adharno,bal):
        self.name=name
        self.adharno=adharno
        self.bal=bal

    def show_details(self):
        print(f"Name:{self.name},\nAdharno:{self.adharno},\nbalance:{self.bal},\nbank_name:{self.bank_name},\nIFSC_code:{self.IFSC_code}")

    def check_bal(self):
        print("Current balance",self.bal) 

    def deposit(self):
        ip=int(input("Enter how much amount you want to add:"))
        if ip>0:
            self.bal+=ip
            print("The deposited balance is:",ip) 
            print("Total balance is:",self.bal)  
        else:
            print("The amount should be greater than 0") 

    def withdraw(self):
        ip=int(input("Enter the amount you want to withdraw:"))
        if ip>self.bal:
            print("The amount you desired is greater then your bank balance")
        else:
            self.bal-=ip
            print("Withdrawed successfully")
        print("available balance is",self.bal)

    def fd(self):
        months=int(input("Enter how much months you want to do Fixed deposit:"))
        amount=float(input("Enter how much mount you want to do Fixed deposit:"))
        maturity=(amount*0.7)*months
        print("The value after your maturity of FD:",maturity )

    def compare(self):
        if user2.bal>user1.bal:
            print(f"User {user2.name} has more balance,{user2.show_details()}")
        if user2.bal<user1.bal:
            print(f"User {user1.name} has more balance,{user1.show_details()}")


user1=SBI("ram",4935686833315,0)
user2=SBI("Anuj",563241257854,0)
user1.show_details()
user1.check_bal()
user1.deposit()
user1.check_bal()
#user1.withdraw()
#user1.check_bal()
#user1.fd()
user2.show_details()
user2.check_bal()
user2.deposit()
user2.check_bal()
print(user1.compare())

