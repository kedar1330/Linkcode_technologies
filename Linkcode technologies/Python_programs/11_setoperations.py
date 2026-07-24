py_stud={"ram","sita","komal","ramu"}
jv_stud={"ram","pavan","gita"}
fd_stud={"gita","komal","payal","ram"}

#1.Total count of each
#2.name of students attending java and python
#3.Who are attending java python and fd
#4.only java students
#5.only py students
#6.name of students who are not attending java and pyhton
#7.count of student who attend 3 batch at a time
#8.name of students who attend only one batch at a time


print(len(py_stud),len(jv_stud),len(fd_stud))#1
print(py_stud.union(jv_stud))#2
print(py_stud|jv_stud|fd_stud)#3
print(jv_stud)#4
print(py_stud)#5
all_stud=py_stud|jv_stud|fd_stud
print(all_stud-(py_stud|jv_stud))#6
print(len(py_stud&jv_stud&fd_stud))#7

#8
for stud in all_stud:
    count=0
    if stud in py_stud:
        count+=1
    if stud in jv_stud:
        count=+1
    if stud in fd_stud:
        count+=1
    if count==1:
        print(stud)