'''
BLACK-AND-WHITE
WinterSalmon
Contains TilePlacementHelper
'''


from data.board.tile import Tile
from data.board.board_interface import BoardInterface
from data.board.direction import DIRECTION

from data.helper.movement_helper_interface import MovementHelperInterface


class TilePlacementHelper(BoardInterface, MovementHelperInterface):
    '''
    Helps user move tile to appropriate position on board
    '''
    def __init__(self, board):
        self.board = board
        self.tile = None
        self.row = 0
        self.col = 0
        self.direction = DIRECTION.RIGHT


    # Implement BoardInterface get_row_count
    def get_row_count(self):
        '''
        returns board max row count
        '''
        return self.board.get_row_count()


    # Implement BoardInterface get_col_count
    def get_col_count(self):
        '''
        returns board max col count
        '''
        return self.board.get_col_count()


    # Implement BoardInterface get_block_overlap_count
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


    # Implement BoardInterface get_block_color
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


    # Implement MovementHelperInterface clear_marker
    def clear_marker(self):
        '''
        clear tile marker
        '''
        self.tile = None
        self.row = 0
        self.col = 0
        self.direction = DIRECTION.RIGHT


    # Implement MovementHelperInterface is_marked_block
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


    # Implement MovementHelperInterface get_cur_row
    def get_cur_row(self):
        '''
        returns current tile row position
        '''
        return self.row


    # Implement MovementHelperInterface get_cur_col
    def get_cur_col(self):
        '''
        returns current tile col position
        '''
        return self.col


    # Implement MovementHelperInterface get_cur_direction
    def get_cur_direction(self):
        '''
        returns current tile dirercion
        '''
        return self.direction


    # Implement MovementHelperInterface set_item
    def set_item(self, tile, row=0, col=0, direction=DIRECTION.RIGHT):
        '''
        set tile to move
        '''
        if isinstance(tile, Tile) and self.board.check_tile_is_on_board(row, col, direction):
            self.tile = tile
            self.row = row
            self.col = col
            self.direction = direction
            return True
        else:
            return False


    # Implement MovementHelperInterface get_item
    def get_item(self):
        '''
        returns current tile
        '''
        return self.tile


    # Implement MovementHelperInterface can_save_item
    def can_save_item(self):
        '''
        returns True if current tile can be saved
        '''
        if self.tile and self.board.can_place_tile(self.tile, self.row, self.col, self.direction):
            return True
        else:
            return False


    # Implement MovementHelperInterface save_item
    def save_item(self):
        '''
        save current tile position and place it on board
        '''
        if self.can_save_item():
            self.board.place_tile(self.tile, self.row, self.col, self.direction)
            return True
        else:
            return False


    # Implement MovementHelperInterface move_up
    def move_up(self):
        '''
        move current tile up
        '''
        move_row = self.row - 1
        if self.tile and self.board.check_tile_is_on_board(move_row, self.col, self.direction):
            self.row = move_row
            return True
        else:
            return False


    # Implement MovementHelperInterface move_down
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


    # Implement MovementHelperInterface move_right
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


    # Implement MovementHelperInterface move_left
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


    # Implement MovementHelperInterface rotate_clockwise
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


    # Implement MovementHelperInterface rotate_counter_clockwise
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
