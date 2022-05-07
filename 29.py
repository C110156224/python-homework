# a = ("124315421345124")
# b = ("124331243154312")
a = input("甲方的數字")
b = input("乙方的數字")
lista = []
listb = []
final = []

rule = [["1","5"],["2","1"],["3",'2'],["4","3"],["5","4"]]
for i in a:
    lista.append(int(i))
for j in b:
    listb.append(int(j))

for k in range(len(lista)):
    if lista[k] == 1:
        if listb[k] == 5:
            final.append("贏")
        elif listb[k] == 2:
            final.append("輸")
        else:
            final.append("和")
    if lista[k] == 2:
        if listb[k] == 1:
            final.append("贏")
        elif listb[k] == 3:
            final.append("輸")
        else:
            final.append("和")
    if lista[k] == 3:
        if listb[k] == 2:
            final.append("贏")
        elif listb[k] == 4:
            final.append("輸")
        else:
            final.append("和")
    if lista[k] == 4:
        if listb[k] == 3:
            final.append("贏")
        elif listb[k] == 5:
            final.append("輸")
        else:
            final.append("和")
    if lista[k] == 5:
        if listb[k] == 4:
            final.append("贏")
        elif listb[k] == 1:
            final.append("輸")
        else:
            final.append("和")
ans = ""
for l in final:
    ans += l
print("洗刷刷結果:"+str(ans))







