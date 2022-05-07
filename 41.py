t = int(input("小名搭幾次電梯:"))
# t = 5
floor = [1]
for i in range(t):
    floor.append(int(input("搭到幾樓")))
# print(floor)
# floor = [1,2,3,5,3,1]
price = 0
for j in range(t):
    if floor[j] < floor[j+1]:
        price += (floor[j+1]-floor[j])*20
    elif floor[j] > floor[j+1]:
        price += (floor[j]-floor[j+1])*10
print(str(price)+"元")
