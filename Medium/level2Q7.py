def median(a: list):
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)-1):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    if len(a)%2 == 1:
        med = a[len(a)//2]
    else:
        m1 = len(a)//2
        m2 = m1+1
        med = round((m1+m2)/2)
    return med


if __name__ == "__main__":
    a = [7, 2, 5, 1, 9, 3]
    res = median(a)
    print(res)