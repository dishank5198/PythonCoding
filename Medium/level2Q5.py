temp = [25, 28, 21, 24, 27]
mini = temp[0]
maxi = temp[0]
for x in temp:
    if x < mini:
        mini = x
    elif x > maxi:
        maxi = x
avg_temp = sum(temp)/len(temp)

print(mini)
print(maxi)
print(avg_temp)