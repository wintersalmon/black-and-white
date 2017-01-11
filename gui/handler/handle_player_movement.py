'''
BLACK-AND-WHITE
WinterSalmon
EventHandler for 'player piece movement event'
'''


from game.status.status import STATUS
from gui.handler.event_handler import EventHandler


class HandlePlayerMovement(EventHandler):
    '''
    EventHandler for 'player piece movement event'
    '''
    def __init__(self, game):
        super().__init__(game)


    def handle(self, event):
        '''
        handle event and return result message
        '''
        helper = self.game.player_tile_placement_helper
        continue_status = True
        message = None

        if event.type == self.key_down:
            result = False
            event_type = 'Wrong Input'
            event_param = None
            if event.key in self.key_options:
                # todo : hide this CODE into game class
                status = STATUS.TILE_PLACEMENT_CHANGE_PATTERN
                board = self.game.get_current_board()
                player = self.game.get_current_player()
                self.game.player_pattern_update_helper.set_target(player)
                player = self.game.player_pattern_update_helper
                self.game.change_status(status, board, player, True)
                continue_status = True
                # todo : hide this CODE into game class

            if event.key in self.key_selections:
                select_item_list = [x for x in range(3)]
                selection = self.get_selection(event.key, select_item_list)
                result = helper.change_selected_tile(selection)
                event_type = 'Chage Tile'
                event_param = selection.get_name()

            elif event.key in self.key_directions:
                direction = self.get_direction(event.key)
                result = helper.move(direction)
                event_type = 'Move Tile'
                event_param = direction.name

            elif event.key in self.key_rotations:
                rotate = self.get_rotation(event.key)
                result = helper.rotate(rotate)
                event_type = 'Rotate Tile'
                event_param = '{} Degress'.format(rotate * 90)

            elif event.key in self.key_okay:
                if helper.can_save_target():
                    helper.save_target()
                    message = self.create_result_message(True, 'Save Tile')
                    continue_status = False
                else:
                    message = self.create_result_message(False, 'Save Tile')
                    continue_status = True

            message = self.create_result_message(result, event_type, event_param)

        self.game.continue_status = continue_status
        return message
