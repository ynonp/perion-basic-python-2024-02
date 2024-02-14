"""
Solutions to:
https://www.tocode.co.il/bundles/python/lessons/05-intro-lab?tab=text
"""

def ex_01():
    print("How old are you (in years) ?")
    age_in_years = int(input())
    age_in_months = age_in_years * 12
    print(f"Wow you are {age_in_months} months old")


def ex_02():
    print("How old are you (in months) ?")
    age_in_months = int(input())
    age_in_years = age_in_months / 12
    print(f"Wow you are {age_in_years} years old")
    # Read more about f-strings in python:
    # http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf
    print(f"Wow you are {age_in_years:0.2} years old")

    years = age_in_months // 12
    months = age_in_months % 12
    if months > 0:
        print(f"Wow you are {years} years and {months} months old")
    else:
        print(f"Wow you are {years} years old")

def ex_03():
    print("pick a number")
    num = int(input())
    if num % 7 == 0:
        print("Boom!")


def ex_04():
    print("pick a number")
    # num is still a string
    num: str = input()
    # character in string => is character in the string
    if '7' in num or int(num) % 7 == 0:
        print("Boom!")

def ex_05():
    x = int(input("First number: "))
    y = int(input("Second number: "))
    z = int(input("Third number: "))
    # I found max in python built-in functions
    # https://docs.python.org/3/library/functions.html
    print(max(x, y, z))

ex_05()
