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
