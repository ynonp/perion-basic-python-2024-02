def copy(source, destination):
    with open(source, 'rb') as fin:
        with open(destination, 'wb') as fout:
            fout.write(fin.read())

with open('data3.txt', 'rb') as fin:
    for line in fin:
        print(line)