#functions in python
#userdefined-1.no return type no arguement,2.no return type with arguement
#1.no return type no arguement
def greet():
    print("welcome user!")
    
greet() #function call--->fun_name()
greet()

#2.no return type with arguement
def greet1(name):
    print("Welcome",name)
name=input("Enter your name:")   
greet1(name)

#3.with return type no arguement
#two ways of function call using 1.store the function call in var and 2. using calling the function in the print statement 
def get_no():
    return 10**2
    
print(get_no())#1st way
var=get_no() #2nd way
print(var)
var+=2
print(var)

#4.With return type with argguement
def cube(num):
    return num**3
num=int(input("Enter a no."))    
var=cube(num) #1st way
print("Cube is",var)

print("cube is",cube(num)) #2nd way

def add(a,b):
    print(a+b)

add(2,5)

# arbitary arguements - *args  --->it can store multiple(infinite) arguements
#*args Therefore, no need to use positional arguements
def add1(*args):
    print("Sum of all no. is",sum(args))
    print(type(args))
    
add1(2,5,7,9,7,6,5,5)

def info(name,age,marks):
    return f"Your name is:{name},age is {age}, marks is {marks}"
name=input("enter your name:")
age=int(input("Enter your age: "))
marks=float(input("Enter your marks:"))
print(info(name,age,marks))
