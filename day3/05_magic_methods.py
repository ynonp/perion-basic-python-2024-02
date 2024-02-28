import random
from dataclasses import dataclass

@dataclass(frozen=True)
class Song:
    name: str

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = [Song(name=song) for song in songs]

    def __iter__(self):
        return iter(self.songs)




class Rope:
    def __init__(self, size=None):
        if size:
            self.size = size
        else:
            self.size = random.randint(0, 100)

    def __len__(self):
        return self.size

    def __str__(self):
        return f"Rope [{self.size=}]"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, Rope):
            return Rope(size=self.size + other.size)
        elif isinstance(other, int):
            return Rope(size=self.size + other)
        else:
            raise Exception(f"Unsupported Operation Rope + {type(other)}")



for song in Album("a", "b", "c", "d"):
    print(song.name)


r = Rope()
t = Rope()
print(t)
print(len(r))
print(r)
print([r, r, r])
print(r + t)
