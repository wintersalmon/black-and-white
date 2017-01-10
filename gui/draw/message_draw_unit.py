'''
BLACK-AND-WHITE
WinterSalmon
Message Draw Unit for pygame
'''


from gui.draw.draw_unit import DrawUnit


class MessageDrawUnit():
    '''
    Message Draw Unit for pygame
    '''
    def __init__(self, draw_unit):
        if not isinstance(draw_unit, DrawUnit):
            raise ValueError('draw_unit should be DrawUnit')
        self.draw_unit = draw_unit
        # board size values
        self.xmargin = None
        self.ymargin = None
        self.text_color = None

    def init(self, xmargin, ymargin, color):
        '''
        initialize board size
        '''
        self.xmargin = xmargin
        self.ymargin = ymargin
        self.text_color = color


    def draw(self, game):
        '''
        message player to pygame displaysurf
        '''
        message = None
        if game:
            message = game.get_current_message()
        if not message:
            return

        left = self.xmargin
        top = self.ymargin
        rgb = self.text_color.get_rgb()
        self.draw_unit.pygame_blit(message, left, top, rgb)
