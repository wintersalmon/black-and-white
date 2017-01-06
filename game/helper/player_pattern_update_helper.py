'''
BLACK-AND-WHITE
WinterSalmon
PlayerPatternUpdateHelper
'''


from game.player import PlayerInterface
from game.pattern.color_pattern import ColorPattern
from game.helper.update_helper import UpdateHelper


class PlayerPatternUpdateHelper(UpdateHelper, PlayerInterface):
    '''
    Interface used to help user update player pattern
    '''
    def __init__(self):
        self.target_player = None
        self.current_pattern = ColorPattern()
        self.current_pattern_counter = 0
        self.next_add_symbol_index = 0

    def change_color(self, index, color):
        '''
        change pattern color at index
        '''
        return self.current_pattern.set_symbol(index, color)

    def enqueue_color(self, color):
        '''
        change pattern color at next queue
        '''
        next_index = self.next_add_symbol_index
        if next_index >= self.current_pattern.get_max_length():
            next_index = 0
        if self.change_color(next_index, color):
            self.next_add_symbol_index = next_index + 1
            return True
        else:
            return False

    def undo_all_changes(self):
        '''
        restore pattern to saved state
        '''
        if self.target_player:
            self.set_target(self.target_player)
            return True
        else:
            return False



    # UpdateHelper Implementations
    def set_target(self, target_player):
        '''
        Implemented UpdateHelper set_target
        set target player
        '''
        if isinstance(target_player, PlayerInterface):
            self.target_player = target_player
            self.current_pattern.clone(self.target_player.get_color_pattern())
            self.current_pattern_counter = 0
            self.next_add_symbol_index = 0
            return True
        else:
            return False

    # UpdateHelper Implementations
    def can_save_target(self):
        '''
        Implemented UpdateHelper can_save_target
        returns True if Changes made to target player can be saved
        '''
        return self.current_pattern and self.current_pattern.is_valid()

    # UpdateHelper Implementations
    def save_target(self):
        '''
        Implemented UpdateHelper save_target
        Save change made to target player
        '''
        if self.can_save_target():
            # remove selected tile and change player pattern
            target_pattern = self.target_player.get_color_pattern()
            target_pattern.clone(self.current_pattern)
            self.target_player.set_color_pattern_counter(self.current_pattern_counter)
            # todo : need to improve code logic
            # self.target_player.remove_tile(self.target_player.selected_tile)
            return True
        else:
            return False



    # PlayerInterface Implementations
    def get_selected_tile(self):
        '''
        Implemented PlayerInterface get_selected_tile
        returns color pattern
        '''
        if self.target_player:
            return self.target_player.get_selected_tile()
        return None

    # PlayerInterface Implementations
    def get_color_pattern(self):
        '''
        Implemented PlayerInterface get_color_pattern
        returns color pattern
        '''
        if self.current_pattern:
            return self.current_pattern
        return None

    # PlayerInterface Implementations
    def get_color_pattern_counter(self):
        '''
        Implemented PlayerInterface get_color_pattern_counter
        returns color pattern counter
        '''
        if self.current_pattern:
            return self.current_pattern_counter
        return None

    # PlayerInterface Implementations
    def get_tile_count(self):
        '''
        Implemented PlayerInterface get_tile_count
        returns player tile count
        '''
        if self.target_player:
            return self.target_player.get_tile_count()
        return None

    # PlayerInterface Implementations
    def get_tile(self, index):
        '''
        Implemented PlayerInterface get_tile
        returns player tile
        '''
        if self.target_player:
            return self.target_player.get_tile(index)
        return None

    # PlayerInterface Implementations
    def get_position(self):
        '''
        Implemented PlayerInterface get_position
        returns player position (row,col)
        '''
        if self.target_player:
            return self.target_player.get_position()
        return None

    # PlayerInterface Implementations
    def get_position_row(self):
        '''
        Implemented PlayerInterface get_position_row
        returns player position row
        '''
        if self.target_player:
            return self.target_player.get_position_row()
        return None

    # PlayerInterface Implementations
    def get_position_col(self):
        '''
        Implemented PlayerInterface get_position_col
        returns player position col
        '''
        if self.target_player:
            return self.target_player.get_position_col()
        return None

    # PlayerInterface Implementations
    def get_number(self):
        '''
        Implemented PlayerInterface get_number
        returns player number
        '''
        if self.target_player:
            return self.target_player.get_number()
        return None

    # PlayerInterface Implementations
    def get_name(self):
        '''
        Implemented PlayerInterface get_name
        returns player name
        '''
        if self.target_player:
            return self.target_player.get_name()
        return None

    # PlayerInterface Implementations
    def get_color(self):
        '''
        Implemented PlayerInterface get_color
        returns player color
        '''
        if self.target_player:
            return self.target_player.get_color()
        return None
