numbers =  input("please entr 10 numbers:")
numberList = numbers.split()
num = []

for number in numberList:
    if number.find(number) == -1:
        num.append(number)
    else:
        continue

print(num)