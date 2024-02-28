from day3.board import Board

def test_x_plays_at_0_0():
    game = Board()
    game.play('X', 0, 0)
    assert game.grid[0][0] == 'X'

def test_parse_board():
    game = Board("""
. . .
. O .
X O X
""")

    assert game.grid[1][1] == 'O'
