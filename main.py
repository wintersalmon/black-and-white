'''
BLACK-AND-WHITE
WinterSalmon
Main
'''

from data.data import Data
from cli.cli import Cli

if __name__ == "__main__":
    print('welcome to black and white')
    GAME = Data()
    CLI = Cli()
    CLI.start(GAME)
    while CLI.next():
        CLI.update()

        CLI.show()
        CLI.show_action_input()

        if CLI.has_action_input():
            CLI.action_input()
