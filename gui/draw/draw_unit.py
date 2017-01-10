'''
BLACK-AND-WHITE
WinterSalmon
Draw Unit for pygame
'''

import pygame
from pygame.locals import *
from game.color.constant import WHITE

class DrawUnit():
    '''
    Draw Unit for pygame
    '''
    def __init__(self, width, height, margin_x=0, margin_y=0, bg_color=None):
        if not pygame:
            raise ValueError('pygame shuld not be None')
        pygame.init()
        self.pygame = pygame

        # window size
        self.displaysurf = self.pygame.display.set_mode((width, height))
        self.width = self.displaysurf.get_width()
        self.height = self.displaysurf.get_height()
        self.margin_x = margin_x
        self.margin_y = margin_y
        self.bg_color = bg_color

        # basic font
        self.basicfont = self.pygame.font.Font('freesansbold.ttf', 18)

        # fps clock
        # self.fpsclock = pygame.time.Clock()
        self.fpsclock = pygame.time.Clock()
        self.fps = 30


    def draw(self, dummydata):
        '''
        draw background
        '''
        if dummydata and self.bg_color:
            self.pygame_fill_background(self.bg_color)


    def set_margin(self, margin_x, margin_y):
        '''
        set margin
        '''
        self.margin_x = margin_x
        self.margin_y = margin_y


    def set_background_color(self, bg_color):
        '''
        set background color
        '''
        self.bg_color = bg_color


    def set_basicfont(self, fontname, fontsize):
        '''
        set basic font
        '''
        self.basicfont = self.pygame.font.Font(fontname, fontsize)


    def set_fps(self, fps):
        '''
        set fps clock
        '''
        if fps >= 0:
            self.fps = fps


    def get_width(self):
        '''
        returns window width
        '''
        return self.width


    def get_height(self):
        '''
        returns window height
        '''
        return self.height


    def get_margin_x(self):
        '''
        returns margin x
        '''
        return self.margin_x


    def get_margin_y(self):
        '''
        returns margin y
        '''
        return self.margin_y


    def get_background_color(self):
        '''
        returns background color
        '''
        return self.bg_color


    def pygame_fill_background(self, rgb):
        '''
        fill displaysuf with rgb color
        '''
        self.displaysurf.fill(rgb)


    def pygame_draw_rect(self, rgb, rect):
        '''
        draw rgb color square to rect position
        '''
        self.pygame.draw.rect(self.displaysurf, rgb, rect)


    def pygame_draw_rect_border(self, rgb, rect, border):
        '''
        draw rgb color square border to rect position
        '''
        self.pygame.draw.rect(self.displaysurf, rgb, rect, border)


    def pygame_blit(self, text, left, top, rgb):
        '''
        draw rgb color text to position left top
        '''
        press_key_surf = self.basicfont.render(text, True, rgb)
        press_key_rect = press_key_surf.get_rect()
        press_key_rect.topleft = (left, top)
        self.displaysurf.blit(press_key_surf, press_key_rect)


    def pygame_fpsclock_tick(self):
        '''
        tick fps clock
        '''
        self.fpsclock.tick(self.fps)
