class Flower():
    def __init__(self):
        self.name  = "glass"
        self.num = 0
        self.price = 0
    def setName(self,name):
        self.name = name
    def setNum(self,num):
        self.num = num
    def setPrice(self,price):
        self.price = price
    def getValue(self):
        return "name：" + self.name + "  price：" + str(self.price) + "  petals amount:" + str(self.num)

def enter():
    while True:                                               
        name = input("please input the name:")
        if name.isalpha() == True:
            break
        else:
            print("please only input letters")
    while True:
        num = input("please input the number of petals:")
        if num.isdigit() == True:
            num = int(num)
            if num > 0:
             break
            else:
                print("number should be greater than 0")
        else:
            print("pleae input integers")
    while True:
        price = input("pleae input the price:")
        try:
            price = float(price)
            if price >= 0:
             break
            else:
                print("the price should not be negative")
        except:
            print(" Price shoule be number.")
    one  = Flower()
    one.setName(name)
    one.setNum(num)
    one.setPrice(price)
    print(one.getValue())

enter()