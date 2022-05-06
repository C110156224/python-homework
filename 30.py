ans = [1,2,3,4]
a = 0
b = 0
user = input("輸入四位數字(不可重複)")
# user = "1543"
use = []
for i in user:
    use.append(int(i))
for j in range(len(ans)):
    if use[j] == ans[j]:
        a += 1
    else:
        for k in range(len(ans)):
            if use[j] == ans[k]:
                b += 1
print(a,"A",b,"B")