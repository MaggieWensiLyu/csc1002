import random
def display():
    count=0 
    for l in G:
        if l == size**2:             #use the largest number in the list to represent the  white block
            l = " "
        try:
             print("%-3d"%l, end = " ")       #make the number takes three place the whole puzzle can be orded 
        except:
             print("%-3s"%l, end = " ")       #make sure the " " can be print
        count += 1 
        if count % size == 0:
             print(" ")
    
def play(dir):
    i = G.index(size *size)
    if dir == l and i % size !=0:          #four direction, there are several places that cannot be changed.
        G[i],G[i-1] = G[i-1],G[i]
    if dir == r and (i+1) % size != 0:
        G[i],G[i+1] = G[i+1],G[i]         #change the number in the list directly 
    if dir == u and i >= size:
        G[i],G[i-size] = G[i-size],G[i]
    if dir == d and i < (size-1)*size:
        G[i],G[i+size] = G[i+size],G[i] 

def testL():
   IsL = False                                      #set a monitor to check whether all conditions are satisfied
   while IsL == False: 
    l = input("please represent left:")
    r = input("please represent right:")
    u = input("please represent up:")
    d = input("please represent down:")
    letters = []                                                   #help to test whether the letters are the same in next step
    letters.append(l)
    letters.append(r)
    letters.append(u)
    letters.append(d)                          
    if  len(l) == 1 and l.isalpha():           
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
   return l,r,u,d

def playOnce():
 display()
 G1 = sorted(G)
 num_steps = 0 
 while G1 != G:                                           #make sure the order is not right then start
    dir = input("next step:")
    play(dir)
    num_steps += 1
    display()
 else:
    print("win")
    print("finish by",num_steps,"steps")

def another():
    newG = input("continue or not?")
    if newG == "continue":
      playOnce()
    elif newG == "not":
      print("bye")
    else:
        print("please enter 'continue' or 'not':")            # avoid invalid input
    
print('''This is a sliding puzzle. Players can design the size of the puzzle(from 3×3 to 10×10). 
      The game ends when all numbers appear in order.''')

while True:                                                    #make sure the size is valid
 size = input("please input the size of the puzzle:(from 3 to 10) ")
 if size.isdigit() and 3 <= int(size) <= 10:
     break
 else:
     print("input numbers between 3 to 10")

l,r,u,d = testL()
size = int(size) 
G = []
#testL()                                      #make sure letters are valid
for k in range(1, size*size + 1):                    #use list to display
    G.append(k)
    m = 1
dirs = [l,r,u,d]
while m <= 100:                                      #make the puzzle solvable by move the right one randomly
     dir = random.choice(dirs)
     play(dir)
     m += 1
playOnce()
another()


