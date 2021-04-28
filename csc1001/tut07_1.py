numDict = {}
numbers =  input("please input some integers:")
numList = numbers.split()
for i in numList:
    if i in numDict:
        numDict[i] = numDict + 1
    elif i == "finish":
        break
    else :
        numDict[i] =  1

for numbers in numDict:
    if numDict[i] == 1:
        print(numbers,"occurs", numDict[i], "time" )
    else:
        print(numbers, "ouucurs", numDict[numbers],"times")