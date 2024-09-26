def rev_num(num1):
    rev_number1 = 0
    while num1 > 0:
        r = num1 % 10
        num1 = num1 // 10
        rev_number1 = (rev_number1*10) + r
    return rev_number1


if __name__ == "__main__":
    num1 = int(input("Enter a number: "))
    rev_number = rev_num(num1)
    print(rev_number)