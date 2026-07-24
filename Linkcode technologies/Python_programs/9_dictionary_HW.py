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
while True:
    print("1.Add student\n2.View total marks/percentage\n3.view topper and student with lowest marks")
    ch=int(input("Enter your choice:"))
    match ch:
        case 1:
            id=int(input("Enter the id no.:"))
            if id in student:
                print("ID alreday exist")
            else:
                name=input("Enter name:")
                age=int(input("Enter the age:"))
                
                sub=[]
                for i in range(3):
                    subject=input(f"enter subject {i+1}:")
                    sub.append(subject)
                    
                marks=[]
                for i in range(3):
                    mark=int(input(f"enter the subject{i+1} marks:"))
                    marks.append(mark)
                    
                student[id]={
                    "Name":name,
                    "age":age,
                    "sub":sub,
                    "marks":tuple(marks)
                }
                    
            print(student)
        case 2:
            print("Total marks and percentage of each student")
            for key,details in student.items():
                total=sum(details["marks"])
                percentage=(total/300)*100
                print("Student ID:",key)
                print("name:",details["Name"])
                print("Age:",details["age"])
                print("total marks:",total)
                print("overall percentage:",percentage)
                print("====================================================")
        case 3:
            print("Topper for each subject and lower for each subject")
            pass
