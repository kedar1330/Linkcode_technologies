class demo:
    #class_var
    ins="Hello"
    #class_method
    @classmethod
    def greet(cls):
        #print("hello good morning")
        return "Hi"
    @classmethod
    def modify(cls,new_val): #updates the class_var
        cls.ins=new_val
        

print(demo.greet())
print(demo.ins)
demo.modify("Linkcode")
print(demo.ins)
