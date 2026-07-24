from reportlab.pdfgen import canvas as cv
class Product:
    def __init__(self):
        self.products=[]
    def add_display_prod(self):
        n=int(input("ENter how many products you want to add:"))
        for i in range(n):
            print(f"\nEnter Details of Product {i+1}")
            name=input("Enter Product Name:")
            brand=input("Enter Brand:")
            mfg=input("Enter Mfg Date:")
            exp=input("Enter Expiry Date:")
            qty=int(input("Enter Qty:"))
            price=float(input("Enter Price:"))
            product={
                "Name":name,
                "Brand":brand,
                "MFG":mfg,
                "EXP":exp,
                "Quantity":qty,
                "Price":price
            }

            self.products.append(product)
        print("Total products in the system")

        for i in self.products:
            pass
            print("Name:",i["Name"])
            print("Brand:",i["Brand"])
            print("Manufacturing:",i["MFG"])
            print("Expiry:",i["EXP"])
            print("Quantity:",i["Quantity"])
            print("Price:",i["Price"])
            print("===========================================")
    
    def Search_product(self):
        print("HOw you want to like to search a product")
        print("1.Search by Brand\n2. Search by Product Name")
        ch=int(input("Enter your choice"))
        match ch:
            case 1:
                pass
                brand=input("Enter the brand name you wwant to search:")
                found=0
                for i in self.products:
                    if brand==i["Brand"]:
                        print("\n------ Product Found ------")
                        print("Name :",i["Name"])
                        print("Brand :",i["Brand"])
                        print("MFG :",i["MFG"])
                        print("EXP :",i["EXP"])
                        print("Quantity :",i["Quantity"])
                        print("Price :",i["Price"])

                        found=1
                if not found:
                    print("Product not found")

            case 2:
                pass
                print("Search by price")
                min_price=float(input("Enter Minimum Price: "))
                max_price=float(input("Enter Maximum Price: "))

                found=0
                for i in self.products:
                    if i["Price"]>=min_price and i["Price"]<=max_price:
                        print("\n-------Product Found-------------")
                        print("Name:",i["Name"])
                        print("brand",i["Brand"])
                        print("MFG:",i["MFG"])
                        print("EXP:",i["EXP"])
                        print("Quantity:",i["Quantity"])
                        print("Price:",i["Price"])
                        found=1
                if not found:
                    print("Products are not present at that price range")

    
    def purchase_product(self):
        print("\n------ Available Products ------")

        for p in self.products:
            print("Name :", p["Name"])
            print("Brand :", p["Brand"])
            print("Quantity :", p["Quantity"])
            print("Price :", p["Price"])
            print("----------------------------")
        product_name = input("\nEnter Product Name to Purchase: ")
        found = 0
        for p in self.products:
            if p["Name"]==product_name:
                found=1

                qty=int(input("Enter Quantity you want to Purchase: "))
                if qty<=p["Quantity"]:
                    total=qty * p["Price"]

                    print("\n--------- BILL ---------")
                    print("Product Name :", p["Name"])
                    print("Brand :", p["Brand"])
                    print("Price :", p["Price"])
                    print("Purchased Quantity :", qty)
                    print("Total Amount :", total)
                    p["Quantity"] = p["Quantity"] - qty
                    self.name = p["Name"]
                    self.brand = p["Brand"]
                    self.qty = qty
                    self.price = p["Price"]
                    self.total = total

                    print("\nPurchase Successful!")
                    print("Remaining Stock :", p["Quantity"])
                else:
                    print("Insufficient Stock!")
                    break

        if not found:
            print("Product not found.")

    


    def pdf(self):
        if not hasattr(self, "name"):
            print("Please purchase a product first.")
            return
        pdf=cv.Canvas("Bill.pdf")

        pdf.setFont("Helvetica-Bold",16)
        pdf.drawString(180,800,"PRODUCT BILL LELE")
        pdf.setFont("Helvetica",12)
        pdf.drawString(50,760,f"Product Name:{self.name}")
        pdf.drawString(50,740,f"Brand:{self.brand}")
        pdf.drawString(50,720,f"Quantity:{self.qty}")
        pdf.drawString(50,700,f"Price:{self.price}")
        pdf.drawString(50,680,f"Total Amount:{self.total}")
        pdf.save()
        print("Bill PDF Generated Successfully!")
        
obj=Product()
        
while True:
    print("\n Product Management System")
    print("\n1.Add and display details\n2.Search products\n3.Purchase the product and generate the bill\n4.Download the bill in pdf\n5.Send the bill via email")
    ch=int(input("Enter your choice:"))
    
    match ch:
        case 1:
            obj.add_display_prod()
        case 2:
            obj.Search_product()
        case 3:
            obj.purchase_product()
        case 4:
            obj.pdf()
        case 5:
            pass
        case _:
            print("Thankyouu")
