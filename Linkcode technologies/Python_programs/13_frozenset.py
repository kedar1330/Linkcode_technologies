#frozen set
x=frozenset([1,2])
print(x,type(x))
roles=frozenset(["admin","faculty","receptionist"])
for i in roles:
    if i=="admin":
        print(i)
        
#roles.add("hacker") will give error as frozen set is immutable