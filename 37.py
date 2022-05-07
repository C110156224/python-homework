n = int(input("輸入整數n(0<n<1,000,000)"))
# n = 22
listn = []
listn.append(n)

if n == 1:
    print("數列:",n)
    print("cycle length:",len(listn))
else:
    while n != 1:
        if n % 2 != 0:
            n = 3 * n + 1
            listn.append(int(n))
        else:
            n = n / 2
            listn.append(int(n))

# print(listn)
x = ""
for i in range(len(listn)):
    x += str(listn[i]) + " "
print("數列:"+str(x))
print("cycle length:"+str(len(listn)))