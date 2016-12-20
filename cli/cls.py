'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Contains Clear Screen Command for cross-platform
'''

import os

def cls():
    '''
    Clear Screen Command for cross-platform
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
