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
    STANDBY_TILE_PLACEMENT = ()
    TILE_PLACEMENT = ()
    FINISHED_TILE_PLACEMENT = ()
    STANDBY_PLAYER_MOVEMENT = ()
    PLAYER_MOVEMENT = ()
    FINISHED_PLAYER_MOVEMENT = ()
    ROUND_OVER = ()
