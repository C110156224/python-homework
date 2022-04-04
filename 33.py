c = int(input("請輸入國文成績"))
e = int(input("請輸入英文成績"))
m = int(input("請輸入微積分成績"))
p = int(input("請輸入體育成績"))
v = int(input("請輸入程式設計成績"))
grade = {c:"國文",e:"英文",m:"微積分",p:"體育",v:"程式設計"}
a = (c + e + m + p + v)/5
list1 = [c,e,m,p,v]
x = 0
for i in range(len(list1)):
        for j in range(len(list1)-1-i):
            if list1[j]<list1[j+1]:
                x=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=x
max = list1[0]
min = list1[4]
print("平均分數:",'%.2f'%a)
print("最高分科目:",grade[max],max)
print("最低分科目:",grade[min],min)
