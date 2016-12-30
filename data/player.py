'''
BLACK-AND-WHITE
WinterSalmon
Player
'''


from data.board.tile import Tile
from data.pattern.color_pattern import ColorPattern


class PlayerInterface():
    '''
    PlayerInterface
    '''


    def get_selected_tile(self):
        '''
        get_selected_tile
        '''
        raise NotImplementedError('You need to implement get_selected_tile')


    def get_color_pattern(self):
        '''
        get_color_pattern
        '''
        raise NotImplementedError('You need to implement get_color_pattern')


    def get_color_pattern_counter(self):
        '''
        get_color_pattern_counter
        '''
        raise NotImplementedError('You need to implement get_color_pattern_counter')


    def get_tile_count(self):
        '''
        get_tile_count
        '''
        raise NotImplementedError('You need to implement get_tile_count')


    def get_tile(self, index):
        '''
        get_tile
        '''
        raise NotImplementedError('You need to implement get_tile')


    def get_position(self):
        '''
        get_position
        '''
        raise NotImplementedError('You need to implement get_position')


    def get_position_row(self):
        '''
        get_position_row
        '''
        raise NotImplementedError('You need to implement get_position_row')


    def get_position_col(self):
        '''
        get_position_col
        '''
        raise NotImplementedError('You need to implement get_position_col')


    def get_number(self):
        '''
        get_number
        '''
        raise NotImplementedError('You need to implement get_number')


    def get_name(self):
        '''
        get_name
        '''
        raise NotImplementedError('You need to implement get_name')



class Player(PlayerInterface):
    '''
    Player
    '''
    def __init__(self, number, name):
        self.tiles = list()
        self.number = number
        self.name = name
        self.row = -1
        self.col = -1
        self.color_pattern = None
        self.pattern_counter = 0
        self.selected_tile = None


    def get_selected_tile(self):
        '''
        returns selected tile numbers
        '''
        return self.selected_tile


    def get_color_pattern(self):
        '''
        get color pattern
        '''
        return self.color_pattern


    def get_color_pattern_counter(self):
        '''
        get pattern counter
        '''
        return self.pattern_counter


    def set_color_pattern_counter(self, counter):
        '''
        set pattern counter
        '''
        if 0 <= counter < self.color_pattern.get_length():
            self.pattern_counter = counter
            return True
        return False


    def set_pattern(self, pattern):
        '''
        set color pattern
        '''
        if isinstance(pattern, ColorPattern):
            self.color_pattern = pattern
            self.pattern_counter = 0
            return True
        return False


    def remove_all_tiles(self):
        '''
        remove all tile from player
        '''
        self.tiles.clear()


    def add_tile(self, tile):
        '''
        add tile to Player
        '''
        if isinstance(tile, Tile):
            self.tiles.append(tile)
            return True
        else:
            return False


    def remove_tile(self, tile):
        '''
        remove tile from Player
        '''
        self.tiles = list(filter((tile).__ne__, self.tiles))


    def select_tile(self, index):
        '''
        returns and select tile
        '''
        tile = self.get_tile(index)
        if tile:
            self.selected_tile = self.tiles[index]
        return tile


    def get_tile(self, index):
        '''
        returns tile to Player
        '''
        if 0 <= index < len(self.tiles):
            return self.tiles[index]
        else:
            return None


    def get_tile_count(self):
        '''
        returns number of tile player has
        '''
        return len(self.tiles)


    def reset_position(self):
        '''
        reset player position on board
        '''
        self.row = -1
        self.col = -1


    def player_on_board(self):
        '''
        returns True if player is on board
        '''
        if self.row == -1 or self.col == -1:
            return False
        else:
            return True


    def set_position(self, row, col):
        '''
        set player position (row, col)
        '''
        self.row = row
        self.col = col


    def get_position(self):
        '''
        returns player position (row, col)
        '''
        return self.row, self.col


    def get_position_row(self):
        '''
        returns player position row
        '''
        return self.row


    def get_position_col(self):
        '''
        returns player position col
        '''
        return self.col


    def get_number(self):
        '''
        returns player number
        '''
        return self.number


    def get_name(self):
        '''
        returns player name
        '''
        return self.name
