def pwd_check(og_pass: str, re_pwd: str):

    if og_pass == re_pwd:
        return True
    else:
        return False


def re_enter_pass(og_pass: str, attempt: int):
    re_pwd = str(input("Re-Enter User Password: "))
    resp = pwd_check(og_pass, re_pwd)
    if resp:
        return "Success!"
    else:
        if attempt < 3:
            attempt += 1
            print("Passwords don't match")
            return re_enter_pass(og_pass, attempt)
        else:
            return "Failure"


if __name__ == "__main__":
    attempt = 1
    usr_name = str(input("Enter User Name: "))
    og_pwd = str(input("Enter User Password: "))
    result = re_enter_pass(og_pwd, attempt)
    print(result)