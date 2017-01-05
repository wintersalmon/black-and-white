'''
BLACK-AND-WHITE
WinterSalmon
Contains class Gui Graphic User Interface made with pygame
'''
import sys
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

from gui.draw.draw_unit import DrawUnit
from gui.draw.board_draw_unit import BoardDrawUnit
from gui.draw.player_draw_unit import PlayerDrawUnit
from gui.draw.message_draw_unit import MessageDrawUnit

WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

TILESIZE = 40 # size of tile height & width in pixels
TILEMARGIN = 10 # size of tile margin between tiles in pixels
TILEBOARDERSIZE = 2 # size of tile boarder in pixels

MAX_COL = 12 # number of columns of icons
MAX_ROW = 5 # number of rows of icons
XMARGIN = int((WINDOWWIDTH - (MAX_COL * (TILESIZE + TILEMARGIN))) / 2)
YMARGIN = int((WINDOWHEIGHT - (MAX_ROW * (TILESIZE + TILEMARGIN))) / 2)

class Gui():
    '''
    Graphic User Interface made with pygame
    '''
    def __init__(self):
        # init pygame
        pygame.init()
        self.fps = 30
        self.fpsclock = pygame.time.Clock()
        self.displaysurf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.displaysurf.fill(NAVYBLUE.get_rgb())
        self.basicfont = pygame.font.Font('freesansbold.ttf', 18)

        self.draw_unit = DrawUnit(pygame, self.displaysurf, self.basicfont)
        self.board_draw_unit = BoardDrawUnit(self.draw_unit)
        self.player_draw_unit = PlayerDrawUnit(self.draw_unit)
        self.message_draw_unit = MessageDrawUnit(self.draw_unit)

        # init game
        self.game = None
        self.last_action_msg = None


    def init(self):
        '''
        displays game init screen and handles event
        '''
        # init draw units
        self.board_draw_unit.init_board_size(WINDOWWIDTH, WINDOWHEIGHT, XMARGIN, YMARGIN, NAVYBLUE)
        self.board_draw_unit.init_tile_size(TILESIZE, TILEMARGIN, TILEBOARDERSIZE, WHITE)
        self.board_draw_unit.init_marker_size(TILESIZE-10, TILEMARGIN+5, TILEBOARDERSIZE, BLUE)
        self.player_draw_unit.init(XMARGIN, TILEMARGIN, TILESIZE/2, TILEMARGIN/2, 2, WHITE)
        self.message_draw_unit.init(XMARGIN, WINDOWHEIGHT - YMARGIN + 10, WHITE)

        self.game = Game()

        player_info_list = list()
        player_info_list.append(('WinterSalmon', RED))
        player_info_list.append(('Kein', BLUE))
        player_info_list.append(('Sshong91', CYAN))
        player_info_list.append(('Wool', ORANGE))

        self.game.init_game(player_info_list, MAX_ROW, MAX_COL)


    def credit(self):
        '''
        displays game credit screen and handles event
        '''
        pass


    def run(self):
        '''
        main game loop
        '''
        while self.game.is_game_running():
            self.draw()
            self.handle_events()
            self.update()
        return


    def draw(self):
        '''
        draw game
        '''
        self.board_draw_unit.draw(self.game.get_current_board(), self.game.players)
        self.player_draw_unit.draw(self.game.get_current_player())
        self.message_draw_unit.draw(self.last_action_msg)


    def handle_events(self):
        '''
        handle all events
        '''
        self.check_for_quit()
        for event in pygame.event.get():
            if self.game.get_current_status() == STATUS.TILE_PLACEMENT:
                self.game.continue_status = self.handle_tile_placement_event(event)
            elif self.game.get_current_status() == STATUS.TILE_PLACEMENT_CHANGE_PATTERN:
                self.game.continue_status = self.handle_change_pattern_event(event)
            elif self.game.get_current_status() == STATUS.PLAYER_MOVEMENT_SET_START_POINT:
                self.game.continue_status = self.handle_set_start_point_event(event)
            elif self.game.get_current_status() == STATUS.PLAYER_MOVEMENT:
                self.game.continue_status = self.handle_player_movement_event(event)


    def update(self):
        '''
        update
        '''
        self.game.update()
        pygame.display.update()
        self.fpsclock.tick(self.fps)


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
            elif event.key in (K_RETURN, K_SPACE):
                if self.game.pattern_update_helper.can_save_player():
                    self.game.pattern_update_helper.save_player()
                    self.last_action_msg = 'Save Pattern'
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

            elif event.key in (K_LEFT, K_a):
                if self.game.tile_placement_helper.move_left():
                    self.last_action_msg = 'Move Tile Left'
                else:
                    self.last_action_msg = 'Cannot move Tile Left'

            elif event.key in (K_RIGHT, K_d):
                if self.game.tile_placement_helper.move_right():
                    self.last_action_msg = 'Move Tile Right'
                else:
                    self.last_action_msg = 'Cannot move Tile Right'

            elif event.key in (K_UP, K_w):
                if self.game.tile_placement_helper.move_up():
                    self.last_action_msg = 'Move Tile Up'
                else:
                    self.last_action_msg = 'Cannot move Tile Up'

            elif event.key in (K_DOWN, K_s):
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

            elif event.key in (K_RETURN, K_SPACE):
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
                    if event.key in (K_LEFT, K_a):
                        self.game.player_movement_helper.move_left_shift()
                        self.last_action_msg = 'Shift Move Player LEFT'

                    elif event.key in (K_RIGHT, K_d):
                        self.game.player_movement_helper.move_right_shift()
                        self.last_action_msg = 'Shift Move Player RIGHT'

                    elif event.key in (K_UP, K_w):
                        self.game.player_movement_helper.move_up_shift()
                        self.last_action_msg = 'Shift Move Player UP'

                    elif event.key in (K_DOWN, K_s):
                        self.game.player_movement_helper.move_down_shift()
                        self.last_action_msg = 'Shift Move Player DOWN'
                else:
                    if event.key in (K_LEFT, K_a):
                        self.game.player_movement_helper.move_left()
                        self.last_action_msg = 'Move Player LEFT'

                    elif event.key in (K_RIGHT, K_d):
                        self.game.player_movement_helper.move_right()
                        self.last_action_msg = 'Move Player RIGHT'

                    elif event.key in (K_UP, K_w):
                        self.game.player_movement_helper.move_up()
                        self.last_action_msg = 'Move Player UP'

                    elif event.key in (K_DOWN, K_s):
                        self.game.player_movement_helper.move_down()
                        self.last_action_msg = 'Move Player DOWN'

                    elif event.key in (K_RETURN, K_SPACE):
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

    def check_for_quit(self):
        '''
        check for quit event and quit the game
        '''
        for event in pygame.event.get((QUIT, KEYUP)): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
