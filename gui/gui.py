'''
BLACK-AND-WHITE
WinterSalmon
Contains class Gui Graphic User Interface made with pygame
'''
import sys
import random
import pygame
from pygame.locals import *

from game.game import Game
from game.board.board import Board
from game.board.tile import TILE
from game.color.constant import *
from game.status.status import STATUS
from game.helper.tile_placement_helper import TilePlacementHelper
from game.helper.player_movement_helper import PlayerMovementHelper
from game.helper.pattern_update_helper import PatternUpdateHelper

from gui.board_draw_unit import BoardDrawUnit


FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

TILESIZE = 40 # size of tile height & width in pixels
TILEMARGIN = 10 # size of tile margin between tiles in pixels
TILEBOARDERSIZE = 2 # size of tile boarder in pixels

MAX_COL = 12 # number of columns of icons
MAX_ROW = 5 # number of rows of icons

XMARGIN = int((WINDOWWIDTH - (MAX_COL * (TILESIZE + TILEMARGIN))) / 2)
YMARGIN = int((WINDOWHEIGHT - (MAX_ROW * (TILESIZE + TILEMARGIN))) / 2)

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
        self.game = None
        self.border_draw_unit = None
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


    def init(self):
        '''
        displays game init screen and handles event
        '''


    def credit(self):
        '''
        displays game credit screen and handles event
        '''
        pass


    def run(self):
        '''
        displays main game screen and handles event
        '''
        # init pygame
        global FPSCLOCK, DISPLAYSURF, BASICFONT
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        DISPLAYSURF.fill(BGCOLOR.get_rgb())

        # init draw units
        self.border_draw_unit = BoardDrawUnit(pygame, DISPLAYSURF)
        self.border_draw_unit.init_board_size(WINDOWWIDTH, WINDOWHEIGHT, XMARGIN, YMARGIN, BGCOLOR)
        self.border_draw_unit.init_tile_size(TILESIZE, TILEMARGIN, TILEBOARDERSIZE, WHITE)
        self.border_draw_unit.init_marker_size(TILESIZE-10, TILEMARGIN+5, TILEBOARDERSIZE, BLUE)

        # init game Game
        self.game = Game()

        player_info_list = list()
        player_info_list.append(('WinterSalmon', RED))
        player_info_list.append(('Kein', BLUE))
        player_info_list.append(('Sshong91', CYAN))
        player_info_list.append(('Wool', ORANGE))

        self.game.init_game(player_info_list, MAX_ROW, MAX_COL)

        while self.game.is_game_running():
            self.draw(self.game)
            self.status = self.game.get_current_status()

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif self.status == STATUS.TILE_PLACEMENT:
                    self.game.continue_status = self.handle_tile_placement_event(event)

                elif self.status == STATUS.TILE_PLACEMENT_CHANGE_PATTERN:
                    self.game.continue_status = self.handle_change_pattern_event(event)

                elif self.status == STATUS.PLAYER_MOVEMENT_SET_START_POINT:
                    self.game.continue_status = self.handle_set_start_point_event(event)

                elif self.status == STATUS.PLAYER_MOVEMENT:
                    self.game.continue_status = self.handle_player_movement_event(event)


            self.game.update()
            pygame.display.update()
            FPSCLOCK.tick(FPS)


    def draw(self, game):
        '''
        draw game
        '''
        self.draw_board(game.get_current_board(), game.players)
        self.draw_player(game.get_current_player())
        self.draw_message(game.get_current_message())


    def draw_board(self, board, players):
        '''
        Draw board
        '''
        if not board:
            return
        self.border_draw_unit.draw(board, players)


    def draw_player(self, player):
        '''
        draw player
        '''
        if not player:
            return

        tile_size = TILESIZE / 2
        tile_margin = TILEMARGIN / 2
        next_position = tile_size + tile_margin

        # player info line
        top = TILEMARGIN
        left = XMARGIN

        player_name = player.get_name()
        player_number = player.get_number()
        player_color = PLAYER_COLORS[player_number - 1]

        pygame.draw.rect(DISPLAYSURF, player_color.get_rgb(), (left, top, tile_size, tile_size))
        left += tile_size + tile_margin

        pressKeySurf = BASICFONT.render(player_name, True, WHITE.get_rgb())
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (left, top)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

        # player pattern
        top += next_position + tile_margin
        left = XMARGIN

        pressKeySurf = BASICFONT.render('Pattern : ', True, WHITE.get_rgb())
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
            # if symbol == COLOR.WHITE:
            #     symbol_color = WHITE
            # elif symbol == COLOR.GRAY:
            #     symbol_color = GRAY
            # elif symbol == COLOR.BLACK:
            #     symbol_color = BLACK

            pygame.draw.rect(DISPLAYSURF, symbol.get_rgb(), (left, top, tile_size, tile_size))
            if boarder:
                pygame.draw.rect(DISPLAYSURF, player_color.get_rgb(), (left, top, tile_size, tile_size), 2)
            left += next_position

        # player Tiles
        top += next_position + tile_margin
        left = XMARGIN

        pressKeySurf = BASICFONT.render('Tiles : ', True, WHITE.get_rgb())
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
                pygame.draw.rect(DISPLAYSURF, first_color.get_rgb(), (left, top, tile_size, tile_size))
                pygame.draw.rect(DISPLAYSURF, player_color.get_rgb(), (left, top, tile_size, tile_size), 2)
                left += tile_size
                pygame.draw.rect(DISPLAYSURF, second_color.get_rgb(), (left, top, tile_size, tile_size))
                pygame.draw.rect(DISPLAYSURF, player_color.get_rgb(), (left, top, tile_size, tile_size), 2)
            else:
                pygame.draw.rect(DISPLAYSURF, first_color.get_rgb(), (left, top, tile_size, tile_size))
                left += next_position
                pygame.draw.rect(DISPLAYSURF, second_color.get_rgb(), (left, top, tile_size, tile_size))

            left += next_position + tile_margin


    def draw_message(self, message):
        '''
        Draw Last Event Message To Screen
        '''
        message = self.last_action_msg
        if not message:
            return
        pressKeySurf = BASICFONT.render(message, True, WHITE.get_rgb())
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (XMARGIN, WINDOWHEIGHT - YMARGIN + 10)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


    def left_top_coords_of_box(self, col, row):
        '''
        docstring
        '''
        # Convert board coordinates to pixel coordinates
        left = col * (TILESIZE + TILEMARGIN) + XMARGIN
        top = row * (TILESIZE + TILEMARGIN) + YMARGIN
        return (left, top)


    def handle_change_pattern_event(self, event):
        '''
        handle change pattern event
        '''
        if event.type == KEYDOWN:
            if event.key == K_BACKQUOTE:
                return False
            elif event.key == K_1:
                self.game.pattern_update_helper.enqueue_change_color(WHITE)
                self.last_action_msg = 'add pattern WHITE'
            elif event.key == K_2:
                self.game.pattern_update_helper.enqueue_change_color(GRAY)
                self.last_action_msg = 'add pattern GRAY'
            elif event.key == K_3:
                self.game.pattern_update_helper.enqueue_change_color(BLACK)
                self.last_action_msg = 'add pattern BLACK'
            elif event.key == K_RETURN or event.key == K_SPACE:
                if self.game.pattern_update_helper.can_save_player():
                    self.game.pattern_update_helper.save_player()
                    self.last_action_msg = 'Save Pattern'
                    print(self.last_action_msg)
                    return False
                self.last_action_msg = 'Cannot Save Pattern'
        return True


    def handle_tile_placement_event(self, event):
        '''
        handle tile placement
        '''
        if event.type == KEYDOWN:
            if event.key == K_BACKQUOTE:
                # todo : hide this CODE into game class
                status = STATUS.TILE_PLACEMENT_CHANGE_PATTERN
                board = self.game.get_current_board()
                player = self.game.get_current_player()
                self.game.pattern_update_helper.set_player(player)
                player = self.game.pattern_update_helper
                self.game.change_status(status, board, player, True)
                # todo : hide this CODE into game class

            elif event.key == K_1:
                self.game.tile_placement_helper.select_tile(0)
                self.last_action_msg = 'Change Tile to 1'

            elif event.key == K_2:
                self.game.tile_placement_helper.select_tile(1)
                self.last_action_msg = 'Change Tile to 2'

            elif event.key == K_3:
                self.game.tile_placement_helper.select_tile(2)
                self.last_action_msg = 'Change Tile to 3'

            elif event.key == K_4:
                self.game.tile_placement_helper.select_tile(3)
                self.last_action_msg = 'Change Tile to 4'

            elif event.key == K_LEFT or event.key == K_a:
                if self.game.tile_placement_helper.move_left():
                    self.last_action_msg = 'Move Tile Left'
                else:
                    self.last_action_msg = 'Cannot move Tile Left'

            elif event.key == K_RIGHT or event.key == K_d:
                if self.game.tile_placement_helper.move_right():
                    self.last_action_msg = 'Move Tile Right'
                else:
                    self.last_action_msg = 'Cannot move Tile Right'

            elif event.key == K_UP or event.key == K_w:
                if self.game.tile_placement_helper.move_up():
                    self.last_action_msg = 'Move Tile Up'
                else:
                    self.last_action_msg = 'Cannot move Tile Up'

            elif event.key == K_DOWN or event.key == K_s:
                if self.game.tile_placement_helper.move_down():
                    self.last_action_msg = 'Move Tile Down'
                else:
                    self.last_action_msg = 'Cannot move Tile Down'

            elif event.key == K_q:
                if self.game.tile_placement_helper.rotate_clockwise():
                    self.last_action_msg = 'Rotate Tile Clockwise'
                else:
                    self.last_action_msg = 'Cannot Rotate Tile Clockwise'

            elif event.key == K_e:
                if self.game.tile_placement_helper.rotate_counter_clockwise():
                    self.last_action_msg = 'Rotate Tile Counter Clockwise'
                else:
                    self.last_action_msg = 'Cannot Rotate Tile Counter Clockwise'

            elif event.key == K_RETURN or event.key == K_SPACE:
                if self.game.tile_placement_helper.can_save_piece():
                    self.game.tile_placement_helper.save_piece()
                    self.game.tile_placement_helper.clear_marker()
                    self.last_action_msg = 'Save Tile'
                    return False
                else:
                    self.last_action_msg = 'Cannot Save Tile'

        return True


    def handle_set_start_point_event(self, event):
        '''
        handle_set_start_point_event
        '''
        pass


    def handle_player_movement_event(self, event):
        '''
        handle player change pattern
        '''
        if event.type == KEYDOWN:
            if self.game.player_movement_helper.is_piece_initialized():
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    if event.key == K_LEFT or event.key == K_a:
                        self.game.player_movement_helper.move_left_shift()
                        self.last_action_msg = 'Shift Move Player LEFT'

                    elif event.key == K_RIGHT or event.key == K_d:
                        self.game.player_movement_helper.move_right_shift()
                        self.last_action_msg = 'Shift Move Player RIGHT'

                    elif event.key == K_UP or event.key == K_w:
                        self.game.player_movement_helper.move_up_shift()
                        self.last_action_msg = 'Shift Move Player UP'

                    elif event.key == K_DOWN or event.key == K_s:
                        self.game.player_movement_helper.move_down_shift()
                        self.last_action_msg = 'Shift Move Player DOWN'
                else:
                    if event.key == K_LEFT or event.key == K_a:
                        self.game.player_movement_helper.move_left()
                        self.last_action_msg = 'Move Player LEFT'

                    elif event.key == K_RIGHT or event.key == K_d:
                        self.game.player_movement_helper.move_right()
                        self.last_action_msg = 'Move Player RIGHT'

                    elif event.key == K_UP or event.key == K_w:
                        self.game.player_movement_helper.move_up()
                        self.last_action_msg = 'Move Player UP'

                    elif event.key == K_DOWN or event.key == K_s:
                        self.game.player_movement_helper.move_down()
                        self.last_action_msg = 'Move Player DOWN'

                    elif event.key == K_RETURN or event.key == K_SPACE:
                        if self.game.player_movement_helper.can_save_piece():
                            self.game.player_movement_helper.save_piece()
                            self.game.player_movement_helper.clear_marker()
                            self.last_action_msg = 'Save Player'
                            return False
                        else:
                            self.last_action_msg = 'Cannot Save Player'
            else:
                if event.key == K_1:
                    if self.game.player_movement_helper.set_start_point(0, 0):
                        self.last_action_msg = 'Player Start At[0,0]'
                elif event.key == K_2:
                    if self.game.player_movement_helper.set_start_point(1, 0):
                        self.last_action_msg = 'Player Start At[1,0]'
                elif event.key == K_3:
                    if self.game.player_movement_helper.set_start_point(2, 0):
                        self.last_action_msg = 'Player Start At[2,0]'
                elif event.key == K_4:
                    if self.game.player_movement_helper.set_start_point(3, 0):
                        self.last_action_msg = 'Player Start At[3,0]'
                elif event.key == K_5:
                    if self.game.player_movement_helper.set_start_point(4, 0):
                        self.last_action_msg = 'Player Start At[4,0]'
        return True
