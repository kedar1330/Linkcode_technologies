from savingsacc import SavingsAcc
class PremiumSaving(SavingsAcc):
    def __init__(self,AccountNo,Accholder,Bal):
        super().__init__(AccountNo,Accholder,Bal)
        
    def calculate_benefits(self):
        if self.Bal>5000:
            benefits=500
            ch=input("Dou you want to add these benefit ampunt tp your account balance?(y/n)")
            if ch=="y":
                self.Bal+=benefits
                print("Benefits added",benefits)
                print("Balance after adding benefits:",self.Bal)
            else:
                print("okay you can claim it afterwards")
        else:
            print("You are not eligible for benefits balance should be more than 5000")

    
obj=PremiumSaving(123,"kedar",10000)
obj.calculate_benefits()



    