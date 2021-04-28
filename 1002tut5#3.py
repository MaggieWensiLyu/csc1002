n=input("please input an integer:")
y=input("please input a series:").split
b=int(n)
length=len([y])
results=[]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = i+j+k
            difference= (sum- b)**2**0.5
            difference=results.append()

result=min(results)



