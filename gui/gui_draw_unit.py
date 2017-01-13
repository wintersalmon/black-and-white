'''
BLACK-AND-WHITE
WinterSalmon
Draw Unit Collection for pygame
'''
from game.game import Game
from game.color.constant import WHITE, NAVYBLUE, BLUE

from gui.draw.draw_unit import DrawUnit
from gui.draw.draw_background import DrawBackground
from gui.draw.draw_board import DrawBoard
from gui.draw.draw_player import DrawPlayer
from gui.draw.draw_message import DrawMessage

class GuiDrawUnit():
    '''
    Draw Unit for pygame
    '''
    def __init__(self, game):
        if not isinstance(game, Game):
            raise ValueError('game should be instance of Game')
        self.game = game
        # init
        max_row = game.get_max_row()
        max_col = game.get_max_col()
        # todo : change window size to adapt to max row,col

        width = 640
        height = 480
        margin_x = 20
        margin_y = 15

        line_size = 30
        text_color = WHITE

        tile_size = 40
        tile_margin = 10
        tile_border_size = 2

        marker_size = tile_size - 8
        marker_margin = tile_margin + 4
        marker_border_size = 2

        # init draw units
        self.draw_unit = DrawUnit(width, height, margin_x, margin_y)

        self.draw_background = DrawBackground(self.draw_unit)
        self.draw_background.init_background_color(NAVYBLUE)

        self.draw_player = DrawPlayer(self.draw_unit, self.game, 0, 0)
        self.draw_player.init_line_info(line_size, text_color)
        self.draw_player.init_tile_info(tile_size/2, tile_margin/2, tile_border_size/2)

        self.draw_board = DrawBoard(self.draw_unit, self.game, 0, 100)
        self.draw_board.init_tile_info(tile_size, tile_margin, tile_border_size, WHITE)
        self.draw_board.init_marker_info(marker_size, marker_margin, marker_border_size, BLUE)

        self.draw_message = DrawMessage(self.draw_unit, self.game, 0, 350)
        self.draw_message.init_line_info(line_size, text_color)

        self.draw_unit_list = list()
        self.draw_unit_list.append(self.draw_background)
        self.draw_unit_list.append(self.draw_player)
        self.draw_unit_list.append(self.draw_board)
        self.draw_unit_list.append(self.draw_message)


    def draw(self):
        '''
        draw game
        '''
        for draw_unit in self.draw_unit_list:
            draw_unit.draw()
