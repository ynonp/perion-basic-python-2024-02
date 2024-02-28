import itertools
from board import Board

class Player:
    ...

# Ex 1
# game_over and status only finish on tie
# play until the board is full
# Create class Player to make the follwing code work
# Create data class "Move" to represent a move in the game (player + row + column)

# Bonus-
# Apply game rules

board = Board()
players = itertools.cycle([Player('X'), Player('O')])

while not board.game_over():
    player = next(players)
    move = player.get_next_move(board)
    board.play(move)

# status ->
# prints either "X Won", "O Won" or "Tie"
print(board.status())

