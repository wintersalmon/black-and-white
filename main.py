'''
BLACK-AND-WHITE
WinterSalmon
Main
'''

from gui.gui import Gui
from cli.cli import Cli

if __name__ == "__main__":
    # if pygame is not installed run game in commandline mode
    try:
        UI = Gui()
    except ImportError:
        UI = Cli()
    UI.init_screen()
    UI.game_screen()
    UI.credit_screen()
