def perfect_num(num):
    perfect_divisor = []
    if num <= 0:
        return "No"
    elif num == 1:
        return "Yes"
    for i in range(1, num):
        if num % i == 0:
            perfect_divisor.append(i)
    if sum(perfect_divisor) == num:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    num = int(input("Enter the number to check for perfect number: "))
    res = perfect_num(num)
    print("{number}: {re}".format(number=num, re=res))