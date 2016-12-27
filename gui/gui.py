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
from data.board.tile import TileWW, TileWG, TileWB, TileGB

from data.board.board import Board

from cli.choice.tile_placement_choice_selector import TilePlacementChoiceSelector

from gui.board_drawer import BoardDrawer
from data.helper.tile_placement_helper import TilePlacementHelper
from data.helper.player_movement_helper import PlayerMovementHelper

from data.status.status import STATUS

from data.player import Player


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

class Gui():
    '''
    Graphic User Interface made with pygame
    '''
    def __init__(self):
        self.game_data = None
        self.max_row = 0
        self.max_col = 0
        self.board = None
        self.current_board_helper = None
        self.tile_placement_helper = None
        self.player_movement_helper = None

        self.players = list()
        self.players.append(Player(1, 'PlayerOne'))
        self.players.append(Player(2, 'PlayerTwo'))
        self.players.append(Player(3, 'PlayerThree'))
        self.players.append(Player(4, 'PlayerFour'))

        row, col = 0, 0
        for player in self.players:
            player.set_position(row, col)
            row += 1

        self.num_of_player_in_game = len(self.players)
        self.game_status = STATUS.TILE_PLACEMENT

        self.current_player = None
        self.current_tile = None

        self.tile_placement_counter = 0
        self.current_tile_placement_player = 0
        self.current_movement_player = 0


    def start(self):
        '''
        Start Game
        '''
        self.game_data = Data()
        self.max_row = BOARDHEIGHT
        self.max_col = BOARDWIDTH
        self.board = Board(self.max_row, self.max_col)

        self.tile_placement_helper = TilePlacementHelper(self.board)
        self.player_movement_helper = PlayerMovementHelper(self.board)

        self.current_board_helper = self.tile_placement_helper

        global FPSCLOCK, DISPLAYSURF
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

        DISPLAYSURF.fill(BGCOLOR)

        while True: # main game loop
            # mouse_clicked = False

            self.draw_board()

            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if self.handle_change_mode(event):
                    continue
                else:
                    if self.game_status == STATUS.TILE_PLACEMENT:
                        self.handle_status_tile_placement(event)
                    elif self.game_status == STATUS.PLAYER_MOVEMENT:
                        self.handle_player_movement(event)


            # self.update_status()
            pygame.display.update()
            FPSCLOCK.tick(FPS)



    # def update_status(self):
    #     '''
    #     update game STATUS
    #     '''
    #     if self.game_status == STATUS.GAME_START:
    #         self.game_status = STATUS.STANDBY_TILE_PLACEMENT
    #     elif self.game_status == STATUS.STANDBY_TILE_PLACEMENT:
    #         self.game_status = STATUS.TILE_PLACEMENT
    #         self.tile_placement_counter += 1
    #         self.tile_placement_helper.new_tile(create_random_tile())
    #     elif self.game_status == STATUS.FINISHED_TILE_PLACEMENT:
    #         if self.tile_placement_counter == self.num_of_player_in_game * 3:
    #             self.game_status = STATUS.STANDBY_PLAYER_MOVEMENT
    #             self.current_movement_player = 0
    #     elif self.game_status == STATUS.STANDBY_PLAYER_MOVEMENT:
    #         self.game_status = STATUS.PLAYER_MOVEMENT
    #     elif self.game_status == STATUS.PLAYER_MOVEMENT:
    #         self.game_status = STATUS.FINISHED_PLAYER_MOVEMENT
    #     elif self.game_status == STATUS.FINISHED_PLAYER_MOVEMENT:
    #         self.current_movement_player += 1
    #         if self.current_movement_player == self.num_of_player_in_game:
    #             self.game_status = STATUS.ROUND_OVER
    #         else:
    #             self.game_status = STATUS.STANDBY_PLAYER_MOVEMENT
    #     elif self.game_status == STATUS.ROUND_OVER:
    #         print('ROUND_OVER')
    #         pygame.quit()
    #         sys.exit()


    def handle_change_mode(self, event):
        if event.type == KEYDOWN:
            if event.key == K_BACKQUOTE:
                self.game_status = STATUS.TILE_PLACEMENT
                self.tile_placement_helper.set_item(create_random_tile())
                self.current_board_helper = self.tile_placement_helper

                return True

            elif event.key == K_1:
                self.current_movement_player = 0
                self.current_player = self.players[0]

                self.game_status = STATUS.PLAYER_MOVEMENT
                self.player_movement_helper.set_item(self.current_player)
                self.current_board_helper = self.player_movement_helper

                return True

            elif event.key == K_2:
                self.current_movement_player = 1
                self.current_player = self.players[1]

                self.game_status = STATUS.PLAYER_MOVEMENT
                self.player_movement_helper.set_item(self.current_player)
                self.current_board_helper = self.player_movement_helper

                return True

            elif event.key == K_3:
                self.current_movement_player = 2
                self.current_player = self.players[2]

                self.game_status = STATUS.PLAYER_MOVEMENT
                self.player_movement_helper.set_item(self.current_player)
                self.current_board_helper = self.player_movement_helper

                return True

            elif event.key == K_4:
                self.current_movement_player = 3
                self.current_player = self.players[3]

                self.game_status = STATUS.PLAYER_MOVEMENT
                self.player_movement_helper.set_item(self.current_player)
                self.current_board_helper = self.player_movement_helper

                return True

        else:
            return False


    def handle_status_tile_placement(self, event):
        '''
        handles user player movement input
        '''
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                self.current_board_helper.move_left()

            elif event.key == K_RIGHT or event.key == K_d:
                self.current_board_helper.move_right()

            elif event.key == K_UP or event.key == K_w:
                self.current_board_helper.move_up()

            elif event.key == K_DOWN or event.key == K_s:
                self.current_board_helper.move_down()

            elif event.key == K_q:
                self.current_board_helper.rotate_clockwise()

            elif event.key == K_e:
                self.current_board_helper.rotate_counter_clockwise()

            # elif event.key == K_n:
            #     self.current_board_helper.set_item(create_random_tile())

            elif event.key == K_RETURN or event.key == K_SPACE:
                if self.current_board_helper.can_save_item():
                    self.current_board_helper.save_item()
                    self.current_board_helper.clear_marker()


    def handle_player_movement(self, event):
        '''
        handles user tile placement input
        '''
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                self.current_board_helper.move_left()

            elif event.key == K_RIGHT or event.key == K_d:
                self.current_board_helper.move_right()

            elif event.key == K_UP or event.key == K_w:
                self.current_board_helper.move_up()

            elif event.key == K_DOWN or event.key == K_s:
                self.current_board_helper.move_down()

            elif event.key == K_RETURN or event.key == K_SPACE:
                if self.current_board_helper.can_save_item():
                    self.current_board_helper.save_item()
                    self.current_board_helper.clear_marker()



    def left_top_coords_of_box(self, col, row):
        '''
        docstring
        '''
        # Convert board coordinates to pixel coordinates
        left = col * (TILESIZE + TILEMARGIN) + XMARGIN
        top = row * (TILESIZE + TILEMARGIN) + YMARGIN
        return (left, top)


    def draw_block(self, row, col):
        '''
        Draw block
        '''
        left, top = self.left_top_coords_of_box(col, row)

        block_count = self.current_board_helper.get_block_overlap_count(row, col)
        block_color = self.current_board_helper.get_block_color(row, col)

        #fill rect
        if block_color == COLOR.WHITE:
            pygame.draw.rect(DISPLAYSURF, WHITE, (left, top, TILESIZE, TILESIZE))
        elif block_color == COLOR.GRAY:
            pygame.draw.rect(DISPLAYSURF, GRAY, (left, top, TILESIZE, TILESIZE))
        elif block_color == COLOR.BLACK:
            pygame.draw.rect(DISPLAYSURF, BLACK, (left, top, TILESIZE, TILESIZE))


        # draw current marker boarder
        if self.current_board_helper and self.current_board_helper.is_marked_block(row, col):
            pygame.draw.rect(DISPLAYSURF, BLUE, (left, top, TILESIZE, TILESIZE), TILEBOARDERSIZE)


        # draw outline
        if block_count == 0:
            pygame.draw.rect(DISPLAYSURF, WHITE, (left, top, TILESIZE, TILESIZE), TILEBOARDERSIZE)
        elif block_count == 2:
            pygame.draw.rect(DISPLAYSURF, GREEN, (left, top, TILESIZE, TILESIZE), TILEBOARDERSIZE)
        elif block_count > 2:
            pygame.draw.rect(DISPLAYSURF, RED, (left, top, TILESIZE, TILESIZE), TILEBOARDERSIZE)


        # draw players
        for player in self.players:
            p_margin = 2
            p_size = TILESIZE / 2 - p_margin * 2
            p_left = left + p_margin
            p_top = top + p_margin
            p_width = p_size
            p_height = p_size

            p_row, p_col = player.get_position()
            if (p_row, p_col) == (row, col):
                number = player.get_number()
                if number == 1:
                    pygame.draw.rect(DISPLAYSURF, RED, (p_left, p_top, p_width, p_height))
                if number == 2:
                    p_left += p_width + p_margin * 2
                    pygame.draw.rect(DISPLAYSURF, BLUE, (p_left, p_top, p_width, p_height))
                if number == 3:
                    p_top += p_height + p_margin * 2
                    pygame.draw.rect(DISPLAYSURF, CYAN, (p_left, p_top, p_width, p_height))
                if number == 4:
                    p_left += p_width + p_margin * 2
                    p_top += p_height + p_margin * 2
                    pygame.draw.rect(DISPLAYSURF, ORANGE, (p_left, p_top, p_width, p_height))



    def draw_board(self):
        '''
        Draw board
        '''
        DISPLAYSURF.fill(BGCOLOR)
        for row in range(self.board.get_row_count()):
            for col in range(self.board.get_col_count()):
                self.draw_block(row, col)





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
