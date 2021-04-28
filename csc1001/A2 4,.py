def isAnagram(s1,s2):
    w1 = list(s1).sort()                    # put letters in the list and make them in the same order
    w2 = list(s2).sort()
    if w1 == w2:
        print("is an anagram")
    else:
        print("is not an angram")

while True:
    s1 = input("please input the first word:")
    s2 = input("please input the second word:")
    if s1.isalpha() == True and s2.isalpha() == True:
        break                                                     #make sure the input is letters
isAnagram(s1,s2)

