'''
BLACK-AND-WHITE
WinterSalmon
Event Handler for pygame events
'''
import pygame
from pygame.locals import *

from game.game import Game

class HandleEvent():
    '''
    Event Handler for pygame events
    '''
    def __init__(self, game):
        if not isinstance(game, Game):
            raise ValueError('game should be Game Instance')
        self.game = game

        # event dictionarys
        self.key_down = dict()


    def add_key_down(self, key, action):
        '''
        add key down action
        '''
        self.key_down[key] = action


    def can_handle_key_down(self, key):
        '''
        returns True if key is in key_down dictionary
        '''
        return key in self.key_down.keys()


    def handle_key_down(self, key):
        '''
        handles key down event
        '''
        if self.can_handle_key_down(key):
            return self.key_down[key]()
        else:
            return None

    def create_local_message(self, result, title, discription=None):
        '''
        create result message
        '''
        result_str = 'SUCCESS' if result else 'FAILED'
        title_str = title if isinstance(title, str) else str(title)
        discription_str = discription if discription else ''
        message = '[{}][{}] {} {}'.format('LOCAL', result_str, title_str, discription_str)
        return message
