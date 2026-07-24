def operation():
 while True:
    result=0
    print("Calculator")
    print("1.add(+)\n2.sub(-)\n3.multiply(*)\n4.Division(/)")
    num1=int(input("Enter the 1st no."))
    result=num1
    while True:
        operator=input("enter the operator:")
        if operator=="=": 
            print("Result is",result)
            break
        num2=int(input("enter the next no."))
        if operator=="+":
            result+=num2
        elif operator=="-":
            result-=num2
        elif operator=="*":
            result*=num2
        elif operator=="/":
            if num2==0:
                print("Can't divide by 0!")
            else:
                result/=num2
        else:
            print("Invalid choice!")
 
    
    
    
operation()