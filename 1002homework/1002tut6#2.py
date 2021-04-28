goods_list = ['apple','orange','cola','juice','banana']
price_list = [3, 4, 5, 6, 4]

def show_goods():
    global goods_list
    global price_list
    for i in range (0, len(goods_list)):
        print(goods_list[i] ,"    ",  price_list[i])
        

print("goods    price")
show_goods()

def add_Money(p_money, p_balance):
    new_balance= p_balance - p_money
    print(new_balance)
    return new_balance 


p_number = int(input("please input the numbers:"))
p_balance = float(input("please input the balance:")) 
p_name = input("please input the name:")
p_money = float()
new_balance = float()

def buy_goods(p_number,p_name, p_balance):
    n = goods_list.index(p_name)
    p_price = price_list[n]
    p_money = p_number * p_price
    return p_money

buy_goods(p_number,p_name, p_balance)
add_Money(p_money, p_balance)
print(new_balance)