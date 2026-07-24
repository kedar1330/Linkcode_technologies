#nested list
x=[[10,20],
   [11.80,12.78],"hi",90]
print(x)
print(x[1])
print(x[1][1])
for i in x:
    if type(i)==list:
        for j in i:
            print(j)
        continue
    print(i)
    
y=[[10,20],[11.2,12.3],[40,62]]
for i in y:
    print(i[0])
    print(i[1])
            
#student management system
stud=[[101,"ram",98],[102,"sita",88],[103,"ramu",78],[104,"gita",99]]
for i in stud:
    print(i[1],"-",i[2])
    
id=int(input("enter the id you want to add:"))
name=input("enter the name:")
marks=float(input("enter marks:"))
data=[id,name,marks]
stud.append(data)   
print(stud)




