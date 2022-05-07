T = int(input("任教幾班:"))
# T = 5
listT = []
for i in range(T):
    listT.append(int(input("每班人數:")))
# listT = [42,39,41,43,30]
max = 0
for j in range(T):
    if listT[j] > max:
        max = listT[j]
print("須購買的電腦數量:"+str(max))