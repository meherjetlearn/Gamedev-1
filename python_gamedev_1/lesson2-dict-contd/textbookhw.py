textbook={"maths":100,
          "english":200,
          "physics":300,
          "chemistry":500,
          "cse":800}
print(textbook)

#update physics book cost to 400
textbook["physics"]=400
print("\nupdated dictionary")
print(textbook)

#add cost of 2 more books
textbook["python"]=100
textbook["javascript"]=200
print("\added 2 new books dictionary")
print(textbook)

#print the cost of the book given by user
inp=input("enter the book name to find the cost")
result=textbook[inp]
print(f'the cost of {inp} books is : {result}')