'''
BLACK-AND-WHITE
WinterSalmon
ColorPattern
'''


from data.board.color import COLOR
from data.pattern.pattern import Pattern


class ColorPattern(Pattern):
    '''
    Pattern
    '''
    def __init__(self):
        super().__init__()
        self._init_add_symbol_rule(COLOR.WHITE, 2)
        self._init_add_symbol_rule(COLOR.GRAY, 1)
        self._init_add_symbol_rule(COLOR.BLACK, 1)
