'''
BLACK-AND-WHITE
WinterSalmon
EventHandler for 'player piece movement event'
'''
import pygame
from pygame.locals import *

from gui.handler.handle_event import HandleEvent
from game.board.direction import DIRECTION


class HandlePlayerMovement(HandleEvent):
    '''
    EventHandler for 'player piece movement event'
    '''
    def __init__(self, game):
        super().__init__(game)

        self.add_key_down(K_UP, lambda: self.handle_event_move(DIRECTION.UP))
        self.add_key_down(K_DOWN, lambda: self.handle_event_move(DIRECTION.DOWN))
        self.add_key_down(K_RIGHT, lambda: self.handle_event_move(DIRECTION.RIGHT))
        self.add_key_down(K_LEFT, lambda: self.handle_event_move(DIRECTION.LEFT))

        self.add_key_down(K_w, lambda: self.handle_event_move(DIRECTION.UP))
        self.add_key_down(K_s, lambda: self.handle_event_move(DIRECTION.DOWN))
        self.add_key_down(K_d, lambda: self.handle_event_move(DIRECTION.RIGHT))
        self.add_key_down(K_a, lambda: self.handle_event_move(DIRECTION.LEFT))

        self.add_key_down(K_1, lambda: self.handle_event_select_tile(1))
        self.add_key_down(K_2, lambda: self.handle_event_select_tile(2))
        self.add_key_down(K_3, lambda: self.handle_event_select_tile(3))
        self.add_key_down(K_4, lambda: self.handle_event_select_tile(4))

        self.add_key_down(K_BACKQUOTE, self.handle_event_skip)

        self.add_key_down(K_RETURN, self.handle_event_confirm)
        self.add_key_down(K_SPACE, self.handle_event_confirm)


    def handle_event_skip(self):
        '''
        handle skip event
        '''
        event_result = True
        event_title = 'Skip Player Movement'
        self.game.continue_status = False
        return self.create_local_message(event_result, event_title)

    def handle_event_confirm(self):
        '''
        handle confirm event
        '''
        helper = self.game.player_piece_movement_helper
        event_result = helper.save_target()
        event_title = 'Player Movement'
        if event_result:
            self.game.continue_status = False
        return self.create_local_message(event_result, event_title)

    def handle_event_select_tile(self, number):
        '''
        handle change pattern event
        '''
        helper = self.game.player_piece_movement_helper
        event_result = helper.change_selected_tile(number)
        event_title = 'Chage Tile'
        event_param = number
        return self.create_local_message(event_result, event_title, event_param)

    def handle_event_move(self, direction):
        '''
        handle move to direction event
        '''
        helper = self.game.player_piece_movement_helper
        event_result = helper.move(direction)
        event_title = 'Move Tile'
        event_param = direction.name
        return self.create_local_message(event_result, event_title, event_param)
