# word = ("12321")
word = input("請輸入字串")
if str(word) == str(word)[::-1]:
    print("yes")
else:
    print("no")
# if str(word) == "".join(reversed(word)) :
#     print("yes")
# else:
#     print("no")