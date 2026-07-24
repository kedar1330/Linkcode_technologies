# Strings and List in python
x=[10,20,30]
print(x)
for items in x:
    print(items)
    
x.append(90) #append opertaion
print(x)
x.insert(1,12) #insert operation
print(x)


#taking input from the user and printing the list
a=[] 
print(a)
for i in range(5):
    ip=input(f"enter {i+1} element:")
    a.append(ip)
print(a)

#remove(element)/pop(index)
x=[10,8,9,"Hi",90,89]
print(x)
x.remove(9)
x.pop()
print(x[2])

#nested list
