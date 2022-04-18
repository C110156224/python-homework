date = input("請輸入月及日").split(" ")
# date = ["08","20"]
date1 = []
for i in range(len(date)):
    date1.append(int(date[i]))



if date1[0] == 1:
    if date1[1] >= 1 and date1[1] <= 21:
        print("星座為:摩羯座")
    if date1[1] >= 22 and date1[1] <= 31:
        print("星座為:水瓶座")
if date1[0] == 2:
    if date1[1] >= 1 and date1[1] <= 18:
        print("星座為:水瓶座")
    if date1[1] >= 19 and date1[1] <= 29:
        print("星座為:雙魚座")
if date1[0] == 3:
    if date1[1] >= 1 and date1[1] <= 20:
        print("星座為:雙魚座")
    if date1[1] >= 21 and date1[1] <= 31:
        print("星座為:牡羊座")
if date1[0] == 4:
    if date1[1] >= 1 and date1[1] <= 20:
        print("星座為:牡羊座")
    if date1[1] >= 21 and date1[1] <= 30:
        print("星座為:金牛座")
if date1[0] == 5:
    if date1[1] >= 1 and date1[1] <= 21:
        print("星座為:金牛座")
    if date1[1] >= 22 and date1[1] <= 31:
        print("星座為:雙子座")
if date1[0] == 6:
    if date1[1] >= 1 and date1[1] <= 21:
        print("星座為:雙子座")
    if date1[1] >= 22 and date1[1] <= 30:
        print("星座為:巨蟹座")
if date1[0] == 7:
    if date1[1] >= 1 and date1[1] <= 22:
        print("星座為:巨蟹座")
    if date1[1] >= 23 and date1[1] <= 31:
        print("星座為:獅子座")
if date1[0] == 8:
    if date1[1] >= 1 and date1[1] <= 23:
        print("星座為:獅子座")
    if date1[1] >= 24 and date1[1] <= 31:
        print("星座為:處女座")
if date1[0] == 9:
    if date1[1] >= 1 and date1[1] <= 23:
        print("星座為:處女座")
    if date1[1] >= 24 and date1[1] <= 30:
        print("星座為:天秤座")
if date1[0] == 10:
    if date1[1] >= 1 and date1[1] <= 23:
        print("星座為:天秤座")
    if date1[1] >= 24 and date1[1] <= 31:
        print("星座為:天蠍座")
if date1[0] == 11:
    if date1[1] >= 1 and date1[1] <= 22:
        print("星座為:天蠍座")
    if date1[1] >= 23 and date1[1] <= 30:
        print("星座為:射手座")
if date1[0] == 12:
    if date1[1] >= 1 and date1[1] <= 22:
        print("星座為:射手座")
    if date1[1] >= 23 and date1[1] <= 31:
        print("星座為:摩羯座")