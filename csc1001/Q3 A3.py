from random import random
import random
class Ecosystem():
    def __init__(self):
        self.river = 3
        self.bear = 0
        self.fish = 0
        self.eco = ["N",'N','N']
    def setRiver(self, river):
        self.river = river
    def setBear(self,bear):
        self.bear = bear
    def setFish(self,fish):
        self.fish = fish
    def getEco(self):
        return self.eco
    def setEco(self):
        self.eco = []
        for k in range(self.river - self.bear - self.fish):
         self.eco.append("N") 
         k += 1
        for i in range(self.fish):                                #insert fish in the river randomly
            pos = random.randint(0,len(self.eco))
            self.eco.insert(pos,"F")
            i += 1
        for j in range(self.bear):                                  #insert bears randomly
            pos = random.randint(0,len(self.eco))
            self.eco.insert(pos,"B")
            j += 1
    def simulation(self,N): 
        born_b = 0
        born_f = 0
        n = 0
        empty = self.eco.count("N")
        while n < N:
         for ele in self.eco:                
            if ele == "N":                                        #check whether this element can be move
                continue
            else:
                if self.eco.index(ele) == 0:                       #choose the direction of mmovement
                    move = "r"
                elif self.eco.index(ele) == len(self.eco) - 1:
                    move = "l"
                else:
                    move = random.choice("lrn")                        
                if move == "l":                                     #start to move
                    m = self.eco.index(ele)
                    if self.eco[m - 1] == "F" and ele == "B":        #the "F" would be removed
                        self.eco.remove(self.eco[m-1])
                    elif self.eco[m - 1] == "B" and ele == "F":
                        self.eco.remove(self.eco[m])
                    else:
                     self.eco[m - 1],self.eco[m] = self.eco[m],self.eco[m - 1]
                     if self.eco[m-1] == self.eco[m] and empty >= 1 and self.eco[m] == "B":
                         empty -= 1 
                         born_b += 1 #to see whether there is empty position to add one more
                     if self.eco[m-1] == self.eco[m] and empty >= 1 and self.eco[m] == "F":
                         born_f += 1
                         empty -= 1
                         
                    
                elif move == "r":
                    m = self.eco.index(ele)
                    if self.eco[m + 1] == "F" and self.eco[m] == "B":        #the "F" would be removed
                        self.eco.remove(self.eco[m+1])
                    elif self.eco[m + 1] == "B" and self.eco[m] == "F":
                        self.eco.remove(self.eco[m])
                    else:
                        self.eco[m+ 1], self.eco[m] = self.eco[m],self.eco[m + 1]
                        if self.eco[m-1] == self.eco[m] and empty >= 1 and self.eco[m] == "B":#to see whether there is empty position to add one more
                         born_b += 1
                         empty -= 1
                        elif self.eco[m-1] == self.eco[m] and empty >= 1 and self.eco[m] == "F":
                            born_f += 1
                            empty -= 1

                if born_b > 0:
                    for i in range (born_b):
                     avai = []   
                     for elem in self.eco:
                             if elem == "N":
                                avai.append(self.eco.index(elem))
                     new_born = random.choice(avai)
                     self.eco[new_born] = "B" #born a same element
                if born_f > 0:
                    for i in range (born_f):
                     avai = []   
                     for elem in self.eco:
                             if elem == "N":
                                avai.append(self.eco.index(elem))
                     new_born = random.choice(avai)
                     self.eco[new_born] = "F" #born a same element

                # else:
                #     continue
         n += 1
         print("step" + str(n) +":" )
         print(self.eco)
                   
def main():
    while True:
        river = input("please input the river length:")
        if river.isdigit() == True:
            river  = int(river)
            if river > 0:
             break
            else:
                print("should be positive integer")       
        else:
            print("should be a positive integer")
    while True:
        fish = input("please input the number of fish:")
        if fish.isdigit() == True:
            fish = int(fish)
            if fish >= 0 and fish <= river:
                break
            else:
                print("should be less than river length and positive integer")
        else:
            print("should be integers")
    while True:
        bear = input("please input the number of bear:")
        if bear.isdigit() == True:
            bear = int(bear)
            if bear >= 0 and bear <= (river - fish):
                break
            else:
                print("should be positive and total amount should be less than the river length")
        else:
            print("should be integers")
    ecosys = Ecosystem()
    ecosys.setBear(bear)
    ecosys.setFish(fish)
    ecosys.setRiver(river)
    ecosys.setEco()
    while True:
        N = input("please input the number of steps:")
        if N.isdigit() == True:
            N = int(N)
            if N >= 0:
                break
        else:
            print("should be positive integr")
    print(ecosys.getEco())
    ecosys.simulation(N)
                
main()
            

        