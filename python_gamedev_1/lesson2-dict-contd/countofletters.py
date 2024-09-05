inputStr = input("Enter the string - ")
charCount = {}

for c in inputStr:
    if c.isalpha():
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1 
            #in ref code it will be given as charCount =1 , you need to correct it
            
print(charCount)