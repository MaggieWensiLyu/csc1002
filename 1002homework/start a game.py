import random
def display():
    count=0 
    while count < len(G):
     if G[count] == size*size:
        print(" ")
        count += 1  
     else:                                     #set a number to control the letters of each line
      print(G[count],end=" ")
      count+=1
      if count % size == 0:                                     #change another line 
        print(end="\n")

def play(dir):
    i = 0
    if dir == l and i % size !=0:          #four direction, there are several places that cannot be changed.
        G[i],G[i-1] = G[i-1],G[i]
        i = i-1
        return i
    if dir == r and (i+1) % size != 0:
        G[i],G[i+1] = G[i+1],G[i]
        i += 1
        return i 
    if dir == u and i < size:
        G[i],G[i-size] = G[i-size],G[i]
        i = i - size
        return i
    if dir == d and i >= (size-1)*size:
        G[i],G[i+size] = G[i+size],G[i] 
        i  =i+size
        return i

size = input("please input the size of the puzzle:(from 3 to 10) ")
l = input("please represent left:")
r = input("please represent right:")
u = input("please represent up:")
d = input("please represent down:")

size = int(size)
G = []
for k in range(1, size*size + 1):
    G.append(k)



m = 1
dirs = [l,r,u,d]
while m <= 10000:
    dir = random.choice(dirs)
    play(dir)
    m += 1
 
display()