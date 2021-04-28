def testL():
    global IsL
    IsL= False                                       #set a monitor to check whether all conditions are satisfied
    if  len(l) == 1 and l.isalpha() == True:           
        IsL = True                                     #set the monitor to True if condition 1 is satisfied
    if len(r) != 1 or r.isalpha() != True:
         IsL = False                                    #if unsatisfied, set to false and stay unchanged
    if len(u) != 1 or u.isalpha() != True:
         IsL = False
    if len(d) != 1 or d.isalpha() != True:
         IsL = False
    lettersC = set(letters)
    if len(letters) != len(lettersC):
        IsL = False

l = input("please represent left:")
r = input("please represent right:")
u = input("please represent up:")
d = input("please represent down:")
letters = []
letters.append(l)
letters.append(r)
letters.append(u)
letters.append(d)

testL()
print(IsL)