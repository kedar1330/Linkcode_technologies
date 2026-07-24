def add(a,b):
    print("Addition is:",a+b)
    
def sub(a,b):
    print("Subtraction is:",a-b)
    
def mul(a,b):
    print("multiplication is:",a*b)
    
def div(a,b):
    print("division is",a/b)
    



print("1.add\n2.sub\n3.multiply\n4.Division")    
ip=int(input("Enter your choice:"))
a=int(input("Enter first no."))
b=int(input("Enter 2nd no."))

match ip:
    case 1:
        add(a,b)
    case 2:
        sub(a,b)
    case 3:
        mul(a,b)
    case 4:
        div(a,b)

        
        
    