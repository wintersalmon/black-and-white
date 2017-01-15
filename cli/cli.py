'''
BLACK-AND-WHITE
WinterSalmon
Cli
'''
from game.game import Game
from game.color.constant import RED, BLUE, CYAN, ORANGE


class Cli():
    '''
    Command Line Interface for the game
    '''
    def __init__(self):
        # init row, col
        max_row = 5
        max_col = 12

        # init Game
        self.game = Game(max_row, max_col)

        # init Draw Unit

        # init Event Handler

        # init fps_clock


    def init_screen(self):
        '''
        displays game init screen and handle events
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
        pass
