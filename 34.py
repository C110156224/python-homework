n = int(input("輸入一個正整數(11~1000):"))
if (n % 2) == 0:
    if (n % 11) == 0:
        if (n % 5) != 0:
            if (n % 7) != 0:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")