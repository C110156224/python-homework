km = float(input("輸入路程公里數"))
price = 0
if km < 1.5:
    price = 75
elif km > 1.5:
    x = (km-1.5)//0.25
    y = (km-1.5)%0.25
    if y > 0:
        price = 75 + x*5 + 5
    else:
        price = 75 + x*5
print ("所需車資為:",int(price))