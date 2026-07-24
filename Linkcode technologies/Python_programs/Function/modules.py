
import math

print(math.sqrt(16))  # Output: 4.0
print(math.factorial(5))  # Output: 120
print(math.ceil(45.29))   # Output: 46
print(math.floor(45.29))  # Output: 45
print(math.pow(2, 3))     # Output: 8.0
print(math.pi)

calc=2*math.pi*2
print(calc)

import random as rd

print(rd.randint(1000, 9999))  # Output: Random integer between 1000 and 9999
print(rd.random())
print(rd.randrange(2, 10, 2))  # Output: Random integer between 2 and 10 (step 2) even nos
print(rd.randrange(1,10,2)) #output : Random integer between 1 and 10 (step 2) odd nos
print(rd.choice(['apple', 'banana', 'cherry']))  # Output: Random choice from the list
x=["hello","hi","bye"]
for i in x:
    print(rd.choice(x))  # Output: Random choice from the list x

print(rd.choices(x, k=2))  # Output: Random choice from the list x
rd.shuffle(x)
print(x)

import datetime as dt
d=dt.datetime.now()
print(d)

print(d.time())
print(d.day)
print(d.month)
print(d.year)

#today date
today=dt.date.today()
print(today)

#after days
after=today+dt.timedelta(days=5)
print(after)

dob=dt.date(2006, 1, 13)
print(dob)
cr=dt.date.today()
print(cr)

print(cr-dob)
print(cr.year - dob.year)
a=input("Enter the first name:")
b=input("Enter the second name:")
ram=input(f"{a},Enter your date of birth in YYYY-MM-DD format: ")
ram_dob=dt.datetime.strptime(ram, "%Y-%m-%d").date()
sita=input(f"{b},Enter your date of birth in YYYY-MM-DD format: ")
sita_dob=dt.datetime.strptime(sita, "%Y-%m-%d").date()
if ram_dob<sita_dob:
    print(f"{a} is older than {b}")
else:
    print(f"{b} is older than {a}")


