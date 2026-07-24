#tuple
from platform import system


x=(10,20,30)
print(x,type(x))
print(x[1])
for i in x:
    print(i)
    
x=("red","blue","black")
print("red in x")
print("green in x")

x=(10,20)
y=(10,20)
z=x
print( x is y)
print(x is z)


#packing and unpacking
x=(10,20,30)
a,b,c=x
print(a,b,c)
#method and function in tuple
print(x.count(20))
print(x.index(30))
#tuple slicing
print(x[1:])
print(x[1:2])
print(x[:3])
#nested tuple
x=((10,20),(30,40),)
print(x[1][0])

#printing all elements in the tuple
for i in x:
    for j in i:
        print(j)

x=((10,20),30,(40,50),"hi")
for i in x:
    if type(i)==tuple:
        for j in i:
            print(j)
        continue
    print(i)
    
#Nested list and tuple mix
x=[10,[20,30],40,(50,60)]
print(x[2])
print(x[3][0])

for i in x:
    if type(i)==list or type(i)==tuple:
        for j in i:
            print(j)
        continue
    print(i)

x=(90,"hi",("red",[10,20]),[100,200])
for i in x:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==list:
                for k in j:
                    print(k)
                continue
            print(j)
        continue
    print(i)
#tuple to list and list to tuple
x=(10,20)
print(x,type(x))
y=list(x)
y.append(90)
print(y,type(y))
x=tuple(y)
print(x,type(x))
