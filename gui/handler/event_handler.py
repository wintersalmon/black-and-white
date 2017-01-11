'''
BLACK-AND-WHITE
WinterSalmon
Event Handler for pygame
'''


import pygame
from pygame.locals import *
from game.game import Game


class EventHandler():
    '''
    Event Handler for pygame
    '''
    def __init__(self, game):
        if game and isinstance(game, Game):
            self.game = game
        else:
            raise ValueError('game should be Game Instance')
        self.key_down = [K_DOWN]
        self.key_directions = [K_LEFT, K_a, K_RIGHT, K_d, K_UP, K_w, K_DOWN, K_s]
        self.key_rotations = [K_q, K_e]
        self.key_selections = [K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0]
        self.key_options = [K_BACKQUOTE]
        self.key_okay = [K_RETURN, K_SPACE]


    def handle(self, event):
        '''
        handle event and return result message
        '''
        raise NotImplementedError('You need to implement handle')


    def create_result_message(self, result, discription, param=None):
        '''
        create result message
        '''
        event_result = 'SUCCESS' if result else 'FAILED'
        param_str = param if param else ''
        message = '[{}] {} {}'.format(event_result, discription, param_str)
        return message


    def get_direction(self, key):
        '''
        get key direction
        '''
        direction = None
        if key in self.key_directions:
            if key in (K_LEFT, K_a):
                direction = DIRECTION.LEFT
            elif key in (K_RIGHT, K_d):
                direction = DIRECTION.RIGHT
            elif key in (K_UP, K_w):
                direction = DIRECTION.UP
            elif key in (K_DOWN, K_s):
                direction = DIRECTION.DOWN
        return direction


    def get_rotation(self, key):
        '''
        get key rotation
        '''
        rotation = 0
        if key in self.key_rotations:
            if key == K_q:
                rotation = 1
            elif key == K_e:
                rotation = 3
        return rotation


    def get_selection(self, key, select_option_list):
        '''
        get key selection
        '''
        idx = -1
        if key in self.key_selections:
            if key == K_1:
                idx = 0
            elif key == K_2:
                idx = 1
            elif key == K_3:
                idx = 2
            elif key == K_4:
                idx = 3
            elif key == K_5:
                idx = 4
            elif key == K_6:
                idx = 5
            elif key == K_7:
                idx = 6
            elif key == K_8:
                idx = 7
            elif key == K_9:
                idx = 8
            elif key == K_0:
                idx = 9
        if 0 <= idx < len(select_option_list):
            return select_option_list[idx]
        else:
            return None
