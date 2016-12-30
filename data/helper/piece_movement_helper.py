'''
BLACK-AND-WHITE
WinterSalmon
Contains PieceMovementHelper
'''


class PieceMovementHelper():
    '''
    Interface used to help user moving piece on board correctly
    Starts with set_piece(piece) : True
    Ends with save_piece() : True
    '''
    def clear_marker(self):
        '''
        clear marker
        '''
        raise NotImplementedError('You need to implement clear_marker')


    def is_marked_block(self, row, col):
        '''
        returns true if the position is marked
        '''
        raise NotImplementedError('You need to implement is_marked_block')


    def get_cur_row(self):
        '''
        returns current piece row position
        '''
        raise NotImplementedError('You need to implement get_cur_row')


    def get_cur_col(self):
        '''
        returns current piece col position
        '''
        raise NotImplementedError('You need to implement get_cur_col')


    def get_cur_direction(self):
        '''
        returns current piece dirercion
        '''
        raise NotImplementedError('You need to implement get_cur_direction')


    def set_piece(self, piece):
        '''
        set piece to move
        '''
        raise NotImplementedError('You need to implement set_piece')


    def get_piece(self):
        '''
        returns current piece
        '''
        raise NotImplementedError('You need to implement get_piece')


    def can_save_piece(self):
        '''
        returns True if current piece can be saved
        '''
        raise NotImplementedError('You need to implement can_save_piece')


    def save_piece(self):
        '''
        save current piece
        '''
        raise NotImplementedError('You need to implement save_piece')


    def move_up(self):
        '''
        move current piece up
        '''
        raise NotImplementedError('You need to implement move_up')


    def move_down(self):
        '''
        move current piece down
        '''
        raise NotImplementedError('You need to implement move_down')


    def move_right(self):
        '''
        move current piece right
        '''
        raise NotImplementedError('You need to implement move_right')


    def move_left(self):
        '''
        move current piece left
        '''
        raise NotImplementedError('You need to implement move_left')


    def rotate_clockwise(self):
        '''
        rotate current piece clockwise (90 degrees)
        '''
        raise NotImplementedError('You need to implement rotate_clockwise')


    def rotate_counter_clockwise(self):
        '''
        rotate current piece counter clockwise (270 degrees)
        '''
        raise NotImplementedError('You need to implement rotate_counter_clockwise')
