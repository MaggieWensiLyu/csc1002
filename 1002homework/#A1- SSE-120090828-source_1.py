import random 
#Heach step, how to switch 
def play(dir):
    i = 0
    dir = input("next step:")
    if dir == l and i % size !=0:          #four direction, there are several places that cannot be changed.
        (G[i],G[i-1]) = (G[i-1],G[i])
        i = i-1
        return i
    if dir == r and (i+1) % size != 0:
        (G[i],G[i+1]) = (G[i+1],G[i])
        i += 1
        return i 
    if dir == u and i < size:
        (G[i],G[i-size]) = (G[i-size],G[i])
        i = i - size
        return i
    if dir == d and i >= (size-1)*size:
        (G[i],G[i+size]) = (G[i+size],G[i]) 
        i  =i+size
        return i

#to test whether the letters can be used, included the length and the content
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

def display():
    count=0                                            #set a number to control the letters of each line
    print(G[count],end=" ")
    count+=1
    if count%3==0:                                     #change another line 
        print(end="\n")


print('''This is a sliding ouzzle. Players can design the size of the puzzle(from 3×3 to 10×10). 
      When playing, users can control the movement of the slide by self-designed charaters.
      The game ends when all numbers appear in order.''')

size = input("please input the size of the puzzle:(from 3 to 10) ")
l = input("please represent left:")
r = input("please represent right:")
u = input("please represent up:")
d = input("please represent down:")

size = int(size)
G = range(0, size+1)



m = 1
dirs = [l,r,u,d]
while m <= 50:
    dir = random.choice(dirs)
    play(dir)
    m += 1
 
display()

#start to operate the game
G1 = sorted(G)
while G1 != G:
    play()
    display()
else:
    print("win")
    print("continue or not")
    gameTwo=input(" ")
    if gameTwo == "continue":
    
        while G.sord() != G :
            play()
            display()


