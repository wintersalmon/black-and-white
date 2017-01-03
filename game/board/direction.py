'''
BLACK-AND-WHITE
WinterSalmon
Class Name
'''

from game.util.auto_number_enum import AutoNumberEnum

class DIRECTION(AutoNumberEnum):
    '''
    Class Description
    '''
    NODIRECTION = ()
    UP = ()
    RIGHT = ()
    DOWN = ()
    LEFT = ()


    @staticmethod
    def rotate(direction, count=1):
        '''
        returns rotated direction by (90 * count) degrees
        '''
        if direction == DIRECTION.NODIRECTION:
            return DIRECTION.NODIRECTION
        elif direction == DIRECTION.UP:
            direction = DIRECTION.RIGHT
        elif direction == DIRECTION.RIGHT:
            direction = DIRECTION.DOWN
        elif direction == DIRECTION.DOWN:
            direction = DIRECTION.LEFT
        elif direction == DIRECTION.LEFT:
            direction = DIRECTION.UP

        if count - 1 > 0:
            return DIRECTION.rotate(direction, count-1)
        else:
            return direction


    @staticmethod
    def adjust_row_col_by_direction(row, col, direction):
        '''
        returns (row,col) adjusted by direction
        '''
        adjust_row = row
        adjust_col = col

        if direction == DIRECTION.LEFT:
            adjust_col -= 1
        elif direction == DIRECTION.RIGHT:
            adjust_col += 1
        elif direction == DIRECTION.UP:
            adjust_row -= 1
        elif direction == DIRECTION.DOWN:
            adjust_row += 1

        return (adjust_row, adjust_col)
