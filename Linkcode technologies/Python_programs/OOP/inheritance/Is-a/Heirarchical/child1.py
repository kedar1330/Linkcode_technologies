from parent import A
class B(A):
    def __init__(self):
        print("Def Cons B")
        super().__init__()
        
c1=B()
