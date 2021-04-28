from math import sin
from math import cos
from math import tan


a=input("please input a:")
b= input("please input b:")
n=input("please input n:")
ft=input("please input a trigonomitirc function:")
f=float()



def cal(a=0,b=0,n=1):
    a=a
    b=b
    n=n
    result=0
    i=1
    while i<=n:
    #to calculate the number inside f（）
        if ft=="sin":
         f= sin(a+(b-a)/n*(i-0.5))
        elif ft=="cos":
         f=cos(a+(b-a)/n*(i-0.5))
        elif ft=="tan":
         f=tan(a+(b-a)/n*(i-0.5))
        #add all the intervals together
        result=result+(b-a)/n*f
        i=i+1
    print(result)
try:
 a=float(a)
 b=float(b)
 n=float(n)
 #test n
 if n%1==0 and n>=1:
   n=int(n)
  #test function
   if ft=="sin" or ft=="cos" or ft=="tan":
       cal(a,b,n)
   else:
      print("invalid function")
 else:
     print("n is not an integer")
except:
   print("invalid input")