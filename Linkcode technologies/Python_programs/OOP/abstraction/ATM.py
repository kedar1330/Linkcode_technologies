from abc import ABC,abstractmethod
class ATM(ABC):
    def __init__(self,bal):
        self.bal=bal

    def getbal(self):
        return self.bal
    
    @abstractmethod
    def withdraw(self,amount):
        pass
    