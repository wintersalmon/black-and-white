'''
BLACK-AND-WHITE
WinterSalmon
Message Draw Unit for pygame
'''
from gui.draw.draw_unit import DrawUnit
from game.game import Game
from game.color.color import Color


class DrawMessage():
    '''
    Message Draw Unit for pygame
    '''
    def __init__(self, draw_unit, game, offset_x=0, offset_y=0):
        if not isinstance(draw_unit, DrawUnit):
            raise ValueError('draw_unit should be instance of DrawUnit')
        if not isinstance(game, Game):
            raise ValueError('game should be instance of Game')

        self.draw_unit = draw_unit
        self.game = game
        # size values
        self.offset_x = offset_x
        self.offset_y = offset_y
        # text values
        self.text_color = None
        self.line_size = None


    def init_line_info(self, line_size, text_color):
        '''
        initialize line info
        '''
        if not isinstance(text_color, Color):
            raise ValueError('bgcolor should be instance of Color')
        self.line_size = line_size
        self.text_color = text_color


    def draw(self):
        '''
        message player to pygame displaysurf
        '''
        message = self.game.get_current_message()
        if message and isinstance(message, str):
            left = self.offset_x + self.draw_unit.get_margin_x()
            top = self.offset_y + self.draw_unit.get_margin_y()
            rgb = self.text_color.get_rgb()
            self.draw_unit.pygame_blit(message, left, top, rgb)
