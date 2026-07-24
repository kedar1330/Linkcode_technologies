from parent import p
class c(p):
    pass
    #method override
    def sound(self):
        print("Child sound")

    def abc(self):
        print("Child ABC")

    def add(self,a,b,c): #method overloading is not possible in Python
        return a+b+c
    
    def add_parent(self,a,b,):
        return super().add(a,b)
    
    