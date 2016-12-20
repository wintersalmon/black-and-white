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

class TilePlacementChoiceSelector(ChoiceSelector):
    '''
    Choices for Tile Placement
    '''
    def __init__(self, board, board_drawer):
        super().__init__()

        self.board = board
        self.board_drawer = board_drawer

        self.tile = None
        self.row = 0
        self.col = 0
        self.direction = DIRECTION.RIGHT

        self.add_choice(['N', 'n'], self.action_create_random_tile, 'New')
        self.add_choice(['U', 'u'], self.action_move_up, 'Up')
        self.add_choice(['R', 'r'], self.action_move_right, 'Right')
        self.add_choice(['D', 'd'], self.action_move_down, 'Down')
        self.add_choice(['L', 'l'], self.action_move_left, 'Left')
        self.add_choice(['T', 't'], self.action_rotate, 'roTate')
        self.add_choice(['S', 's'], self.action_save, 'Save')
        self.add_choice(['E', 'e'], self.action_exit, 'Exit')


    def action_create_random_tile(self):
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

        self.tile = tile
        self.row = 0
        self.col = 0
        self.direction = DIRECTION.RIGHT
        self.board_drawer.set_marker(self.tile, self.row, self.col, self.direction)


    def action_move_up(self):
        '''
        action to move up
        '''
        self.row -= 1
        self.board_drawer.set_marker(self.tile, self.row, self.col, self.direction)
        return False


    def action_move_down(self):
        '''
        action to move up
        '''
        self.row += 1
        self.board_drawer.set_marker(self.tile, self.row, self.col, self.direction)
        return False


    def action_move_right(self):
        '''
        action to move right
        '''
        self.col += 1
        self.board_drawer.set_marker(self.tile, self.row, self.col, self.direction)
        return False


    def action_move_left(self):
        '''
        action to move left
        '''
        self.col -= 1
        self.board_drawer.set_marker(self.tile, self.row, self.col, self.direction)
        return False


    def action_rotate(self):
        '''
        action to rotate
        '''
        self.direction = DIRECTION.rotate(self.direction)
        self.board_drawer.set_marker(self.tile, self.row, self.col, self.direction)
        return False


    def action_save(self):
        '''
        action to save
        '''
        if self.tile and self.board.can_place_tile(self.tile, self.row, self.col, self.direction):
            self.board.place_tile(self.tile, self.row, self.col, self.direction)
            self.tile = None
            self.row = 0
            self.col = 0
            self.direction = DIRECTION.RIGHT
            self.board_drawer.reset_marker()
        return False


    def action_exit(self):
        '''
        action to rotate
        '''
        return True
