'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Contains TilePlacementChoiceSelector
'''


import random

from cli.choice.choice_selector import ChoiceSelector
from data.board.tile import TileWW, TileWG, TileWB, TileGB
from data.board.direction import DIRECTION


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


def action_move_up(tile, row, col, direction, board=None):
    '''
    action to move up
    '''
    return tile, row - 1, col, direction


def action_move_down(tile, row, col, direction, board=None):
    '''
    action to move up
    '''
    return tile, row + 1, col, direction


def action_move_right(tile, row, col, direction, board=None):
    '''
    action to move right
    '''
    return tile, row, col + 1, direction


def action_move_left(tile, row, col, direction, board=None):
    '''
    action to move left
    '''
    return tile, row, col - 1, direction


def action_rotate(tile, row, col, direction, board=None):
    '''
    action to rotate
    '''
    return tile, row, col, DIRECTION.rotate(direction)


def action_save(tile, row, col, direction, board=None):
    '''
    action to save
    '''
    if board.can_place_tile(tile, row, col, direction):
        board.place_tile(tile, row, col, direction)
        tile = create_random_tile()
        row = 0
        col = 0
        direction = DIRECTION.RIGHT
    return tile, row, col, direction


def action_exit(tile, row, col, direction, board=None):
    '''
    action to rotate
    '''
    exit()


class TilePlacementChoiceSelector(ChoiceSelector):
    '''
    Choices for Tile Placement
    '''
    def __init__(self):
        super().__init__()
        self.add_choice(['U', 'u'], action_move_up, 'Up')
        self.add_choice(['R', 'r'], action_move_right, 'Right')
        self.add_choice(['D', 'd'], action_move_down, 'Down')
        self.add_choice(['L', 'l'], action_move_left, 'Left')
        self.add_choice(['T', 't'], action_rotate, 'roTate')
        self.add_choice(['S', 's'], action_save, 'Save')
        self.add_choice(['E', 'e'], action_exit, 'Exit')
