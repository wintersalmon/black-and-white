'''
BLACK-AND-WHITE
WinterSalmon
Contains PlayerMovementHelper
'''


from data.board.board_interface import BoardInterface
from data.helper.piece_movement_helper import PieceMovementHelper
from data.player import Player, PlayerInterface


class PlayerMovementHelper(BoardInterface, PlayerInterface, PieceMovementHelper):
    '''
    Helps user move player to appropriate position on board
    '''
    def __init__(self, board):
        self.board = board
        self.player = None
        self.row = -1
        self.col = -1
        self.pattern_counter = 0
        self.piece_initialized = False


    def __increase_counter(self, counter):
        counter += 1
        if counter >= self.player.get_color_pattern().get_length():
            counter = 0
        return counter


    def is_piece_initialized(self):
        '''
        returns True if piece is already on board
        '''
        return self.piece_initialized


    def set_start_point(self, row, col):
        '''
        set piece start position
        '''
        if not self.board.check_row_col_boundary(row, col):
            return False

        if col != 0:
            return False

        pattern_color = self.player.get_color_pattern().get_symbol(0)
        block_color = self.board.get_block_color(row, col)

        if pattern_color != block_color:
            return False

        self.row = row
        self.col = col
        self.piece_initialized = True
        return True


    def move_up_shift(self):
        '''
        move selected player up
        '''
        if self.player and self.is_piece_initialized():
            move_row = self.row - 1
            if self.board.check_row_col_boundary(move_row, self.col):
                cur_color = self.board.get_block_color(self.row, self.col)
                next_color = self.get_block_color(move_row, self.col)
                if cur_color == next_color:
                    self.row = move_row
                    return True
        return False


    def move_down_shift(self):
        '''
        move selected player down
        '''
        if self.player and self.is_piece_initialized():
            move_row = self.row + 1
            if self.board.check_row_col_boundary(move_row, self.col):
                cur_color = self.board.get_block_color(self.row, self.col)
                next_color = self.get_block_color(move_row, self.col)
                if cur_color == next_color:
                    self.row = move_row
                    return True
        return False


    def move_right_shift(self):
        '''
        move selected player right
        '''
        if self.player and self.is_piece_initialized():
            move_col = self.col + 1
            if self.board.check_row_col_boundary(self.row, move_col):
                cur_color = self.board.get_block_color(self.row, self.col)
                next_color = self.get_block_color(self.row, move_col)
                if cur_color == next_color:
                    self.col = move_col
                    return True
        return False


    def move_left_shift(self):
        '''
        move current piece left
        '''
        if self.player and self.is_piece_initialized():
            move_col = self.col - 1
            if self.board.check_row_col_boundary(self.row, move_col):
                cur_color = self.board.get_block_color(self.row, self.col)
                next_color = self.get_block_color(self.row, move_col)
                if cur_color == next_color:
                    self.col = move_col
                    return True
        return False



# Implemented PlayerInterface
    def get_selected_tile(self):
        '''
        get_selected_tile
        '''
        if self.player:
            return self.player.get_selected_tile()
        return None

    # Implemented PlayerInterface
    def get_color_pattern(self):
        '''
        get_color_pattern
        '''
        if self.player:
            return self.player.get_color_pattern()
        return None

    # Implemented PlayerInterface
    def get_color_pattern_counter(self):
        '''
        get_color_pattern_counter
        '''
        if self.player:
            return self.pattern_counter
        return None

    # Implemented PlayerInterface
    def get_tile_count(self):
        '''
        get_tile_count
        '''
        if self.player:
            return self.player.get_tile_count()
        return None

    # Implemented PlayerInterface
    def get_tile(self, index):
        '''
        get_tile
        '''
        if self.player:
            return self.player.get_tile(index)
        return None

    # Implemented PlayerInterface
    def get_position(self):
        '''
        get_position
        '''
        if self.player:
            return (self.row, self.col)
        return None

    # Implemented PlayerInterface
    def get_position_row(self):
        '''
        get_position_row
        '''
        if self.player:
            return self.row
        return None

    # Implemented PlayerInterface
    def get_position_col(self):
        '''
        get_position_col
        '''
        if self.player:
            return self.col
        return None

    # Implemented PlayerInterface
    def get_number(self):
        '''
        get_number
        '''
        if self.player:
            return self.player.get_number()
        return None

    # Implemented PlayerInterface
    def get_name(self):
        '''
        get_name
        '''
        if self.player:
            return self.player.get_name()
        return None




    # Implemented BoardInterface
    def get_row_count(self):
        '''
        returns board max row count
        '''
        return self.board.get_row_count()

    # Implemented BoardInterface
    def get_col_count(self):
        '''
        returns board max col count
        '''
        return self.board.get_col_count()

    # Implemented BoardInterface
    def get_block_overlap_count(self, row, col):
        '''
        returns overlapped block counts located on [row,col]
        '''
        return self.board.get_block_overlap_count(row, col)

    # Implemented BoardInterface
    def get_block_color(self, row, col):
        '''
        returns color of the block located on [row,col]
        '''
        return self.board.get_block_color(row, col)




    # Implemented PieceMovementHelper
    def clear_marker(self):
        '''
        clear player marker
        '''
        self.player = None

    # Implemented PieceMovementHelper
    def is_marked_block(self, row, col):
        '''
        returns true if the position is marked
        '''
        if self.row == row and self.col == col:
            return True
        else:
            return False

    # Implemented PieceMovementHelper
    def get_cur_row(self):
        '''
        returns current piece row position
        '''
        return self.row

    # Implemented PieceMovementHelper
    def get_cur_col(self):
        '''
        returns current piece col position
        '''
        return self.col

    # Implemented PieceMovementHelper
    def get_cur_direction(self):
        '''
        always returns None
        dosen't use this function for player movement
        '''
        return None

    # Implemented PieceMovementHelper
    def set_piece(self, player):
        '''
        set player to move
        '''
        if not isinstance(player, Player):
            raise ValueError('player must be Player')

        row, col = player.get_position()

        if not self.board.check_row_col_boundary(row, col):
            self.piece_initialized = False
        else:
            self.piece_initialized = True

        self.player = player
        self.row = row
        self.col = col
        self.pattern_counter = self.player.get_color_pattern_counter()
        return True

    # Implemented PieceMovementHelper
    def get_piece(self):
        '''
        returns current player
        '''
        return self.player

    # Implemented PieceMovementHelper
    def can_save_piece(self):
        '''
        returns True if current player can be saved
        '''
        if self.player and self.board.check_row_col_boundary(self.row, self.col):
            return True
        else:
            return False

    # Implemented PieceMovementHelper
    def save_piece(self):
        '''
        save current player position and place it on board
        '''
        if self.can_save_piece():
            self.player.set_position(self.row, self.col)
            self.player.set_color_pattern_counter(self.pattern_counter)
            return True
        else:
            return False

    # Implemented PieceMovementHelper
    def move_up(self):
        '''
        move selected player up
        '''
        if self.player and self.is_piece_initialized():
            move_row = self.row - 1
            if self.board.check_row_col_boundary(move_row, self.col):
                color = self.board.get_block_color(move_row, self.col)
                counter = self.__increase_counter(self.pattern_counter)
                if color == self.player.get_color_pattern().get_symbol(counter):
                    self.row = move_row
                    self.pattern_counter = counter
                    return True
        return False

    # Implemented PieceMovementHelper
    def move_down(self):
        '''
        move selected player down
        '''
        if self.player and self.is_piece_initialized():
            move_row = self.row + 1
            if self.board.check_row_col_boundary(move_row, self.col):
                color = self.board.get_block_color(move_row, self.col)
                counter = self.__increase_counter(self.pattern_counter)
                if color == self.player.get_color_pattern().get_symbol(counter):
                    self.row = move_row
                    self.pattern_counter = counter
                    return True
        return False

    # Implemented PieceMovementHelper
    def move_right(self):
        '''
        move selected player right
        '''
        if self.player and self.is_piece_initialized():
            move_col = self.col + 1
            if self.board.check_row_col_boundary(self.row, move_col):
                color = self.board.get_block_color(self.row, move_col)
                counter = self.__increase_counter(self.pattern_counter)
                if color == self.player.get_color_pattern().get_symbol(counter):
                    self.col = move_col
                    self.pattern_counter = counter
                    return True
        return False

    # Implemented PieceMovementHelper
    def move_left(self):
        '''
        move current piece left
        '''
        if self.player and self.is_piece_initialized():
            move_col = self.col - 1
            if self.board.check_row_col_boundary(self.row, move_col):
                color = self.board.get_block_color(self.row, move_col)
                counter = self.__increase_counter(self.pattern_counter)
                if color == self.player.get_color_pattern().get_symbol(counter):
                    self.col = move_col
                    self.pattern_counter = counter
                    return True
        return False

    # Implemented PieceMovementHelper
    def rotate_clockwise(self):
        '''
        always returns False
        dosen't use this function for player movement
        '''
        return False

    # Implemented PieceMovementHelper
    def rotate_counter_clockwise(self):
        '''
        always returns False
        dosen't use this function for player movement
        '''
        return False
