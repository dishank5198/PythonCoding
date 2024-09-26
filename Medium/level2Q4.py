def rotate_arr(a: list, d: int):
    rotated_arr = [0]*len(a)
    for x in a:
        new_index = a.index(x) - d
        rotated_arr[new_index] = x
    return rotated_arr


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    move_by = 2
    res = rotate_arr(a, move_by)
    print(res)