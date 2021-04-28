# print('\x00'+ "22")
# print('\x02')
# print('\x03')
# print('\x04')
# # print(len(('\x05'))
# # print('\x06' + "22")

# s = "123456"
# # print(s[:-2:-1])
# s = ["1","2","3","4","5"]
# print("  ".join(s))
# print( list(zip([1,2,3],[4,5]))) 
# a = 2
# b =  a
# b =  3
# print(a)
# l = [1,1,2,3,4]
# l.remove(l[l.index(1)])
# print(l)

eco = ["N","N","N","F","B","N","B","B","F",'F','F',"N","F"]
ele = "B"
move = "r"
if move == "l":                                     #start to move
                    m = eco.index(ele)
                    if eco[m - 1] == "F" and ele == "B":        #the "F" would be removed
                       eco.remove(eco[m-1])
                    elif eco[m - 1] == "B" and ele == "F":
                        eco.remove(eco[m])
                    else:
                     eco[m - 1],eco[m] = eco[m],eco[m - 1]
                    
elif move == "r":
                    m = eco.index(ele)
                    if eco[m + 1] == "F" and eco[m] == "B":        #the "F" would be removed
                        eco.remove(eco[m+1])
                    elif eco[m + 1] == "B" and eco[m] == "F":
                        eco.remove(eco[m])
                    else:
                        eco[m + 1], eco[m] = eco[m],eco[m + 1]
print(eco)