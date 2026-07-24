from A import A
class B(A):
    def abc(self):
        print("hello abc")
    def __init__(self):
        print("constructor of class B")


obj=B()
print("roll no is:",obj.roll_no)
obj.abc()
obj.xyz()

print(B.mro()) #method resolution order (mro) --> it will show the order of method calling in case of multiple inheritance
