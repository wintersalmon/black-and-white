'''
BLACK-AND-WHITE
WinterSalmon
Contains PlayerMovementHelper
'''


from data.board.board_interface import BoardInterface
from data.helper.movement_helper_interface import MovementHelperInterface
from data.player import Player


class PlayerMovementHelper(BoardInterface, MovementHelperInterface):
    '''
    Helps user move player to appropriate position on board
    '''
    def __init__(self, board):
        self.board = board
        self.player = None
        self.row = -1
        self.col = -1


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
        return self.board.get_block_overlap_count(row, col)


    # Implement BoardInterface get_block_color
    def get_block_color(self, row, col):
        '''
        returns color of the block located on [row,col]
        '''
        return self.board.get_block_color(row, col)



    # Implement MovementHelperInterface clear_marker
    def clear_marker(self):
        '''
        clear player marker
        '''
        self.player = None


    # Implement MovementHelperInterface is_marked_block
    def is_marked_block(self, row, col):
        '''
        returns true if the position is marked
        '''
        if self.row == row and self.col == col:
            return True
        else:
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
        always returns None
        dosen't use this function for player movement
        '''
        return None


    # Implement MovementHelperInterface set_item
    def set_item(self, player, row=None, col=None, direction=None):
        '''
        set player to move
        '''
        if not isinstance(player, Player):
            return False

        if row is None and col is None:
            row, col = player.get_position()

        if row == -1 or col == -1:
            row, col = 0, 0

        if not self.board.check_row_col_boundary(row, col):
            return False

        self.player = player
        self.row = row
        self.col = col
        return True


    # Implement MovementHelperInterface set_item
    def get_item(self):
        '''
        returns current player
        '''
        return self.player


    # Implement MovementHelperInterface set_item
    def can_save_item(self):
        '''
        returns True if current player can be saved
        '''
        if self.player and self.board.check_row_col_boundary(self.row, self.col):
            return True
        else:
            return False


    # Implement MovementHelperInterface set_item
    def save_item(self):
        '''
        save current player position and place it on board
        '''
        if self.can_save_item():
            self.player.set_position(self.row, self.col)
            return True
        else:
            return False


    # Implement MovementHelperInterface set_item
    def move_up(self):
        '''
        move selected player up
        '''
        if self.player:
            move_row = self.row - 1
            if self.board.check_row_col_boundary(move_row, self.col):
                self.row = move_row
                return True
        return False


    # Implement MovementHelperInterface set_item
    def move_down(self):
        '''
        move selected player down
        '''
        if self.player:
            move_row = self.row + 1
            if self.board.check_row_col_boundary(move_row, self.col):
                self.row = move_row
                return True
        return False


    # Implement MovementHelperInterface set_item
    def move_right(self):
        '''
        move selected player right
        '''
        if self.player:
            move_col = self.col + 1
            if self.board.check_row_col_boundary(self.row, move_col):
                self.col = move_col
                return True
        return False


    # Implement MovementHelperInterface set_item
    def move_left(self):
        '''
        move current tile left
        '''
        if self.player:
            move_col = self.col - 1
            if self.board.check_row_col_boundary(self.row, move_col):
                self.col = move_col
                return True
        return False


    # Implement MovementHelperInterface set_item
    def rotate_clockwise(self):
        '''
        always returns False
        dosen't use this function for player movement
        '''
        return False


    # Implement MovementHelperInterface set_item
    def rotate_counter_clockwise(self):
        '''
        always returns False
        dosen't use this function for player movement
        '''
        return False
