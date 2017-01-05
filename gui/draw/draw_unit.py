'''
BLACK-AND-WHITE
WinterSalmon
Draw Unit for pygame
'''
class DrawUnit():
    '''
    Draw Unit for pygame
    '''
    def __init__(self, pygame, displaysurf, basicfont):
        if not pygame:
            raise ValueError('pygame shuld not be None')
        if not displaysurf:
            raise ValueError('displaysurf shuld not be None')
        if not basicfont:
            raise ValueError('basicfont shuld not be None')
        self.pygame = pygame
        self.displaysurf = displaysurf
        self.basicfont = basicfont


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
