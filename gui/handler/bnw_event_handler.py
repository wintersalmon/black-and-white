'''
BLACK-AND-WHITE
WinterSalmon
Black And White Draw Unit
'''
import sys
import pygame
from pygame.locals import *

from game.game import Game
from game.status.status import STATUS

from gui.handler.handle_change_pattern import HandleChangePattern
from gui.handler.handle_player_movement import HandlePlayerMovement
from gui.handler.handle_player_placement import HandlePlayerPlacement
from gui.handler.handle_tile_placement import HandleTilePlacement


class BNWEventHandler():
    '''
    Black And White Draw Unit
    '''
    def __init__(self, game):
        if not isinstance(game, Game):
            raise ValueError('game should be instance of Game')
        self.game = game

        self.key_down = dict()

        self.event_handlers = dict()
        self.event_handlers[STATUS.TILE_PLACEMENT] = HandleTilePlacement(self.game)
        self.event_handlers[STATUS.TILE_PLACEMENT_CHANGE_PATTERN] = HandleChangePattern(self.game)
        self.event_handlers[STATUS.PLAYER_MOVEMENT_SET_START_POINT] = HandlePlayerPlacement(self.game)
        self.event_handlers[STATUS.PLAYER_MOVEMENT] = HandlePlayerMovement(self.game)


    def handle_events(self):
        '''
        draw game
        '''
        self.check_for_quit()

        status = self.game.get_current_status()
        if status not in self.event_handlers.keys():
            return
        handler = self.event_handlers[status]

        for event in pygame.event.get():
            if self.is_key_down(event) and handler.can_handle_key_down(event.key):
                message = handler.handle_key_down(event.key)
                if message:
                    self.game.set_current_message(message)



    def is_key_down(self, event):
        '''
        returns True if event is KEY DOWN
        '''
        return event.type == KEYDOWN


    def check_for_quit(self):
        '''
        check for quit event and quit the game
        '''
        for event in pygame.event.get((QUIT, KEYUP)): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
