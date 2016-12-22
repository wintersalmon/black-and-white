'''
BLACK-AND-WHITE
WinterSalmon
Contains GameOverEvent class
'''


from data.event.event import Event, EVENT

class GameOverEvent(Event):
    '''
    Event Class representing game over event
    '''
    def __init__(self):
        super().__init__(EVENT.GAME_OVER, dict())
        self.description_detail = 'Game Over'


    def get_description_detail(self):
        '''
        returns 'Tile Placement Event' detail
        '''
        return self.description_detail

