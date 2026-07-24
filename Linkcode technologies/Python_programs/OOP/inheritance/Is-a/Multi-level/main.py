from BankAccount import BankAccount
from savingsacc import SavingsAcc
while True:
    print("WELCOME to Linkcode bank")
    print("1.User panel\n2Admin panel")
    ch=int(input("Enter your chice:"))
    if ch==1:
        while True:
            print("1.Create account\n2.Deposit\n3.Withdraw\n4.Check balance")
            choice=int(input("Enter your choice:"))
            match choice:
                case 1:
                    accno=int(input("Enter account number:"))
                    name=input("Enter account holder name:")
                    bal=float(input("Enter balance:"))
                    object=BankAccount(accno,name,bal)
                    print("Account created successfully")
                case 2:
                    object.Deposit()
                case 3:
                    object.withdraw()
                case 4:
                    print("Balance is:",object.get_balance())
                case _:
                    print("Invalid choice")

    if ch==2:
        pass
        while True:
            print("1.Create account\n2.calculate interest\n3.Apply interest\n4.Check balance\n5.Check benefits")
            ch=int(input("Enter your choice:"))
            match ch:
                case 1:
                    accno=int(input("Enter account number:"))
                    name=input("Enter account holder name:")
                    bal=float(input("Enter balance:"))
                    object=BankAccount(accno,name,bal)
                    print("Account created successfully")
                case 2:
                    object.calculate_interest()
                case 3:
                    object.apply_interest()
                case 4:
                    print("Balance is:",object.get_balance())
                case 5:
                    object.calculate_benefits()
                case _:
                    print("Invalid choice")
                