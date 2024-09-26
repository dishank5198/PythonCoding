comps_available = 1
S = 'ABCBAC'
visited = set()
unserviced_set = set()
unserviced_counter = 0
for i in S:
    if i not in visited and comps_available > 0:
        visited.add(i)
        comps_available = comps_available-1
    elif i in unserviced_set:
        unserviced_set.remove(i)
    elif i not in visited and comps_available == 0:
        unserviced_set.add(i)
        unserviced_counter = unserviced_counter+1
    elif i in visited:
        visited.remove(i)
        comps_available = comps_available+1

print(unserviced_counter)