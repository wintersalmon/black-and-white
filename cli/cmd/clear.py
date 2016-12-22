'''
BLACK-AND-WHITE
WinterSalmon
Contains Clear Screen Command for cross-platform
'''

import os

def clear():
    '''
    Clear Screen Command for cross-platform
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
