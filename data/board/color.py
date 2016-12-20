'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Class Name
'''

from data.board.auto_number_enum import AutoNumberEnum

class COLOR(AutoNumberEnum):
    '''
    Class Description
    '''
    NOCOLOR = ()
    WHITE = ()
    GRAY = ()
    BLACK = ()

    @staticmethod
    def mix_color(src_color, dst_color):
        '''
        Method Description
        '''
        if src_color == COLOR.BLACK or dst_color == COLOR.BLACK:
            return COLOR.BLACK
        elif src_color == COLOR.GRAY or dst_color == COLOR.GRAY:
            return COLOR.GRAY
        elif src_color == COLOR.WHITE or dst_color == COLOR.WHITE:
            return COLOR.WHITE
        else:
            return COLOR.NOCOLOR


    @staticmethod
    def get_color_text(color):
        '''
        Class Description
        '''
        if color == COLOR.NOCOLOR:
            return '@'
        if color == COLOR.WHITE:
            return 'W'
        if color == COLOR.GRAY:
            return 'G'
        if color == COLOR.BLACK:
            return 'B'
        return 'E'
