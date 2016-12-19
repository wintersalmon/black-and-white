#pylint: disable=E1101
#pylint: disable=W0212
'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
AutoNumberEnum
'''

from enum import Enum

class AutoNumberEnum(Enum):
    '''
    Custom Enum used to Creat auto increased number enum
    '''
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj
