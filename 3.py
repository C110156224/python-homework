a = int(input("請輸入西元年"))
list1=["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
a1 = a % 12
if a1 == 0:
    print(list1[8])
if a1 == 1:
    print(list1[9])
if a1 == 2:
    print(list1[10])
if a1 == 3:
    print(list1[11])
if a1 == 4:
    print(list1[0])
if a1 == 5:
    print(list1[1])
if a1 == 6:
    print(list1[2])
if a1 == 7:
    print(list1[3])
if a1 == 8:
    print(list1[4])
if a1 == 9:
    print(list1[5])
if a1 == 10:
    print(list1[6])
if a1 == 11:
    print(list1[7])