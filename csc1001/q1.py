finalValue = input("please input your final value:")
annualRate = input("please input the annual intrest rate:")
numberOfYear = input("please input the number of years:")
#to input the values
def findOutYears(annualRate1=0,numberOfYear1=0,finalValue1=0):
   increaseAmount= (1+ annualRate1/100)**numberOfYear1
   initialAmount = finalValue1/increaseAmount
   if initialAmount!=0:
      print("the initial value is:",initialAmount)
   else:
        print("error")

#to try whether it is valid
try:
    finalValue1 = float(finalValue)
    annualRate1 = float(annualRate)
    numberOfYear1 = float(numberOfYear)
    findOutYears(annualRate1,numberOfYear1,finalValue1)
except:
     print("invalid number")

#to find out the years

#to run the program
