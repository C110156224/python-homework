m = int(input("小明身上有幾元(0~100):"))
n = int(input("販賣機有幾種飲料(1~30):"))
listdrink = []
x = 0
for i in range(0,n):
    x = int(input("飲料價格"))
    listdrink.append(x)
listdrink1 = []
for j in range(0,len(listdrink)):
    if m >= listdrink[j]:
        y = m // listdrink[j]
        if y > 0:
         listdrink1.append(listdrink[j])
print(len(listdrink1))