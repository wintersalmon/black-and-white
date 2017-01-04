'''
BLACK-AND-WHITE
WinterSalmon
Board Draw Unit for pygame
'''


from game.board.board_interface import BoardInterface


class BoardDrawUnit():
    '''
    Board Draw Unit for pygame
    '''
    def __init__(self):
        # board size values
        self.board_width = None
        self.board_height = None
        self.board_xmargin = None
        self.board_ymargin = None
        # tile size values
        self.tile_size = None
        self.tile_margin = None


    def init_board_size(self, width, height, xmargin, ymargin):
        '''
        initialize board size
        '''
        self.board_width = width
        self.board_height = height
        self.board_xmargin = xmargin
        self.board_ymargin = ymargin


    def init_tile_size(self, size, margin):
        '''
        initialize tile size
        '''
        self.tile_size = size
        self.tile_margin = margin


    def draw(self, displaysurf, board):
        '''
        draw board on screen
        '''
        if not displaysurf:
            raise ValueError('displaysurf shuld not be None')

        if not isinstance(board, BoardInterface):
            raise ValueError('board must be instance of BoardInterface')

        for row in range(board.get_row_count()):
            for col in range(board.get_col_count()):
                self.draw_block(board, row, col)


    def draw_block(self, board, row, col):
        '''
        draw block, boarder, marker
        '''
        # todo : set variables
        left, top = self.left_top_coords_of_block(row, col)
        left, top, block_color, border_color, marker_color = (0, 0, 0, 0, 0)

        self.draw_block_fill(left, top, block_color)
        self.draw_block_border(left, top, border_color)
        self.draw_block_marker(left, top, marker_color)


    def draw_block_fill(self, left, top, color):
        '''
        fill block with color
        '''
        pass


    def draw_block_border(self, left, top, color):
        '''
        draw block border with color
        '''
        pass


    def draw_block_marker(self, left, top, color):
        '''
        draw block marker with color
        '''
        pass

    def left_top_coords_of_block(self, row, col):
        '''
        Convert (row, col) to pixel coordinates (left, top)
        '''
        left = col * (self.tile_size + self.tile_size) + self.board_xmargin
        top = row * (self.tile_size + self.tile_size) + self.board_ymargin
        return (left, top)