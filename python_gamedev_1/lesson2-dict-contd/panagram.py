numberAsString = input("Enter the number - ")

numCount = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "0":0
    }
    
for num in numberAsString:
    if num in numCount:
        numCount[num] += 1
 
panagram = True
for count in numCount.values():
    if count == 0:
        panagram = False

if panagram:
    print("Entered number is a Panagram")
else:
    print("Entered number is not a Panagram")