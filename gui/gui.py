'''
BLACK-AND-WHITE
WinterSalmon
Contains class Gui Graphic User Interface made with pygame
'''
from game.game import Game
from game.color.constant import RED, BLUE, CYAN, ORANGE

from gui.draw.bnw_draw_unit import BNWDrawUnit
from gui.handler.bnw_event_handler import BNWEventHandler
from gui.fps_clock import FPSClock

class Gui():
    '''
    Graphic User Interface made with pygame
    '''
    def __init__(self):
        max_col = 12
        max_row = 5

        self.game = Game(max_row, max_col)
        self.bnw_draw_unit = BNWDrawUnit(self.game)
        self.bnw_event_handler = BNWEventHandler(self.game)
        self.fps_colock = FPSClock()


    def init_screen(self):
        '''
        displays game init screen and handles event
        '''
        player_info_list = list()
        player_info_list.append(('WinterSalmon', RED))
        player_info_list.append(('Kein', BLUE))
        player_info_list.append(('Sshong91', CYAN))
        player_info_list.append(('Wool', ORANGE))
        self.game.init_game(player_info_list)


    def credit_screen(self):
        '''
        displays game credit screen and handles event
        '''
        pass


    def game_screen(self):
        '''
        displays main game screen and handles event
        '''
        while self.game.is_game_running():
            self.bnw_draw_unit.draw()

            self.bnw_event_handler.handle_events()
            self.game.update()
            self.bnw_draw_unit.update()

            self.fps_colock.tick()
