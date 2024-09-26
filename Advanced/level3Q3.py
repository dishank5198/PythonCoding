def JtoI(w: str):
    w = w.replace('j', "J")
    w = w.replace('J', "I")
    return w


with open('word.txt', 'r') as file:
    content = file.read()
    for w in content.split(','):
        w = w.rstrip(',.')
        w = JtoI(w)
        print(w)

    file.close()
