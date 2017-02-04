'''
BLACK-AND-WHITE
WinterSalmon
PlayerPiecePlacementHelper
'''

from game.player import PlayerInterface
from game.helper.player_piece_movement_helper import PlayerPieceMovementHelper


class PlayerPiecePlacementHelper(PlayerPieceMovementHelper):
    '''
    Helps user Place Player Piece to appropriate position on board
    '''
    def __init__(self, board):
        super().__init__(board)

    def _change_piece_position(self, row, col):
        if col == 0 and self.board.check_row_col_boundary(row, col):
            self.row = row
            self.col = col
            return True
        else:
            return False


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
            self.row = 0
            self.col = 0
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
        pattern_color = self.target_pattern.get_symbol(self.color_pattern_counter)
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
