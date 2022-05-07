n = int(input("輸入筆數:"))
# n = 4
listn = []
for i in range(n):
    listn.append(input().split(" "))
# listn = [["Cat","貓"],["Dog","狗"],["Bird","鳥"],["Snake","蛇"]]    
# animal = "Cat"
animal = input("輸入查詢的單字:")
for j in range(n):
    if animal == listn[j][0]:
        print(str(animal)+"中文意思是:"+str(listn[j][1]))