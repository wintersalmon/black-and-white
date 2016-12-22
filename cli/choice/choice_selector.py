'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Contains ChoiceSelector
'''


from cli.choice.choice import Choice
from cli.cmd.getch import getch


class ChoiceSelector():
    '''
    ChoiceSelector
    '''
    def __init__(self):
        self.choices = list()


    def add_choice(self, keys, action, description):
        '''
        add choice to list
        '''
        choice = Choice(keys, action, description)
        self.choices.append(choice)


    def show_full_choices(self):
        '''
        shows full choice list
        '''
        for choice in self.choices:
            print(choice.get_shortstatement(), end=' ')
        print(' : ')


    def find_matching_action(self, selection):
        '''
        returns choice action that matches user input
        '''
        for choice in self.choices:
            if selection in choice:
                return choice.get_action()
        return None


    def choice_user_selection(self):
        '''
        returns choice action that matches user input
        '''
        self.show_full_choices()
        selection = getch()
        return self.find_matching_action(selection)


    def get_choices(self):
        '''
        returns choice list
        '''
        return self.choices
