class xyz:
    #public var
    x=90
    #private var
    __a=89

    def getA(self):
        return self.__a
    def abc(self):
        return "Public method"

    def __show(self):
        return "Private method"
    def call_show(self):
        return self.__show()
    def setvalue(self,new_val): #Pulic method accessing and updating private var (__a)
        self.__a=new_val
        print("Updated value")
        print(self.__a)



obj=xyz()
print(obj.x)
print(obj.getA())
print(obj.abc())
print(obj.call_show())
obj.setvalue(900)