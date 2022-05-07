# n = 5
n = int(input("小狗可能跑幾個地方(2~10):"))
maybe = []
for i in range(n):
    maybe.append(int(input("可能距離家距離:")))
# maybe = [15,18,25,24,19]
x = 0
for j in range(n):
    if maybe[j] % 9 == 0 or maybe[j] % 11 == 0:
        x +=1
        print("第",j+1,"個點:",maybe[j])
if x == 0:
    print(0)