def pairs(a: list, s: int):
    pair_lst = []
    cop_a = a.copy()
    visited_list = []
    for x in a:
        if x < s and x not in visited_list:
            visited_list.append(x)
            diff = s-x
            temp = cop_a.pop(cop_a.index(x))
            if diff in cop_a:
                visited_list.append(diff)
                temp_diff = cop_a.pop(cop_a.index(diff))
                pair_lst.append((temp, temp_diff))
    return len(pair_lst)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    s = 7
    res = pairs(a, s)
    print(res)