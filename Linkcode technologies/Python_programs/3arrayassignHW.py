x=[101,57,6,98,6,32,10,57,98]
ip=int(input("Enter the element you want to search:"))
if ip in x:
    print("Key found")
else:
    print("Not found")
#duplicate values   
for i in x:
    if x.count(i)>1:
        print(i," ")
        
print()
#unique values
for i in x:
    if x.count(i)==1:
        print(i," ")
print()

#sorting
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]

print("Sorted List:", x)
#Even Elements=0 and odd elements=1
print("Even Elements=0 and odd elements=1:")

for i in range(len(x)):
    if x[i]%2==0:
        x[i]=0
    else:
        x[i]=1
       
print(x)

