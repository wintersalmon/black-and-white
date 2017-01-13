'''
BLACK-AND-WHITE
WinterSalmon
Contains class Gui Graphic User Interface made with pygame
'''
import sys
import pygame
from pygame.locals import *

from game.game import Game
from game.color.constant import *
from game.status.status import STATUS
from game.board.direction import DIRECTION

from gui.draw.draw_unit import DrawUnit
from gui.draw.draw_background import DrawBackground
from gui.draw.draw_board import DrawBoard
from gui.draw.draw_player import DrawPlayer
from gui.draw.draw_message import DrawMessage

# from gui.handler.handle_change_pattern import HandleChangePattern
# from gui.handler.handle_player_movement import HandlePlayerMovement
# from gui.handler.handle_player_placement import HandlePlayerPlacement
# from gui.handler.handle_tile_placement import HandleTilePlacement

KEY_DIRECTIONS = [K_LEFT, K_a, K_RIGHT, K_d, K_UP, K_w, K_DOWN, K_s]
KEY_ROTATION = [K_q, K_e]
KEY_SELECTIONS = [K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0]
KEY_OPTIONS = [K_BACKQUOTE]
KEY_OKAY = [K_RETURN, K_SPACE]

class Gui():
    '''
    Graphic User Interface made with pygame
    '''
    def __init__(self):
        max_col = 12
        max_row = 5

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

        # init game data
        self.game = Game(max_row, max_col)
        self.last_action_msg = None

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

        # init handlers
        self.handlers = dict()
        self.handlers[STATUS.TILE_PLACEMENT] = self.handle_tile_placement_event
        self.handlers[STATUS.TILE_PLACEMENT_CHANGE_PATTERN] = self.handle_change_pattern_event
        self.handlers[STATUS.PLAYER_MOVEMENT_SET_START_POINT] = self.handle_player_placement_event
        self.handlers[STATUS.PLAYER_MOVEMENT] = self.handle_player_movement_event


    def init(self):
        '''
        displays game init screen and handles event
        '''
        player_info_list = list()
        player_info_list.append(('WinterSalmon', RED))
        player_info_list.append(('Kein', BLUE))
        player_info_list.append(('Sshong91', CYAN))
        player_info_list.append(('Wool', ORANGE))

        self.game.init_game(player_info_list)


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
        for draw_unit in self.draw_unit_list:
            draw_unit.draw()


    def handle_events(self):
        '''
        handle all events
        '''
        self.check_for_quit()
        status = self.game.get_current_status()
        if status in self.handlers.keys():
            for event in pygame.event.get():
                self.game.continue_status = self.handlers[status](event)


    def update(self):
        '''
        update
        '''
        self.game.update()
        pygame.display.update()
        self.draw_unit.pygame_fpsclock_tick()
        # self.fpsclock.tick(self.fps)


    def handle_change_pattern_event(self, event):
        '''
        handle change pattern event
        '''
        helper = self.game.player_pattern_update_helper
        if event.type == KEYDOWN:
            result = False
            event_type = 'Wrong Input'

            if event.key in KEY_OPTIONS:
                return False

            elif event.key in KEY_SELECTIONS:
                select_option_list = [WHITE, GRAY, BLACK]
                selection = self.get_selection(event.key, select_option_list)
                result = helper.enqueue_color(selection)
                event_type = 'Select Color'
                event_param = selection.get_name()

            elif event.key in KEY_OKAY:
                if helper.can_save_target():
                    helper.save_target()
                    self.push_local_event(True, 'Change Player Pattern')
                    return False
                else:
                    self.push_local_event(False, 'Change Player Pattern')
                    return True
            self.push_local_event(result, event_type, event_param)
        return True


    def handle_tile_placement_event(self, event):
        '''
        handle tile placement
        '''
        helper = self.game.player_tile_placement_helper
        if event.type == KEYDOWN:
            result = False
            event_type = 'Wrong Input'
            event_param = None
            if event.key in KEY_OPTIONS:
                # todo : hide this CODE into game class
                status = STATUS.TILE_PLACEMENT_CHANGE_PATTERN
                board = self.game.get_current_board()
                player = self.game.get_current_player()
                self.game.player_pattern_update_helper.set_target(player)
                player = self.game.player_pattern_update_helper
                self.game.change_status(status, board, player, True)
                return True
                # todo : hide this CODE into game class

            if event.key in KEY_SELECTIONS:
                select_item_list = [x for x in range(3)]
                selection = self.get_selection(event.key, select_item_list)
                result = helper.change_selected_tile(selection)
                event_type = 'Chage Tile'
                event_param = selection.get_name()

            elif event.key in KEY_DIRECTIONS:
                direction = self.get_direction(event.key)
                result = helper.move(direction)
                event_type = 'Move Tile'
                event_param = direction.name

            elif event.key in KEY_ROTATION:
                rotate = self.get_rotation(event.key)
                result = helper.rotate(rotate)
                event_type = 'Rotate Tile'
                event_param = '{} Degress'.format(rotate * 90)

            elif event.key in KEY_OKAY:
                if helper.can_save_target():
                    helper.save_target()
                    self.push_local_event(True, 'Save Tile')
                    return False
                else:
                    self.push_local_event(False, 'Save Tile')
                    return True

            self.push_local_event(result, event_type, event_param)

        return True


    def handle_player_placement_event(self, event):
        '''
        handle_player_placement_event
        '''
        helper = self.game.player_piece_placement_helper
        if event.type == KEYDOWN:
            result = False
            event_type = 'Wrong Input'
            event_param = None
            if event.key in KEY_DIRECTIONS:
                direction = self.get_direction(event.key)
                result = helper.move(direction)
                event_type = 'Player Placement'
                event_param = direction.name

            elif event.key in KEY_OKAY:
                if helper.can_save_target():
                    helper.save_target()
                    self.push_local_event(True, 'Player Placement')
                    return False
                else:
                    self.push_local_event(False, 'Player Placement')
                    return True

            self.push_local_event(result, event_type, event_param)

        return True


    def handle_player_movement_event(self, event):
        '''
        handle player change pattern
        '''
        helper = self.game.player_piece_movement_helper
        if event.type == KEYDOWN:
            result = False
            event_type = 'Wrong Input'
            event_param = None
            if event.key in KEY_DIRECTIONS:
                direction = self.get_direction(event.key)
                result = helper.move(direction)
                event_type = 'Move Player'
                event_param = direction.name
            elif event.key in KEY_OKAY:
                if helper.can_save_target():
                    helper.save_target()
                    self.push_local_event(True, 'Move Player')
                    return False
                else:
                    self.push_local_event(False, 'Move Player')
                    return True
            else:
                return True

            self.push_local_event(result, event_type, event_param)

        return True


    def get_direction(self, key):
        '''
        get key direction
        '''
        direction = None
        if key in (K_LEFT, K_a):
            direction = DIRECTION.LEFT
        elif key in (K_RIGHT, K_d):
            direction = DIRECTION.RIGHT
        elif key in (K_UP, K_w):
            direction = DIRECTION.UP
        elif key in (K_DOWN, K_s):
            direction = DIRECTION.DOWN
        return direction


    def get_rotation(self, key):
        '''
        get key rotation
        '''
        rotation = 0
        if key == K_q:
            rotation = 1
        elif key == K_e:
            rotation = 3
        return rotation


    def get_selection(self, key, select_option_list):
        '''
        get key selection
        '''
        idx = -1
        if key == K_1:
            idx = 0
        elif key == K_2:
            idx = 1
        elif key == K_3:
            idx = 2
        elif key == K_4:
            idx = 3
        elif key == K_5:
            idx = 4
        elif key == K_6:
            idx = 5
        elif key == K_7:
            idx = 6
        elif key == K_8:
            idx = 7
        elif key == K_9:
            idx = 8
        elif key == K_0:
            idx = 9
        if 0 <= idx < len(select_option_list):
            return select_option_list[idx]
        else:
            return None


    def push_local_event(self, result, discription, param=None):
        '''
        push new local event
        '''
        event_result = 'SUCCESS' if result else 'FAILED'
        param_str = param if param else ''
        self.last_action_msg = '[{}] {} {}'.format(event_result, discription, param_str)
        self.game.set_current_message(self.last_action_msg)
        # print(self.last_action_msg)
        # print(self.game.get_current_message())


    def check_for_quit(self):
        '''
        check for quit event and quit the game
        '''
        for event in pygame.event.get((QUIT, KEYUP)): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
