'''
BLACK-AND-WHITE
WinterSalmon
Player Draw Unit for pygame
'''


from gui.draw.draw_unit import DrawUnit
from game.player import PlayerInterface
from game.color.constant import WHITE


class PlayerDrawUnit():
    '''
    Board Draw Unit for pygame
    '''
    def __init__(self, draw_unit):
        if not isinstance(draw_unit, DrawUnit):
            raise ValueError('draw_unit should be DrawUnit')
        self.draw_unit = draw_unit
        # board size values
        self.board_width = None
        self.board_height = None
        self.board_xmargin = None
        self.board_ymargin = None
        # tile size values
        self.tile_size = None
        self.tile_margin = None
        self.tile_border_size = None
        self.tile_default_border_color = None
        self.next_position = None


    def init_board_size(self, width, height, xmargin, ymargin):
        '''
        initialize board size
        '''
        self.board_width = width
        self.board_height = height
        self.board_xmargin = xmargin
        self.board_ymargin = ymargin


    def init_tile_size(self, size, margin, border_size, color):
        '''
        initialize tile size
        '''
        self.tile_size = size
        self.tile_margin = margin
        self.tile_border_size = border_size
        self.tile_default_border_color = color
        self.next_position = self.tile_size + self.tile_margin


    def draw(self, player):
        '''
        draw player to pygame displaysurf
        '''
        if not player or not isinstance(player, PlayerInterface):
            return

        left = self.board_xmargin
        top = self.board_ymargin
        self.draw_player_info(left, top, player)

        top += self.next_position + self.tile_margin
        self.draw_player_pattern(left, top, player)

        top += self.next_position + self.tile_margin
        self.draw_player_tiles(left, top, player)


    def draw_player_info(self, left, top, player):
        '''
        draw player info
        '''
        player_rgb = player.get_color().get_rgb()
        text_rgb = WHITE.get_rgb()

        rect = (left, top, self.tile_size, self.tile_size)
        self.draw_unit.pygame_draw_rect(player_rgb, rect)

        left += self.tile_size + self.tile_margin
        text = player.get_name()
        self.draw_unit.pygame_blit(text, left, top, text_rgb)


    def draw_player_pattern(self, left, top, player):
        '''
        draw player pattern
        '''
        player_rgb = player.get_color().get_rgb()
        text_rgb = WHITE.get_rgb()

        # print text
        text = 'Pattern : '
        self.draw_unit.pygame_blit(text, left, top, text_rgb)

        # print pattern tiles
        left += 90
        counter = player.get_color_pattern_counter()
        pattern = player.get_color_pattern().get_pattern()
        for index, symbol in enumerate(pattern):
            rect = (left, top, self.tile_size, self.tile_size)
            tile_rgb = symbol.get_rgb()
            self.draw_unit.pygame_draw_rect(tile_rgb, rect)
            if index == counter:
                self.draw_unit.pygame_draw_rect_border(player_rgb, rect, self.tile_border_size)
            left += self.next_position


    def draw_player_tiles(self, left, top, player):
        '''
        draw player tiles
        '''
        player_rgb = player.get_color().get_rgb()
        text = 'Tiles : '
        text_rgb = WHITE.get_rgb()
        self.draw_unit.pygame_blit(text, left, top, text_rgb)

        left += 90
        for idx in range(player.get_tile_count()):
            tile = player.get_tile(idx)
            tile_rgbs = list()
            tile_rgbs.append(tile.get_block(0).get_color().get_rgb())
            tile_rgbs.append(tile.get_block(1).get_color().get_rgb())
            for rgb in tile_rgbs:
                rect = (left, top, self.tile_size, self.tile_size)
                self.draw_unit.pygame_draw_rect(rgb, rect)
                if tile == player.get_selected_tile():
                    self.draw_unit.pygame_draw_rect_border(player_rgb, rect, self.tile_border_size)
                left += self.next_position
            left += self.tile_margin
