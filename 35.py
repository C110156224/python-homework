# sa = "dog"
# sb = ["cat","dog","fish"]
sa = input("sa")
sb = input("sb").split(" ")
if sa in sb:
    print("子字串判斷為:Yes")
else:
    print("子字串判斷為:No")