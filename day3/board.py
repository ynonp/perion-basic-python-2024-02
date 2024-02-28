from dataclasses import dataclass

@dataclass(frozen=True)
class Move:
    player: str
    row: int
    column: int

class Board:
    grid = [['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]

    def __init__(self, initial_state = None):
        if initial_state is not None:
            self.grid = Board.read_grid_from_string(initial_state)

    def play(self, move):
        self.grid[move.row][move.column] = move.player

    def __str__(self):
        return '\n'.join(
            ' '.join(row) for row in self.grid)

    def game_over(self):
        return '.' not in str(self)

    @staticmethod
    def read_grid_from_string(grid_string):
        return [r.split(' ')
                for r in grid_string.strip().split('\n')]


# The special variable __name__ contains either:
# If the program was started ON THIS FILE => __main__
# If this file was loaded as "import" => filename
if __name__ == "__main__":
    game = Board()
    game.play(player='X', row=0, column=1)
    game.play(player='O', row=1, column=1)
    # draws the board:
    # . X .
    # . O .
    # . . .
    print(game)