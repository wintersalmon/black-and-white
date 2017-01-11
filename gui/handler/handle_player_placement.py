'''
BLACK-AND-WHITE
WinterSalmon
EventHandler for 'player piece placement event'
'''


from gui.handler.event_handler import EventHandler


class HandlePlayerPlacement(EventHandler):
    '''
    EventHandler for 'player piece placement event'
    '''
    def __init__(self, game):
        super().__init__(game)


    def handle(self, event):
        '''
        handle event and return result message
        '''
        helper = self.game.player_piece_placement_helper
        continue_status = True
        message = None

        if event.type == self.key_down:
            result = False
            event_type = 'Wrong Input'
            event_param = None
            if event.key in self.key_directions:
                direction = self.get_direction(event.key)
                result = helper.move(direction)
                event_type = 'Player Placement'
                event_param = direction.name

            elif event.key in self.key_okay:
                if helper.can_save_target():
                    helper.save_target()
                    message = self.create_result_message(True, 'Player Placement')
                    continue_status = False
                else:
                    message = self.create_result_message(False, 'Player Placement')
                    continue_status = True

            message = self.create_result_message(result, event_type, event_param)

        self.game.continue_status = continue_status
        return message
