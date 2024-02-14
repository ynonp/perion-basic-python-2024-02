"""
Working with lists
(see 04_strings.py)

1. Create a list with: [10, 20, 30, 40]
2. Use any data type you need: ['a', 'b', 30, 40, [1, 2, 3], True]
3. len(l) -> return length of list
4. l.append(10) -> add item to list
5. l[...] -> return an item from a list
6. 10 in l -> check if item is in list
7. for item in l: -> iterate

"""

import copy
l = [10, 20, 30, 40]
j = copy.copy(l)
t = l[:]

x = 10
if x in l:
    print("10 is in the list")

for item in l:
    print(item)

