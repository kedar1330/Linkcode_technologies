from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class Ticket_services:
    pass
    def generate_ticket(self, booking, payment):
        pass
        if booking is None:
            print("No Booking Found")
            return

        if payment is None:
            print("Payment Not Completed")
            print("Ticket Cannot Be Generated")
            return

        file_name = "Ticket_" + str(booking.booking_id) + ".pdf"

        pdf = canvas.Canvas(file_name, pagesize=letter)
        pdf.setTitle("Airline Ticket")

        y = 750

        pdf.drawString(200, y, "AIRLINE RESERVATION SYSTEM")
        y -= 50

        pdf.drawString(50, y, "---------------- Ticket Details ----------------")
        y -= 40

        pdf.drawString(50, y, "Booking ID: " + str(booking.booking_id))
        y -= 30

        pdf.drawString(50, y, "Passenger ID: " + str(booking.passenger_id))
        y -= 30

        pdf.drawString(50, y, "Passenger Name: " + booking.passenger_name)
        y -= 30

        pdf.drawString(50, y, "Flight No: " + str(booking.flight_no))
        y -= 30

        pdf.drawString(50, y, "Source: " + booking.source)
        y -= 30

        pdf.drawString(50, y, "Destination: " + booking.destination)
        y -= 30

        pdf.drawString(50, y, "Seats Booked: " + str(booking.seats))
        y -= 30

        pdf.drawString(50, y, "Ticket Price: Rs. " + str(booking.price))
        y -= 30

        pdf.drawString(50, y, "Total Amount: Rs. " + str(booking.total_price))
        y -= 30

        pdf.drawString(50, y, "Payment Status: " + payment.status)
        y -= 50

        pdf.drawString(50, y, "Thank You For Choosing Our Airline")

        pdf.save()

        print("Ticket Generated Successfully")
        print("Ticket Saved As:", file_name)