'''
BLACK-AND-WHITE
WinterSalmon
EventHandler for 'tile placement event'
'''
import pygame
from pygame.locals import *

from gui.handler.handle_event import HandleEvent
from game.status.status import STATUS
from game.board.direction import DIRECTION


# from gui.handler.event_handler import EventHandler
# from game.game import Game
# from game.status.status import STATUS


class HandleTilePlacement(HandleEvent):
    '''
    EventHandler for 'tile placement event'
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

        self.add_key_down(K_e, lambda: self.handle_event_rotate(1))
        self.add_key_down(K_q, lambda: self.handle_event_rotate(3))

        self.add_key_down(K_BACKQUOTE, self.handle_event_change_pattern)
        self.add_key_down(K_TAB, self.handle_event_change_mode)

        self.add_key_down(K_RETURN, self.handle_event_confirm)
        self.add_key_down(K_SPACE, self.handle_event_confirm)


    def handle_event_change_mode(self):
        '''
        handle change mode event
        '''
        event_result = self.game.set_mode_change_pattern()
        event_title = 'Change Mode To Pattern'
        return self.create_local_message(event_result, event_title)


    def handle_event_change_pattern(self):
        '''
        handle change pattern event
        '''
        # todo : hide this CODE into game class
        status = STATUS.TILE_PLACEMENT_CHANGE_PATTERN
        board = self.game.get_current_board()
        player = self.game.get_current_player()
        self.game.player_pattern_update_helper.set_target(player)
        player = self.game.player_pattern_update_helper
        self.game.change_status(status, board, player, True)
        # todo : hide this CODE into game class
        return self.create_local_message(True, 'Change Pattern')

    def handle_event_confirm(self):
        '''
        handle confirm event
        '''
        helper = self.game.player_tile_placement_helper
        event_result = helper.save_target()
        event_title = 'Tile Placement'
        if event_result:
            self.game.continue_status = False
        return self.create_local_message(event_result, event_title)

    def handle_event_select_tile(self, number):
        '''
        handle change pattern event
        '''
        helper = self.game.player_tile_placement_helper
        event_result = helper.change_selected_tile(number)
        event_title = 'Chage Tile'
        event_param = number
        return self.create_local_message(event_result, event_title, event_param)

    def handle_event_rotate(self, rotate):
        '''
        handle rotate event
        '''
        helper = self.game.player_tile_placement_helper
        event_result = helper.rotate(rotate)
        event_title = 'Rotate Tile'
        event_param = '{} Degress'.format(rotate * 90)
        return self.create_local_message(event_result, event_title, event_param)

    def handle_event_move(self, direction):
        '''
        handle move to direction event
        '''
        helper = self.game.player_tile_placement_helper
        event_result = helper.move(direction)
        event_title = 'Move Tile'
        event_param = direction.name
        return self.create_local_message(event_result, event_title, event_param)
