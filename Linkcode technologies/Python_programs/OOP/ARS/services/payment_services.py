from models.payment import Payment
import random


class Payment_services:


    def __init__(self):

        self.payment_list = []



    def make_payment(self, booking):


        if booking is None:

            print("No Booking Available")

            return False



        print("\n" + "=" * 50)
        print("              PAYMENT OPTIONS")
        print("=" * 50)


        print("1. Card Payment")
        print("2. UPI Payment")
        print("3. Net Banking")


        choice = int(input("Select Payment Method: "))



        payment_method = ""



        if choice == 1:


            payment_method = "Card"


            print("\nEnter Card Details")

            card_no = input("Enter Card Number: ")

            expiry = input("Enter Expiry Date: ")

            cvv = input("Enter CVV: ")


            print("Card Details Submitted")



        elif choice == 2:


            payment_method = "UPI"


            print("\nEnter UPI Details")

            upi_id = input("Enter UPI ID: ")


            print("UPI Details Submitted")



        elif choice == 3:


            payment_method = "Net Banking"


            print("\nEnter Net Banking Details")


            bank_name = input("Enter Bank Name: ")

            username = input("Enter Username: ")

            password = input("Enter Password: ")


            print("Net Banking Details Submitted")



        else:

            print("Invalid Payment Option")

            return False




        print("\nAmount to Pay:", booking.total_price)



        confirm = input(
            "Proceed to Pay? (yes/no): "
        )



        if confirm.lower() == "yes":


            payment_id = random.randint(10000,99999)



            p = Payment(

                payment_id,

                booking.booking_id,

                payment_method,

                booking.total_price

            )


            p.status = "Successful"


            self.payment_list.append(p)



            print("\nPayment Successful")

            print("Payment ID:", payment_id)



            return True



        else:


            print("\nPayment Cancelled")

            print("Ticket will not be generated")


            return False





    def view_payment(self):


        if len(self.payment_list)==0:

            print("No Payments Available")

            return



        for p in self.payment_list:

            p.display()