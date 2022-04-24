one = input("請輸入考試次數及學生數:").split(" ")
# one = ["6","3"]
oneagain = []
for i in range(len(one)):
    oneagain.append(int(one[i]))
two = input("每次考試所占的比率").split(" ")
# two = ["0.1","0.1","0.3","0.1","0.1","0.3"]
twoagain = []
for j in range(len(two)):
    twoagain.append(float(two[j]))
p = oneagain[1]
q = oneagain[0]
pagain = []
for k in range(p):
    pp = input().split(" ")
    ppp = []
    for l in range(len(pp)):
        ppp.append(int(pp[l]))
    pagain.append(ppp)
# pagain = [[70,80,90,80,100,80],[60,70,80,70,40,70],[30,50,40,60,50,40]]
totalagain = 0
for m in range(p):
    grade = pagain[m]
    for n in range(q):
        total = grade[n] * twoagain[n]
        totalagain += total
        ans = totalagain/p
print("%.2f"%ans)
