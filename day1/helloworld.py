"""
0. Comments ...
1. Variables (scope)
2. Loops, if, (control structures)
3. Functions
4. IO (print, input, files)
5. Ecosystem (install external packages)
"""

"""
0. Comments
I use the three quotes or # to create a comment
"""

# this is also a comment (line comment)

"""
1. Variables
Variables don't have type (but we can "hint" on one)
We define variables by assignment
"""
x = 10
y = "hello world"
z = 8.12
t = True

"""
2. Ifs and loops
"""
if x < 20:
    y = "it's small"
    z = 90
    t = False
elif x < 50:
    y = "it's medium"
else:
    y = "it's large"

for i in range(10):
    print(f"i = {i}")


"""
3. Functions
The command "def" defines a function
Use: def <function_name>(param1, param2, param3):
        block
"""


def twice(x: int) -> int:
    return x * 2

# Same as:
def same_twice(x):
    return x * 2


print("who are you?")
name = input()
print(f"welcome, Mr. {name}")

print("and what's your favorite number?")
favorite_number = int(input())
print(f"I like this one because when you add 1 you get: {favorite_number + 1}")

story = """wow I type
multi line strings
so every newline will be
a real new line"""

print(twice("hello"))

"""
Install external packages from pycharm
PyCharm Menu (or File) -> 
    Settings -> 
    Left Side Project ->
    Python Interpreter ->
    Click "+" ->
    Select Package ->
    Click "Install" 
"""




