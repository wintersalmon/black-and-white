'''
BLACK-AND-WHITE
WinterSalmon
EventHandler for 'player change pattern event'
'''


from game.color.constant import WHITE, GRAY, BLACK
from gui.handler.event_handler import EventHandler


class HandleChangePattern(EventHandler):
    '''
    EventHandler for 'player change pattern event'
    '''
    def __init__(self, game):
        super().__init__(game)


    def handle(self, event):
        '''
        handle event and return result message
        '''
        helper = self.game.player_pattern_update_helper
        continue_status = True
        message = None

        if event.type == self.key_down:
            result = False
            event_type = 'Wrong Input'

            if event.key in self.key_options:
                continue_status = False

            elif event.key in self.key_down:
                select_option_list = [WHITE, GRAY, BLACK]
                selection = self.get_selection(event.key, select_option_list)
                result = helper.enqueue_color(selection)
                event_type = 'Select Color'
                event_param = selection.get_name()

            elif event.key in self.key_okay:
                if helper.can_save_target():
                    helper.save_target()
                    message = self.create_result_message(True, 'Change Player Pattern')
                    continue_status = False
                else:
                    message = self.create_result_message(False, 'Change Player Pattern')
                    continue_status = True
            message = self.create_result_message(result, event_type, event_param)

        self.game.continue_status = continue_status
        return message

