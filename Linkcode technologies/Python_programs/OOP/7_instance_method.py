class demo:
    #instance_var
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    #instance_method
    def welcome(self):
        return "Hello students"
    #method for updating the name
    def modify(self):
        new_val=input("Enter new name:")
        ex_name=self.name
        self.name=new_val
        print(f"existing_value:{ex_name},updated value:{self.name}")


s1=demo("Ram",208,21)#manual inputs
print(s1.name,s1.id,s1.age) #calling using obj.var
print(s1.welcome()) #calling using the print function as the return keywoord is used
s1.modify() #direct call because no use of return keyword

