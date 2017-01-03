'''
BLACK-AND-WHITE
WinterSalmon
Cli
'''

from game.game import Game

class Cli():
    '''
    Command Line Interface for the game
    '''
    def __init__(self):
        self.game_Game = None

    def start(self, game_Game):
        '''
        init with game Game and start the game
        '''
        if isinstance(game_Game, Game):
            self.game_Game = game_Game
        else:
            self.game_Game = None

    def next(self):
        '''
        Method Description
        '''
        return False

    def update(self):
        '''
        update game date
        '''
        return

    def show(self):
        '''
        show game status to screen
        '''
        return

    def has_action_input(self):
        '''
        returns whether game stauts requires action input
        '''
        return False

    def show_action_input(self):
        '''
        show required action input to screen
        '''
        return

    def action_input(self):
        '''
        recieve action input from user
        '''
        return
