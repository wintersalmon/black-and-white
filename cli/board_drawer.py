'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Class Description
'''

from data.board.color import COLOR
from data.board.board import Board

class BoardDrawer():
    '''
    Class Description
    '''
    def __init__(self, board):
        self.board = None
        if isinstance(board, Board):
            self.board = board


    def draw_color(self):
        '''
        Method Description
        '''
        if self.board:
            for row in range(self.board.get_row_count()):
                for col in range(self.board.get_col_count()):
                    color = self.board.get_block_color(row, col)
                    if color == COLOR.WHITE:
                        print('W', end=' ')
                    if color == COLOR.GRAY:
                        print('G', end=' ')
                    if color == COLOR.BLACK:
                        print('B', end=' ')
                    if color == COLOR.NOCOLOR:
                        print('@', end=' ')
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
                    print(counter, end=' ')
                print('')
        else:
            print('board not initialized')
