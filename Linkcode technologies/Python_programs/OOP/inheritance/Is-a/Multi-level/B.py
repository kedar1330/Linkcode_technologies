from A import Gp
class P(Gp):
    pqr="hey"
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
