def each_letter(word: str):
    return [i for i in word]


word_lst = ['Red', 'Blue', 'Black', 'White', 'Pink']
res = map(each_letter, word_lst)

print(list(res))