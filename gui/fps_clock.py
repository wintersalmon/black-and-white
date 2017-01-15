'''
BLACK-AND-WHITE
WinterSalmon
FPS Clock made with pygame
'''
import pygame
from pygame.locals import *

class FPSClock():
    '''
    FPS Clock made with pygame
    '''
    def __init__(self):
        self.fps_clock = pygame.time.Clock()
        self.fps = 30

    def sef_fps(self, fps):
        '''
        chage current fps (returns True if success)
        fps must be greater then zero
        '''
        if fps > 0:
            self.fps = fps
            return True
        else:
            return False

    def get_fps(self):
        '''
        returns current fps
        '''
        return self.fps

    def tick(self):
        '''
        wait for fps tick
        '''
        self.fps_clock.tick(self.fps)
