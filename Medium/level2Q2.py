def unique_ele(a: list) -> list:
    u_list = []
    for x in a:
        if x not in u_list:
            u_list.append(x)
    return u_list


if __name__ == "__main__":
    a = [1,1,2,2,2,2,2,2,3,3,4,4,5,5,6,6,7]
    res = unique_ele(a)
    print(res)