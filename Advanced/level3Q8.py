a = "Robert000Smith000123"
word_lst = []
count = 0
lst = []
final_dict = dict()
for x in a:
    if x == '0':
        if len(word_lst) > 0:
            name_str = ''.join(word_lst)
            word_lst = []
            lst.append(name_str)
        else:
            continue
    else:
        word_lst.append(x)
if len(word_lst) > 0:
    last_str = ''.join(word_lst)
    lst.append(last_str)
if len(lst) > 0:
    final_dict['first_name'] = lst[0]
    final_dict['lst_name'] = lst[1]
    final_dict['id'] = lst[2]

print(final_dict)