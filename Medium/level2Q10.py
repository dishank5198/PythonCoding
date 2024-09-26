def stone_plie(num):
    pile_lst = []
    for x in range(num):
        if x % 2 == 0 and num % 2 == 0:
            pile_lst.append(x)
        elif num % 2 != 0 and x % 2 !=0:
            pile_lst.append(x)
    return pile_lst


if __name__ == "__main__":
    num = int(input("Enter number of piles: "))
    res = stone_plie(num)
    print(res)