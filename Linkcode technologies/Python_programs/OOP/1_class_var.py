class demo:
    def __init__(self):
       print("demo constructor called")

#objname=cn()
obj=demo()

#class variable
class demo1:
    ins_name="Linkcode"

#variable calling without using object classname.varname
print(demo1.ins_name)

#variable calling using object objrefvar.varname
obj1=demo1()
print(obj1.ins_name)





