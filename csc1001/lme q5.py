#input number
i=input("please input an integer:")

#def prinums():
    
i=eval(i)
if i>=2 and i==int(i):
    num=1
    k=int()
    while num<=i:
        Flag=True
        for k in range (2,num):
          if num%k==0: 
            k=k+1
            Flag=False
          break
        else:
            print(num)
        num=num+1

#    prinums()