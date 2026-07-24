#First type of error
print("Start")
try:
    print(10/2)
except ZeroDivisionError:
    print("Don't Divide by zero")

print("Program End")
print("-----------------------------------------------")
print("Start")
try:
    ip=int(input("Enter the no."))
    print(ip)
except ValueError as e: #here the entire msg is printed which is already in the system with the help of "as"
    print(e)
print("Program end")
print("-------------------------------------------------")
try:
    x=[1,2]
    print(x[9])
except IndexError:
    print("Please enter valid index")
print("program end")
print("---------------------------------------------------")
print("Start")
try:
    x=[10,20]
    print(x[1])
    print(10/0)
except IndexError as e:
    print(e)
except ZeroDivisionError:
    print("Dont divide by zero")
print("Program end")

#Handling multiple error and gvivng a generalized msg
print("Start")
try:
    ip=int(input("Enter the no."))
    print(10/ip)
except (ValueError,ZeroDivisionError):
    print("Something went wrong")
finally:
    print("I always get executed")
print("End")



class Ageerror(Exception):
   pass
print("start")
try:
 age=int(input("Enter the no."))
 if age>18:
    print("Eligible")
 else:
    raise Ageerror("Age should be greater than 18") #"raise" is used to create our own error and throw that error
except Ageerror:
    print("Age should be greater than 18")

print("===========")



