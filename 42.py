a = int(input("輸入係數a"))
b = int(input("輸入係數b"))
c = int(input("輸入係數c"))
# a = 1
# b = 4
# c = 3
x1 = 0
x2 = 0
d = (b*b-4*a*c)
# print(d)
if d < 0:
    print("無解")
elif d == 0:
    x1 = ((-b) + d**0.5)/2*a
    print("x =",x1)
elif d > 0:
    x1 = ((-b) + d**0.5)/2*a
    x2 = ((-b) - d**0.5)/2*a
    print("x =",x1)
    print("x =",x2)
