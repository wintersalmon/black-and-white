'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Gui
'''

from data.data import Data

class Gui():
    '''
    Graphic User Interface for the game
    '''
    def __init__(self):
        self.game_data = None

    def start(self, game_data):
        '''
        init with game data and start the game
        '''
        if isinstance(game_data, Data):
            self.game_data = game_data
        else:
            self.game_data = None

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
