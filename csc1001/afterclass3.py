x=[]
y = input("how manyy times do you want:")
str="please input the number:"
sum = 0

def put():
   while y>=0:
      x.append(str)
      y= y-1


def add():
    while y >= 0:
        sum = sum +[y-1]
    return sum


try :
    y = int(y)
except:
    print("mistake")
put()
add()
print(sum)