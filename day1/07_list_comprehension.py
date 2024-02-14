"""
List Comprehension - build a list from another list
It's actually a combination of "map" and "filter"
"""

l = [10, 20, 30, 40]
# Take all the values that are < 30
small_values = [v for v in l if v < 30]

numbers = range(100)
squares = [x * x
           for x in numbers]

# Define f() and p(), and run comprehension
# new_list = [f(x) for x in old_list if p(x)]
import string
print([
    a + b + c
    for a in string.ascii_lowercase
    for b in string.ascii_lowercase
    for c in string.ascii_lowercase
])

