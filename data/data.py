'''
BLACK-AND-WHITE
WinterSalmon
Class Name
'''


from data.board.board import Board
from data.tile_deck import TileDeck
from data.helper.player_movement_helper import PlayerMovementHelper
from data.helper.tile_placement_helper import TilePlacementHelper
from data.helper.pattern_update_helper import PatternUpdateHelper
from data.status.status import STATUS

class Data():
    '''
    Class Description
    '''
    def __init__(self):
        self.board = None
        self.status = STATUS.NOSTATUS

        self.tile_placement_helper = None
        self.player_movement_helper = None
        self.pattern_update_helper = None

        self.players = None
        self.deck = None

        self.turn_counter = 0
        self.current_player = None
        self.current_tile = None

        self.current_board_drawer = None
        self.current_player_drawer = None

        self.game_running = False


    def next_player(self):
        '''
        increase turn counter and get next player
        '''
        self.turn_counter += 1
        index = (self.turn_counter - 1) % len(self.players)
        self.current_player = self.players[index]
        return self.current_player


    def init_game(self, board, players):
        '''
        set game
        '''
        if not isinstance(board, Board):
            raise TypeError('parameter board need to be Board Type')

        self.board = board

        self.tile_placement_helper = TilePlacementHelper(self.board)
        self.player_movement_helper = PlayerMovementHelper(self.board)
        self.pattern_update_helper = PatternUpdateHelper()

        self.players = players
        self.deck = TileDeck()

        self.turn_counter = 0
        self.current_player = None
        self.current_tile = None

        self.change_status(STATUS.GAME_START)


    def change_status(self, status):
        '''
        change_status
        '''
        if isinstance(status, STATUS):
            self.status = status
            if self.status == STATUS.GAME_START:
                self.game_running = True
                self.current_board_drawer = self.board
                self.current_player_drawer = self.current_player

            elif self.status == STATUS.TILE_PLACEMENT:
                self.tile_placement_helper.set_piece(self.current_player)

                self.current_board_drawer = self.tile_placement_helper
                self.current_player_drawer = self.current_player

            elif self.status == STATUS.PLAYER_MOVEMENT:
                self.player_movement_helper.set_piece(self.current_player)

                self.current_board_drawer = self.player_movement_helper
                self.current_player_drawer = self.player_movement_helper

            elif self.status == STATUS.PLAYER_CHANGE_PATTERN:
                self.pattern_update_helper.set_player(self.current_player)

                self.current_board_drawer = self.board
                self.current_player_drawer = self.pattern_update_helper

            else:
                self.current_board_drawer = self.board
                self.current_player_drawer = self.current_player

            return True
        return False
