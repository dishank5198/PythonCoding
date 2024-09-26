def num_divisibilty(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Consultadd - Python Training")
    elif num % 5 == 0:
        print("Python Training")
    elif num % 3 == 0:
        print("Consultadd")
    else:
        print("Number not divisible by 3 or 5")


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    num_divisibilty(number)
