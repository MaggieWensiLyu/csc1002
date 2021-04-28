num = int(input("please input a number:"))
try :
     num > 0 
except :
        print("mistake")

while num % 2 == 0:
     num = num / 2 
     print("2")

while num % 3 == 0:
         num = num / 3
         print("3")

while num % 5 == 0 :
        num = num / 5
        print("5")

while num % 7 == 0 :
       num = num / 7
       print("7")