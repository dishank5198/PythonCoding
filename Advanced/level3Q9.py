a = 'wwwwaaadebbbbbw'
lst_tup = []
i = 0
j = 1
count = 1
while i < len(a):
    if i == len(a)-1:
        new_tup = (a[i], count)
        lst_tup.append(new_tup)
        i = i + 1
        break
    if a[i] == a[j]:
        count = count+1
        j = j+1
        if j == len(a):
            new_tup = (a[i], count)
            lst_tup.append(new_tup)
            break
    else:
        new_tup = (a[i], count)
        lst_tup.append(new_tup)
        count = 1
        i = j
        j = i+1
str_new = ''
for x in lst_tup:
    str_new = str_new+x[0]+str(x[1])
print(str_new)