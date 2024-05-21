vowelCounter = 0
yCounter = 0
vowels = ["a","e","i","o","u"]
print(type(vowelCounter))

phrase = input("Please put in a phrase and I'll count the vowels ")
for x in phrase:
    if(x in vowels):
        vowelCounter +=1
    elif(x == "y"):
        yCounter += 1
if(vowelCounter!=0):
    print(vowelCounter)
else:
    print(yCounter)


