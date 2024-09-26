def anagram_check(str1, str2):
    found = False
    if len(str1) != len(str2):
        return found
    str1_lst = list(str1)
    for x in str2:
        found = False
        if x in str1_lst:
            found = True
            str1_lst.remove(x)
    return found


if __name__ == "__main__":
    str1 = str(input("Enter String 1: "))
    str2 = str(input("Enter String 2: "))
    result = anagram_check(str1, str2)
    print(result)