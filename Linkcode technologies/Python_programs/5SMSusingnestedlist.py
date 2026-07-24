stud=[[101,"ram",98],[102,"sita",88],[103,"ramu",78],[104,"gita",99]]
while True:
    print("Student management system\n1.add\n2.view\n3.update\n4.delete\n5.Topper\n6.exit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            ip=int(input("How many students you want to add:\n"))
            for i in range(ip):
                id=int(input("Enter Id"))
                name=input("Enter name:")
                marks=int(input("Enter marks:"))
                stud.append([id,name,marks])
                print(f"Student {i+1} added")
        case 2:
            for i in stud:
                print(i)
        case 3:
            sid=int(input("Enter your id:"))
            for i in stud:
                if sid==i[0]:
                    print("1.update marks\n2.update name\n3.update All\n4.exit")
                    choice=int(input("Enter your choice:\n"))
                    if choice==1:
                        new_marks=int(input("Enter new marks to update:"))
                        i[2]=new_marks
                        print(f"Updated {i[0]} id to {new_marks} marks!")
                    if choice==2:
                        new_name=input("Enter new name:")
                        i[1]=new_name
                        print(f"Updated {i[0]} id to {new_name} name!")
                    if choice==3:
                        new_marks=int(input("Enter new marks to update:"))
                        i[2]=new_marks
                        new_name=input("Enter new name:")
                        i[1]=new_name
                        print(f"Updated to {i[0]} to {new_name} name and {new_marks} marks!")
                        
        case 4:
            sid=int(input("Enter the id you want to delete:\n"))
            for i in stud:
               if sid==i[0]:
                    stud.remove(i)
                    print("Id deleted successfully")
                    print(stud)
        case 5:
            pass
        case 6:
            exit()
        