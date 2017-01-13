'''
BLACK-AND-WHITE
WinterSalmon
Player Draw Unit for pygame
'''
from gui.draw.draw_unit import DrawUnit
from game.game import Game
from game.player import PlayerInterface
from game.color.color import Color


class DrawPlayer():
    '''
    Board Draw Unit for pygame
    '''
    def __init__(self, draw_unit, game, offset_x, offset_y):
        if not isinstance(draw_unit, DrawUnit):
            raise ValueError('draw_unit should be instance of DrawUnit')
        if not isinstance(game, Game):
            raise ValueError('game should be instance of Game')

        self.draw_unit = draw_unit
        self.game = game
        # size values
        self.offset_x = offset_x
        self.offset_y = offset_y
        # tile values
        self.tile_size = None
        self.tile_margin = None
        self.tile_border_size = None
        # text values
        self.text_color = None
        self.line_size = None


    def init_tile_info(self, tile_size, tile_margin, tile_border_size):
        '''
        initialize tile info
        '''
        self.tile_size = int(tile_size)
        self.tile_margin = int(tile_margin)
        self.tile_border_size = int(tile_border_size)


    def init_line_info(self, line_size, text_color):
        '''
        initialize line info
        '''
        if not isinstance(text_color, Color):
            raise ValueError('bgcolor should be instance of Color')
        self.line_size = int(line_size)
        self.text_color = text_color


    def draw(self):
        '''
        draw player to pygame displaysurf
        '''
        # todo : improve code
        player = self.game.get_current_player()
        if player and isinstance(player, PlayerInterface):
            left = self.offset_x + self.draw_unit.get_margin_x()
            top = self.offset_y + self.draw_unit.get_margin_y()
            self.draw_player_info(left, top, player)

            top += self.line_size + self.tile_margin
            self.draw_player_pattern(left, top, player)

            top += self.line_size + self.tile_margin
            self.draw_player_tiles(left, top, player)


    def draw_player_info(self, left, top, player):
        '''
        draw player info
        '''
        player_rgb = player.get_color().get_rgb()
        text_rgb = self.text_color.get_rgb()

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
        text_rgb = self.text_color.get_rgb()

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
            left += self.line_size


    def draw_player_tiles(self, left, top, player):
        '''
        draw player tiles
        '''
        player_rgb = player.get_color().get_rgb()
        text = 'Tiles : '
        text_rgb = self.text_color.get_rgb()
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
                left += self.line_size
            left += self.tile_margin
