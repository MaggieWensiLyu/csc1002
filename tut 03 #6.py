line = int(input("please input the lines:"))
numofline = 0
try :
    line > 0
except :
        print("mistake")

while numofline <= line :
#print the left ones

     for num in range(1,numofline +1, 1):
             if num <= numofline :
                  print("%4d"% num, end = " ")
             else :
                   print("%4d"%" ", end =" ")

     for num in range(numofline,0 ,-1):
            if num <= numofline :
                print("%4d"%num, end = " ")
            else :
                print("%4d"%" ", end =" ")
     numofline = numofline +1
