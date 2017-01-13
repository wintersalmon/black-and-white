'''
BLACK-AND-WHITE
WinterSalmon
Draw Unit for pygame
'''
import pygame
from pygame.locals import *
# from game.color.constant import WHITE


class DrawUnit():
    '''
    Draw Unit for pygame
    '''
    def __init__(self, width, height, margin_x=0, margin_y=0):
        self.pygame = pygame
        self.pygame.init()
        self.displaysurf = self.pygame.display.set_mode((width, height))
        self.basicfont = self.pygame.font.Font('freesansbold.ttf', 18)
        self.fpsclock = pygame.time.Clock()
        self.fps = 30

        self.width = self.displaysurf.get_width()
        self.height = self.displaysurf.get_height()
        self.margin_x = margin_x
        self.margin_y = margin_y


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

    def pygame_fps_tick(self):
        '''
        tick fps clock
        '''
        self.fpsclock.tick(self.fps)
