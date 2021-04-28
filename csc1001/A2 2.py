def primeNum():
    primeNumber = [2]
    numbers = 3
    count = 1
    for numbers in range(3,1000) :        # first find a lot of prime numbers
        prime = True
        for i in range(2,numbers):
            if numbers % i == 0:
               prime = False
               break
        if prime == True:
         primeNumber.append(numbers)
    return primeNumber

def emirp(primeNumber):
   emirprime = [] 
   while len(emirprime) <= 100:                    # make sure the number of emprime is enough
     for k in primeNumber:
       l = str(k)
       m = l[ : : -1]
       if primeNumber.count(int(m)) >= 1 and l != m:       #make sure the reverse number is not itelf(like 11)
           emirprime.append(k)
   return emirprime


primeNumber = primeNum()
emirprime = emirp(primeNumber)
finalList = emirprime[:100]                    #pick 100 emprime
numEle = 0 
for ele in finalList:
    print("%4d"%ele, end ='')                 # align on right 
    numEle += 1
    if numEle % 10 == 0:                      #make sure 10 numbers in a line
        print(" ")

