#create
#file=open("myfile1.txt",'x')
#print(f"{file} created")

# to create file inside a specific folder
try:
 file = open("my_projects/myfile2.txt",'x')
 file.close()
 print("File created")
except FileExistsError:
   print("File already exist")
   
with open("my_projects/myfile2.txt",'w') as f:
    f.write("Hello World!")
    print("data inserted")

with open("my_projects/myfile2.txt",'r') as f:
    op=f.read()
    print(op)

#append --->a write()

with open("my_projects/myfile2.txt",'a') as f:
    f.write("How r u?","Data inserted")
    print("data inserted")

with open("my_projects/myfile2.txt",'r') as f:
    op=f.read()
    print(op)

