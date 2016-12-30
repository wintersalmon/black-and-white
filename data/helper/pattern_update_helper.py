'''
BLACK-AND-WHITE
WinterSalmon
PatternUpdateHelper
'''


from data.pattern.color_pattern import ColorPattern
from data.player import Player, PlayerInterface
from data.helper.player_update_helper import PlayerUpdateHelper


class PatternUpdateHelper(PlayerInterface, PlayerUpdateHelper):
    '''
    Helps player update pattern correctly
    '''
    def __init__(self):
        self.player = None
        self.pattern = ColorPattern()
        self.pattern_counter = 0
        self.next_add_symbol_index = 0


    def enqueue_change_color(self, color):
        '''
        Enqueue Change Color
        '''
        if self.next_add_symbol_index >= self.pattern.get_max_length():
            self.next_add_symbol_index = 0
        result = self.change_pattern_color(self.next_add_symbol_index, color)
        if result:
            self.next_add_symbol_index += 1
            return True
        else:
            return False


    def undo_all_changes(self):
        '''
        restore pattern to saved state
        '''
        self.pattern.clone(self.player.get_color_pattern())


    def change_pattern_color(self, index, color):
        '''
        change symbol at index
        '''
        return self.pattern.set_symbol(index, color)




    # Implemented PlayerUpdateHelper
    def set_player(self, player):
        '''
        set player
        '''
        if isinstance(player, Player):
            self.player = player
            self.pattern.clone(self.player.color_pattern)
            self.pattern_counter = 0
            self.next_add_symbol_index = 0
            return True
        return False

    # Implemented PlayerUpdateHelper
    def can_save_player(self):
        '''
        returns True if Changes can be saved
        '''
        return self.pattern and self.pattern.is_valid()

    # Implemented PlayerUpdateHelper
    def save_player(self):
        '''
        Save changes made to player
        '''
        if self.can_save_player():
            self.player.color_pattern.clone(self.pattern)
            self.player.set_color_pattern_counter(self.pattern_counter)
            self.player.remove_tile(self.player.selected_tile)
            return True
        return False




    # Implemented PlayerInterface
    def get_color_pattern(self):
        '''
        returns color pattern
        '''
        if self.pattern:
            return self.pattern
        return None

    # Implemented PlayerInterface
    def get_color_pattern_counter(self):
        '''
        returns color pattern counter
        '''
        if self.pattern:
            return self.pattern_counter
        return None

    # Implemented PlayerInterface
    def get_tile_count(self):
        '''
        returns player tile count
        '''
        if self.player:
            return self.player.get_tile_count()
        return None

    # Implemented PlayerInterface
    def get_tile(self, index):
        '''
        returns player tile
        '''
        if self.player:
            return self.player.get_tile()
        return None

    # Implemented PlayerInterface
    def get_position(self):
        '''
        returns player position (row,col)
        '''
        if self.player:
            return self.player.get_position()
        return None

    # Implemented PlayerInterface
    def get_position_row(self):
        '''
        returns player position row
        '''
        if self.player:
            return self.player.get_position_row()
        return None

    # Implemented PlayerInterface
    def get_position_col(self):
        '''
        returns player position col
        '''
        if self.player:
            return self.player.get_position_col()
        return None

    # Implemented PlayerInterface
    def get_number(self):
        '''
        returns number
        '''
        if self.player:
            return self.player.get_number()
        return None

    # Implemented PlayerInterface
    def get_name(self):
        '''
        returns name
        '''
        if self.player:
            return self.player.get_name()
        return None
