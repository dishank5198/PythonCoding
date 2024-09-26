def reverse_sent(str1):
    str1 = str(str1)
    str1_lst = str1.split(' ')
    rev_lst = []
    for x in range(len(str1_lst)-1, -1, -1):
        rev_lst.append(str1_lst[x])
    rev_str = ' '.join(rev_lst)
    rev_str = rev_str.lstrip(' ')
    return rev_str


if __name__ == "__main__":
    str_ip = str(input("Enter a String to reverse: "))
    res = reverse_sent(str_ip)
    print(res)