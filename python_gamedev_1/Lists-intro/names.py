
name=["name1","name2","name3","name4"]
choice=0
while choice!=5:
  print("select a choice :\n1. Add name in a list\n2 Delete name from the list\n3. Replace a name in the list\n4. View all name\n5. Press any other number to exit\n")
  choice=int(input())

  if choice==1:
    newname=input("Enter the name you want to add: \n")
    name.append(newname)
    print("Added successfully...\n")
  elif choice==2:
    newname=input("Enter the name you want to delete from the list:\n")
    if newname in name:
      name.remove(newname)
      print("Removed Successfully...\n")
    else:
      print("Invalid name\n")
      
  elif choice==3:
    replacename=input("Enter the name to replace from the list:\n")
    newname=input("Enter the new name:\n")
    if replacename not in name:
      print("Invalid name\n")
    else:
      index=name.index(replacename)
      name[index]=newname
      print("Replaced Successfully...\n")
  elif choice==4:
    print(name)
  else:
    print("Invalid option")
  