# x = str(1234)
x = str(input("請輸入一組四位數字"))
y = []
for i in x:
    y.append(((int(i)+7)%10))
z = [str(y[2]),str(y[3]),str(y[0]),str(y[1])]
strZ ="".join(z)
print("加密後數字為",strZ)
