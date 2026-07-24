#sets 
#properties of sets
#unique data,unordered,mutable
#manual i/p
x={1,2}
print(x,type(x))

#user i/p
x=set()
x.add(10)
print(x,type(x))

#loop
x={10,20,30,40,10,20}
print(x)
for i in x:
    print(i)
#printing of val depends on the internal hashing in the compiler

#functions And methods
x.add(90)
print(x)

x.remove(40)#it will show error if no element is passed
print(x)

x.discard(7)#it will not show error if  element not present in the set
print(x)
x.discard(30)
print(x)

print(x.pop())

#returns empty set
x.clear()
print(x)

a={1,2}
b=a.copy()
print(b)

a.update([10,20,30])#used to add multiple elements in the set using list as arguement
print(a)

s={10,50,90}
print(len(s),min(s),max(s),sum(s))

#set operations
a={1,2,3}
b={3,4,5}
print(a)
print(b)

#entire table i.e union
print(a.union(b))
print(a|b)

#common elements Intersection
print(a.intersection(b))
print(a&b)

#data from table 1 i.e difference
print(a.difference(b))
print(a-b)

#data from table 1 and 2 ignoring intersection  i.e symmetric difference
print(a.symmetric_difference(b))
print(a^b)


