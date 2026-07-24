from BankAccount import BankAccount
class SavingsAcc(BankAccount):
    pass
    def __init__(self,AccountNo,Accholder,Bal):
        pass
        super().__init__(AccountNo,Accholder,Bal)
        self.interest=0.05
        

    def calculate_interest(self):
        P_amt=float(input("Enter the principal amount:"))
        month=float(input("Enter the time in months:"))
        Simple_interest=(P_amt*self.interest*month)/(100*12)
        return f"Simple interest is:{Simple_interest}"

    def apply_interest(self):
        self.Bal+=self.Simple_interest
        return f"Balance after applying interest is:{self.Bal}"
    
