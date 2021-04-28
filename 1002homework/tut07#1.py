class Account:
    def __init__(self,id,balance = 100,annualRate = 1):
        self.__ID = id
        self.__balance =  balance
        self.__annualInterestRate = annualRate
    
    def setID(self):
        self.__ID = id 

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualRate(self, annualRate):
        self.__annualInterestRate = annualRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12
    
    def getMonthlyInterest(self):
        return self.__balance * self.__annualInterestRate / 12

    def getBalance(self):
        return self.__balance

    def withdraw(self):
        while True:
          withdrawMoney = float(input("how much do you want to withdraw:"))
          break
        self.__balance += -withdrawMoney

    def deposit(self):
        while True:
            deposite = float(input("how much do you want to deposite:"))
            break
        self.__balance += deposite 
       
# def main():
#     while True:
#             id = input("please input your ID:")
#             if id.isdigit() == True:
#                 break
#     while True:
#             balance = float(input("please input a balance:"))
#             break
#     while True:
#             annualRate = float(input("please input the annual interest rate:"))
#             break
#     account = Account(id,balance,annualRate)   
#     account.deposit()
#     account.withdraw()
#     print(account.getMonthlyInterestRate())
#     print(account.getMonthlyInterest())
#     print(account.getBalance)
    
# main()

# a = Account(1)
# b = Account(2)
# c = Account(3)
# d = Account(5)

while True:
    identity = int(input("ID:"))
    if identity <= 5 and identity >= 1:
        break
ac = Account(identity)
nextStep = "a"
while nextStep != "stop":
    print(''' 1: check the balance
            2: withdraw
            3:deposite
            4:exist''')
    while True: 
        step = int(input("enter your choice:"))
        if step >= 1 and step <= 4 :
            break
    if step == 1:
        print(ac.getBalance())
    elif step == 2:
        ac.withdraw()
        print(ac.getBalance())
    elif step == 3:
        ac.deposit()
        print(ac.getBalance)
    else:
        nextStep = "stop"
