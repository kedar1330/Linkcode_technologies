from models.booking import Booking
import random


class Booking_services:


    def __init__(self):

        self.booking_list = []

    def book_flight(self, flight_services, passenger):


        flight_no = int(input("Enter Flight ID: "))


        flight = flight_services.get_flight(flight_no)


        if flight is None:

            print("Flight Not Found")
            return None



        print("\nFlight Details")

        flight.display()



        seats = int(input("Enter Number of Seats: "))



        if seats > flight.available_seats:

            print("Seats Not Available")

            return None

        total_price = flight.price * seats



        print("Price per Seat:", flight.price)

        print("Total Price:", total_price)



        booking_id = random.randint(10000,99999)



        b = Booking(

            booking_id,

            passenger.passenger_id,

            passenger.name,

            flight.flight_no,

            flight.source,

            flight.destination,

            seats,

            flight.price,

            total_price

        )



        self.booking_list.append(b)



        # Update seats after booking

        flight.available_seats -= seats



        print("\nBooking Created Successfully")

        print("Your Booking ID:", booking_id)



        return b

    def cancel_booking(self, flight_services):


        if len(self.booking_list)==0:

            print("No Booking Available")

            return



        booking_id=int(input("Enter Booking ID: "))



        for b in self.booking_list:


            if b.booking_id == booking_id:



                self.booking_list.remove(b)
                flight_services.update_seats_after_cancel(

                    b.flight_no,

                    b.seats

                )



                print("Booking Cancelled Successfully")

                return



        print("Booking Not Found")
    def view_booking(self):


        if len(self.booking_list)==0:

            print("No Booking Available")

            return



        for b in self.booking_list:

            b.display()
    def get_booking(self, booking_id):


        for b in self.booking_list:


            if b.booking_id == booking_id:

                return b



        return None