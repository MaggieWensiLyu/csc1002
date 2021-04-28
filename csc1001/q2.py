#to diaplay the numbers
def displays():
     for i in nums:
        print(i)

#to see whether it is positive
def positiveOrNot():
   if number1> 0:
       number2=number1
       return number2
   else:
      number1=0
      return number2


#to see whether it is integer
def integerOrNot():
    number= float(num)
    if number%1==0:   
       number1=number
       return number1
    else: 
       print('NOT AN INTEGER')
       number1=0
       return number1

    
#run the program
num= input("please input a number:")
number1=None
number2=None
integerOrNot()
positiveOrNot()
nums=[str(number2)]
displays()
