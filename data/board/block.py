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

    def mix_color(self, new_color):
        '''
        Method Description
        '''
        self.color = self.color + new_color

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
