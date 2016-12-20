'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Main Test
'''

from gui.board_drawer import BoardDrawer
from data.board.board import Board
from data.board.tile import TileWW, TileWG, TileWB, TileGB
from data.board.direction import DIRECTION


def test_board():
    '''
    Method Description
    '''
    row_count = 5
    col_count = 12
    board = Board(row_count, col_count)
    board_drawer = BoardDrawer(board)

    board_drawer.draw_color()
    board_drawer.draw_overlap_counter()
    for row in range(row_count):
        for col in range(col_count-1):
            tile = None
            if col%3 == 0:
                tile = TileWW()
            elif col%3 == 1:
                tile = TileWG()
            elif col%3 == 2:
                tile = TileWB()
            else:
                tile = TileGB()

            direction = DIRECTION.RIGHT
            result = board.place_tile(tile, row, col, direction)
            print(row, col, result)
    board_drawer.draw_color()
    board_drawer.draw_overlap_counter()


if __name__ == "__main__":
    print('welcome to black and white Test')
    test_board()
