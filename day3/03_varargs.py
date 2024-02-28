def sum_squares(*numbers):
    # return sum(i * i for i in numbers)
    result = 0
    for i in numbers:
        result += i * i
    return result


def longer_than(n, *texts):
    return [t for t in texts if len(t) > n]


def key_with_max_value(**d):
    return sorted(d.keys(), key=d.get)[-1]

print(sum_squares(1, 2, 5, 8))
print(sum_squares(*range(8)))
print(longer_than(4, 'wow', 'I can write texts', 'without []'))
print(key_with_max_value(a=7, b=20, c=2))

d = {'a': 7, 'b': 20, 'c': 2}
print(key_with_max_value(**d))


def wow(name, age):
    ...

wow(name='demo', age=2)
wow(age=2, name='demo')

