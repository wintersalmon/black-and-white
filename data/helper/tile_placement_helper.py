'''
BLACK-AND-WHITE
WinterSalmon
Contains TilePlacementHelper
'''


from data.board.tile import Tile
from data.board.board_interface import BoardInterface
from data.board.direction import DIRECTION

from data.helper.piece_movement_helper import PieceMovementHelper


class TilePlacementHelper(BoardInterface, PieceMovementHelper):
    '''
    Helps user move tile to appropriate position on board
    '''
    def __init__(self, board):
        self.board = board
        self.player = None
        self.tile = None
        self.row = 0
        self.col = 0
        self.direction = DIRECTION.RIGHT


    def select_tile(self, number):
        '''
        change selected tile
        '''
        tile = self.player.select_tile(number)
        if tile:
            self.tile = tile
            return True
        else:
            return False


    # Implemented BoardInterface get_row_count
    def get_row_count(self):
        '''
        returns board max row count
        '''
        return self.board.get_row_count()


    # Implemented BoardInterface get_col_count
    def get_col_count(self):
        '''
        returns board max col count
        '''
        return self.board.get_col_count()


    # Implemented BoardInterface get_block_overlap_count
    def get_block_overlap_count(self, row, col):
        '''
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


    # Implemented BoardInterface get_block_color
    def get_block_color(self, row, col):
        '''
        returns color of the block located on [row,col]
        '''
        color = self.board.get_block_color(row, col)

        if self.tile:
            # is current [row,col]
            if self.row == row and self.col == col:
                color += self.tile.get_block(0).get_color()

            # is current [row,col,direction]
            row2, col2 = DIRECTION.adjust_row_col_by_direction(self.row, self.col, self.direction)
            if row2 == row and col2 == col:
                color += self.tile.get_block(1).get_color()

        return color


    # Implemented PieceMovementHelper clear_marker
    def clear_marker(self):
        '''
        clear tile marker
        '''
        self.tile = None
        self.row = 0
        self.col = 0
        self.direction = DIRECTION.RIGHT


    # Implemented PieceMovementHelper is_marked_block
    def is_marked_block(self, row, col):
        '''
        returns true if the position is marked
        '''
        if self.row == row and self.col == col:
            return True

        adj_row, adj_col = DIRECTION.adjust_row_col_by_direction(self.row, self.col, self.direction)
        if adj_row == row and adj_col == col:
            return True

        return False


    # Implemented PieceMovementHelper get_cur_row
    def get_cur_row(self):
        '''
        returns current tile row position
        '''
        return self.row


    # Implemented PieceMovementHelper get_cur_col
    def get_cur_col(self):
        '''
        returns current tile col position
        '''
        return self.col


    # Implemented PieceMovementHelper get_cur_direction
    def get_cur_direction(self):
        '''
        returns current tile dirercion
        '''
        return self.direction


    # Implemented PieceMovementHelper set_piece
    def set_piece(self, player):
        '''
        set tile to move
        '''
        self.player = player
        tile = self.player.get_tile(0)
        row = 0
        col = 0
        direction = DIRECTION.RIGHT
        if isinstance(tile, Tile) and self.board.check_tile_is_on_board(row, col, direction):
            self.tile = self.player.select_tile(0)
            self.row = row
            self.col = col
            self.direction = direction
            return True
        else:
            return False


    # Implemented PieceMovementHelper get_piece
    def get_piece(self):
        '''
        returns current tile
        '''
        return self.tile


    # Implemented PieceMovementHelper can_save_piece
    def can_save_piece(self):
        '''
        returns True if current tile can be saved
        '''
        if self.tile and self.board.can_place_tile(self.tile, self.row, self.col, self.direction):
            return True
        else:
            return False


    # Implemented PieceMovementHelper save_piece
    def save_piece(self):
        '''
        save current tile position and place it on board
        '''
        if self.can_save_piece():
            self.board.place_tile(self.tile, self.row, self.col, self.direction)
            self.player.remove_tile(self.tile)
            return True
        else:
            return False


    # Implemented PieceMovementHelper move_up
    def move_up(self):
        '''
        move current piece up
        '''
        move_row = self.row - 1
        if self.tile and self.board.check_tile_is_on_board(move_row, self.col, self.direction):
            self.row = move_row
            return True
        else:
            return False


    # Implemented PieceMovementHelper move_down
    def move_down(self):
        '''
        move current tile down
        '''
        move_row = self.row + 1
        if self.tile and self.board.check_tile_is_on_board(move_row, self.col, self.direction):
            self.row = move_row
            return True
        else:
            return False


    # Implemented PieceMovementHelper move_right
    def move_right(self):
        '''
        move current tile right
        '''
        move_col = self.col + 1
        if self.tile and self.board.check_tile_is_on_board(self.row, move_col, self.direction):
            self.col = move_col
            return True
        else:
            return False


    # Implemented PieceMovementHelper move_left
    def move_left(self):
        '''
        move current item left
        '''
        move_col = self.col - 1
        if self.tile and self.board.check_tile_is_on_board(self.row, move_col, self.direction):
            self.col = move_col
            return True
        else:
            return False


    # Implemented PieceMovementHelper rotate_clockwise
    def rotate_clockwise(self):
        '''
        rotate current tile clockwise (90 degrees)
        '''
        rotate_direction = DIRECTION.rotate(self.direction)
        if self.tile and self.board.check_tile_is_on_board(self.row, self.col, rotate_direction):
            self.direction = rotate_direction
            return True
        else:
            return False


    # Implemented PieceMovementHelper rotate_counter_clockwise
    def rotate_counter_clockwise(self):
        '''
        rotate current tile counter clockwise (270 degrees)
        '''
        rotate_direction = self.direction
        rotate_direction = DIRECTION.rotate(rotate_direction)
        rotate_direction = DIRECTION.rotate(rotate_direction)
        rotate_direction = DIRECTION.rotate(rotate_direction)
        if self.tile and self.board.check_tile_is_on_board(self.row, self.col, rotate_direction):
            self.direction = rotate_direction
            return True
        else:
            return False
