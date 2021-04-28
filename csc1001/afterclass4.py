x = input("please input an x:")
y =list(x)
num = 0

def countNum():
    for x in y:
        num =num+1
        return num
    print(num)
       

def printNum():
  for i in range(num, 0, -1):
    print(i)

countNum()
printNum()
