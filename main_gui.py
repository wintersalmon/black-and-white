'''
BLACK-AND-WHITE
WinterSalmon
Main Gui
'''

from game.game import Game
from gui.gui import Gui

if __name__ == "__main__":
    GUI = Gui()
    GUI.init()
    GUI.run()
    GUI.credit()
