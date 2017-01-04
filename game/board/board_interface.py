'''
BLACK-AND-WHITE
WinterSalmon
Contains BoardInterface
'''


class BoardInterface():
    '''
    Interface used to access board
    '''
    def get_row_count(self):
        '''
        returns board max row count
        '''
        raise NotImplementedError('You need to implement set_piece')


    def get_col_count(self):
        '''
        returns board max column count
        '''
        raise NotImplementedError('You need to implement set_piece')


    def get_block_overlap_count(self, row, col):
        '''
        returns overlapped block counts located on [row,col]
        '''
        raise NotImplementedError('You need to implement set_piece')


    def get_block_color(self, row, col):
        '''
        returns color of the block located on [row,col]
        '''
        raise NotImplementedError('You need to implement set_piece')


    def is_marked(self, row, col):
        '''
        returns True if block[row,col] is marked
        '''
        raise NotImplementedError('You need to implement is_marked')
