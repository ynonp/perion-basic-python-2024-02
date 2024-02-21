with open('data.txt', encoding='utf8') as f:
    for line in f:
        print(line)


with open('data2.txt', encoding='utf8') as f:
    print(f.read())

with open('data3.txt', encoding='iso8859-1') as f:
    print(f.read())

with open('output.txt', 'w', encoding='utf8') as f:
    f.write("hello world\n")


# f.__enter__()
# f.__exit__()