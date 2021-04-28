while True:
    number = input("please input your card:")
    k = 1
    if number.find('4') == 0 or number.find('5') == 0 or number.find('6') == 0 or number[0:2] == "37":
        k= 0
    if number.isdigit() == True and k == 0 and len(number) >= 13 and len(number) <= 16:
        break