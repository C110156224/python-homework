n1 = int(input("請輸入第1個數字"))
n2 = int(input("請輸入第2個數字"))
n3 = int(input("請輸入第3個數字"))
n4 = int(input("請輸入第4個數字"))
n5 = int(input("請輸入第5個數字"))
n6 = int(input("請輸入第6個數字"))
n7 = int(input("請輸入第7個數字"))
n8 = int(input("請輸入第8個數字"))
n9 = int(input("請輸入第9個數字"))
n10 = int(input("請輸入第10個數字"))
list1 = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
x = 0
for i in range(len(list1)):
    for j in range (len(list1)-1-i):
        if list1[j] < list1[j+1]:
            x = list1[j]
            list1[j]= list1[j+1]
            list1[j+1] = x
print("最大的3個數字為:"+str(list1[0])+","+str(list1[1])+","+str(list1[2]))
print("最小的3個數字為:"+str(list1[7])+","+str(list1[8])+","+str(list1[9]))