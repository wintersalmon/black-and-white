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
        self.continue_status = False


    def next_player(self):
        '''
        increase turn counter and get next player
        '''
        self.turn_counter += 1
        index = (self.turn_counter - 1) % len(self.players)
        self.current_player = self.players[index]
        return self.current_player


    def start(self, board, players):
        '''
        init game variables and start game
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

        self.game_running = True
        self.current_board_drawer = self.board
        self.current_player_drawer = self.current_player

        # self.status = STATUS.GAME_START
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

            elif self.status == STATUS.TILE_PLACEMENT_NEXT_PLAYER:
                for player in self.players:
                    # todo : remove all tiles
                    for _ in range(3):
                        if self.deck.size() > 0:
                            tile = self.deck.draw()
                            player.add_tile(tile)

            elif self.status == STATUS.TILE_PLACEMENT:
                self.tile_placement_helper.set_piece(self.current_player)

                self.current_board_drawer = self.tile_placement_helper
                self.current_player_drawer = self.current_player

            elif self.status == STATUS.TILE_PLACEMENT_CHANGE_PATTERN:
                self.pattern_update_helper.set_player(self.current_player)

                self.current_board_drawer = self.board
                self.current_player_drawer = self.pattern_update_helper

            elif self.status == STATUS.PLAYER_MOVEMENT:
                self.player_movement_helper.set_piece(self.current_player)

                self.current_board_drawer = self.player_movement_helper
                self.current_player_drawer = self.player_movement_helper

            else:
                self.current_board_drawer = self.board
                self.current_player_drawer = self.current_player

            return True
        return False


    def is_game_over(self):
        '''
        returns True if game over condition matches
        '''
        return not self.game_running


    def update_status(self):
        '''
        Need to Start() game first
        Update game status to next status
        '''
        if self.status == STATUS.GAME_START:
            self.status = STATUS.NEXT_ROUND

        elif self.status == STATUS.NEXT_ROUND:
            if self.is_game_over():
            # if self.turn_counter % (len(self.players) * 4 * 2) == 0:
                self.status = STATUS.GAME_OVER
            else:
                self.change_status(STATUS.TILE_PLACEMENT_NEXT_PLAYER)
                # self.status = STATUS.TILE_PLACEMENT_NEXT_PLAYER

        elif self.status == STATUS.TILE_PLACEMENT_NEXT_PLAYER:
            self.next_player()
            if self.turn_counter % (len(self.players) * 3) == 0:
                self.status = STATUS.PLAYER_MOVEMENT_NEXT_PLAYER
            else:
                self.continue_status = True
                # self.status = STATUS.TILE_PLACEMENT
                self.change_status(STATUS.TILE_PLACEMENT)

        elif self.status == STATUS.TILE_PLACEMENT:
            if not self.continue_status:
                self.status = STATUS.TILE_PLACEMENT_NEXT_PLAYER

        elif self.status == STATUS.TILE_PLACEMENT_CHANGE_PATTERN:
            if not self.continue_status:
                self.status = STATUS.TILE_PLACEMENT_NEXT_PLAYER

        elif self.status == STATUS.PLAYER_MOVEMENT_NEXT_PLAYER:
            self.next_player()
            if self.turn_counter % (len(self.players) * 4) == 0:
                self.status = STATUS.NEXT_ROUND
            else:
                self.continue_status = True
                # self.status = STATUS.PLAYER_MOVEMENT
                self.change_status(STATUS.PLAYER_MOVEMENT)

        elif self.status == STATUS.PLAYER_MOVEMENT_SET_START_POINT:
            if not self.continue_status:
                # self.status = STATUS.PLAYER_MOVEMENT
                self.change_status(STATUS.PLAYER_MOVEMENT)

        elif self.status == STATUS.PLAYER_MOVEMENT:
            if not self.continue_status:
                self.status = STATUS.PLAYER_MOVEMENT_NEXT_PLAYER

        elif self.status == STATUS.GAME_OVER:
            return False

        else:
            raise EnvironmentError('Game not started')

        return True
