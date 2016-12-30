'''
BLACK-AND-WHITE
WinterSalmon
Gui made with pygame
'''
import sys
import random

import pygame
from pygame.locals import *
from data.data import Data
from data.board.color import COLOR
from data.board.direction import DIRECTION
from data.board.tile import TileWW, TileWG, TileWB, TileGB, TILE

from data.board.board import Board

from cli.choice.tile_placement_choice_selector import TilePlacementChoiceSelector

from gui.board_drawer import BoardDrawer
from data.helper.tile_placement_helper import TilePlacementHelper
from data.helper.player_movement_helper import PlayerMovementHelper
from data.helper.pattern_update_helper import PatternUpdateHelper

from data.status.status import STATUS

from data.player import Player

from data.pattern.color_pattern import ColorPattern



FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

TILESIZE = 40 # size of tile height & width in pixels
TILEMARGIN = 10 # size of tile margin between tiles in pixels
TILEBOARDERSIZE = 2 # size of tile boarder in pixels

BOARDWIDTH = 12 # number of columns of icons
BOARDHEIGHT = 5 # number of rows of icons

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (TILESIZE + TILEMARGIN))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (TILESIZE + TILEMARGIN))) / 2)

#            R    G    B
WHITE    = (255, 255, 255)
GRAY     = (100, 100, 100)
BLACK    = (  0,   0,   0)

NAVYBLUE = ( 60,  60, 100)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

PLAYER_COLORS = [RED, BLUE, CYAN, ORANGE]

class Gui():
    '''
    Graphic User Interface made with pygame
    '''
    def __init__(self):
        self.game_data = None
        self.current_board_helper = None

        self.players = list()

        row, col = 0, 0
        for player in self.players:
            player.set_position(row, col)
            row += 1

        self.current_game_status = STATUS.TILE_PLACEMENT
        self.current_player = None
        self.current_tile = None
        self.current_player_helper = PatternUpdateHelper()
        self.last_action_msg = None


    def check_game_over(self):
        '''
        Stop Game if Game Over
        '''
        if False:
            pygame.quit()
            sys.exit()
        return


    def main_loop(self):
        '''
        game main loop
        '''
        continue_loop = True
        while continue_loop:
            self.draw_board()

            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if self.game_data.status == STATUS.PLAYER_CHANGE_PATTERN:
                        continue_loop = self.handle_change_pattern_event(event)
                    elif self.game_data.status == STATUS.TILE_PLACEMENT:
                        continue_loop = self.handle_tile_placement(event)
                    else:
                        continue_loop = self.handle_player_movement(event)

            pygame.display.update()
            FPSCLOCK.tick(FPS)
        return


    def start(self):
        '''
        Start Game
        '''
        # init pygame
        global FPSCLOCK, DISPLAYSURF, BASICFONT
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        DISPLAYSURF.fill(BGCOLOR)

        # init game data
        self.game_data = Data()
        max_row = BOARDHEIGHT
        max_col = BOARDWIDTH
        board = Board(max_row, max_col)

        self.players = list()
        self.players.append(Player(1, 'WinterSalmon'))
        self.players.append(Player(2, 'Kein'))
        self.players.append(Player(3, 'Sshong91'))
        self.players.append(Player(4, 'Wool'))

        patterns = list()
        for player in self.players:
            pattern = create_random_color_pattern()
            patterns.append(pattern)
            player.set_pattern(pattern)

        self.game_data.init_game(board, self.players)

        self.current_board_helper = None
        self.current_player_helper = self.game_data.pattern_update_helper

        while True:
            # give 3 card to each player
            for player in self.game_data.players:
                for _ in range(3):
                    if self.game_data.deck.size() > 0:
                        tile = self.game_data.deck.draw()
                        player.add_tile(tile)

            # for each player place tile
            for _ in range(1):
                for _ in self.game_data.players:
                    self.game_data.next_player()
                    self.game_data.change_status(STATUS.TILE_PLACEMENT)
                    self.main_loop()
                    self.check_game_over()

            # move each player once
            for _ in range(1):
                for player in self.game_data.players:
                    self.game_data.next_player()
                    self.game_data.change_status(STATUS.PLAYER_MOVEMENT)
                    self.main_loop()
                    self.check_game_over()
        return


    def left_top_coords_of_box(self, col, row):
        '''
        docstring
        '''
        # Convert board coordinates to pixel coordinates
        left = col * (TILESIZE + TILEMARGIN) + XMARGIN
        top = row * (TILESIZE + TILEMARGIN) + YMARGIN
        return (left, top)


    def draw_message(self):
        '''
        Draw Last Event Message To Screen
        '''
        message_format = '{} : {}'
        status_string = 'no status'
        last_action_msg = 'no actions'

        if self.game_data.status:
            status_string = self.game_data.status.name

        if self.last_action_msg:
            last_action_msg = self.last_action_msg

        message = message_format.format(status_string, last_action_msg)
        pressKeySurf = BASICFONT.render(message, True, WHITE)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (XMARGIN, WINDOWHEIGHT - YMARGIN + 10)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    def draw_player(self):
        '''
        draw player
        '''
        if self.game_data.current_player_drawer:
            player = self.game_data.current_player_drawer
        else:
            return

        tile_size = TILESIZE / 2
        tile_margin = TILEMARGIN / 2
        next_position = tile_size + tile_margin

        # player info line
        top = TILEMARGIN
        left = XMARGIN

        player_name = self.game_data.current_player.get_name()
        player_number = self.game_data.current_player.get_number()
        player_color = PLAYER_COLORS[player_number - 1]

        pygame.draw.rect(DISPLAYSURF, player_color, (left, top, tile_size, tile_size))
        left += tile_size + tile_margin

        pressKeySurf = BASICFONT.render(player_name, True, WHITE)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (left, top)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

        # player pattern
        top += next_position + tile_margin
        left = XMARGIN

        pressKeySurf = BASICFONT.render('Pattern : ', True, WHITE)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (left, top)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

        # (left, top) = pressKeyRect.topright
        left += 90

        counter = player.get_color_pattern_counter()
        pattern = player.get_color_pattern().get_pattern()
        for index, symbol in enumerate(pattern):
            if index == counter:
                boarder = True
            else:
                boarder = False
            if symbol == COLOR.WHITE:
                symbol_color = WHITE
            elif symbol == COLOR.GRAY:
                symbol_color = GRAY
            elif symbol == COLOR.BLACK:
                symbol_color = BLACK

            pygame.draw.rect(DISPLAYSURF, symbol_color, (left, top, tile_size, tile_size))
            if boarder:
                pygame.draw.rect(DISPLAYSURF, player_color, (left, top, tile_size, tile_size), 2)
            left += next_position



        # player Tiles
        top += next_position + tile_margin
        left = XMARGIN

        pressKeySurf = BASICFONT.render('Tiles : ', True, WHITE)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (left, top)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

        # (left, top) = pressKeyRect.topright
        left += 90

        for idx in range(player.get_tile_count()):
            tile = player.get_tile(idx)

            if tile == player.get_selected_tile():
                boarder = True
            else:
                boarder = False

            if tile.get_type() == TILE.WW:
                first_color = WHITE
                second_color = WHITE
            elif tile.get_type() == TILE.WG:
                first_color = WHITE
                second_color = GRAY
            elif tile.get_type() == TILE.WB:
                first_color = WHITE
                second_color = BLACK
            elif tile.get_type() == TILE.GB:
                first_color = GRAY
                second_color = BLACK

            if boarder:
                pygame.draw.rect(DISPLAYSURF, first_color, (left, top, tile_size, tile_size))
                pygame.draw.rect(DISPLAYSURF, player_color, (left, top, tile_size, tile_size), 2)
                left += tile_size
                pygame.draw.rect(DISPLAYSURF, second_color, (left, top, tile_size, tile_size))
                pygame.draw.rect(DISPLAYSURF, player_color, (left, top, tile_size, tile_size), 2)
            else:
                pygame.draw.rect(DISPLAYSURF, first_color, (left, top, tile_size, tile_size))
                left += next_position
                pygame.draw.rect(DISPLAYSURF, second_color, (left, top, tile_size, tile_size))

            left += next_position + tile_margin


    def draw_block(self, row, col):
        '''
        Draw block
        '''
        left, top = self.left_top_coords_of_box(col, row)

        if self.current_board_helper:
            board = self.current_board_helper
        else:
            board = self.game_data.board
        board = self.game_data.current_board_drawer
        player = self.game_data.current_player_drawer

        block_count = board.get_block_overlap_count(row, col)
        block_color = board.get_block_color(row, col)

        #fill rect
        if block_color == COLOR.WHITE:
            pygame.draw.rect(DISPLAYSURF, WHITE, (left, top, TILESIZE, TILESIZE))
        elif block_color == COLOR.GRAY:
            pygame.draw.rect(DISPLAYSURF, GRAY, (left, top, TILESIZE, TILESIZE))
        elif block_color == COLOR.BLACK:
            pygame.draw.rect(DISPLAYSURF, BLACK, (left, top, TILESIZE, TILESIZE))

        # draw outline
        if block_count == 0:
            pygame.draw.rect(DISPLAYSURF, WHITE, (left, top, TILESIZE, TILESIZE), TILEBOARDERSIZE)
        elif block_count == 2:
            pygame.draw.rect(DISPLAYSURF, GREEN, (left, top, TILESIZE, TILESIZE), TILEBOARDERSIZE)
        elif block_count > 2:
            pygame.draw.rect(DISPLAYSURF, RED, (left, top, TILESIZE, TILESIZE), TILEBOARDERSIZE)


        # draw current marker boarder
        if (not isinstance(board, Board)) and board.is_marked_block(row, col):
            number = self.game_data.current_player.get_number()
            player_color = PLAYER_COLORS[number - 1]
            pygame.draw.rect(DISPLAYSURF, player_color, (left + 5, top + 5, TILESIZE - 10, TILESIZE - 10), TILEBOARDERSIZE)


        # draw players
        for player in self.game_data.players:
            p_margin = 2
            p_size = TILESIZE / 2 - p_margin * 2
            p_left = left + p_margin
            p_top = top + p_margin
            p_width = p_size
            p_height = p_size

            p_row, p_col = player.get_position()
            if (p_row, p_col) == (row, col):
                number = player.get_number()

                player_color = PLAYER_COLORS[number-1]

                if number == 1:
                    pass
                if number == 2:
                    p_left += p_width + p_margin * 2
                if number == 3:
                    p_top += p_height + p_margin * 2
                if number == 4:
                    p_left += p_width + p_margin * 2
                    p_top += p_height + p_margin * 2

                pygame.draw.rect(DISPLAYSURF, player_color, (p_left, p_top, p_width, p_height))


    def draw_board(self):
        '''
        Draw board
        '''
        DISPLAYSURF.fill(BGCOLOR)
        for row in range(self.game_data.board.get_row_count()):
            for col in range(self.game_data.board.get_col_count()):
                self.draw_block(row, col)
        self.draw_player()
        self.draw_message()
        # self.draw_pattern()


    def handle_change_pattern_event(self, event):
        '''
        handle change pattern event
        '''
        if event.key == K_BACKQUOTE:
            self.game_data.change_status(STATUS.TILE_PLACEMENT)
        elif event.key == K_1:
            self.game_data.pattern_update_helper.enqueue_change_color(COLOR.WHITE)
            self.last_action_msg = 'add pattern WHITE'
        elif event.key == K_2:
            self.game_data.pattern_update_helper.enqueue_change_color(COLOR.GRAY)
            self.last_action_msg = 'add pattern GRAY'
        elif event.key == K_3:
            self.game_data.pattern_update_helper.enqueue_change_color(COLOR.BLACK)
            self.last_action_msg = 'add pattern BLACK'
        elif event.key == K_RETURN or event.key == K_SPACE:
            if self.game_data.pattern_update_helper.can_save_player():
                self.game_data.pattern_update_helper.save_player()
                self.game_data.current_player.remove_tile(self.game_data.current_tile)
                self.last_action_msg = 'Save Pattern'
                return False
            self.last_action_msg = 'Cannot Save Pattern'

        return True


    def handle_tile_placement(self, event):
        '''
        handle tile placement
        '''
        if event.key == K_BACKQUOTE:
            self.game_data.change_status(STATUS.PLAYER_CHANGE_PATTERN)

        elif event.key == K_1:
            self.game_data.tile_placement_helper.select_tile(0)
            self.last_action_msg = 'Change Tile to 1'

        elif event.key == K_2:
            self.game_data.tile_placement_helper.select_tile(1)
            self.last_action_msg = 'Change Tile to 2'

        elif event.key == K_3:
            self.game_data.tile_placement_helper.select_tile(2)
            self.last_action_msg = 'Change Tile to 3'

        elif event.key == K_4:
            self.game_data.tile_placement_helper.select_tile(3)
            self.last_action_msg = 'Change Tile to 4'

        elif event.key == K_LEFT or event.key == K_a:
            if self.game_data.tile_placement_helper.move_left():
                self.last_action_msg = 'Move Tile Left'
            else:
                self.last_action_msg = 'Cannot move Tile Left'

        elif event.key == K_RIGHT or event.key == K_d:
            if self.game_data.tile_placement_helper.move_right():
                self.last_action_msg = 'Move Tile Right'
            else:
                self.last_action_msg = 'Cannot move Tile Right'

        elif event.key == K_UP or event.key == K_w:
            if self.game_data.tile_placement_helper.move_up():
                self.last_action_msg = 'Move Tile Up'
            else:
                self.last_action_msg = 'Cannot move Tile Up'

        elif event.key == K_DOWN or event.key == K_s:
            if self.game_data.tile_placement_helper.move_down():
                self.last_action_msg = 'Move Tile Down'
            else:
                self.last_action_msg = 'Cannot move Tile Down'

        elif event.key == K_q:
            if self.game_data.tile_placement_helper.rotate_clockwise():
                self.last_action_msg = 'Rotate Tile Clockwise'
            else:
                self.last_action_msg = 'Cannot Rotate Tile Clockwise'

        elif event.key == K_e:
            if self.game_data.tile_placement_helper.rotate_counter_clockwise():
                self.last_action_msg = 'Rotate Tile Counter Clockwise'
            else:
                self.last_action_msg = 'Cannot Rotate Tile Counter Clockwise'

        elif event.key == K_RETURN or event.key == K_SPACE:
            if self.game_data.tile_placement_helper.can_save_piece():
                self.game_data.tile_placement_helper.save_piece()
                self.game_data.tile_placement_helper.clear_marker()
                self.last_action_msg = 'Save Tile'
                return False
            else:
                self.last_action_msg = 'Cannot Save Tile'

        return True


    def handle_player_movement(self, event):
        '''
        handle player change pattern
        '''
        if self.game_data.player_movement_helper.is_piece_initialized():
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                if event.key == K_LEFT or event.key == K_a:
                    self.game_data.player_movement_helper.move_left_shift()
                    self.last_action_msg = 'Shift Move Player LEFT'

                elif event.key == K_RIGHT or event.key == K_d:
                    self.game_data.player_movement_helper.move_right_shift()
                    self.last_action_msg = 'Shift Move Player RIGHT'

                elif event.key == K_UP or event.key == K_w:
                    self.game_data.player_movement_helper.move_up_shift()
                    self.last_action_msg = 'Shift Move Player UP'

                elif event.key == K_DOWN or event.key == K_s:
                    self.game_data.player_movement_helper.move_down_shift()
                    self.last_action_msg = 'Shift Move Player DOWN'
            else:
                if event.key == K_LEFT or event.key == K_a:
                    self.game_data.player_movement_helper.move_left()
                    self.last_action_msg = 'Move Player LEFT'

                elif event.key == K_RIGHT or event.key == K_d:
                    self.game_data.player_movement_helper.move_right()
                    self.last_action_msg = 'Move Player RIGHT'

                elif event.key == K_UP or event.key == K_w:
                    self.game_data.player_movement_helper.move_up()
                    self.last_action_msg = 'Move Player UP'

                elif event.key == K_DOWN or event.key == K_s:
                    self.game_data.player_movement_helper.move_down()
                    self.last_action_msg = 'Move Player DOWN'

                elif event.key == K_RETURN or event.key == K_SPACE:
                    if self.game_data.player_movement_helper.can_save_piece():
                        self.game_data.player_movement_helper.save_piece()
                        self.game_data.player_movement_helper.clear_marker()
                        self.last_action_msg = 'Save Player'
                        return False
                    else:
                        self.last_action_msg = 'Cannot Save Player'
        else:
            if event.key == K_1:
                if self.game_data.player_movement_helper.set_start_point(0, 0):
                    self.last_action_msg = 'Player Start At[0,0]'
            elif event.key == K_2:
                if self.game_data.player_movement_helper.set_start_point(1, 0):
                    self.last_action_msg = 'Player Start At[1,0]'
            elif event.key == K_3:
                if self.game_data.player_movement_helper.set_start_point(2, 0):
                    self.last_action_msg = 'Player Start At[2,0]'
            elif event.key == K_4:
                if self.game_data.player_movement_helper.set_start_point(3, 0):
                    self.last_action_msg = 'Player Start At[3,0]'
            elif event.key == K_5:
                if self.game_data.player_movement_helper.set_start_point(4, 0):
                    self.last_action_msg = 'Player Start At[4,0]'
        return True


'''
functions used for debugging
'''

def create_board_type_one(max_row, max_col):
    '''
    Method Description
    '''
    board = Board(max_row, max_col)

    for row in range(max_row):
        for col in range(max_col-1):
            tile = None
            if col%3 == 0:
                tile = TileWW()
            elif col%3 == 1:
                tile = TileWG()
            elif col%3 == 2:
                tile = TileWB()
            else:
                tile = TileGB()

            direction = DIRECTION.RIGHT
            board.place_tile(tile, row, col, direction)

    return board


def create_random_tile():
    '''
    returns random created tile
    '''
    tile = None
    tile_type = random.randrange(0, 4)

    if tile_type == 0:
        tile = TileWW()
    elif tile_type == 1:
        tile = TileWG()
    elif tile_type == 2:
        tile = TileWB()
    else:
        tile = TileGB()

    return tile


def create_random_color_pattern():
    '''
    returns random created ColorPattern
    '''
    # symbols = [COLOR.WHITE, COLOR.WHITE, COLOR.GRAY, COLOR.BLACK]
    # pattern = ColorPattern()

    # selections = symbols[:]
    # random.shuffle(selections)
    # pattern.set_pattern(selections)

    return ColorPattern()
