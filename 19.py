# test = 2
test = int(input("測試的資料量"))
# inputblood = [["O","A","B"],["B","B","O"]]
inputblood = []
for i in range(test):
    inputblood.append(input().split(" "))
# print(inputblood)
bloodlist = [["O","O","O"],["O","A","A"],["O","A","O"],["O","B","B"],["O","B","O"],["O","AB","A"],["O","AB","B"],["A","A","A"],["A","A","O"],["A","B","A"],["A","B","B"],["A","B","O"],["A","B","AB"],["A","AB","A"],["A","AB","B"],["A","AB","AB"],["B","B","B"],["B","B","O"],["B","AB","A"],["B","AB","B"],["B","AB","AB"],["AB","AB","A"],["AB","AB","B"],["AB","AB","AB"]]
for j in range(len(inputblood)):
    if inputblood[j] in bloodlist:
        print("Yes")
    else:
        print("Inpossible")