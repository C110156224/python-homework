# card = ["A","K","5","9","10"]
card = input("輸入五張牌").split(" ")
cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
ans = 0
for i in range(len(card)):
    x = card[i]
    ans += cards[x]
print(ans)