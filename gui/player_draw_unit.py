'''
BLACK-AND-WHITE
WinterSalmon
Player Draw Unit for pygame
'''


from game.player import PlayerInterface
from game.color.constant import WHITE


class PlayerDrawUnit():
    '''
    Board Draw Unit for pygame
    '''
    def __init__(self, pygame, displaysurf, basicfont):
        if not pygame:
            raise ValueError('pygame shuld not be None')

        if not displaysurf:
            raise ValueError('displaysurf shuld not be None')

        self.pygame = pygame
        self.displaysurf = displaysurf
        self.basicfont = basicfont
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
        self.__pygame_draw_rect(player_rgb, rect)

        left += self.tile_size + self.tile_margin
        text = player.get_name()
        self.__pygame_blit(text, left, top, text_rgb)


    def draw_player_pattern(self, left, top, player):
        '''
        draw player pattern
        '''
        player_rgb = player.get_color().get_rgb()
        text_rgb = WHITE.get_rgb()

        # print text
        text = 'Pattern : '
        self.__pygame_blit(text, left, top, text_rgb)

        # print pattern tiles
        left += 90
        counter = player.get_color_pattern_counter()
        pattern = player.get_color_pattern().get_pattern()
        for index, symbol in enumerate(pattern):
            rect = (left, top, self.tile_size, self.tile_size)
            tile_rgb = symbol.get_rgb()
            self.__pygame_draw_rect(tile_rgb, rect)
            if index == counter:
                self.__pygame_draw_rect_border(player_rgb, rect, self.tile_border_size)
            left += self.next_position


    def draw_player_tiles(self, left, top, player):
        '''
        draw player tiles
        '''
        player_rgb = player.get_color().get_rgb()
        text = 'Tiles : '
        text_rgb = WHITE.get_rgb()
        self.__pygame_blit(text, left, top, text_rgb)

        left += 90
        for idx in range(player.get_tile_count()):
            tile = player.get_tile(idx)
            tile_rgbs = list()
            tile_rgbs.append(tile.get_block(0).get_color().get_rgb())
            tile_rgbs.append(tile.get_block(1).get_color().get_rgb())
            for rgb in tile_rgbs:
                rect = (left, top, self.tile_size, self.tile_size)
                self.__pygame_draw_rect(rgb, rect)
                if tile == player.get_selected_tile():
                    self.__pygame_draw_rect_border(player_rgb, rect, self.tile_border_size)
                left += self.next_position
            left += self.tile_margin


    def __pygame_draw_rect(self, rgb, rect):
        self.pygame.draw.rect(self.displaysurf, rgb, rect)

    def __pygame_draw_rect_border(self, rgb, rect, border):
        self.pygame.draw.rect(self.displaysurf, rgb, rect, border)

    def __pygame_blit(self, text, left, top, rgb):
        press_key_surf = self.basicfont.render(text, True, rgb)
        press_key_rect = press_key_surf.get_rect()
        press_key_rect.topleft = (left, top)
        self.displaysurf.blit(press_key_surf, press_key_rect)
