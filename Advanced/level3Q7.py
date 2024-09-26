def create_dict(a: list, b: list):
    new_dict = dict()
    for x, y in zip(a, b):
        new_dict[x] = y
    return new_dict


if __name__ == "__main__":
    a = ['Sam', 'Alice', 'Mona']
    b = ['Commerce', 'Science', 'Computer']
    res = create_dict(a, b)
    print(res)
