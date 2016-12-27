'''
BLACK-AND-WHITE
WinterSalmon
Player
'''

class Player():
    '''
    Player
    '''
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.row = -1
        self.col = -1


    def reset_position(self):
        '''
        reset player position on board
        '''
        self.row = -1
        self.col = -1


    def player_on_board(self):
        '''
        returns True if player is on board
        '''
        if self.row == -1 or self.col == -1:
            return False
        else:
            return True


    def set_position(self, row, col):
        '''
        set player position (row, col)
        '''
        self.row = row
        self.col = col


    def get_position(self):
        '''
        returns player position (row, col)
        '''
        return self.row, self.col


    def get_number(self):
        '''
        returns player number
        '''
        return self.number


    def get_name(self):
        '''
        returns player name
        '''
        return self.name
