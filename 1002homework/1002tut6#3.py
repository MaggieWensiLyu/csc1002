m1 = int(input("please input a number:"))
m2 = int(input("please input other number:"))
num = []

if m1 > m2:
    m3 = m1 - m2
    m4 = m2
else:
    m3 = m2 - m1 
    m4 = m2

def findNum():
    for i in range(1, m3):
        if m3 % i ==0 and m4 % i == 0:
             num.append(i)

findNum()
num.sort(reverse=True)
print(num[0])