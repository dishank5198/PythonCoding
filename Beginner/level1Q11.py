def sum_of_digit(num):
    if len(str(num)) == 1:
        return num
    sum_digit = 0
    while num > 0:
        q = num//10
        r = num % 10
        sum_digit += r
        num = q
        if len(str(sum_digit)) > 1 and num == 0:
            num = sum_digit
            sum_digit = 0
    return sum_digit


if __name__ == "__main__":
    num1 = int(input("Enter a number: "))
    res = sum_of_digit(num1)
    print(res)