'''
BLACK-AND-WHITE
WinterSalmon
EventHandler for 'player change pattern event'
'''
import pygame
from pygame.locals import *

from gui.handler.handle_event import HandleEvent
from game.color.constant import WHITE, GRAY, BLACK


class HandleChangePattern(HandleEvent):
    '''
    EventHandler for 'tile placement event'
    '''
    def __init__(self, game):
        super().__init__(game)

        self.add_key_down(K_1, lambda: self.handle_event_select_color(WHITE))
        self.add_key_down(K_2, lambda: self.handle_event_select_color(GRAY))
        self.add_key_down(K_3, lambda: self.handle_event_select_color(BLACK))
        self.add_key_down(K_w, lambda: self.handle_event_select_color(WHITE))
        self.add_key_down(K_g, lambda: self.handle_event_select_color(GRAY))
        self.add_key_down(K_b, lambda: self.handle_event_select_color(BLACK))

        self.add_key_down(K_BACKQUOTE, self.handle_event_cancel)

        self.add_key_down(K_RETURN, self.handle_event_confirm)
        self.add_key_down(K_SPACE, self.handle_event_confirm)

    def handle_event_cancel(self):
        '''
        handle cancel event
        '''
        event_result = True
        event_title = 'Cancel Change Pattern'
        self.game.continue_status = False
        return self.create_local_message(event_result, event_title)

    def handle_event_confirm(self):
        '''
        handle confirm event
        '''
        helper = self.game.player_pattern_update_helper
        event_result = helper.save_target()
        event_title = 'Change Pattern'
        if event_result:
            self.game.continue_status = False
        return self.create_local_message(event_result, event_title)

    def handle_event_select_color(self, color):
        '''
        handle select Color event
        '''
        helper = self.game.player_pattern_update_helper
        event_result = helper.enqueue_color(color)
        event_title = 'Select Color'
        event_discription = color.get_name()
        return self.create_local_message(event_result, event_title, event_discription)
