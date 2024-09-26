with open('hello.txt', 'r') as file:
    content = file.read()
    file.close()
content_lst = content.split(" ")
for x in content_lst:
    if len(x) % 2 == 0:
        print(x)