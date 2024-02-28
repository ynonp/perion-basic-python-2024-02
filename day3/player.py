from day3.board import Move

class Player:
    def __init__(self, ch):
        self.ch = ch

    def get_next_move(self, board):
        print(f"Ok player {self.ch}, what's your next move?")
        print(board)
        next_move = input()
        row, column = next_move.split()
        return Move(self.ch, int(row), int(column))