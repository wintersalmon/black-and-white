'''
BLACK-AND-WHITE
WinterSalmon
Contains Choice
'''


class Choice():
    '''
    Choice class used to store choice key, action, information
    '''
    def __init__(self, keys, action, description):
        self.keys = keys
        self.action = action
        self.description = description


    def __contains__(self, key):
        return key in self.keys


    def get_all_key_string(self):
        '''
        returns key in string combined with '|'
        example
        ['A', 'B', 'C'] -> 'A|B|C'
        '''
        key_string = ''
        for key in self.keys:
            key_string += key + '|'
        return key_string[:-1]


    def get_full_statement(self):
        '''
        returns full statement of Choice
        example { des="Yes" , key=['Y', 'y'] } -> 'Yes(Y|y)'
        '''
        return self.description + '(' + self.get_all_key_string() + ')'


    def get_shortstatement(self):
        '''
        returns short statement of Choice
        example { des="Yes" , key=['Y', 'y'] } -> 'Yes(Y)'
        '''
        return self.description + '(' + self.keys[0] + ')'


    def get_keys(self):
        '''
        returns keys
        '''
        return self.keys


    def get_action(self):
        '''
        returns action
        '''
        return self.action


    def get_description(self):
        '''
        returns description
        '''
        return self.description
