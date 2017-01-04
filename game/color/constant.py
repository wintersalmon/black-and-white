'''
BLACK-AND-WHITE
WinterSalmon
Contains All Colors
'''
from game.color.color import Color
from game.color.color import ColorCode as CODE

NOCOLOR = Color(CODE.NOCOLOR, (-1, -1, -1))

WHITE = Color(CODE.WHITE, (255, 255, 255))
GRAY = Color(CODE.GRAY, (100, 100, 100))
BLACK = Color(CODE.BLACK, (0, 0, 0))

RED = Color(CODE.RED, (255, 0, 0))
GREEN = Color(CODE.GREEN, (0, 255, 0))
BLUE = Color(CODE.BLUE, (0, 0, 255))

YELLOW = Color(CODE.WHITE, (255, 255, 0))
ORANGE = Color(CODE.WHITE, (255, 128, 0))
PURPLE = Color(CODE.WHITE, (255, 0, 255))
CYAN = Color(CODE.WHITE, (0, 255, 255))

NAVYBLUE = Color(CODE.WHITE, (60, 60, 255))
