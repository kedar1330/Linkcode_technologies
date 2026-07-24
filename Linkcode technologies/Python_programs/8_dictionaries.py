#dictionaries in python4
x={}
print(x,type(x))
#add -->refvar[key]=value
x["rollno"]=101
x["name"]="Ram"
print(x)

#access-->x[key]--->value
print(x["name"])
#update--->ref[key]=new_val
x["name"]="Sita"
print(x["name"])

Stud={
    "Rollno":101,
    "Name":"ram",
    "age":20,
    "sub":["eng","maths","Science"],
    "marks":(90,89,67)
}

print(Stud)

#methods in dictionaries
print(Stud.keys())
print(Stud.values())
print(Stud.items())

#loop
for key in Stud: #by default it will call keys only
    print(key)
    
#for values
for values in Stud.values():
    print(values)
    
#for items
for k,v in Stud.items():
    print(k,v)

for v in Stud["sub"]:
    print(v)
    
for i in Stud.keys():
    if "sub"==list:
        for j in "sub":
            print(j)
            
#sub:Marks
for i in range(len(Stud["sub"])):#3
    print(f"{Stud["sub"][i]}:{Stud["marks"][i]}")
    
#zip() function- simplifies the above operation of #sub:Marks
for sv,mv in zip(Stud["sub"],Stud["marks"]):
    print(sv,mv)


#nested dictionaries
student={
    1:{
         "Name":"ram",
         "age":20,
         "sub":["eng","maths","Science"],
         "marks":(90,89,67)
    },
    2:{
         "Name":"sita",
         "age":23,
         "sub":["eng","maths","Science"],
         "marks":(99,80,76)
    },
    3:{
         "Name":"sham",
         "age":22,
         "sub":["eng","maths","Science"],
         "marks":(91,83,64)
    }
}    

print(student[2])  
print(student[2]["Name"])
print(student[1]["sub"][2])

for key in student:
    for v in student[key]["marks"]:
        print(v,end=' ')
    print()
#generate the student ids and their informations    
for key in student:
    print(f"Student Id :{key}:{student[key]}")
    print("===============================================================================")
    
#another example of above problem
for key,details in student.items():
    print("Student Id:",key)
    for k,v in details.items():
        print(f"{k}:{v}")
    print("-----------------------------------------------")
    



       
