def isValid(sums, sum2):
    if (sums + sum2) % 10 == 0:
        print("is valid")
    else:
        print("is not valid") 

def sumOfDoubleEvenPlace(sumOfTwo):
    count = 0
    sum2 = 0
    while count < len(sumOfTwo)+1:
     if count % 2 != 0:                             #make it is in odd position
        sum2 += sumOfTwo[count]
     count += 1
    return sum2

def getDigit(number):
    sumOfTwo = []
    numList1 = list(number)
    numList1 = numList1[: :-1]                     #first reverse the list, then from right to left switch to left to right
    count = 0
    for num in numList1:
     if count % 2 != 0:
        num1 = int(num)
        num2 = 2 * num1
        if num2 > 9:
            num3 = str(num2)                       #make it to a string  to add the two numbers
            num2 =int(num3[0])+int(num3[1]) 
        sumOfTwo.append(num2)
        count += 1
     elif count % 2 == 0 :                         # numbers on the odd place should be  itself
        sumOfTwo.append(int(num)) 
        count += 1
    return sumOfTwo

def sumofOddPlace(sumOfTwo):
    count = 0 
    sums = 0
    for i in sumOfTwo:
        if count % 2 == 0:                     # sum then odd place
           sums += i
        count += 1
    return sums

while True:
    number = input("please input your card:")
    k = 1
    if number.find('4') == 0 or number.find('5') == 0 or number.find('6') == 0 or number[0:2] == "37":   # make sure it begins with the right number
        k= 0
    if number.isdigit() == True and k == 0 and len(number) >= 13 and len(number) <= 16: #make sure the lengh is valid 
        break

sumOfTwo = getDigit(number) 
sums = sumofOddPlace(sumOfTwo)
sum2 = sumOfDoubleEvenPlace(sumOfTwo)
isValid(sums,sum2)