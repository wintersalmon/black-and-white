'''
BLACK-AND-WHITE
WinterSalmon
PlayerTilePlacementHelper
'''


from game.player import PlayerInterface
from game.board.tile import Tile
from game.board.board_interface import BoardInterface
from game.board.direction import DIRECTION
from game.helper.piece_update_helper import PieceUpdateHelper


class PlayerTilePlacementHelper(PieceUpdateHelper, BoardInterface):
    '''
    Helps user move tile to appropriate position on board
    '''
    def __init__(self, board):
        self.board = board
        self.target_player = None
        # current tiles
        self.tile = None
        self.row = 0
        self.col = 0
        self.direction = None


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

    def get_cur_direction(self):
        '''
        returns current tile dirercion
        '''
        return self.direction

    def change_selected_tile(self, number):
        '''
        change target player selected tile
        '''
        if not self.__has_target():
            return False

        tile = self.target_player.select_tile(number)
        if not isinstance(tile, Tile):
            return False

        self.tile = tile
        return True


    def __has_target(self):
        return self.target_player and self.tile

    def __change_tile_position(self, row, col, direction):
        if self.board.check_tile_is_on_board(row, col, direction):
            self.row = row
            self.col = col
            self.direction = direction
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
            self.tile = self.target_player.select_tile(0)
            self.row = 0
            self.col = 0
            self.direction = DIRECTION.RIGHT
            return True
        else:
            return False

    # PieceUpdateHelper Implementations
    def can_save_target(self):
        '''
        Implemented PieceUpdateHelper can_save_target
        returns True if Changes made to target player selected tile can be saved
        '''
        if not self.__has_target():
            return False

        if not self.board.can_place_tile(self.tile, self.row, self.col, self.direction):
            return False

        return True

    # PieceUpdateHelper Implementations
    def save_target(self):
        '''
        Implemented PieceUpdateHelper save_target
        Save change made to target player selected tile
        '''
        if self.can_save_target():
            # todo : check if player has self.tile
            self.board.place_tile(self.tile, self.row, self.col, self.direction)
            self.target_player.remove_tile(self.tile)
            return True
        else:
            return False

    # PieceUpdateHelper Implementations
    def move(self, direction, option=None):
        '''
        Implemented PieceUpdateHelper move
        move selected tile acording to given direction and option
        '''
        if not self.__has_target():
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
        return self.__change_tile_position(row, col, self.direction)

    # PieceUpdateHelper Implementations
    def placement(self, row, col):
        '''
        Implemented PieceUpdateHelper placement
        place selected tile to given position(row,col)
        '''
        if not self.__has_target():
            return False

        # if same position is selected rotate tile
        if (row, col) == (self.row, self.col):
            return self.rotate()
        else:
            return self.__change_tile_position(row, col, self.direction)

    # PieceUpdateHelper Implementations
    def rotate(self, count=1):
        '''
        Implemented PieceUpdateHelper rotate
        rotate selected tile by 90 * count degrees
        '''
        if count < 0:
            return False
        # ignore count more then 4 (which is equal to 360 rotation)
        count %= 4

        direction = self.direction
        for _ in range(count):
            direction = DIRECTION.rotate(self.direction)

        return self.__change_tile_position(self.row, self.col, direction)



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
        count = self.board.get_block_overlap_count(row, col)

        if self.tile:
            # is current [row,col]
            if self.row == row and self.col == col:
                count += 1

            # is current [row,col,direction]
            row2, col2 = DIRECTION.adjust_row_col_by_direction(self.row, self.col, self.direction)
            if row2 == row and col2 == col:
                count += 1

        return count

    # BoardInterface Implemented
    def get_block_color(self, row, col):
        '''
        Implemented BoardInterface get_block_color
        returns color of the block located on [row,col]
        '''
        color = self.board.get_block_color(row, col)

        if self.tile:
            # is current [row,col]
            if self.row == row and self.col == col:
                color = self.tile.get_block(0).get_mixed_color(color)

            # is current [row,col,direction]
            row2, col2 = DIRECTION.adjust_row_col_by_direction(self.row, self.col, self.direction)
            if row2 == row and col2 == col:
                color = self.tile.get_block(1).get_mixed_color(color)

        return color

    # BoardInterface Implemented
    def is_marked(self, row, col):
        '''
        Implemented BoardInterface is_marked
        returns true if the position is marked
        '''
        if self.row == row and self.col == col:
            return True

        adj_row, adj_col = DIRECTION.adjust_row_col_by_direction(self.row, self.col, self.direction)
        if adj_row == row and adj_col == col:
            return True

        return False
