'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Class Name
'''

from data.board.color import COLOR

class Block():
    '''
    Class Description
    '''
    def __init__(self):
        self.color = COLOR.NOCOLOR

    def get_color(self):
        '''
        Method Description
        '''
        return self.color

    def mix_color(self, mix_color):
        '''
        Method Description
        '''
        if self.color == COLOR.BLACK or mix_color == COLOR.BLACK:
            self.color = COLOR.BLACK
        elif self.color == COLOR.GRAY or mix_color == COLOR.GRAY:
            self.color = COLOR.GRAY
        else:
            self.color = COLOR.WHITE

class WhiteBlock(Block):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.color = COLOR.WHITE

class GrayBlock(Block):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.color = COLOR.GRAY

class BlackBlock(Block):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.color = COLOR.BLACK
