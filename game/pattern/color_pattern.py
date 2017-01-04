'''
BLACK-AND-WHITE
WinterSalmon
ColorPattern
'''


from game.color.constant import WHITE, GRAY, BLACK
from game.pattern.pattern import Pattern


class ColorPattern(Pattern):
    '''
    Pattern
    '''
    def __init__(self):
        super().__init__()
        self._init_add_symbol_rule(WHITE, 2)
        self._init_add_symbol_rule(GRAY, 1)
        self._init_add_symbol_rule(BLACK, 1)
