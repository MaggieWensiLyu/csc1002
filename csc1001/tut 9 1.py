# m = {"a":1,"b":2,"c":3,"d":4}
# for c in m:
#     key,value = value,key
# m_reverse = m
# print(m_reverse)

# k =zip(m)
# l = []
# for z in k :
#      value,key = z
#      l.append(z)

# m_reverse = {z}

# num = range(1,11)
# even = list(filter(lambda x: x % 2 == 0,num)) 
# triple = [x**3 for x in even]
# # print(triple)
# from functools import reduce
# sum = reduce(lambda x,y:x + y , triple)
# print(sum)

x = 1
y = 4
def transform(x):
 m = []   
 while x > 1:
    m.append(x % 2)
    x = x // 2
 m.reverse()   
 return m

 x,y = list
