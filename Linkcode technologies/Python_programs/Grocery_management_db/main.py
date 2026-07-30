from operations import *
while True:
    print("""-------------Grocery Management System------------""")
    print("1.Add product\n2.Read all\n3.Search product\n4.Update product\n5.Delete product\n6.Add to cart\n7.View Bill")
    ch=int(input("Enter your choice:"))

    match ch:
        case 1:
            pass
            add_prod()
        case 2:
            pass
            view_all()
        case 3:
            pass
            search()
        case 4:
            pass
            update()
        case 5:
            pass
            delete_record()
        case 6:
            pass
            add_to_cart()
        case _:
            print("Invalid choice")          
