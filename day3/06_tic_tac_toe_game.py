class Board:
    ...

game = Board()
game.play(player='X', row=0, column=1)
game.play(player='O', row=1, column=1)
# draws the board:
# . X .
# . O .
# . . .
print(game)



# Bonus-
# Create a Board from an existing image
start = Board("""
. X .
. O .
. . .
""")

start.play('O', 2, 2)
print(start)
# . X .
# . O .
# . . O



