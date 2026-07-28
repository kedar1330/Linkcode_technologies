from reportlab.pdfgen import canvas
import os


class ticket_services:

    def __init__(self, booking_service):
        self.booking_service = booking_service

    def generate_ticket_pdf(self):

        booking_id = int(input("Enter Booking ID: "))

        for b in self.booking_service.booking_list:

            if b.booking_id == booking_id:

                os.makedirs("tickets", exist_ok=True)

                filename = f"tickets/Ticket_{booking_id}.pdf"

                c = canvas.Canvas(filename)

                c.setFont("Helvetica-Bold", 18)
                c.drawString(150, 800, "AIRLINE RESERVATION TICKET")

                c.setFont("Helvetica", 12)

                y = 760

                c.drawString(50, y, f"Booking ID : {b.booking_id}")
                y -= 25

                c.drawString(50, y, f"Passenger Name : {b.passenger_name}")
                y -= 25

                c.drawString(50, y, f"Flight Number : {b.flight_no}")
                y -= 25

                c.drawString(50, y, f"Source : {b.source}")
                y -= 25

                c.drawString(50, y, f"Destination : {b.destination}")
                y -= 25

                c.drawString(50, y, f"Seat Number : {b.seat_no}")
                y -= 25

                c.drawString(50, y, f"Price : ₹{b.price}")
                y -= 40

                c.drawString(50, y, "Thank You For Choosing Our Airline!")

                c.save()

                print("Ticket Generated Successfully")
                print("Saved As :", filename)

                return

        print("Booking Not Found")