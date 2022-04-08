# list1 = [[60,50,30],[100,10,90],[80,40,20]]
list1 = []
# n = 3
n = int(input("請輸入陣列大小"))
for i in range(n):
    list1.append(input().split( ))
for z in range(n):
    for y in range(n):
        list1[z][y] = int(list1[z][y])
        # print(type(list1[z][y]))
max1 = 0
max2 = 0
max3 = 0
for j in range(n):
    for k in range(n):
        if list1[j][k] > max1:
            max1 = list1[j][k]
# print(max1)
for a in range(n):
    for b in range(n):
        if list1[a][b] > max2 and list1[a][b] < max1:
            max2 = list1[a][b]
# print(max2)
for c in range(n):
    for d in range(n):
        if list1[c][d] > max3 and list1[c][d] < max1 and list1[c][d] < max2:
            max3 = list1[c][d]
# print(max3)
print("最大值為:",max1 + max2 + max3)
for e in range(n):
    for f in range(n):
        if list1[e][f] == max1:
            max1place = [str(e+1),str(f+1)]
        if list1[e][f] == max2:
            max2place = [str(e+1),str(f+1)]
        if list1[e][f] == max3:
            max3place = [str(e+1),str(f+1)]
print("位置為(",",".join(max1place),"),(",",".join(max2place),"),(",",".join(max3place),")")