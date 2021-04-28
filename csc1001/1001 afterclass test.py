hours = input("please input the working hours:")
hoursRate = input("please input the rate:")

try :
     hours = int(hours)
     hours >= 0
except :
    print("error")

try:
    hoursRate=int(hoursRate)
    hoursRate >= 0
except:
    print("hours")

    
if hours <= 40:
    salary= hoursRate * hours
else :
    salary= 40* hoursRate+ (hours-40)*hoursRate*1.5

print("salary= " , salary)