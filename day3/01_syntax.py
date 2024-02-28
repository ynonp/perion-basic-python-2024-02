class Person:
    age = 0

    def __str__(self):
        return f"Person [{self.age=}]"

    def __repr__(self):
        return self.__str__()

    def grow_up(self):
        self.age += 1

    def hi(self):
        if 0 <= self.age <= 120:
            print(f"Hi! I'm {self.age} years old")
        else:
            print("--- Dead ---")

def grow_up_everybody(people):
    for person in people:
        person.grow_up()

people = [Person() for _ in range(10)]
grow_up_everybody(people)

print(people)



# can say hi - it's alive
# p.hi()
# for i in range(200):
#     p.grow_up()
#     # can't say hi - it's dead
#     p.hi()