def common_elements(a: list, b: list):
    common_eles = []
    for x in a:
        if x in b and x not in common_eles:
            common_eles.append(x)
    return common_eles


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 5]
    b = [4, 5, 6, 7, 8]
    res = common_elements(a, b)
    print(res)