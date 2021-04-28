m=input("please input an m:")
n=1

try:
    m=int(m)
    while n**2<= m:
       n= n+1
    print(n)
except:
    print("error")

