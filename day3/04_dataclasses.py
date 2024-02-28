from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    email: str


u = User(id=1, email='user@test.com')
t = User(id=2, email='another@test.com')
r = User(id=1, email='user@test.com')

print(u)
if u == r:
    print("yay")

