def gcd(x, y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x


def lcm(x, y):
    l_cm = (x*y)/gcd(x, y)
    return l_cm


if __name__ == "__main__":
    x = int(input("Enter number 1 for lcm: "))
    y = int(input("Enter number 2 for lcm: "))
    lcm_ = lcm(x, y)
    print("LCM of the numbers is: "+str(int(lcm_)))