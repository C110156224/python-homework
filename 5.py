m = int(input("請輸入階層值M"))
n = 1
sum = 1

while sum < m:
    sum = 1
    n = n + 1
    for i in range(1, n):
        sum *= i
print("超過M為"+str(m)+"的最小階層N值為:"+str(n-1))