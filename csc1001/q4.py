N= input("please input a number N:")
m=1

try:
 N=float(N)
 if N%1==0 and N>0:
  print("m","   ","m+1","   ","m**(m+1)")
  while m<=N:
    print(m,"   ",m+1,"     ",m**(m+1))
    m=m+1
 else:
     print("invalid number")
except:
    print("not number")
