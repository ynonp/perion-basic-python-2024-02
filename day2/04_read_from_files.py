f = open('data.txt', encoding='utf8')
for line in f:
    print(line)
f.close()

f = open('data.txt', encoding='utf8')
all_the_text = f.read()
print(f"File has {len(all_the_text)} characters")
f.close()
