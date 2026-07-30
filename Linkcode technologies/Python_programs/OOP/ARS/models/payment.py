class Payment:

    def __init__(self, payment_id, booking_id, payment_method, amount):

        self.payment_id = payment_id
        self.booking_id = booking_id
        self.payment_method = payment_method
        self.amount = amount
        self.status = "Pending"


    def display(self):

        print("-" * 50)
        print("------------- Payment Details -------------")

        print("Payment ID:", self.payment_id)
        print("Booking ID:", self.booking_id)
        print("Payment Method:", self.payment_method)
        print("Amount:", self.amount)
        print("Payment Status:", self.status)

        print("-" * 50)