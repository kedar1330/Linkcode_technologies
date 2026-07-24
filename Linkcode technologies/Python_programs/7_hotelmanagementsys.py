#Hotel management system
menu=((1, "paneer", 400),
(2, "chicken", 600),
(3, "Dessert", 150),
(4, "Noodles", 200))

while True:
    print("1.view\n2.order\n3.Generate Bill\n4.exit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            print("---Hotel Menu Card---")
            for items in menu:
                print(f"{items[1]}--->{items[2]}")
        case 2:
            print("Order your food items:")
            Ord=[]
            while True:
                ip=int(input("Enter the items id you want to add:"))
                for i in menu:
                    if ip==i[0]:
                        print("Price is:",i[2])
                        qty=int(input("Enter the total no. of quantity:"))
                        total=qty*i[2]
                        print("SUBTotal price is",total)
                        Ord.append([i[1],qty,total])
                        print("Current order is:",Ord)
                print("\nDo you want to add more items?")
                print("1. Yes")
                print("2. No")
                ch=int(input("Enter your choice:"))
                if ch==2:
                    break;
            print("\nFinal Order:")
            print(Ord)

        case 3:
            print("--------Generated Bill-----------")

            print("Items Ordered:")
            print(Ord)

            bill = 0

            for i in Ord:
                bill = bill + i[2]    

            GST = 25

            print("Food Total:", bill)
            print("GST is:", GST)
            print("Total Bill is:", bill + GST)
        case 4:
            print("Thankyou visit again!")
            break;
        case _:
            print("invalid choice")