def vowel_counter(a: str):
    count = 0
    vowel_lst = ['a', 'e', 'i', 'o', 'u']
    a = a.split(' ')
    for x in a:
        for z in x:
            if z.lower() in vowel_lst:
                count += 1
    return count


if __name__ == "__main__":
    a = str(input("Enter a String: "))
    res = vowel_counter(a)
    print(res)