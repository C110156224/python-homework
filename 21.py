a =  [[123,456,789,321,654],["Tom","Cat","Nana","Lim","Won"],["DTGD","CSIE","ASIE","DBA","FDD"]]
id = int(input("請輸入一個學號"))
for i in range(len(a[0])):
    if id == a[0][i]:
        print(a[0][i],a[1][i],a[2][i])