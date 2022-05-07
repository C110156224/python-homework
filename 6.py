a = input("輸入1~7個數字字串").split(",")
# a = [1,3,9,5,7,1]
x = 0
a2 = []
a3 = []
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j+1] > a[j]:
            x = a[j]
            a[j] = a[j+1]
            a[j+1] = x
for m in range(len(a)):
    a2.append(str(a[m]))
for n in range(len(a)-1,-1,-1):
    a3.append(str(a[n]))
max = int("".join(a2))
min = int("".join(a3))
print("最大值數列與最小值數列差值為:"+str(max-min))