doors = []
i = 0
while i <= 99:
    doors.append(True)
    i += 1

stu = 1
while stu <= 99:
    k = stu
    # while k <= 100:
    if k % 2 != 0: 
       m = k    
       while m <= 99  : 
        doors[m] = False
        m += 1
    else:
          n = k
          while n <= 99:
              doors[n] = True
              n += 1
    stu += 1

open = []
for doorNum in range(0,99):
    if doors[doorNum] == True:
        open.append(doorNum +1)
    doorNum += 1
print("the open doors are:")
count = 1
for doorNum in open:
    print(doorNum,end =" ")
    count += 1
    if count % 6 == 0:
        print(" ")  
    