# Write a class called Summer to make the following code work
class Summer:
    total = 0

    def add(self, n):
        self.total += n


s = Summer()
t = Summer()

s.add(10)
s.add(20)
# Bonus: make this work
# s.add(30, 40)
s.add(30)

t.add(50)

# prints: 60 (in the bonus prints 130)
print(s.total)

# prints: 50
print(t.total)
