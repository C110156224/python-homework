n = int(input("請輸入查詢組數"))
listinput = []
list1 = ["123","456","789","336","775","566"]
list2 = ["456","789","888","558","666","221"]
list3 = [9000,5000,6000,10000,12000,7000]
for i in range(0,n):
    listinput.append(input("帳號 密碼").split(" "))
for k in range(0,n):
    if listinput[k][0] in list1 and listinput[k][1] in list2:
        for j in range(len(list1)):
            if listinput[k][0] == list1[j] and listinput[k][1] == list2[j]:
                print(list3[j])
    else:
        print("error")