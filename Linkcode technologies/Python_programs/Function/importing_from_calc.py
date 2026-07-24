# call entire function from that module(calc)i.e file name is calc.py

import calc
print(calc.add(10, 5))  
print(calc.sub(10, 5))  

#call specific functions from that module i.e add and sub
from calc import add, sub
print(add(20, 10))  
print(sub(20, 10))  

