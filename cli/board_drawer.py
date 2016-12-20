'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Class Description
'''


from data.board.board import Board
from data.board.direction import DIRECTION
from data.board.color import COLOR


class BoardDrawer():
    '''
    Class Description
    '''
    def __init__(self, board):
        self.board = board
        self.row_count = board.get_row_count()
        self.col_count = board.get_col_count()
        self.tile_marker = [[None for col in range(self.col_count)] for row in range(self.row_count)]


    def draw_color(self):
        '''
        Method Description
        '''
        if self.board:
            for row in range(self.board.get_row_count()):
                for col in range(self.board.get_col_count()):
                    color = self.board.get_block_color(row, col)
                    if self.tile_marker[row][col]:
                        overlap_color = self.tile_marker[row][col].get_color()
                        mixed_color = COLOR.mix_color(color, overlap_color)
                        color_text = color.get_color_text(mixed_color)
                        color_text = '[' + color_text + ']'
                    else:
                        color_text = color.get_color_text(color)
                    print(color_text, end='\t')
                print('')
        else:
            print('board not initialized')


    def draw_overlap_counter(self):
        '''
        Method Description
        '''
        if self.board:
            for row in range(self.board.get_row_count()):
                for col in range(self.board.get_col_count()):
                    counter = self.board.get_block_overlap_count(row, col)
                    print(counter, end='\t')
                print('')
        else:
            print('board not initialized')


    def reset_marker(self):
        '''
        Method Description
        '''
        for row in range(self.row_count):
            for col in range(self.col_count):
                self.tile_marker[row][col] = None


    def set_tile_marker(self, tile, row, col, direction):
        '''
        Method Description
        '''
        if self.board.can_place_tile(tile, row, col, direction):
            self.reset_marker()

            self.tile_marker[row][col] = tile.get_block(0)

            ad_row, ad_col = DIRECTION.adjust_row_col_by_direction(row, col, direction)
            self.tile_marker[ad_row][ad_col] = tile.get_block(1)
