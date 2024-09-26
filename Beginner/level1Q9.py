def num_freq(num_lst):
    num_lst = list(num_lst)
    freq_count = dict()
    for x in num_lst:
        if x not in freq_count:
            freq_count[x] = 1
        else:
            freq_count[x] = freq_count.get(x)+1
    return freq_count


if __name__ == "__main__":
    freq_counter = num_freq([1,2,3,4,2,1,5,6,5,2,3,3,4])
    print(freq_counter)