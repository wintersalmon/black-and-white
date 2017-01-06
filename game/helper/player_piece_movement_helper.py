'''
BLACK-AND-WHITE
WinterSalmon
PlayerPieceMovementHelper
'''


from game.player import PlayerInterface
from game.board.board_interface import BoardInterface
from game.board.direction import DIRECTION
from game.helper.piece_update_helper import PieceUpdateHelper
from game.pattern.color_pattern import ColorPattern

class PlayerPieceMovementHelper(PieceUpdateHelper, BoardInterface, PlayerInterface):
    '''
    Helps user move Player Piece to appropriate position on board
    '''
    def __init__(self, board):
        self.board = board
        self.target_player = None
        self.target_pattern = ColorPattern()
        self.color_pattern_counter = 0
        self.row = 0
        self.col = 0



    def get_cur_row(self):
        '''
        returns current tile row position
        '''
        return self.row

    def get_cur_col(self):
        '''
        returns current tile col position
        '''
        return self.col

    def _has_target(self):
        return self.target_player

    def _change_piece_position(self, row, col):
        if not self.board.check_row_col_boundary(row, col):
            return False

        counter = self._inc_color_pattern_counter(self.color_pattern_counter)

        block_color = self.board.get_block_color(row, col)
        pattern_color = self.target_pattern.get_symbol(counter)
        if block_color != pattern_color:
            return False

        self.row = row
        self.col = col
        self.color_pattern_counter = counter
        return True

    def _inc_color_pattern_counter(self, counter):
        counter += 1
        if counter >= self.target_pattern.get_length():
            counter = 0
        return counter

    # PieceUpdateHelper Implementations
    def set_target(self, target_player):
        '''
        Implemented PieceUpdateHelper set_target
        set target player
        '''
        if isinstance(target_player, PlayerInterface):
            # todo : check if player has more then one tile
            self.target_player = target_player
            self.target_pattern.clone(self.target_player.get_color_pattern())
            self.color_pattern_counter = self.target_player.get_color_pattern_counter()
            self.row = self.target_player.get_position_row()
            self.col = self.target_player.get_position_col()
            return True
        else:
            return False

    # PieceUpdateHelper Implementations
    def can_save_target(self):
        '''
        Implemented PieceUpdateHelper can_save_target
        returns True if Changes made to target player piece can be saved
        '''
        if not self._has_target():
            return False

        if not self.board.check_row_col_boundary(self.row, self.col):
            return False

        block_color = self.board.get_block_color(self.row, self.col)
        target_pattern = self.target_player.get_color_pattern()
        pattern_color = target_pattern.get_symbol(self.color_pattern_counter)
        if block_color != pattern_color:
            return False

        return True

    # PieceUpdateHelper Implementations
    def save_target(self):
        '''
        Implemented PieceUpdateHelper save_target
        Save change made to target player piece
        '''
        if self.can_save_target():
            self.target_player.set_position(self.row, self.col)
            self.target_player.set_color_pattern_counter(self.color_pattern_counter)
            return True
        else:
            return False

    # PieceUpdateHelper Implementations
    def move(self, direction, option=None):
        '''
        Implemented PieceUpdateHelper move
        move selected tile acording to given direction and option
        '''
        if not self._has_target():
            return False

        row = self.row
        col = self.col
        if direction == DIRECTION.UP:
            row -= 1
        elif direction == DIRECTION.DOWN:
            row += 1
        elif direction == DIRECTION.LEFT:
            col -= 1
        elif direction == DIRECTION.RIGHT:
            col += 1
        return self._change_piece_position(row, col)

    # PieceUpdateHelper Implementations
    def placement(self, row, col):
        '''
        Implemented PieceUpdateHelper placement
        place selected tile to given position(row,col)
        '''
        if not self._has_target():
            return False

        return self._change_piece_position(row, col)

    # PieceUpdateHelper Implementations
    def rotate(self, count=1):
        '''
        Implemented PieceUpdateHelper rotate
        Allways returns False
        Player Piece doesn't use this function
        '''
        return False



    # BoardInterface Implemented
    def get_row_count(self):
        '''
        Implemented BoardInterface get_row_count
        returns board max row count
        '''
        return self.board.get_row_count()

    # BoardInterface Implemented
    def get_col_count(self):
        '''
        Implemented BoardInterface get_col_count
        returns board max col count
        '''
        return self.board.get_col_count()

    # BoardInterface Implemented
    def get_block_overlap_count(self, row, col):
        '''
        Implemented BoardInterface get_block_overlap_count
        returns overlapped block counts located on [row,col]
        '''
        return self.board.get_block_overlap_count(row, col)

    # BoardInterface Implemented
    def get_block_color(self, row, col):
        '''
        Implemented BoardInterface get_block_color
        returns color of the block located on [row,col]
        '''
        return self.board.get_block_color(row, col)

    # BoardInterface Implemented
    def is_marked(self, row, col):
        '''
        Implemented BoardInterface is_marked
        returns true if the position is marked
        '''
        return self.row == row and self.col == col



    # PlayerInterface Implemented
    def get_selected_tile(self):
        '''
        Implemented PlayerInterface get_selected_tile
        returns target player's selected tile
        '''
        if self._has_target():
            return self.target_player.get_selected_tile()
        else:
            return None

    # PlayerInterface Implemented
    def get_color_pattern(self):
        '''
        Implemented PlayerInterface get_color_pattern
        get_color_pattern
        '''
        if self._has_target():
            return self.target_pattern
        else:
            return None

    # PlayerInterface Implemented
    def get_color_pattern_counter(self):
        '''
        Implemented PlayerInterface get_color_pattern_counter
        get_color_pattern_counter
        '''
        if self._has_target():
            return self.color_pattern_counter
        return None

    # PlayerInterface Implemented
    def get_tile_count(self):
        '''
        Implemented PlayerInterface get_tile_count
        get_tile_count
        '''
        if self._has_target():
            return self.target_player.get_tile_count()
        else:
            return None

    # PlayerInterface Implemented
    def get_tile(self, index):
        '''
        Implemented PlayerInterface get_tile
        get_tile
        '''
        if self._has_target():
            return self.target_player.get_tile(index)
        else:
            return None

    # PlayerInterface Implemented
    def get_position(self):
        '''
        Implemented PlayerInterface get_position
        get_position
        '''
        if self._has_target():
            return (self.row, self.col)
        else:
            return None

    # PlayerInterface Implemented
    def get_position_row(self):
        '''
        Implemented PlayerInterface get_position_row
        get_position_row
        '''
        if self._has_target():
            return self.row
        else:
            return None

    # PlayerInterface Implemented
    def get_position_col(self):
        '''
        Implemented PlayerInterface get_position_col
        get_position_col
        '''
        if self._has_target():
            return self.col
        else:
            return None

    # PlayerInterface Implemented
    def get_number(self):
        '''
        Implemented PlayerInterface get_number
        get_number
        '''
        if self._has_target():
            return self.target_player.get_number()
        else:
            return None

    # PlayerInterface Implemented
    def get_name(self):
        '''
        Implemented PlayerInterface get_name
        get_name
        '''
        if self._has_target():
            return self.target_player.get_name()
        else:
            return None

    # PlayerInterface Implemented
    def get_color(self):
        '''
        Implemented PlayerInterface get_color
        get_color
        '''
        if self._has_target():
            return self.target_player.get_color()
        else:
            return None
