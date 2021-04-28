num = input('please input a number:')
num = int(num)
check = int(input('please input a dominator:'))

remainder = num % 2 
left = num % 4
AGAINremainder= num % check

if remainder == 1:
   print("it is odd")
elif remainder == 0 and left == 0:
   print('it can be devided by four')
else :  
    print('it is even')

if AGAINremainder == 0:
    print('yes,it can be divided evenly')
else :
    print('it cannot be devided evenly')
