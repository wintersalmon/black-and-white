'''
BLACK-AND-WHITE
WinterSalmon
Background Draw Unit for pygame
'''
from gui.draw.draw_unit import DrawUnit
from game.color.color import Color


class DrawBackground():
    '''
    Background Draw Unit for pygame
    '''
    def __init__(self, draw_unit):
        if not isinstance(draw_unit, DrawUnit):
            raise ValueError('draw_unit should be instance of DrawUnit')
        self.draw_unit = draw_unit
        # background color
        self.bgcolor = None


    def init_background_color(self, bgcolor):
        '''
        init background color
        '''
        if not isinstance(bgcolor, Color):
            raise ValueError('bgcolor should be instance of Color')
        self.bgcolor = bgcolor


    def draw(self):
        '''
        draw background to pygame displaysurf
        '''
        if not self.bgcolor:
            return
        self.draw_unit.pygame_fill_background(self.bgcolor.get_rgb())
