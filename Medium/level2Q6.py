def pow_of_2(num):
    if num == 1:
        return True
    elif num % 2 != 0:
        return False
    else:
        return pow_of_2(num//2)


if __name__ == "__main__":
    num = int(input("Enter a number to check power of 2: "))
    res = pow_of_2(num)
    print(res)