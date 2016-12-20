'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Main Test
'''

import random

from cli.board_drawer import BoardDrawer
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

    tile = create_random_tile()
    row = 0
    col = 0
    direction = DIRECTION.RIGHT

    while True:
        board_drawer.set_marker(tile, row, col, direction)
        board_drawer.draw_color()

        choices = ['U', 'R', 'D', 'L', 'T', 'S', 'E']
        choices_lower = ['u', 'r', 'd', 'l', 't', 's', 'e']
        choice_descriptions = ['Up', 'right', 'Down', 'Left', 'Turn', 'Save', 'Exit']
        print(row, col, direction)
        for des, key, key_sub in zip(choice_descriptions, choices, choices_lower):
            print(des  + '(' + key + '|' + key_sub + ')', end=' ')
        user_choice = input(' : ')
        if user_choice in choices or user_choice in choices_lower:
            if user_choice == 's' or user_choice == 'S':
                if board.can_place_tile(tile, row, col, direction):
                    board.place_tile(tile, row, col, direction)
                    tile = create_random_tile()
                    row = 0
                    col = 0
                    direction = DIRECTION.RIGHT
            if user_choice == 'r' or user_choice == 'R':
                if col + 1 < max_col:
                    col += 1
            if user_choice == 'l' or user_choice == 'L':
                if col - 1 >= 0:
                    col -= 1
            if user_choice == 'd' or user_choice == 'D':
                if row + 1 < max_row:
                    row += 1
            if user_choice == 'u' or user_choice == 'U':
                if row - 1 >= 0:
                    row -= 1
            if user_choice == 't' or user_choice == 'T':
                direction = DIRECTION.rotate(direction)
            if user_choice == 'e' or user_choice == 'E':
                break


if __name__ == "__main__":
    print('welcome to black and white Test')
    test_board_tile_placing()
