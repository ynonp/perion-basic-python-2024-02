from day3.board import Board, Move

def test_x_plays_at_0_0():
    game = Board()
    game.play(Move('X', 0, 0))
    assert game.grid[0][0] == 'X'

def test_game_over_1():
    game = Board("""
    . . .
    . O .
    X O X
    """)
    assert game.game_over() == False

def test_game_over_2():
    game = Board("""
    X O X
    O O X
    X O X
    """)
    assert game.game_over() == True


def test_parse_board():
    game = Board("""
. . .
. O .
X O X
""")

    assert game.grid[1][1] == 'O'
