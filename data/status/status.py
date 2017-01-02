'''
BLACK-AND-WHITE
WinterSalmon
Contains Status Enum class
'''

from data.util.auto_number_enum import AutoNumberEnum

class STATUS(AutoNumberEnum):
    '''
    Enum class for Status
    '''
    NOSTATUS = ()

    GAME_START = ()
    NEXT_ROUND = ()
    GAME_OVER = ()

    TILE_PLACEMENT_NEXT_PLAYER = ()
    TILE_PLACEMENT = ()
    TILE_PLACEMENT_CHANGE_PATTERN = ()

    PLAYER_MOVEMENT_NEXT_PLAYER = ()
    PLAYER_MOVEMENT_SET_START_POINT = ()
    PLAYER_MOVEMENT = ()
