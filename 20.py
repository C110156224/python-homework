a = int(input("組數為:"))
# a = 3
s = []
for i in range(a):
    s.append(input("第"+str(i+1)+"組").split(" "))
# s = [["5","3"],["6","4"],["7","6"]]
c = []
for j in range(a):
    b = s[j]
    n = []
    for k in range(2):
        n.append(int(b[k]))
    c.append(n)
for x in range(a):
    x1 = c[x]
    big = x1[0] * 250
    small = x1[1] * 175
    print("第",x+1,"組應收費用為:",big+small)
    
        