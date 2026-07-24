import random as r
import time as t
class userlogin:
    def __init__(self):
        self.mobno=" "
        self.__otp=None
        self.__attempts=0

    def check_attempts(self):
        if self.__attempts<3:
            self.check_login()

    def check_login(self):
        self.mobno=input("Enter your mobile no.")
        if len(self.mobno)==10 and self.mobno.isdigit():
            self.__otp=r.randint(1000,9999)
            print("Your otp is:",self.__otp)
            self.send_time=t.time()
            print(self.send_time)

        

            self.user_otp=int(input("Enter the otpfor validation:"))
            self.rec_time=t.time()
            print(self.rec_time)
            if self.rec_time-self.send_time>1:
                print("OTP expired")
                
                print("Do you want to resend the OTP(Y/N)")
                ch=input("Enter your choice:")
                if ch=="Y":
                    pass
                    self.check_login()
                if ch=="N":
                    print("Okay thankyou Visit again!")
                    return

            if self.user_otp==self.__otp:
                print("welcome user!")
                return
            else:
                print("Otp does not match")
                self.__attempts+=1
                print(3-self.__attempts,"Left!")
                if self.__attempts==3:
                    print("Attempt reached! Try again after some time")
                    return
                self.check_attempts()
        else:
            print("Please enter correct mobile no.")

obj=userlogin()
obj.check_login()
