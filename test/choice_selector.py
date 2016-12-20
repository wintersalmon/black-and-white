'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Contains ChoiceSelectors
'''

import random

from test.choice import Choice
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


class TilePlacementChoiceSelector():
    '''
    Choices for Tile Placement
    '''
    def __init__(self):
        self.choices = list()

        choice_up = Choice(['U', 'u'], action_move_up, 'Up')
        choice_right = Choice(['R', 'r'], action_move_right, 'Right')
        choice_down = Choice(['D', 'd'], action_move_down, 'Down')
        choice_left = Choice(['L', 'l'], action_move_left, 'Left')
        choice_rotate = Choice(['T', 't'], action_rotate, 'roTate')
        choice_save = Choice(['S', 's'], action_save, 'Save')
        choice_exit = Choice(['E', 'e'], action_exit, 'Exit')

        self.choices.append(choice_up)
        self.choices.append(choice_down)
        self.choices.append(choice_right)
        self.choices.append(choice_left)
        self.choices.append(choice_rotate)
        self.choices.append(choice_save)
        self.choices.append(choice_exit)


    def show_full_choices(self):
        '''
        shows full choice list
        '''
        for choice in self.choices:
            print(choice.get_full_statement(), end=' ')


    def find_matching_action(self, selection):
        '''
        returns choice action that matches user input
        '''
        for choice in self.choices:
            if selection in choice:
                return choice.get_action()
        return None


    def choice_user_selection(self):
        '''
        returns choice action that matches user input
        '''
        self.show_full_choices()
        selction = input(' : ')
        return self.find_matching_action(selction)


    def get_choices(self):
        '''
        returns choice list
        '''
        return self.choices
