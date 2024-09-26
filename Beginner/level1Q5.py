def factorial(num):
    final_prod = 1
    if num == 0 or num == 1:
        return final_prod
    for i in range(num, 0, -1):
        final_prod = final_prod*i

    return final_prod


if __name__ == "__main__":
    num_for_fact = int(input("Enter a number who's factorial you want to find: "))
    ans = factorial(num_for_fact)
    print("Factorial of {num} is {ans}".format(num=num_for_fact, ans=ans))