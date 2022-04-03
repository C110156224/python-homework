money = int(input("請輸入金額"))
n100 = money//100
n50 = (money%100)//50
n10 = ((money%100)%50)//10
n5 = (((money%100)%50)%10)//5
n1 = (((money%100)%50)%10)%5
ans = n100 + n50 + n10 + n5 + n1
print(ans)