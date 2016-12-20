'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Main Test
'''

import random

from cli.board_drawer import BoardDrawer
from cli.choice.tile_placement_choice_selector import TilePlacementChoiceSelector
from data.board.board import Board
from data.board.tile import TileWW, TileWG, TileWB, TileGB
from data.board.direction import DIRECTION


def create_board_type_one(max_row, max_col):
    '''
    Method Description
    '''
    board = Board(max_row, max_col)

    for row in range(max_row):
        for col in range(max_col-1):
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
            board.place_tile(tile, row, col, direction)

    return board


def create_random_tile():
    '''
    returns random type of tile
    '''
    tile_type = random.randrange(0, 4)

    if tile_type == 0:
        tile = TileWW()
    elif tile_type == 1:
        tile = TileWG()
    elif tile_type == 2:
        tile = TileWB()
    else:
        tile = TileGB()

    return tile


def test_board():
    '''
    test board create and print
    '''
    max_row = 5
    max_col = 12
    board = create_board_type_one(max_row, max_col)
    board_drawer = BoardDrawer(board)

    board_drawer.draw_color()
    board_drawer.draw_overlap_counter()

def test_board_tile_placing():
    '''
    test board tile placing
    '''
    max_row = 5
    max_col = 12
    board = Board(max_row, max_col)
    board_drawer = BoardDrawer(board)

    tile_placement_choices = TilePlacementChoiceSelector(board, board_drawer)

    result = False
    while not result:
        board_drawer.draw_color()

        action = tile_placement_choices.choice_user_selection()
        if action:
            result = action()


if __name__ == "__main__":
    print('welcome to black and white Test')
    test_board_tile_placing()
