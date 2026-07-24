set1={12,35,8,25,5}
set2={25,6,35,15,8}
sets=set1|set2
for i in sets:
    if i%5==0:
        print(i)
        
print("sum of even no. for set 1")
x=[]        
for i in set1:
    if i%2==0:
        x.append(i)
print(sum(x))



print("sum of even no. for set 2")
y=[]
for i in set2:
    if i%2==0:
        y.append(i)
print(sum(y))

print("sum of even no. of set1 and set2 combined")
w=x+y
print(sum(w))

CE=set1.intersection(set2)
print(CE)
print(sum(CE))
a=sum(CE)
b=a*a
print(b)
print(b*b*b)

print("Non repeating elements and multiplaication of them")
Diff=set1.symmetric_difference(set2)
print(Diff)

mul=1
for i in Diff:
    mul*=i
print(mul)
    