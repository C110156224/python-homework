x = 2
y = 2
a = ["該點位於第一象限","該點位於第二象限","該點位於第三象限","該點位於第四象限","該點位於原點","該點位於上半平面Y軸上","該點位於下半平面Y軸上","該點位於左半平面X軸上","該點位於右半平面X軸上"]
long=x**2 + y**2
if x == 0:
    if y == 0:
        print(a[4])
    elif y > 0:
        print(a[5],"離原點距離為根號",long)
    elif y < 0:
        print(a[6],"離原點距離為根號",long)
elif x < 0:
    if y == 0:
        print(a[7],"離原點距離為根號",long)
    elif y > 0:
        print(a[1],"離原點距離為根號",long)
    elif y < 0:
        print(a[2],"離原點距離為根號",long)
elif x > 0:
    if y == 0:
        print(a[8],"離原點距離為根號",long)
    elif y > 0:
        print(a[0],"離原點距離為根號",long)
    elif y < 0:
        print(a[3],"離原點距離為根號",long)