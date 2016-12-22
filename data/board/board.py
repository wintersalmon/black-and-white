'''
BLACK-AND-WHITE
WinterSalmon
This module contains classes about board
'''


# from collections import namedtuple
from data.board.tile import Tile
from data.board.block import Block
from data.board.direction import DIRECTION
from data.board.color import COLOR


class Board():
    '''
    This class contains data about board
    '''
    def __init__(self, row_count, col_count):
        self.row_count = row_count
        self.col_count = col_count
        self.tiles = [[None for col in range(self.col_count)] for row in range(self.row_count)]
        self.blocks = [[Block() for col in range(self.col_count)] for row in range(self.row_count)]
        self.block_counts = [[0 for col in range(self.col_count)] for row in range(self.row_count)]


    def get_row_count(self):
        '''
        returns board max row count
        '''
        return self.row_count


    def get_col_count(self):
        '''
        returns board max column count
        '''
        return self.col_count


    def get_block_overlap_count(self, row, col):
        '''
        returns overlapped block counts located on [row,col]
        '''
        if self.__check_row_col_boundary(row, col):
            return self.block_counts[row][col]
        else:
            return -1


    def get_block_color(self, row, col):
        '''
        returns color of the block located on [row,col]
        '''
        if self.__check_row_col_boundary(row, col):
            return self.blocks[row][col].get_color()
        else:
            return COLOR.NOCOLOR


    def can_place_tile(self, tile, row, col, direction):
        '''
        Check if the new tile location satisfies every Tile Placement Rule
        '''
        if not isinstance(tile, Tile):
            return False
        if not self.__check_tile_on_board(row, col, direction):
            return False
        if not self.__check_tile_overlapping(row, col, direction):
            return False
        if not self.__check_tile_adjacent_color(tile, row, col, direction):
            return False
        return True


    def place_tile(self, tile, row, col, direction):
        '''
        If possible add tile to specific location [row][col]+direction
        '''
        if self.can_place_tile(tile, row, col, direction):
            self.__add_tile(tile, row, col, direction)
            return True
        else:
            return False


    def __add_tile(self, tile, row, col, direction):
        '''
        Adds Tile to [row][col]+direction
        '''
        self.tiles[row][col] = (tile, direction)

        first_block = tile.get_block(0)
        self.__add_block(first_block, row, col)

        second_block = tile.get_block(1)
        ad_row, ad_col = DIRECTION.adjust_row_col_by_direction(row, col, direction)
        self.__add_block(second_block, ad_row, ad_col)


    def __add_block(self, block, row, col):
        '''
        Adds Block to [row][col]
        '''
        self.blocks[row][col].mix_color(block.get_color())
        self.block_counts[row][col] += 1


    def __check_tile_on_board(self, row, col, direction):
        '''
        Check if the new tile location does not violate Boundary Rule
        Boundary Rule : tile should be placed with in the board boundary
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


    def __check_tile_overlapping(self, row, col, direction):
        '''
        Check if the new tile location does not violate Overlapping Rule
        Overlapping Rule : no more then two tiles can overlap in one block
        '''
        if self.block_counts[row][col] >= 2:
            return False

        second_row = row
        second_col = col
        if direction == DIRECTION.LEFT:
            second_col -= 1
        if direction == DIRECTION.RIGHT:
            second_col += 1
        if direction == DIRECTION.UP:
            second_row -= 1
        if direction == DIRECTION.DOWN:
            second_row += 1

        if self.block_counts[second_row][second_col] >= 2:
            return False

        return True


    def __check_tile_adjacent_color(self, tile, row, col, direction):
        '''
        Check if the new tile location does not violate Adjacent Color Rule
        Adjacent Color Rule : Black(or Gray) should not be placed adjancet to itself
        '''
        block_one_color = tile.get_block(0).get_color()
        block_two_color = tile.get_block(1).get_color()

        compare_colors = [COLOR.GRAY, COLOR.BLACK]

        if block_one_color in compare_colors:
            block_one_adjacent_colors = self.__get_adjacent_block_color(row, col)
            if block_one_color in block_one_adjacent_colors:
                return False

        if block_two_color in compare_colors:
            block_two_adjacent_colors = self.__get_adjacent_block_color(row, col, direction)
            if block_two_color in block_two_adjacent_colors:
                return False

        return True


    def __get_adjacent_block_color(self, row, col, direction=DIRECTION.NODIRECTION):
        '''
        returns a list containing adjacent block colors
        '''
        adjacent_colors = list()

        if direction != DIRECTION.NODIRECTION:
            ad_row, ad_col = DIRECTION.adjust_row_col_by_direction(row, col, direction)
            success = self.__check_row_col_boundary(ad_row, ad_col)
            if success:
                row = ad_row
                col = ad_col
            else:
                return adjacent_colors

        # GET UP BLOCK
        if row > 0:
            color = self.blocks[row-1][col].get_color()
            adjacent_colors.append(color)

        # GET DOWN BLOCK
        if row < self.row_count - 1:
            color = self.blocks[row+1][col].get_color()
            adjacent_colors.append(color)

        # GET LEFT BLOCK
        if col > 0:
            color = self.blocks[row][col-1].get_color()
            adjacent_colors.append(color)

        # GET RIGHT BLOCK
        if col < self.col_count -1:
            color = self.blocks[row][col+1].get_color()
            adjacent_colors.append(color)

        return adjacent_colors


    def __check_row_col_boundary(self, row, col):
        '''
        returns True if [row][col] is inside the board
        '''
        if row < 0 or row >= self.row_count:
            return False
        if col < 0 or col >= self.col_count:
            return False
        return True
