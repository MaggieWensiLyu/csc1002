word1= input("please input the first word:")
word2 = input("please input the second word:")

l1= list(word1)
l2 =list(word2)

l1.sort()
print(l1)
l2.sort()
print(l2)

if l2 == l1 :
    print("yes")
else:
    print("no")