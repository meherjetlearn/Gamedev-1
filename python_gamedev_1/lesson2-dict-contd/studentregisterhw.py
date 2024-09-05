studentregister={}

while True:
    choice = input("Do you want to add student details? type y/n")
    if(choice =="y"):
        s=int(input("enter student id"))
        studentregister[s]={}

        a=input("enter age")
        studentregister[s]["age"]=a

        name=input("enter the student name")
        studentregister[s]["name"]=name
        

        marks=int(input("enter total marks"))
        studentregister[s]["marks"]=marks
        print(studentregister)
    elif(choice=="n"):
        break
    
find=int(input("enter the studentid to find the total marks"))
result = studentregister.get(find, {}).get('marks')
print(f' total marks of student id{find} = {result}')


    



