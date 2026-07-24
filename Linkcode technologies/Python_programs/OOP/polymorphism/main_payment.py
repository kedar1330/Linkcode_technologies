from payment_gateway import payment_gateway
from UPI import UPI
from card import card

pg=payment_gateway()
ip=int(input("payment:1.upi,2.card,3.exit\nEnter your choice:"))
if ip==1:
    pg.payment_process(UPI())
elif ip==2:
    pg.payment_process(card())
else:
    print("brfiuber")

    

       