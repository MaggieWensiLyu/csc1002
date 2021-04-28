x= input("please input an x:")
factorial =1

try :
    x = int(x)
except:
    print("mistake")

while x >=1 :
    factorial = x *factorial
    x = x-1

print("x factorial =", factorial)