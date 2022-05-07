# n = 8
n = int(input("輸入整數n:"))
x = []
x.append(n)
airn = 0
if n%2 !=0:
    airn = int(n/2-1.5)
elif n%2 == 0:
    airn = int(n/2-2)
while n > 2:
    n -= 2
    x.append(n)

air = " "
QQ = 0
long = ""

for a in range(len(x)-1):
    QQ = len(x)-(a+1)
    # print(a)
    # print(QQ)
    print(air*airn,x[QQ])
    long += str(x[QQ])
for b in range(len(x)):
    long += str(x[b])
print(long)
for c in range(len(x)-1):
    print(air*airn,x[c+1])
