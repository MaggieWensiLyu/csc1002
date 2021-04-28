# Method 1
# Check whether each number smaller than n is a prime
# Append the primes into a list
num = int(input("Please enter an integer n, n > 2: "))
prime_list = list()
for digit in range(2, num):
    flag = True
    # for i in range(2, digit):
    for i in range(2, int(digit ** 0.5 + 1)):
        if digit % i == 0:
            flag = False
            break
    if flag:
        prime_list.append(digit)
print("All the prime numbers smaller than", num, "are:")
print(prime_list)


# Method 2
# Create a list containing all the numbers smaller than n
# Replace the composite (non-prime) numbers with 0
# Create another list containing all the non-zero numbers in the first list
num = int(input("Please enter an integer n, n > 2: "))
num_list = list(range(2, num))
for i in num_list:
    if i != 0:
        for index in range(num_list.index(i) + i, num - 2, i):
            num_list[index] = 0
prime_list = [digit for digit in num_list if digit != 0]
print("All the prime numbers smaller than", num, "are:")
print(prime_list)
