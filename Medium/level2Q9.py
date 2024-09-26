def index_err(a: list, index: int):
    try:
        ele_ = a[index]
        print(ele_)
    except:
        print("Index {i} is out of range.".format(i=index))


if __name__ == "__main__":
    a = [20, 33, 76, 97, 1]
    index = int(input("Enter the index to retrive: "))
    index_err(a, index)