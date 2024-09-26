with open('demo.txt', 'r') as f:
    read_buff = f.buffer
    new_str = read_buff.readlines()
    count = len(new_str)
    print(count)
    f.close()
