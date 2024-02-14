"""
Working with strings:

1. len('hello') => 'hello'.__len__() => length of string
2. 'hello'[...] => get character
3. 'l' in 'hello' => 'hello'.__contains__('l')
4. for ch in 'hello' => iterate the characters
5. 'hello'[::-1] => reverse
6. 'hello'[2] => get third character
7. 'hello'[2:5]
8. 'hello'.index('e')
9. str() => convert something to string
10. int('73') => convert string to integer
"""

# return sum of digits of n
def sum_of_digits(n):
    result = 0
    for ch in str(n):
        result += int(ch)
    return result

# print 10
print(sum_of_digits(82))







