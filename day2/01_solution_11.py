# Python Modue Index
# https://docs.python.org/3/py-modindex.html

# All Exceptions in python
# https://docs.python.org/3/library/exceptions.html

from random import randint

max_number = float("-inf")

def read_number():
    while True:
        try:
            return float(input())
        except Exception as err:
            print("Sorry, that's not a number")

def ex1():
    for i in range(10):
        x = read_number()
        if x > max_number:
            max_number = x

    print(max_number)

def ex2():
    age_in_months = read_number()
    print(age_in_months / 12)

def ex3():
    text = []
    while True:
        line = input()
        if line == "":
            break
        else:
            text.append(line)
    for line in text[::-1]:
        print(line)

    print('\n'.join(text[::-1]))


def ex4():
    while True:
        n = randint(1, 1_000_000)
        if n % 7 == 0 and n % 13 == 0 and n % 15 == 0:
            print(n)
            return

