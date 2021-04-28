def conv(base,n):
    if n < base:
        num.append(str(n)) 
    else:
        num.append(str(n % base))
        conv(base,n // base)

num = []
# num.reverse()
base = int(input("please input base"))
n = int(input("please input n"))
conv(base,n)
print("".join(num))

