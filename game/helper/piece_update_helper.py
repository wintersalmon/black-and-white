'''
BLACK-AND-WHITE
WinterSalmon
PieceUpdateHelper
'''

from game.helper.update_helper import UpdateHelper

class PieceUpdateHelper(UpdateHelper):
    '''
    Interface used to help user update piece position on Board
    '''
    def move(self, direction, option):
        '''
        move piece acording to given direction and option
        '''
        raise NotImplementedError('You need to implement clear_marker')

    def placement(self, row, col):
        '''
        place piece to given position(row,col)
        '''
        raise NotImplementedError('You need to implement clear_marker')

    def rotate(self, count):
        '''
        rotate piece by 90 * count degrees
        '''
        raise NotImplementedError('You need to implement clear_marker')
