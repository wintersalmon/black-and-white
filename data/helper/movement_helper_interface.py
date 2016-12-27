'''
BLACK-AND-WHITE
WinterSalmon
Contains MovementHelperInterface
'''


class MovementHelperInterface():
    '''
    Interface used to help user moving item on board correctly
    Starts with set_item(item) : True
    Ends with save_item() : True
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
        returns current item row position
        '''
        raise NotImplementedError('You need to implement get_cur_row')


    def get_cur_col(self):
        '''
        returns current item col position
        '''
        raise NotImplementedError('You need to implement get_cur_col')


    def get_cur_direction(self):
        '''
        returns current item dirercion
        '''
        raise NotImplementedError('You need to implement get_cur_direction')


    def set_item(self, item, row, col, direction):
        '''
        set item to move
        '''
        raise NotImplementedError('You need to implement set_item')


    def get_item(self):
        '''
        returns current item
        '''
        raise NotImplementedError('You need to implement get_item')


    def can_save_item(self):
        '''
        returns True if current item can be saved
        '''
        raise NotImplementedError('You need to implement can_save_item')


    def save_item(self):
        '''
        save current item
        '''
        raise NotImplementedError('You need to implement save_item')


    def move_up(self):
        '''
        move current item up
        '''
        raise NotImplementedError('You need to implement move_up')


    def move_down(self):
        '''
        move current item down
        '''
        raise NotImplementedError('You need to implement move_down')


    def move_right(self):
        '''
        move current item right
        '''
        raise NotImplementedError('You need to implement move_right')


    def move_left(self):
        '''
        move current item left
        '''
        raise NotImplementedError('You need to implement move_left')


    def rotate_clockwise(self):
        '''
        rotate current item clockwise (90 degrees)
        '''
        raise NotImplementedError('You need to implement rotate_clockwise')


    def rotate_counter_clockwise(self):
        '''
        rotate current item counter clockwise (270 degrees)
        '''
        raise NotImplementedError('You need to implement rotate_counter_clockwise')
