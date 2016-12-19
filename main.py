'''
BLACK-AND-WHITE
WinterSalmon
2016.12.19
Main
'''

from data.data import Data
from gui.gui import Gui

if __name__ == "__main__":
    print('welcome to black and white')
    GAME = Data()
    GUI = Gui()
    GUI.start(GAME)
    while GUI.next():
        GUI.update()

        GUI.show()
        GUI.show_action_input()

        if GUI.has_action_input():
            GUI.action_input()
