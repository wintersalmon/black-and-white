'''
BLACK-AND-WHITE
WinterSalmon
Contains COLOR and Color
'''


from game.util.auto_number_enum import AutoNumberEnum


class ColorCode(AutoNumberEnum):
    '''
    COLOR CODE
    '''
    NOCOLOR = ()

    WHITE = ()
    GRAY = ()
    BLACK = ()

    RED = ()
    GREEN = ()
    BLUE = ()

    YELLOW = ()
    ORANGE = ()
    PURPLE = ()
    CYAN = ()
    NAVYBLUE = ()


class Color():
    '''
    Class containing information about color
    '''
    def __init__(self, code, rgb):
        self.code = code
        self.rgb = rgb


    def get_id(self):
        '''
        returns COLOR code
        '''
        return self.code.value


    def get_name(self):
        '''
        returns COLOR name
        '''
        return self.code.name


    def get_rgb(self):
        '''
        returns RGB value
        '''
        return self.rgb


    def __key(self):
        return (self.get_name(), self.get_rgb())

    def __hash__(self):
        return hash(self.__key())

    def __str__(self):
        return self.code.name

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.code == other.code
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
