'''
BLACK-AND-WHITE
WinterSalmon
Board Draw Unit for pygame
'''
from gui.draw.draw_unit import DrawUnit
from game.game import Game
from game.board.board_interface import BoardInterface
from game.color.constant import NOCOLOR, GREEN, RED


class DrawBoard():
    '''
    Board Draw Unit for pygame
    '''
    def __init__(self, draw_unit, game, offset_x=0, offset_y=0):
        if not isinstance(draw_unit, DrawUnit):
            raise ValueError('draw_unit should be instance of DrawUnit')
        if not isinstance(game, Game):
            raise ValueError('game should be instance of Game')

        self.draw_unit = draw_unit
        self.game = game
        # size values
        self.board_width = self.draw_unit.get_width()
        self.board_height = self.draw_unit.get_height()
        self.offset_x = offset_x
        self.offset_y = offset_y
        # tile size values
        self.tile_size = None
        self.tile_margin = None
        self.tile_border_size = None
        self.tile_default_border_color = None
        # marker size values
        self.marker_size = None
        self.marker_margin = None
        self.marker_border_size = None
        self.marker_default_border_color = None


    def init_tile_info(self, size, margin, border_size, color):
        '''
        initialize tile size
        '''
        self.tile_size = int(size)
        self.tile_margin = int(margin)
        self.tile_border_size = int(border_size)
        self.tile_default_border_color = color


    def init_marker_info(self, size, margin, border_size, color):
        '''
        initialize tile size
        '''
        self.marker_size = int(size)
        self.marker_margin = int(margin)
        self.marker_border_size = int(border_size)
        self.marker_default_border_color = color


    def draw(self):
        '''
        draw board and players to pygame displaysurf
        '''
        board = self.game.get_current_board()
        players = self.game.players

        if board and isinstance(board, BoardInterface):
            self._draw_board(board)

        if players and isinstance(players, list) and len(players) > 0:
            self._draw_players(players)


    def _draw_board(self, board):
        '''
        draw board to pygame displaysurf
        '''
        for row in range(board.get_row_count()):
            for col in range(board.get_col_count()):
                self.__draw_block(board, row, col)


    def _draw_players(self, players):
        '''
        draw players on board to pygame displaysurf
        '''
        for player in players:
            row = player.get_position_row()
            col = player.get_position_col()
            number = player.get_number()
            color = player.get_color()

            if row != -1 and col != -1:
                self.__draw_player_on_block(row, col, number, color)

    def __draw_block(self, board, row, col):
        '''
        draw block, boarder, marker
        '''
        left, top = self.__left_top_coords_of_block(row, col)
        marker_left, marker_top = self.__left_top_coords_of_marker(row, col)

        # get block color
        block_color = board.get_block_color(row, col)

        # get border color
        block_count = board.get_block_overlap_count(row, col)
        border_color = block_color
        if block_count == 2:
            border_color = GREEN
        elif block_count > 2:
            border_color = RED

        # get marker color
        marker_color = NOCOLOR
        if board.is_marked(row, col):
            marker_color = self.marker_default_border_color

        # draw each part of block
        self.__draw_block_fill(left, top, block_color)
        self.__draw_block_border(left, top, border_color)
        self.__draw_block_marker(marker_left, marker_top, marker_color)

    def __draw_block_fill(self, left, top, color):
        if color == NOCOLOR:
            return
        rgb = color.get_rgb()
        rect = (left, top, self.tile_size, self.tile_size)
        self.draw_unit.pygame_draw_rect(rgb, rect)

    def __draw_block_border(self, left, top, color):
        if color == NOCOLOR:
            color = self.tile_default_border_color
        rgb = color.get_rgb()
        rect = (left, top, self.tile_size, self.tile_size)
        border = self.tile_border_size
        self.draw_unit.pygame_draw_rect_border(rgb, rect, border)

    def __draw_block_marker(self, left, top, color):
        if color == NOCOLOR:
            return
        rgb = color.get_rgb()
        rect = (left, top, self.marker_size, self.marker_size)
        border = self.marker_border_size
        self.draw_unit.pygame_draw_rect_border(rgb, rect, border)

    def __draw_player_on_block(self, row, col, number, color):
        left, top = self.__left_top_coords_of_block(row, col)

        p_margin = 2
        p_size = self.tile_size / 2 - p_margin * 2
        p_left = left + p_margin
        p_top = top + p_margin
        p_width = p_size
        p_height = p_size

        if number == 1:
            pass
        elif number == 2:
            p_left += p_width + p_margin * 2
        elif number == 3:
            p_top += p_height + p_margin * 2
        elif number == 4:
            p_left += p_width + p_margin * 2
            p_top += p_height + p_margin * 2
        else:
            raise ValueError('player number must be between 1 ~ 4')

        rgb = color.get_rgb()
        rect = (p_left, p_top, p_width, p_height)
        self.draw_unit.pygame_draw_rect(rgb, rect)

    def __left_top_coords_of_block(self, row, col):
        '''
        Convert (row, col) to pixel coordinates (left, top)
        '''
        margin_x = self.draw_unit.get_margin_x() + self.offset_x
        margin_y = self.draw_unit.get_margin_y() + self.offset_y
        left = col * (self.tile_size + self.tile_margin) + margin_x
        top = row * (self.tile_size + self.tile_margin) + margin_y
        return (left, top)

    def __left_top_coords_of_marker(self, row, col):
        '''
        Convert (row, col) to pixel coordinates (left, top)
        '''
        left, top = self.__left_top_coords_of_block(row, col)
        left += (self.tile_size - self.marker_size) / 2
        top += (self.tile_size - self.marker_size) / 2
        return (left, top)
