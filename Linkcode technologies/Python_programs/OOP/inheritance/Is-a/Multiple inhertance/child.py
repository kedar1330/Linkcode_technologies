from parent1 import p1
from parent2 import p2

class child(p1,p2):
    def __init__(self,p1name,p2name,c_name):
        self.c_name = c_name
        #classname.__init__(self,parameter)  #calling parent class constructor
        #super().__init__(parameter)  #calling parent class constructor will not work in multiple inheritance
        p1.__init__(self,p1name)
        p2.__init__(self,p2name)


obj=child("John","Alice","Kedar")
print(obj.p1name) #p1 name printing
print(obj.p2name) #p2 name printing
print(obj.c_name) #c_name printing


