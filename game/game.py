'''
BLACK-AND-WHITE
WinterSalmon
Class Name
'''

from game.player import Player
from game.board.board import Board
from game.tile_deck import TileDeck
from game.helper.player_movement_helper import PlayerMovementHelper
from game.helper.tile_placement_helper import TilePlacementHelper
from game.helper.pattern_update_helper import PatternUpdateHelper
from game.status.status import STATUS

class Game():
    '''
    Class Description
    '''
    def __init__(self):
        self.current_status = STATUS.NOSTATUS
        self.turn_counter = 0
        self.game_running = False
        self.game_over = False
        self.continue_status = False

        self.board = None
        self.players = list()
        self.deck = None

        self.tile_placement_helper = None
        self.player_movement_helper = None
        self.pattern_update_helper = None

        self.current_board = None
        self.current_player = None
        self.current_tile = None
        self.current_message = None

        self.rule_max_round_count = 0
        self.current_round_count = 0


    def get_players(self):
        '''
        returns players
        '''
        return self.players


    def get_current_status(self):
        '''
        returns current STATUS
        '''
        return self.current_status


    def get_current_board(self):
        '''
        returns current Board
        '''
        return self.current_board


    def get_current_player(self):
        '''
        returns current Player
        '''
        return self.current_player


    def get_current_message(self):
        '''
        returns current Message
        '''
        return self.current_message


    def is_game_running(self):
        '''
        returns True if game is running
        '''
        return self.game_running


    def is_game_over(self):
        '''
        returns True if game over condition matches
        '''
        # return (self.turn_counter > 0) and (self.turn_counter % divider == 0)
        for player in self.players:
            row, col = player.get_position()
            if self.board.check_row_col_boundary(row, col):
                if col == self.board.get_col_count() - 1:
                    self.game_over = True
        return self.game_over


    def init_game(self, player_names, max_row, max_col):
        '''
        initialize game
        '''
        if not len(player_names) > 0:
            raise ValueError('len(player_names) must be above zero')
        if not max_row > 0:
            raise ValueError('max_row must be above zero')
        if not max_col > 0:
            raise ValueError('max_col must be above zero')

        self.current_status = STATUS.GAME_START
        self.turn_counter = 0
        self.game_running = True
        self.game_over = False
        self.continue_status = False

        self.board = Board(max_row, max_col)
        self.deck = TileDeck()
        self.players.clear()
        for number, name in enumerate(player_names):
            player = Player(number + 1, name)
            self.players.append(player)

        self.tile_placement_helper = TilePlacementHelper(self.board)
        self.player_movement_helper = PlayerMovementHelper(self.board)
        self.pattern_update_helper = PatternUpdateHelper()

        self.current_player = None
        self.current_tile = None
        self.current_board = None

        self.rule_max_round_count = 1
        self.current_round_count = 0


    def change_status(self, status, board=None, player=None, status_loop=True):
        '''
        change current status
        '''
        self.current_status = status
        self.continue_status = status_loop
        self.current_board = board
        self.current_player = player


    def update(self):
        '''
        Need to init_game() first
        Update game status
        '''
        self.handle_events()
        self.update_status()


    def handle_events(self):
        '''
        update all queued events
        '''
        # todo : add handle event function
        pass


    def update_status(self):
        '''
        update game status
        '''
        if self.current_status == STATUS.GAME_START:
            self.change_status(STATUS.NEXT_ROUND, self.board)

        elif self.current_status == STATUS.NEXT_ROUND:
            if self.is_game_over():
                self.change_status(STATUS.GAME_OVER)
            else:
                for player in self.players:
                    player.remove_all_tiles()
                    for _ in range(self.rule_max_round_count):
                        tile = self.deck.draw()
                        if tile:
                            player.add_tile(tile)
                self.current_round_count = self.rule_max_round_count * len(self.players)
                self.change_status(STATUS.TILE_PLACEMENT_NEXT_PLAYER)

        elif self.current_status == STATUS.TILE_PLACEMENT_NEXT_PLAYER:
            if self.current_round_count > 0:
                self.current_round_count -= 1
                self.__next_turn()
                player = self.current_player
                self.tile_placement_helper.set_piece(player)
                board = self.tile_placement_helper
                self.change_status(STATUS.TILE_PLACEMENT, board, player, True)
            else:
                self.current_round_count = 1 * len(self.players)
                self.change_status(STATUS.PLAYER_MOVEMENT_NEXT_PLAYER)

        elif self.current_status == STATUS.TILE_PLACEMENT:
            if not self.continue_status:
                self.change_status(STATUS.TILE_PLACEMENT_NEXT_PLAYER)

        elif self.current_status == STATUS.TILE_PLACEMENT_CHANGE_PATTERN:
            if not self.continue_status:
                self.change_status(STATUS.TILE_PLACEMENT_NEXT_PLAYER)

        elif self.current_status == STATUS.PLAYER_MOVEMENT_NEXT_PLAYER:
            if self.current_round_count > 0:
                self.current_round_count -= 1
                self.__next_turn()
                player = self.current_player
                self.player_movement_helper.set_piece(player)
                board = self.player_movement_helper
                player = self.player_movement_helper
                self.change_status(STATUS.PLAYER_MOVEMENT, board, player, True)
            else:
                self.change_status(STATUS.NEXT_ROUND)

        elif self.current_status == STATUS.PLAYER_MOVEMENT_SET_START_POINT:
            if not self.continue_status:
                self.change_status(STATUS.PLAYER_MOVEMENT)

        elif self.current_status == STATUS.PLAYER_MOVEMENT:
            if not self.continue_status:
                self.current_status = STATUS.PLAYER_MOVEMENT_NEXT_PLAYER

        elif self.current_status == STATUS.GAME_OVER:
            self.game_running = False

        else:
            return False

        return True


    def __next_turn(self):
        '''
        increase turn counter and get next player
        '''
        player = self.get_next_player()
        return self.change_current_turn_player(player)


    def get_next_player(self):
        '''
        get next turn player
        '''
        index = self.turn_counter % len(self.players)
        self.current_player = self.players[index]
        return self.current_player


    def change_current_turn_player(self, player):
        '''
        change current turn player
        '''
        if isinstance(player, Player):
            self.turn_counter += 1
            self.current_player = player
            return True
        return False
