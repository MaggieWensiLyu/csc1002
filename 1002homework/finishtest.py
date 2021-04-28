import random
def display():
    count=0 
    while count < len(G):
     if G[count] == size*size:
        print(' ',end=" ")
        count += 1  
     else:                                     #set a number to control the letters of each line
        print(G[count],end=" ")
        count+=1
     if count % size == 0:                                     #change another line 
        print(end="\n")

def play(dir):
    i = G.index(size *size)
    if dir == l and i % size !=0:          #four direction, there are several places that cannot be changed.
        G[i],G[i-1] = G[i-1],G[i]
    if dir == r and (i+1) % size != 0:
        G[i],G[i+1] = G[i+1],G[i]
    if dir == u and i >= size:
        G[i],G[i-size] = G[i-size],G[i]
    if dir == d and i < (size-1)*size:
        G[i],G[i+size] = G[i+size],G[i] 

def testL():
    IsL = True                                        #set a monitor to check whether all conditions are satisfied
    if  len(l) == 1 and l.isalpha() == True:           
        IsL = True                                     #set the monitor to True if condition 1 is satisfied
    if len(r) != 1 and r.isalpha() != True:
        IsL = False                                    #if unsatisfied, set to false and stay unchanged
    if len(u) != 1 and u.isalpha() != True:
        IsL = False
    if len(d) != 1 and d.isalpha() != True:
        IsL = False
    return IsL

def playOnce():
 display()
 G1 = sorted(G)
 while G1 != G:
    dir = input("next step:")
    play(dir)
    display()
 else:
    print("win")

def another():
    newG = input("continue or not?")
    if newG == "continue":
      playOnce()
    elif newG == "not":
      print("bye")
    else:
        print("please enter 'continue' or 'not':")
    

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
while m <= 1000:
    dir = random.choice(dirs)
    play(dir)
    m += 1
 

    
playOnce()
another()
