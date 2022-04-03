x = int(input("請輸入一個正整數(<10)"))
z = 0
for i in range(1,x+1):
    for j in range(1,i+1):
        z = i*j
        print(z,end=" ")
    print()