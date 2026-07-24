from B import P
class C(P):
    abc="Bye"
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks

obj=C("Kedar",20,90)
print(obj.xyz,obj.pqr,obj.abc)
print(obj.name,obj.age,obj.marks)