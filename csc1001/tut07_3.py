list = input("please input a list of numbers:")
list1 = list.split()

def mean():
    n = 0
    sum = 0
    for num in list1:
        num =  float(num)
        sum = sum + num
        n = n + 1
    mean = sum / n 
    return mean, n 

def deviation(mean, n):
    for num in list1:
        num = int(num)
        var = 0
        x = (num - mean) ** 2
        var = var + x
    deviations  = var / n
    deviations = deviations ** 0.5
    return deviations

mean,n = mean()

print(mean)
print(n)

deviations = deviation(mean,n)
print(deviations)
