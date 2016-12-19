'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Class Name
'''
# from collections import namedtuple
from data.board.tile import Tile
from data.board.block import Block
from data.board.direction import DIRECTION

class Board():
    '''
    Class Description
    '''
    def __init__(self, row_count, col_count):
        self.row_count = row_count
        self.col_count = col_count
        self.tiles = [[None for col in range(self.col_count)] for row in range(self.row_count)]
        self.blocks = [[Block() for col in range(self.col_count)] for row in range(self.row_count)]

    def clear(self):
        '''
        Method Description
        '''
        # del self.tiles[:]
        # del self.blocks[:]
        self.tiles = [[None for col in range(self.col_count)] for row in range(self.row_count)]
        self.blocks = [[Block() for col in range(self.col_count)] for row in range(self.row_count)]

    def get_block_color(self, row, col):
        '''
        Method Description
        '''
        return self.blocks[row][col].get_color()

    def place_tile(self, tile, row, col, direction):
        '''
        Method Description
        '''
        # Todo : Verify tile overlap, adjacent color
        if not isinstance(tile, Tile):
            return False
        if not self.is_tile_on_board(row, col, direction):
            return False
        if not self.check_tile_adjacent_color(tile, row, col, direction):
            return False

        self.__add_tile(tile, row, col, direction)

        return True

    def __add_tile(self, tile, row, col, direction):
        '''
        Method Description
        '''
        self.tiles[row][col] = tile

        block_one = tile.get_block(0)
        block_two = tile.get_block(1)

        color_one = block_one.get_color()
        color_two = block_two.get_color()

        self.blocks[row][col].mix_color(color_one)

        if direction == DIRECTION.LEFT:
            self.blocks[row][col-1].mix_color(color_two)
        if direction == DIRECTION.RIGHT:
            self.blocks[row][col+1].mix_color(color_two)
        if direction == DIRECTION.UP:
            self.blocks[row-1][col].mix_color(color_two)
        if direction == DIRECTION.DOWN:
            self.blocks[row+1][col].mix_color(color_two)

    def is_tile_on_board(self, row, col, direction):
        '''
        Method Description
        '''
        min_row_correction_value = 0
        max_row_correction_value = self.row_count
        min_col_correction_value = 0
        max_col_correction_value = self.col_count

        if direction == DIRECTION.LEFT:
            min_col_correction_value += 1
        if direction == DIRECTION.RIGHT:
            max_col_correction_value -= 1
        if direction == DIRECTION.UP:
            min_row_correction_value += 1
        if direction == DIRECTION.DOWN:
            max_row_correction_value -= 1

        if row < min_row_correction_value or row >= max_row_correction_value:
            return False
        if col < min_col_correction_value or col >= max_col_correction_value:
            return False

        return True

    def check_tile_adjacent_color(self, tile, row, col, direction):
        '''
        Method Description
        '''
        return True
