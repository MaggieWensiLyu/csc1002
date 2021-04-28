#test whether it is an integer
i=input("please input an integer:")
count=0


#use append to add into a list if it is a prium number
try:
 i=float(i)
 testInt=i%1
 if testInt==0:
   i=int(i)
 else:
   i=0
#test whether it is a positive integer
 if i<=2:
     print("not positive integer greater than 2")
 priNums=list()
 for num in range (2,i):
#control when to add
    PrimeOrNot=True
#tast all the numbers smaller than itself
    for k in range (2,num):
      if num%k==0:
          PrimeOrNot= False
          break
    if PrimeOrNot==True:
       priNums.append(num)
 if i>=2:
  print("prime numbers smaller than",i, "include:")
 for n in range(0,len(priNums)) :
  print(priNums[count],end=" ")
#control when to change line
  count+=1
  if count%8==0:
     print(end="\n ")
except:
     print("error")
