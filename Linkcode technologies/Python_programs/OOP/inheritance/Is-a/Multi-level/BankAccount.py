class BankAccount:
    def __init__(self,AccountNo,Accholder,Bal):
        self.AccountNo=AccountNo
        self.Accholder=Accholder
        self.Bal=Bal
    
    def Deposit(self):
        Amt=int(input("Enter the amount to deposit:"))
        self.Bal+=Amt
        print("Ammount Deposited Successfully")
        print("Current balance:",self.Bal)

    def withdraw(self):
        Amount=int(input("Enter the amount to be withdrawn:"))
        self.Bal-=Amount
        print(Amount,"Withdrawn Successfully")
        

    def get_balance(self):
        print("Remaining Balance:",self.Bal )
