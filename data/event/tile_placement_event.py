'''
BLACK-AND-WHITE
WinterSalmon
Contains TilePlacementEvent class
'''


from data.event.event import Event, EVENT

class TilePlacementEvent(Event):
    '''
    Event Class representing tile placement event
    '''
    def __init__(self, args):
        super().__init__(EVENT.TILE_PLACEMENT, args)
        self.description_detail_fmt = 'Player({}) ({}, {}, {})'
        self.player = args['player']
        self.row = args['row']
        self.col = args['col']
        self.dir = args['dir']


    def get_description_detail(self):
        '''
        returns 'Tile Placement Event' detail
        '''
        return self.description_detail_fmt.format(self.player, self.row, self.col, self.dir.name)


    def get_player(self):
        '''
        returns which player placed the tile
        '''
        return self.player


    def get_row(self):
        '''
        returns the row of the tile placed
        '''
        return self.row


    def get_col(self):
        '''
        returns the column of the tile placed
        '''
        return self.col


    def get_dir(self):
        '''
        returns the direction of the tile placed
        '''
        return self.dir
