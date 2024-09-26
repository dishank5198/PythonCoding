op = lambda x, str1: True if str1[0] == x else False

x = str(input("Enter Character for check: "))
x = x[0]
str1 = str(input("Enter a String: "))
res = op(x, str1)
print(res)