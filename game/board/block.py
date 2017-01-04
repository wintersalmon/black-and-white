'''
BLACK-AND-WHITE
WinterSalmon
Class Name
'''


from game.color.constant import NOCOLOR, WHITE, GRAY, BLACK


class Block():
    '''
    Class Description
    '''
    def __init__(self):
        self.color = NOCOLOR

    def get_color(self):
        '''
        Method Description
        '''
        return self.color

    def mix_color(self, color):
        '''
        Method Description
        '''
        self.color = self.get_mixed_color(color)


    def get_mixed_color(self, color):
        '''
        returns Mixed Color
        '''
        if self.color == BLACK or color == BLACK:
            return BLACK
        elif self.color == GRAY or color == GRAY:
            return GRAY
        elif self.color == WHITE or color == WHITE:
            return WHITE
        else:
            return NOCOLOR


class WhiteBlock(Block):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.color = WHITE

class GrayBlock(Block):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.color = GRAY

class BlackBlock(Block):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.color = BLACK
