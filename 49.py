en = input("請輸入英文句子:").split(" ")
# print(en)
# en = ['an', 'apple', 'a', 'day', 'keeps', 'the', 'doctor', 'away']
ne = []
for i in range(len(en)-1,-1,-1):
    ne.append(en[i])
print("輸出結果:"+str(ne))