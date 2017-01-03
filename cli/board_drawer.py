'''
BLACK-AND-WHITE
WinterSalmon
Class Description
'''


from game.board.direction import DIRECTION
from game.board.color import COLOR


class BoardDrawer():
    '''
    Class Description
    '''
    def __init__(self, board):
        self.board = board
        self.row_count = board.get_row_count()
        self.col_count = board.get_col_count()
        self.marker = [[None for col in range(self.col_count)] for row in range(self.row_count)]
        self.b_marker = [[None for col in range(self.col_count)] for row in range(self.row_count)]


    def draw_color(self):
        '''
        Method Description
        '''
        if self.board:
            for row in range(self.board.get_row_count()):
                for col in range(self.board.get_col_count()):
                    color = self.board.get_block_color(row, col)
                    if self.marker[row][col]:
                        if self.b_marker[row][col]:
                            overlap_color = self.marker[row][col].get_color()
                            mixed_color = COLOR.mix_color(color, overlap_color)
                            color_text = color.get_color_text(mixed_color)
                            color_text = '[' + color_text + ']'
                        else:
                            overlap_color = self.marker[row][col].get_color()
                            mixed_color = COLOR.mix_color(color, overlap_color)
                            color_text = color.get_color_text(mixed_color)
                            color_text = '<' + color_text + '>'
                    else:
                        color_text = color.get_color_text(color)
                    print(color_text, end='\t')
                print('\n')
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
                print('\n')
        else:
            print('board not initialized')


    def reset_marker(self):
        '''
        Method Description
        '''
        for row in range(self.row_count):
            for col in range(self.col_count):
                self.marker[row][col] = None
                self.b_marker[row][col] = False


    def set_marker(self, tile, row, col, direction):
        '''
        Method Description
        '''
        self.reset_marker()
        if self.board.can_place_tile(tile, row, col, direction):

            self.marker[row][col] = tile.get_block(0)
            self.b_marker[row][col] = True

            ad_row, ad_col = DIRECTION.adjust_row_col_by_direction(row, col, direction)

            self.marker[ad_row][ad_col] = tile.get_block(1)
            self.b_marker[ad_row][ad_col] = True
        else:
            if row >= 0 and row < self.row_count and col >= 0 and col < self.col_count:
                self.marker[row][col] = tile.get_block(0)
                self.b_marker[row][col] = False

            ad_row, ad_col = DIRECTION.adjust_row_col_by_direction(row, col, direction)

            if ad_row >= 0 and ad_row < self.row_count and ad_col >= 0 and ad_col < self.col_count:
                self.marker[ad_row][ad_col] = tile.get_block(1)
                self.b_marker[ad_row][ad_col] = False
