def add_Money(p_money, p_balance):
    new_balance= p_money + p_balance
    return new_balance 

p_money = float(input("please input the money:"))
p_balance = float(input("please input the balance:")) 

print(add_Money(p_money, p_balance))