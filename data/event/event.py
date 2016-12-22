'''
BLACK-AND-WHITE
WinterSalmon
Contains Event Class
'''


from data.board.auto_number_enum import AutoNumberEnum


class Event():
    '''
    Used to represent an event happend in game
    '''

    DES_HEADER_FORMAT = 'Event[{}] : '

    def __init__(self, code, args):
        if not isinstance(args, dict):
            raise ValueError("Event args argument MUST BE DICT TYPE")
        self.code = code
        self.args = args


    def get_code(self):
        '''
        returns event code
        '''
        return self.code


    def get_description_header(self):
        '''
        returns event description header
        '''
        return Event.DES_HEADER_FORMAT.format(self.code)


    def get_description_detail(self):
        '''
        returns event description detail
        '''
        raise NotImplementedError('You need to implement get_description_detail')


    def get_description(self):
        '''
        returns event description string
        '''
        return self.get_description_header() + self.get_description_body()


    def get_args(self):
        '''
        returns event argument list
        '''
        return self.args



class EventCode(AutoNumberEnum):
    '''
    Event Code used to identify event
    '''
    NOEVENT = ()
    TILE_PLACEMENT = ()
