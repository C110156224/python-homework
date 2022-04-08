n = int(input("輸入整數"))
if n%2>0:
    for i in range(n+1,0,-2):
        for j in range(i):
            print(' ',end='')
        for k in range(n+2-i):
            print('x ',end='')
        print()
    for x in range(n-1,0,-2):
        for y in range(n+2-x+1):
            print(" ",end="")
        for z in range(x,1,-1):
            print("x ",end="")
        print()
if n%2<1:
    for i in range(n+2,0,-2):
        for j in range(i):
            print(' ',end='')
        for k in range(n-i+1):
            print('x ',end='')
        print(

        )
    for x in range(n-1,0,-2):
        for y in range(n+2-x+1):
            print(" ",end="")
        for z in range(x-2+2,2,-1):
            print("x ",end="")
        print()
