'''
BLACK-AND-WHITE
WinterSalmon
PlayerUpdateHelper
'''


class PlayerUpdateHelper():
    '''
    Interface used to help Player update variables
    Need to call set_player(player) to use helper
    Need to call save_player() to confirm changes
    '''
    def set_player(self, player):
        '''
        set player
        '''
        raise NotImplementedError('You need to implement set_player')


    def can_save_player(self):
        '''
        returns True if Changes can be saved
        '''
        raise NotImplementedError('You need to implement can_save_player')


    def save_player(self):
        '''
        Save changes made to player
        '''
        raise NotImplementedError('You need to implement save_player')
