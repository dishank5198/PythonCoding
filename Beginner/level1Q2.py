def count_alpha_num(str_):
    num_counter = 0
    alpha_counter = 0
    for x in str_:
        if x.isnumeric():
            num_counter += 1
        elif x.isalpha():
            alpha_counter += 1
    return num_counter, alpha_counter


if __name__ == "__main__":
    string_ip = str(input("Enter a string: "))
    num_count, aplha_count = count_alpha_num(string_ip)
    print(f"Alphabets: {aplha_count}, Number: {num_count}")